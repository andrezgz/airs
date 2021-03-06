#==============================================================================
# Author:      Jorgen Bodde
# Copyright:   (c) Jorgen Bodde
# License:     GPLv2 (see LICENSE.txt)
#==============================================================================

import sys
import platform
if platform.python_version()[0:3] <= '2.4':
    from pysqlite2 import dbapi2 as sqlite3
else:
    import sqlite3
import os.path
import datetime
from data import series_list

VERSION = 5

# main script that initializes the database
_main_sql = """\
CREATE TABLE series (id INTEGER PRIMARY KEY, name VARCHAR, url VARCHAR, 
                     last_update VARCHAR, update_period INTEGER, postponed INTEGER,
                     notes VARCHAR, folder VARCHAR);
create table episode (id INTEGER PRIMARY KEY, title VARCHAR, number VARCHAR, 
                      season VARCHAR, aired VARCHAR, last_update VARCHAR, 
                      status INTEGER,  series_id INTEGER, changed INTEGER, 
                      seen INTEGER, prio_entries VARCHAR, new INTEGER, 
                      locked INTEGER);
CREATE TABLE version (id INTEGER PRIMARY KEY, version INTEGER, updated_on VARCHAR);
INSERT INTO version (version, updated_on) VALUES (%(version)i, "%(date)s");
create table searches (id integer primary key, name varchar, url varchar, options VARCHAR, defoptions VARCHAR, show INTEGER);
create table options (id integer primary key, name varchar, value varchar);
insert into searches (name, url, options, defoptions, show) values ("Newzleech", "http://www.newzleech.com/?mode=usenet&q=@series@+@season_nr@+@episode_nr@", "", "", 0);
insert into searches (name, url, options, defoptions, show) values ("Yabsearch", "http://www.yabsearch.nl/search/@series@+@season_nr@+@episode_nr@", "", "", 0);
insert into searches (name, url, options, defoptions, show) values ("NzbIndex", "http://www.nzbindex.nl/?go=search&new=1&searchitem=@series@+@season_nr@+@episode_nr@", "", "", 0);
insert into options (name, value) values ("default_search", "1");
create table episodefile (id integer primary key, fullpath varchar, size integer, reldir varchar, episode_id integer, series_id integer, filetype integer); 
"""

#-------------------------------------------------------------------------------
# upgrade script for v1 to v2

upgr_v1_v2 = """\
ALTER TABLE series ADD last_update VARCHAR;,
ALTER TABLE series ADD update_period INTEGER;
ALTER TABLE series ADD postponed INTEGER;
ALTER TABLE episode ADD queued INTEGER;
update episode set queued = 0;
update series set update_period = 0;
update series set postponed = 0;
update version set version=2, updated_on="%(date)s" where id=1;
"""
#-------------------------------------------------------------------------------
# upgrade script for v2 to v3

upgr_v2_v3 = """\
update version set version=3, updated_on="%(date)s" where id=1;
"""

#-------------------------------------------------------------------------------
# upgrade script for v3 to v4

upgr_v3_v4 = """\
create table searches (id integer primary key, name varchar, url varchar, options VARCHAR, defoptions VARCHAR, show INTEGER);
create table options (id integer primary key, name varchar, value varchar);
insert into searches (name, url, options, defoptions, show) values ("Newzleech", "http://www.newzleech.com/?mode=usenet&q=@series@+@season_nr@+@episode_nr@", "", "", 0);
insert into searches (name, url, options, defoptions, show) values ("Yabsearch", "http://www.yabsearch.nl/search/@series@+@season_nr@+@episode_nr@", "", "", 0);
insert into searches (name, url, options, defoptions, show) values ("NzbIndex", "http://www.nzbindex.nl/?go=search&new=1&searchitem=@series@+@season_nr@+@episode_nr@", "", "", 0);
insert into options (name, value) values ("default_search", "1");
alter table series add notes VARCHAR;
alter table episode add seen INTEGER;
update series set notes="";
update episode set seen=0;
update version set version=4, updated_on="%(date)s" where id=1;
"""

#-------------------------------------------------------------------------------
# upgrade script for v4 to v5

upgr_v4_v5 = """\
alter table episode add prio_entries VARCHAR;
alter table episode add new INTEGER;
alter table episode add locked INTEGER;
alter table series add folder VARCHAR;
update episode set prio_entries="";
update episode set new = 1;
update episode set locked=0;
update series set folder="";
update version set version=5, updated_on="%(date)s" where id=1;
"""

