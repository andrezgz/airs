#==============================================================================
# Author:      Jorgen Bodde
# Copyright:   (c) Jorgen Bodde
# License:     GPLv2 (see LICENSE.txt)
#==============================================================================

from storm.locals import *
from storm.locals import SQL
import os
import datetime
import pickle
import appcfg

EP_NEW         = 0
EP_TO_DOWNLOAD = 1
EP_DOWNLOADING = 2
EP_READY       = 3
EP_SEEN        = 4
EP_DOWNLOADED  = 5

# period definitions
# > 0 = custom days
# 0 = always
# -1 to -7 = update monday to sunday
# -8 and -9 = bi-weekly and monthly
min_period = -9
period_trans  = { -1: "monday",   -2: "tuesday",   -3: "wednesday",
                  -4: "thursday", -5: "friday",    -6: "saturday",
                  -7: "sunday",   -8: "bi-weekly", -9: "monthly" }
period_custom = ( -999, "custom" )

def get_series_path(series):
    """ Returns the series path, if relative, it will append the root path
    from the settings. If not relative, it will return the path """
    seriespath = series.folder.strip()
    rootpath = appcfg.options[appcfg.CFG_SERIES_PATH]
    if seriespath == '':
        return ''
    
    if os.path.isabs(seriespath):
        return seriespath
    else:
        if rootpath == '':
            return ''
        else:
            return os.path.join(rootpath, seriespath)
        
def prio_to_string(priorities):
    s = ''
    for key in priorities:
        if s != '':
            s += '|'
        s += '%s:%i' % (key, priorities[key])
    return s


def string_to_prio(s):
    prios = dict()
    lst = s.split('|')
    for item in lst:
        s1, s2 = item.split(':')
        prios[s1] = int(s2)
    return prios
     

def date_to_str(d):
    return "%04i%02i%02i" % (d.year, d.month, d.day)

    
def idx_to_weekdelta(idx):
    """ Gets weekdelta based upon idx """
    # ok it looks like a 2^x but it does not have to be
    wd = {0: 1,
          1: 2,
          2: 4,
          3: 8}
    if idx in wd:
        return wd[idx]
    return 0
    
#
# Module that contains functionality
# to store a number of series and functionality
#

def _convertDate(datestr):
    if datestr:
        try:
            dy = int(datestr[6:])
            mn = int(datestr[4:6])
            yr = int(datestr[0:4])
            return date(yr, mn, dy)
        except ValueError:
            return None   
    else:
        return None


class Series(object):
    """
    List of episodes manager
    """
    __storm_table__ = "series"
    id = Int(primary = True)
    name = Unicode()
    url = Unicode()
    postponed = Int()
    last_update = Unicode()
    update_period = Int()       # in how many days later
    folder = Unicode()

    
    def __storm_loaded__(self):
        if self.update_period is None:
            self.update_period = 0
    
    
    def setLastUpdate(self, d = None):
        if d:
            self.last_update = unicode("%04i%02i%02" % (d.year, d.month, d.day))
        else:
            self.last_update = unicode(datetime.date.today().strftime("%Y%m%d"))    
    
    def getLastUpdate(self):
        s = self.last_update
        if s and len(s) > 7:
            try:
                d = datetime.date(day = int(s[6:8]), month = int(s[4:6]), year = int(s[0:4]))
                return d
            except ValueError:
                pass
        return None
            

class Episode(object):
    """
    Serie episode item
    """
    __storm_table__ = "episode"
    id = Int(primary = True)
    title = Unicode()             # title of episode
    number = Unicode()            # follow up number
    season = Unicode()            # season string e.g. (S01E01)
    aired = Unicode()             # date when aired
    last_update = Unicode()       # last update
    status = Int()                # status of episode
    changed = Int()
    series_id = Int()             # id of series table entry
    prio_entries = Unicode()      # not to be used directly
    new = Int()
    locked = Int()
        
    def __init__(self):
        self.title = u""
        self.number = u""
        self.season = u""
        self.aired = u""
        self.last_update = u""
        self.status = EP_READY
        self.changed = 0 
        self.locked = 0
        self.new = 0
        self.priorities = dict()
            

    def __storm_loaded__(self):
        self.priorities = dict()
        if self.prio_entries != "":
            prios = string_to_prio(self.prio_entries)
            for key in prios:
                self.priorities[key] = prios[key]
        
        
    def getPriority(self, key):
        """
        Returns priority setting of this episode
        """
        if key in self.priorities:
            return self.priorities[key]
        return 0
        

    def setPriority(self, key, value):
        """
        Set priority setting of this episode
        """
        self.priorities[key] = int(value)
        self.prio_entries = unicode(prio_to_string(self.priorities))
        
    
    def setAired(self, d):
        """
        Sets date
        """
        if d:
            self.aired = unicode("%04i%02i%02i" % (d.year, d.month, d.day))
        else:
            self.aired = unicode('')
    
    def setLastUpdate(self, d = None):
        """
        Sets date
        """
        if d:
            self.last_update = unicode("%04i%02i%02" % (d.year, d.month, d.day))
        else:
            self.last_update = unicode(datetime.date.today().strftime("%Y%m%d"))
          
    def getStrDate(self):
        if len(self.aired) > 7:
            s = self.aired
            return "%s-%s-%s" % (s[0:4], s[4:6], s[6:8])
        return ''
    
    def getAired(self):
        s = self.aired
        if s and len(s) > 7:
            try:
                d = datetime.date(day = int(s[6:8]), month = int(s[4:6]), year = int(s[0:4]))
                return d
            except ValueError:
                pass
        return None    
                    
    
class SeriesList(object):
    """
    List of series collection manager 
    """
    def __init__(self):        
        # series dictionary
        self._series = dict()

        
    def addEpisode(self, serie_id, episode_nr, episode_title):
        """
        Adds an episode to the series list, if the series
        did not yet exist, a new one is added.
        """
        ser = self.addSeries(serie_id)
        return ser.addEpisode(episode_nr, episode_title)
            

    def attachEpisode(self, serie_id, episode):
        """
        Attach an episode only when the ID of the episode
        does not yet exist, else discard it
        """
        sid = serie_id.lower()
        if sid in self._series:
            return self._series[sid].attachEpisode(episode)
        
        return False
    
    
    def addSeries(self, serie_id):
        """
        Adds the series only, returns a series object 
        if the series is actually added it emits a signal else
        it will only return a reference
        """
        sid = serie_id.lower()
        if sid not in self._series:
            seps = Series(serie_id)
            self._series[sid] = seps
        else:
            seps = self._series[sid]
        
        return seps
    