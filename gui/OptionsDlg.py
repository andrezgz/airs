import os
import platform

import wx
import wx.xrc as xrc
import xmlres
from data import appcfg


class OptionsDlg(wx.Dialog):
    def __init__(self, parent, id = wx.ID_ANY):

        pre = wx.PreDialog()
        res = xmlres.loadGuiResource("OptionsDlg.xrc")
        res.LoadOnDialog(pre, parent, "OptionsDialog")
        self.PostCreate(pre)

        self._layout = xrc.XRCCTRL(self, "ID_LAYOUT")
        self._layout.Append("Mobile (bare text)", appcfg.LAYOUT_MOBILE)
        self._layout.Append("Screen (small fonts and icons)", appcfg.LAYOUT_SCREEN)
        self._layout.Append("TV (big fonts and icons)", appcfg.LAYOUT_TV)

        layout = appcfg.options[appcfg.CFG_LAYOUT_SCREEN]
        for idx in xrange(0, self._layout.GetCount()):
            if self._layout.GetClientData(idx) == layout:
                self._layout.SetSelection(idx)
                break

        self._playerPath = xrc.XRCCTRL(self, "ID_PLAYER_PATH")
        self._playerArgs = xrc.XRCCTRL(self, "ID_PLAYER_ARGS")
        self._playerBtn = xrc.XRCCTRL(self, "ID_PLAYER_BROWSE")

        self._seriesPath = xrc.XRCCTRL(self, "ID_SERIES_ROOT")
        self._seriesBtn = xrc.XRCCTRL(self, "ID_SERIES_BROWSE")
        
        self._webURL = xrc.XRCCTRL(self, "ID_WEB_URL")
        self._webPort = xrc.XRCCTRL(self, "ID_WEB_PORT")
        
        self._autoUpdate = xrc.XRCCTRL(self, "ID_AUTO_UPDATE")
        self._gracePeriod = xrc.XRCCTRL(self, "ID_GRACE_PERIOD")
        
        self._autoTimed = xrc.XRCCTRL(self, "ID_TIMED_UPDATE")
        self._timedUpdate = xrc.XRCCTRL(self, "ID_TIME_PERIOD")
        
        self._fuzzyMatch = xrc.XRCCTRL(self, "ID_FUZZY_MATCH")
        
        self._playerPath.SetValue(appcfg.options[appcfg.CFG_PLAYER_PATH])
        self._playerArgs.SetValue(appcfg.options[appcfg.CFG_PLAYER_ARGS])
        self._seriesPath.SetValue(appcfg.options[appcfg.CFG_SERIES_PATH])
        self._webPort.SetValue(str(appcfg.options[appcfg.CFG_WEB_PORT]))
        self._webURL.SetValue(appcfg.options[appcfg.CFG_WEB_URL])
        self._autoUpdate.SetValue(appcfg.options[appcfg.CFG_AUTO_UPDATE])
        self._gracePeriod.SetValue(str(appcfg.options[appcfg.CFG_GRACE_PERIOD]))
        self._timedUpdate.SetValue(appcfg.options[appcfg.CFG_TIMED_UPDATE])
        self._autoTimed.SetValue(appcfg.options[appcfg.CFG_AUTO_UPDATE_TIMED])
        self._fuzzyMatch.SetValue(appcfg.options[appcfg.CFG_FUZZY_MATCH])
        
        self.Bind(wx.EVT_BUTTON, self.__OnOK,  xrc.XRCCTRL(self, "wxID_OK"))
        self.Bind(wx.EVT_BUTTON, self._browseSeries, self._seriesBtn)
        self.Bind(wx.EVT_BUTTON, self._browsePlayer, self._playerBtn)


    def _browsePlayer(self, event):
        if platform.system().lower() == "windows":
            wildcard = "*.*"
        else:
            wildcard = "*"

        defpath = self._playerPath.GetValue().strip()
        if defpath == '':
            if platform.system() == 'Linux':
                defpath = "/usr/bin/"
            else:
                defpath = "C:\\Program Files\\"
            
        dlg = wx.FileDialog(self, "Select the player executable", os.path.dirname(defpath),
                            "", wildcard, wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self._playerPath.SetValue(dlg.GetPath())


    def _browseSeries(self, event):
        dlg = wx.DirDialog(self, "Select path for series", self._seriesPath.GetValue())
        if dlg.ShowModal() == wx.ID_OK:
            self._seriesPath.SetValue(dlg.GetPath())


    # --------------------------------------------------------------------------
    def __OnOK(self, event):
        """ Press OK, verify the path and notify if the path is not valid """

        try:
            port = int(self._webPort.GetValue())
        except ValueError:
            wx.MessageBox("Please specify a valid port!", "Error", wx.ICON_ERROR)
            return
            
        try:
            graceperiod = int(self._gracePeriod.GetValue())
        except ValueError:
            wx.MessageBox("Please specify a valid startup wait time", "Error", wx.ICON_ERROR)
            return
            
        appcfg.options[appcfg.CFG_LAYOUT_SCREEN] = self._layout.GetClientData(self._layout.GetSelection())
        appcfg.options[appcfg.CFG_PLAYER_PATH] = self._playerPath.GetValue()
        appcfg.options[appcfg.CFG_SERIES_PATH] = self._seriesPath.GetValue()
        appcfg.options[appcfg.CFG_PLAYER_ARGS] = self._playerArgs.GetValue()
        appcfg.options[appcfg.CFG_WEB_PORT] = port
        appcfg.options[appcfg.CFG_WEB_URL] = self._webURL.GetValue()
        appcfg.options[appcfg.CFG_AUTO_UPDATE] = self._autoUpdate.GetValue()
        appcfg.options[appcfg.CFG_GRACE_PERIOD] = graceperiod        
        appcfg.options[appcfg.CFG_TIMED_UPDATE] = self._timedUpdate.GetValue()
        appcfg.options[appcfg.CFG_AUTO_UPDATE_TIMED] = self._autoTimed.GetValue()
        appcfg.options[appcfg.CFG_FUZZY_MATCH] = self._fuzzyMatch.GetValue()
        appcfg.Write()

        event.Skip()