#-------------------------------------------------------------------------------
# upgrade script for v5 to v6

upgr_v5_v6 = """\
create table episodefile (id integer primary key, fullpath varchar, size integer, reldir varchar, episode_id integer, series_id integer, filetype integer);
/* update version set version=6, updated_on="%(date)s" where id=1; */
"""

# NOTE: episode.seen is obsolete, and should be removed upon a new creation

#-------------------------------------------------------------------------------

def _conv_date_v2(s):
    if s:
        try:
            dy = int(s[0:2])
            mn = int(s[3:5])
            yr = int(s[6:])
            if yr < 100:
                if yr < 99 and yr > 39:
                    yr = 1900 + yr
                else:
                    yr = 2000 + yr
            return "%04i%02i%02i" % (yr, mn, dy)
        except ValueError:
            return ""   
    else:
        return ""    

#-------------------------------------------------------------------------------
def upgr_pre_v3(conn):
    """
    This method transforms all date fields from all episodes
    so that in this version the sorting will go al lot easier
    """
    
    c = conn.cursor()
        
    c.execute("select id, last_update from series")
    lst = list()
    for rec in c:
        lst.append( (rec[0], _conv_date_v2(rec[1])) )
    
    for i in lst:
        c.execute("update series set last_update=\"%s\" where id=%i" % (i[1], i[0])) 
    conn.commit()
    
    # cleanup in the episode table, recreate with better fields
    c.execute("select title, number, season, aired, seen, queued, last_in, series_id from episode")
    records = [ rec for rec in c ]
    
    c.execute("drop table episode")
    
    # recreate table and transform
    c.execute("create table episode (id INTEGER PRIMARY KEY, title VARCHAR, number VARCHAR, " + \
              "                      season VARCHAR, aired VARCHAR, last_update VARCHAR, " + \
              "                      status INTEGER,  series_id INTEGER, changed INTEGER)")
    
    td = datetime.date.today().strftime("%Y%m%d")
    for r in records:
        st = series_list.EP_READY
        upd = ""
        changed = 0
        if r[5] != 0:
            st = series_list.EP_TO_DOWNLOAD
        elif r[4] != 0:
            st = series_list.EP_SEEN
        elif r[6] != 0:
            st = series_list.EP_READY
            upd = td
            changed = 1
            
        rec = (r[0], r[1], r[2], _conv_date_v2(r[3]), upd, st, r[7], changed) 
        c.execute("insert into episode (title, number, season, aired, last_update, status, series_id, changed) values " +\
                  "(?, ?, ?, ?, ?, ?, ?, ?)", rec)
        
    conn.commit()    
    c.close()
    
#-------------------------------------------------------------------------------
def create(dbfile):
    # can't create if already exists
    if os.path.exists(dbfile):
        return False
    
    conn = sqlite3.connect(dbfile)
    if not conn:
        return False
    
    conn.executescript(_main_sql % { "version": VERSION, "date": datetime.date.today().strftime("%Y%m%d") })
    conn.commit()
    conn.close()
    
    return True
    

#-------------------------------------------------------------------------------

# upgrade directory
# upgrade FROM version TO one higher
_upgrade_list = { 1: (None,        upgr_v1_v2, None),
                  2: (upgr_pre_v3, upgr_v2_v3, None),
                  3: (None,        upgr_v3_v4, None),
                  4: (None,        upgr_v4_v5, None) }

def upgrade(dbfile):

    # needs existing DB!
    if not os.path.exists(dbfile):
        return False
    
    conn = sqlite3.connect(dbfile)
    if not conn:
        return False
    
    # get version
    upgrading = True
    while upgrading: 
        c = conn.cursor()
        c.execute("select version from version")
        for v in c:
            version = v[0]
            if version < VERSION:
                pre_func, sql, post_func = _upgrade_list[version]
                # pre transform data
                if pre_func:
                    pre_func(conn)

                # upgrade the script
                conn.executescript(sql % { "date": datetime.date.today().strftime("%Y%m%d") })
                conn.commit()

                # post transform
                if post_func:
                    post_func(conn)

            else:
                upgrading = False
            break
        c.close()
        
    conn.close()
        
    return True
