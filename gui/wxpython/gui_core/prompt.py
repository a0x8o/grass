"""
@package gui_core.prompt

@brief wxGUI command prompt

Classes:
 - prompt::GPrompt
 - prompt::GPromptSTC

(C) 2009-2014 by the GRASS Development Team

This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.

@author Martin Landa <landa.martin gmail.com>
@author Michael Barton <michael.barton@asu.edu>
@author Vaclav Petras <wenzeslaus gmail.com> (copy&paste customization)
@author Wolf Bergenheim <wolf bergenheim.net> (#962)
"""

import difflib
import sys
import shutil

import wx
import wx.stc

from grass.script import core as grass
from grass.script import task as gtask

from grass.grassdb import history

from grass.pydispatch.signal import Signal

from core import globalvar
from core import utils
from core.gcmd import EncodeString, DecodeString, GError


class GPrompt:
    """Abstract class for interactive wxGUI prompt

    Signal promptRunCmd - emitted to run command from prompt
                        - attribute 'cmd'

    See subclass GPromptPopUp and GPromptSTC.
    """

    def __init__(self, parent, giface, menuModel):
        self.parent = parent  # GConsole
        self.panel = self.parent.GetPanel()

        self.promptRunCmd = Signal("GPrompt.promptRunCmd")

        # probably only subclasses need this
        self._menuModel = menuModel

        self.mapList = self._getListOfMaps()
        self.mapsetList = utils.ListOfMapsets()

        # auto complete items
        self.autoCompList = []
        self.autoCompFilter = None

        # command description (gtask.grassTask)
        self.cmdDesc = None

        # list of traced commands
        self.commands = []

        # reload map lists when needed
        if giface:
            giface.currentMapsetChanged.connect(self._reloadListOfMaps)
            giface.grassdbChanged.connect(self._reloadListOfMaps)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> e2ac90a444 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> d69d602427 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> da1f354017 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> e2ac90a444 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> de8a1fa341 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> d241321b80 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 01a2cb48f6 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 47f2e379fb (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 46c77518c7 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> ac5d03ef05 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 8ef5c8e5e3 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 016af75c85 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> bca28e773e (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> edaa97bcbf (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 521cb8be11 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 9a37b8a6ad (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> b845e8d135 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> be93d1fccc (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> d7be28bb1b (g.proj: fix reading input WKT (#1582))
=======
=======
<<<<<<< HEAD
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> e4a266d5e1 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 24abee9ad6 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> c3243bb1bd (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main

        # reload map lists when needed
        if giface:
            giface.currentMapsetChanged.connect(self._reloadListOfMaps)
            giface.grassdbChanged.connect(self._reloadListOfMaps)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> d3904a14b8 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> d9be065247 (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> b845e8d135 (g.proj: fix reading input WKT (#1582))
>>>>>>> f296bbcae1 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> b845e8d135 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 42533ebf37 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 8fa433b01b (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> be93d1fccc (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e2ac90a444 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> d7be28bb1b (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> dd6ab211c8 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> ebd08a840c (g.proj: fix reading input WKT (#1582))
=======
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> e4a266d5e1 (g.proj: fix reading input WKT (#1582))
>>>>>>> 651687e3fd (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> e4a266d5e1 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 573458c7fe (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> d6601a1e75 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 0d53ace193 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 67baae8b16 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 9a000933e9 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 6d863be9ad (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> dc8b886312 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 17c5b80c11 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 460748a7fb (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 9fb6588182 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> a97572757d (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 10ccb1268a (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6307e79ee9 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 819b2acedb (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> c585c92c1e (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> eb742340df (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 76ed571f8d (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 1f5d06186a (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 24abee9ad6 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> da1f354017 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> c3243bb1bd (g.proj: fix reading input WKT (#1582))
>>>>>>> d69d602427 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 1411c71e15 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> d6e1feb5a7 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> dbe7a0c10a (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 2867fee4a7 (g.proj: fix reading input WKT (#1582))

        # reload map lists when needed
        if giface:
            giface.currentMapsetChanged.connect(self._reloadListOfMaps)
            giface.grassdbChanged.connect(self._reloadListOfMaps)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> d3904a14b8 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> d9be065247 (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> b845e8d135 (g.proj: fix reading input WKT (#1582))
>>>>>>> f296bbcae1 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> b845e8d135 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 42533ebf37 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 8fa433b01b (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> be93d1fccc (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e2ac90a444 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> d7be28bb1b (g.proj: fix reading input WKT (#1582))
>>>>>>> dd6ab211c8 (g.proj: fix reading input WKT (#1582))

    def _readHistory(self):
        """Get list of commands from history file"""
        hist = list()
        env = grass.gisenv()
        try:
            fileHistory = codecs.open(
                os.path.join(
                    env["GISDBASE"],
                    env["LOCATION_NAME"],
                    env["MAPSET"],
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e2ac90a444 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
                    ".wxgui_history",
                ),
                encoding="utf-8",
                mode="r",
                errors="replace",
            )
        except IOError:
            return hist

        try:
            for line in fileHistory.readlines():
                hist.append(line.replace("\n", ""))
        finally:
            fileHistory.close()

        return hist

    def _loadHistory(self):
        """Load history from a history file to data structures"""
        self.cmdbuffer = self._readHistory()
        self.cmdindex = len(self.cmdbuffer)
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))

        # reload map lists when needed
        if giface:
            giface.currentMapsetChanged.connect(self._reloadListOfMaps)
            giface.grassdbChanged.connect(self._reloadListOfMaps)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))

    def _readHistory(self):
        """Get list of commands from history file"""
        hist = list()
        env = grass.gisenv()
        try:
            fileHistory = codecs.open(
                os.path.join(
                    env["GISDBASE"],
                    env["LOCATION_NAME"],
                    env["MAPSET"],
<<<<<<< HEAD
                    ".wxgui_history",
<<<<<<< HEAD
<<<<<<< HEAD
                ),
                encoding="utf-8",
                mode="r",
                errors="replace",
            )
        except IOError:
            return hist

        try:
            for line in fileHistory.readlines():
                hist.append(line.replace("\n", ""))
        finally:
            fileHistory.close()

        return hist

    def _loadHistory(self):
        """Load history from a history file to data structures"""
        self.cmdbuffer = self._readHistory()
        self.cmdindex = len(self.cmdbuffer)
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))

    def _readHistory(self):
        """Get list of commands from history file"""
        hist = list()
        env = grass.gisenv()
        try:
            fileHistory = codecs.open(
                os.path.join(
                    env["GISDBASE"],
                    env["LOCATION_NAME"],
                    env["MAPSET"],
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e2ac90a444 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebd08a840c (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da1f354017 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
                    ".wxgui_history",
=======
                    ".bash_history",
>>>>>>> d3904a14b8 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
                    ".bash_history",
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
=======
                    ".wxgui_history",
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
                    ".bash_history",
>>>>>>> 42533ebf37 (g.proj: fix reading input WKT (#1582))
=======
                    ".wxgui_history",
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
                    ".bash_history",
>>>>>>> be93d1fccc (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e2ac90a444 (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
                ),
                encoding="utf-8",
                mode="r",
                errors="replace",
            )
        except IOError:
            return hist

        try:
            for line in fileHistory.readlines():
                hist.append(line.replace("\n", ""))
        finally:
            fileHistory.close()

        return hist

    def _loadHistory(self):
        """Load history from a history file to data structures"""
        self.cmdbuffer = self._readHistory()
        self.cmdindex = len(self.cmdbuffer)
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))

        # reload map lists when needed
        if giface:
            giface.currentMapsetChanged.connect(self._reloadListOfMaps)
            giface.grassdbChanged.connect(self._reloadListOfMaps)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))

    def _readHistory(self):
        """Get list of commands from history file"""
        hist = list()
        env = grass.gisenv()
        try:
            fileHistory = codecs.open(
                os.path.join(
                    env["GISDBASE"],
                    env["LOCATION_NAME"],
                    env["MAPSET"],
<<<<<<< HEAD
                    ".wxgui_history",
<<<<<<< HEAD
<<<<<<< HEAD
                ),
                encoding="utf-8",
                mode="r",
                errors="replace",
            )
        except IOError:
            return hist

        try:
            for line in fileHistory.readlines():
                hist.append(line.replace("\n", ""))
        finally:
            fileHistory.close()

        return hist

    def _loadHistory(self):
        """Load history from a history file to data structures"""
        self.cmdbuffer = self._readHistory()
        self.cmdindex = len(self.cmdbuffer)
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))

    def _readHistory(self):
        """Get list of commands from history file"""
        hist = list()
        env = grass.gisenv()
        try:
            fileHistory = codecs.open(
                os.path.join(
                    env["GISDBASE"],
                    env["LOCATION_NAME"],
                    env["MAPSET"],
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    ".wxgui_history",
=======
                    ".bash_history",
<<<<<<< HEAD
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
=======
                    ".wxgui_history",
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
                    ".wxgui_history",
>>>>>>> osgeo-main
=======
                    ".wxgui_history",
>>>>>>> osgeo-main
=======
                    ".bash_history",
>>>>>>> be93d1fccc (g.proj: fix reading input WKT (#1582))
=======
                    ".wxgui_history",
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
                    ".bash_history",
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
=======
                    ".wxgui_history",
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
                    ".wxgui_history",
>>>>>>> osgeo-main
=======
                    ".wxgui_history",
>>>>>>> osgeo-main
>>>>>>> main
=======
                    ".wxgui_history",
>>>>>>> osgeo-main
=======
                    ".wxgui_history",
>>>>>>> osgeo-main
=======
                    ".wxgui_history",
>>>>>>> osgeo-main
=======
                    ".wxgui_history",
>>>>>>> osgeo-main
=======
                    ".wxgui_history",
>>>>>>> osgeo-main
=======
                    ".wxgui_history",
>>>>>>> osgeo-main
=======
                    ".wxgui_history",
>>>>>>> osgeo-main
=======
                    ".wxgui_history",
>>>>>>> osgeo-main
=======
                    ".bash_history",
>>>>>>> 24abee9ad6 (g.proj: fix reading input WKT (#1582))
=======
                    ".wxgui_history",
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
                    ".wxgui_history",
>>>>>>> osgeo-main
=======
                    ".wxgui_history",
>>>>>>> osgeo-main
=======
>>>>>>> d3904a14b8 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> de8a1fa341 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    ".bash_history",
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 5202d5f7da (g.proj: fix reading input WKT (#1582))
=======
=======
=======
                    ".wxgui_history",
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 01a2cb48f6 (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> 42533ebf37 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 46c77518c7 (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
                    ".bash_history",
>>>>>>> be93d1fccc (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e2ac90a444 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 59def94d1b (g.proj: fix reading input WKT (#1582))
=======
=======
=======
                    ".wxgui_history",
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    ".bash_history",
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> ebd08a840c (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 769ad64a54 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
                    ".wxgui_history",
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 56bc21b402 (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> 573458c7fe (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e1642feb6f (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> 0d53ace193 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> dab7af79b2 (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> 9a000933e9 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 9af2478db1 (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> dc8b886312 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 2f9b4a6e73 (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> 460748a7fb (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> ab354ae66a (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> a97572757d (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 8bfd50f462 (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> 6307e79ee9 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> a6287b7801 (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> c585c92c1e (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> bc42470098 (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> 76ed571f8d (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 3b8c627dda (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
                    ".bash_history",
>>>>>>> 24abee9ad6 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> da1f354017 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 7a9bff206b (g.proj: fix reading input WKT (#1582))
=======
=======
=======
                    ".wxgui_history",
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> 1411c71e15 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 2c11751de0 (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    ".bash_history",
>>>>>>> dbe7a0c10a (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 851366e8db (g.proj: fix reading input WKT (#1582))
=======
=======
                    ".wxgui_history",
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
                    ".wxgui_history",
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
                ),
                encoding="utf-8",
                mode="r",
                errors="replace",
            )
        except IOError:
            return hist

        try:
            for line in fileHistory.readlines():
                hist.append(line.replace("\n", ""))
        finally:
            fileHistory.close()

        return hist

    def _loadHistory(self):
        """Load history from a history file to data structures"""
        self.cmdbuffer = self._readHistory()
        self.cmdindex = len(self.cmdbuffer)
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))

    def _getListOfMaps(self):
        """Get list of maps"""
        result = {}
        result["raster"] = grass.list_strings("raster")
        result["vector"] = grass.list_strings("vector")

        return result

    def _reloadListOfMaps(self):
        self.mapList = self._getListOfMaps()

    def _runCmd(self, cmdString):
        """Run command

        :param str cmdString: command to run
        """
        if not cmdString:
            return

        # parse command into list
        try:
            cmd = utils.split(str(cmdString))
        except UnicodeError:
            cmd = utils.split(EncodeString(cmdString))
        cmd = list(map(DecodeString, cmd))

        self.promptRunCmd.emit(cmd={"cmd": cmd, "cmdString": str(cmdString)})

        self.CmdErase()
        self.ShowStatusText("")

    def CopyHistory(self, targetFile):
        """Copy history file to the target location.
        Returns True if file is successfully copied."""
        env = grass.gisenv()
        historyFile = os.path.join(
            env["GISDBASE"],
            env["LOCATION_NAME"],
            env["MAPSET"],
            ".wxgui_history",
        )
        try:
            shutil.copyfile(historyFile, targetFile)
        except (IOError, OSError) as e:
            GError(
                _("Unable to copy file {} to {}'.\n\nDetails: {}").format(
                    historyFile, targetFile, e
                )
            )
            return False
        return True

    def GetCommands(self):
        """Get list of launched commands"""
        return self.commands

    def ClearCommands(self):
        """Clear list of commands"""
        del self.commands[:]


class GPromptSTC(GPrompt, wx.stc.StyledTextCtrl):
    """Styled wxGUI prompt with autocomplete and calltips"""

    def __init__(self, parent, giface, menuModel, margin=False):
        GPrompt.__init__(self, parent=parent, giface=giface, menuModel=menuModel)
        wx.stc.StyledTextCtrl.__init__(self, self.panel, id=wx.ID_ANY)

        #
        # styles
        #
        self.SetWrapMode(True)
        self.SetUndoCollection(True)

        #
        # create command and map lists for autocompletion
        #
        self.AutoCompSetIgnoreCase(False)

        #
        # line margins
        #
        # TODO print number only from cmdlog
        self.SetMarginWidth(1, 0)
        self.SetMarginWidth(2, 0)
        if margin:
            self.SetMarginType(0, wx.stc.STC_MARGIN_NUMBER)
            self.SetMarginWidth(0, 30)
        else:
            self.SetMarginWidth(0, 0)

        #
        # miscellaneous
        #
        self.SetViewWhiteSpace(False)
        self.SetUseTabs(False)
        self.UsePopUp(True)
        self.SetUseHorizontalScrollBar(True)

        # support light and dark mode
        bg_color = wx.SystemSettings().GetColour(wx.SYS_COLOUR_WINDOW)
        fg_color = wx.SystemSettings().GetColour(wx.SYS_COLOUR_WINDOWTEXT)
        selection_color = wx.SystemSettings().GetColour(wx.SYS_COLOUR_HIGHLIGHT)
        self.StyleSetBackground(wx.stc.STC_STYLE_DEFAULT, bg_color)
        self.StyleSetForeground(wx.stc.STC_STYLE_DEFAULT, fg_color)
        self.SetCaretForeground(fg_color)
        self.SetSelBackground(True, selection_color)
        self.StyleClearAll()

        # show hint
        self._showHint()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
<<<<<<< HEAD
=======
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
>>>>>>> 7733cc06c4 (Fix missing function prototypes (#2727))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d7db4d7708 (Fix missing function prototypes (#2727))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
=======
<<<<<<< HEAD
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
>>>>>>> 7733cc06c4 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
>>>>>>> d7db4d7708 (Fix missing function prototypes (#2727))
=======
=======
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c99e518a1a (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
        # read history file
        self._loadHistory()
        if giface:
            giface.currentMapsetChanged.connect(self._loadHistory)
<<<<<<< HEAD
<<<<<<< HEAD
            giface.entryToHistoryAdded.connect(
                lambda entry: self._addEntryToCmdHistoryBuffer(entry)
            )
<<<<<<< HEAD
=======
            giface.entryToHistoryAdded.connect(self._addEntryToCmdHistoryBuffer)
            giface.entryFromHistoryRemoved.connect(
                self._removeEntryFromCmdHistoryBuffer
            )
>>>>>>> 192a521175 (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
            giface.entryToHistoryAdded.connect(self._addEntryToCmdHistoryBuffer)
>>>>>>> 8135f68d14 (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
            giface.entryFromHistoryRemoved.connect(
                self._removeEntryFromCmdHistoryBuffer
            )
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c99e518a1a (Fix missing function prototypes (#2727))
=======
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> c99e518a1a (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
>>>>>>> 7733cc06c4 (Fix missing function prototypes (#2727))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
>>>>>>> d7db4d7708 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c99e518a1a (Fix missing function prototypes (#2727))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
        #
        # bindings
        #
        self.Bind(wx.EVT_WINDOW_DESTROY, self.OnDestroy)
        self.Bind(wx.EVT_CHAR, self.OnChar)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyPressed)
        self.Bind(wx.stc.EVT_STC_AUTOCOMP_SELECTION, self.OnItemSelected)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemChanged)
        if sys.platform != "darwin":  # unstable on Mac with wxPython 3
            self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
            self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)

        # signal which requests showing of a notification
        self.showNotification = Signal("GPromptSTC.showNotification")

        # signal to notify selected command
        self.commandSelected = Signal("GPromptSTC.commandSelected")

    def OnTextSelectionChanged(self, event):
        """Copy selected text to clipboard and skip event.
        The same function is in GStc class (goutput.py).
        """
        wx.CallAfter(self.Copy)
        event.Skip()

    def OnItemChanged(self, event):
        """Change text in statusbar
        if the item selection in the auto-completion list is changed"""
        # list of commands
        if self.toComplete["entity"] == "command":
            item = (
                self.toComplete["cmd"].rpartition(".")[0]
                + "."
                + self.autoCompList[event.GetIndex()]
            )
            try:
                nodes = self._menuModel.SearchNodes(key="command", value=item)
                desc = ""
                if nodes:
                    self.commandSelected.emit(command=item)
                    desc = nodes[0].data["description"]
            except KeyError:
                desc = ""
            self.ShowStatusText(desc)
        # list of flags
        elif self.toComplete["entity"] == "flags":
            desc = self.cmdDesc.get_flag(self.autoCompList[event.GetIndex()])[
                "description"
            ]
            self.ShowStatusText(desc)
        # list of parameters
        elif self.toComplete["entity"] == "params":
            item = self.cmdDesc.get_param(self.autoCompList[event.GetIndex()])
            desc = item["name"] + "=" + item["type"]
            if not item["required"]:
                desc = "[" + desc + "]"
            desc += ": " + item["description"]
            self.ShowStatusText(desc)
        # list of flags and commands
        elif self.toComplete["entity"] == "params+flags":
            if self.autoCompList[event.GetIndex()][0] == "-":
                desc = self.cmdDesc.get_flag(
                    self.autoCompList[event.GetIndex()].strip("-")
                )["description"]
            else:
                item = self.cmdDesc.get_param(self.autoCompList[event.GetIndex()])
                desc = item["name"] + "=" + item["type"]
                if not item["required"]:
                    desc = "[" + desc + "]"
                desc += ": " + item["description"]
            self.ShowStatusText(desc)
        else:
            self.ShowStatusText("")

    def OnItemSelected(self, event):
        """Item selected from the list"""
        lastWord = self.GetWordLeft()
        # to insert selection correctly if selected word partly matches written
        # text
        match = difflib.SequenceMatcher(None, event.GetText(), lastWord)
        matchTuple = match.find_longest_match(0, len(event.GetText()), 0, len(lastWord))

        compl = event.GetText()[matchTuple[2] :]
        text = self.GetTextLeft() + compl
        # add space or '=' at the end
        end = "="
        for char in (".", "-", "="):
            if text.split(" ")[-1].find(char) >= 0:
                end = " "

        compl += end
        text += end

        self.AddText(compl)
        pos = len(text)
        self.SetCurrentPos(pos)

        cmd = text.strip().split(" ")[0]

        if not self.cmdDesc or cmd != self.cmdDesc.get_name():
            try:
                self.cmdDesc = gtask.parse_interface(cmd)
            except OSError:
                self.cmdDesc = None

    def _showHint(self):
        """Shows usability hint"""
        self.StyleSetForeground(0, wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT))
        self.WriteText(_("Type command here and press Enter"))
        self._hint_shown = True

    def _hideHint(self):
        """Hides usability hint"""
        if self._hint_shown:
            self.ClearAll()
            self.StyleSetForeground(
                0, wx.SystemSettings().GetColour(wx.SYS_COLOUR_WINDOWTEXT)
            )
            self._hint_shown = False

    def OnKillFocus(self, event):
        """Hides autocomplete and shows hint"""
        # hide autocomplete
        if self.AutoCompActive():
            self.AutoCompCancel()
        # show hint
        if self.IsEmpty():
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            self._showHint()
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
            self._showHint()
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
=======
<<<<<<< HEAD
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 7733cc06c4 (Fix missing function prototypes (#2727))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d7db4d7708 (Fix missing function prototypes (#2727))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c99e518a1a (Fix missing function prototypes (#2727))
=======
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
            self._showHint()
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 7733cc06c4 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d7db4d7708 (Fix missing function prototypes (#2727))
=======
=======
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c99e518a1a (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
            wx.CallAfter(self._showHint)
=======
            self._showHint()
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7733cc06c4 (Fix missing function prototypes (#2727))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d7db4d7708 (Fix missing function prototypes (#2727))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c99e518a1a (Fix missing function prototypes (#2727))
=======
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
            self._showHint()
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
>>>>>>> c99e518a1a (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
=======
            self._showHint()
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
=======
=======
            self._showHint()
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
>>>>>>> 7733cc06c4 (Fix missing function prototypes (#2727))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
>>>>>>> d7db4d7708 (Fix missing function prototypes (#2727))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
>>>>>>> c99e518a1a (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
        event.Skip()

    def OnSetFocus(self, event):
        """Prepares prompt for entering commands."""
        self._hideHint()
        event.Skip()

    def SetTextAndFocus(self, text):
        pos = len(text)
        self.commandSelected.emit(command=text)
        self.SetText(text)
        self.SetSelectionStart(pos)
        self.SetCurrentPos(pos)
        self.SetFocus()

    def _loadHistory(self):
        """Load history from a history file to data structures"""
        try:
            history_path = history.get_current_mapset_gui_history_path()
            history.ensure_history_file(history_path)
            self.cmdbuffer = [
                entry["command"] for entry in history.read(history_path)
            ] or []
            self.cmdindex = len(self.cmdbuffer)
        except (OSError, ValueError) as e:
            GError(str(e))

    def _addEntryToCmdHistoryBuffer(self, entry):
        """Add entry to command history buffer.

        :param entry dict: entry with 'command' and 'command_info' keys
        command value is a string.
        """
        # create command string
        entry = entry["command"]
        # add command to history
        self.cmdbuffer.append(entry)
        # update also traced commands
        self.commands.append(entry)

        # keep command history to a manageable size
        if len(self.cmdbuffer) > 200:
            del self.cmdbuffer[0]
        self.cmdindex = len(self.cmdbuffer)

    def _removeEntryFromCmdHistoryBuffer(self, index):
        """Remove entry from command history buffer.
        :param index: index of deleted command
        """
        # remove command at the given index from history buffer
        if index < len(self.cmdbuffer):
            self.cmdbuffer.pop(index)

        # update cmd index size
        self.cmdindex = len(self.cmdbuffer)

    def EntityToComplete(self):
        """Determines which part of command (flags, parameters) should
        be completed at current cursor position"""
        entry = self.GetTextLeft()
        toComplete = {"cmd": None, "entity": None}
        try:
            cmd = entry.split()[0].strip()
        except IndexError:
            return toComplete

        try:
            splitted = utils.split(str(entry))
        except ValueError:  # No closing quotation error
            return toComplete
        if len(splitted) > 0 and cmd in globalvar.grassCmd:
            toComplete["cmd"] = cmd
            if entry[-1] == " ":
                words = entry.split(" ")
                if any(word.startswith("-") for word in words):
                    toComplete["entity"] = "params"
                else:
                    toComplete["entity"] = "params+flags"
            else:
                # get word left from current position
                word = self.GetWordLeft(withDelimiter=True)

                if word[0] == "=" and word[-1] == "@":
                    toComplete["entity"] = "mapsets"
                elif word[0] == "=":
                    # get name of parameter
                    paramName = self.GetWordLeft(
                        withDelimiter=False, ignoredDelimiter="="
                    ).strip("=")
                    if paramName:
                        try:
                            param = self.cmdDesc.get_param(paramName)
                        except (ValueError, AttributeError):
                            return toComplete
                    else:
                        return toComplete

                    if param["values"]:
                        toComplete["entity"] = "param values"
                    elif param["prompt"] == "raster" and param["element"] == "cell":
                        toComplete["entity"] = "raster map"
                    elif param["prompt"] == "vector" and param["element"] == "vector":
                        toComplete["entity"] = "vector map"
                elif word[0] == "-":
                    toComplete["entity"] = "flags"
                elif word[0] == " ":
                    toComplete["entity"] = "params"
        else:
            toComplete["entity"] = "command"
            toComplete["cmd"] = cmd

        return toComplete

    def GetWordLeft(self, withDelimiter=False, ignoredDelimiter=None):
        """Get word left from current cursor position. The beginning
        of the word is given by space or chars: .,-=

        :param withDelimiter: returns the word with the initial delimiter
        :param ignoredDelimiter: finds the word ignoring certain delimiter
        """
        textLeft = self.GetTextLeft()

        parts = []
        if ignoredDelimiter is None:
            ignoredDelimiter = ""

        for char in set(" .,-=") - set(ignoredDelimiter):
            delimiter = "" if not withDelimiter else char
            parts.append(delimiter + textLeft.rpartition(char)[2])
        return min(parts, key=len)

    def ShowList(self):
        """Show sorted auto-completion list if it is not empty"""
        if len(self.autoCompList) > 0:
            self.autoCompList.sort()
            self.AutoCompShow(0, itemList=" ".join(self.autoCompList))

    def OnKeyPressed(self, event):
        """Key pressed capture special treatment for tabulator to show help"""
        pos = self.GetCurrentPos()
        if event.GetKeyCode() == wx.WXK_TAB:
            # show GRASS command calltips (to hide press 'ESC')
            entry = self.GetTextLeft()
            try:
                cmd = entry.split()[0].strip()
            except IndexError:
                cmd = ""

            if cmd not in globalvar.grassCmd:
                return

            info = gtask.command_info(cmd)

            self.CallTipSetBackground("#f4f4d1")
            self.CallTipSetForeground("BLACK")
            self.CallTipShow(pos, info["usage"] + "\n\n" + info["description"])
        elif (
            event.GetKeyCode() in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER)
            and not self.AutoCompActive()
        ):
            # run command on line when <return> is pressed
            self._runCmd(self.GetCurLine()[0].strip())
        elif (
            event.GetKeyCode() in [wx.WXK_UP, wx.WXK_DOWN] and not self.AutoCompActive()
        ):
            # Command history using up and down
            if len(self.cmdbuffer) < 1:
                return

            self.DocumentEnd()

            # move through command history list index values
            if event.GetKeyCode() == wx.WXK_UP:
                self.cmdindex -= 1
            if event.GetKeyCode() == wx.WXK_DOWN:
<<<<<<< HEAD
                self.cmdindex += 1
=======
                self.cmdindex = self.cmdindex + 1
>>>>>>> e9b8764134 (style: Fixes if-stmt-min-max (PLR1730) (#3950))
            self.cmdindex = max(self.cmdindex, 0)
            self.cmdindex = min(self.cmdindex, len(self.cmdbuffer) - 1)

            try:
                # without strip causes problem on windows
                txt = self.cmdbuffer[self.cmdindex].strip()
            except KeyError:
                txt = ""

            # clear current line and insert command history
            self.DelLineLeft()
            self.DelLineRight()
            pos = self.GetCurrentPos()
            self.InsertText(pos, txt)
            self.LineEnd()

            self.ShowStatusText("")
        else:
            event.Skip()

    def OnChar(self, event):
        """Key char capture for autocompletion, calltips, and command history

        .. todo::
            event.ControlDown() for manual autocomplete
        """
        # keycodes used: "." = 46, "=" = 61, "-" = 45
        pos = self.GetCurrentPos()
        # complete command after pressing '.'
        if event.GetKeyCode() == 46:
            self.autoCompList = []
<<<<<<< HEAD
=======
            entry = self.GetTextLeft()
>>>>>>> 962f525ded (style: Fixes unnecessary-collection-call (C408) for empty collections (#3945))
            self.InsertText(pos, ".")
            self.CharRight()
            self.toComplete = self.EntityToComplete()
            try:
                if self.toComplete["entity"] == "command":
                    for command in globalvar.grassCmd:
                        try:
                            if command.find(self.toComplete["cmd"]) == 0:
                                dotNumber = list(self.toComplete["cmd"]).count(".")
                                self.autoCompList.append(
                                    command.split(".", dotNumber)[-1]
                                )
                        except UnicodeDecodeError as error:
                            sys.stderr.write(DecodeString(command) + ": " + str(error))

            except (KeyError, TypeError):
                return
            self.ShowList()

        # complete flags after pressing '-'
        elif (
            (event.GetKeyCode() == 45)
            or event.GetKeyCode() == wx.WXK_NUMPAD_SUBTRACT
            or event.GetKeyCode() == wx.WXK_SUBTRACT
        ):
            self.autoCompList = []
<<<<<<< HEAD
=======
            entry = self.GetTextLeft()
>>>>>>> 962f525ded (style: Fixes unnecessary-collection-call (C408) for empty collections (#3945))
            self.InsertText(pos, "-")
            self.CharRight()
            self.toComplete = self.EntityToComplete()
            if self.toComplete["entity"] == "flags" and self.cmdDesc:
                if self.GetTextLeft()[-2:] == " -":  # complete e.g. --quite
                    for flag in self.cmdDesc.get_options()["flags"]:
                        if len(flag["name"]) == 1:
                            self.autoCompList.append(flag["name"])
                else:
                    for flag in self.cmdDesc.get_options()["flags"]:
                        if len(flag["name"]) > 1:
                            self.autoCompList.append(flag["name"])
            self.ShowList()

        # complete map or values after parameter
        elif event.GetKeyCode() == 61:
            self.autoCompList = []
            self.InsertText(pos, "=")
            self.CharRight()
            self.toComplete = self.EntityToComplete()
            if self.toComplete["entity"] == "raster map":
                self.autoCompList = self.mapList["raster"]
            elif self.toComplete["entity"] == "vector map":
                self.autoCompList = self.mapList["vector"]
            elif self.toComplete["entity"] == "param values":
                param = self.GetWordLeft(
                    withDelimiter=False, ignoredDelimiter="="
                ).strip(" =")
                self.autoCompList = self.cmdDesc.get_param(param)["values"]
            self.ShowList()

        # complete mapset ('@')
        elif event.GetKeyCode() == 64:
            self.autoCompList = []
            self.InsertText(pos, "@")
            self.CharRight()
            self.toComplete = self.EntityToComplete()

            if self.toComplete["entity"] == "mapsets":
                self.autoCompList = self.mapsetList
            self.ShowList()

        # complete after pressing CTRL + Space
        elif event.GetKeyCode() == wx.WXK_SPACE and event.ControlDown():
            self.autoCompList = []
            self.toComplete = self.EntityToComplete()

            # complete command
            if self.toComplete["entity"] == "command":
                for command in globalvar.grassCmd:
                    if command.find(self.toComplete["cmd"]) == 0:
                        dotNumber = list(self.toComplete["cmd"]).count(".")
                        self.autoCompList.append(command.split(".", dotNumber)[-1])

            # complete flags in such situations (| is cursor):
            # r.colors -| ...w, q, l
            # r.colors -w| ...w, q, l
            elif self.toComplete["entity"] == "flags" and self.cmdDesc:
                for flag in self.cmdDesc.get_options()["flags"]:
                    if len(flag["name"]) == 1:
                        self.autoCompList.append(flag["name"])

            # complete parameters in such situations (| is cursor):
            # r.colors -w | ...color, map, rast, rules
            # r.colors col| ...color
            elif self.toComplete["entity"] == "params" and self.cmdDesc:
                for param in self.cmdDesc.get_options()["params"]:
                    if param["name"].find(self.GetWordLeft(withDelimiter=False)) == 0:
                        self.autoCompList.append(param["name"])

            # complete flags or parameters in such situations (| is cursor):
            # r.colors | ...-w, -q, -l, color, map, rast, rules
            # r.colors color=grey | ...-w, -q, -l, color, map, rast, rules
            elif self.toComplete["entity"] == "params+flags" and self.cmdDesc:
                self.autoCompList = []

                for param in self.cmdDesc.get_options()["params"]:
                    self.autoCompList.append(param["name"])
                for flag in self.cmdDesc.get_options()["flags"]:
                    if len(flag["name"]) == 1:
                        self.autoCompList.append("-" + flag["name"])
                    else:
                        self.autoCompList.append("--" + flag["name"])

                self.ShowList()

            # complete map or values after parameter
            # r.buffer input=| ...list of raster maps
            # r.buffer units=| ... feet, kilometers, ...
            elif self.toComplete["entity"] == "raster map":
                self.autoCompList = []
                self.autoCompList = self.mapList["raster"]
            elif self.toComplete["entity"] == "vector map":
                self.autoCompList = []
                self.autoCompList = self.mapList["vector"]
            elif self.toComplete["entity"] == "param values":
                self.autoCompList = []
                param = self.GetWordLeft(
                    withDelimiter=False, ignoredDelimiter="="
                ).strip(" =")
                self.autoCompList = self.cmdDesc.get_param(param)["values"]

            self.ShowList()

        elif event.GetKeyCode() == wx.WXK_SPACE:
            items = self.GetTextLeft().split()
            if len(items) == 1:
                cmd = items[0].strip()
                if cmd in globalvar.grassCmd and (
                    not self.cmdDesc or cmd != self.cmdDesc.get_name()
                ):
                    try:
                        self.cmdDesc = gtask.parse_interface(cmd)
                    except OSError:
                        self.cmdDesc = None
            event.Skip()

        else:
            event.Skip()

    def ShowStatusText(self, text):
        """Requests showing of notification, e.g. showing in a statusbar."""
        self.showNotification.emit(message=text)

    def GetTextLeft(self):
        """Returns all text left of the caret"""
        pos = self.GetCurrentPos()
        self.HomeExtend()
        entry = self.GetSelectedText()
        self.SetCurrentPos(pos)

        return entry

    def OnDestroy(self, event):
        """The clipboard contents can be preserved after
        the app has exited"""
        if wx.TheClipboard.IsOpened():
            wx.TheClipboard.Flush()
        event.Skip()

    def CmdErase(self):
        """Erase command prompt"""
        self.Home()
        self.DelLineRight()
