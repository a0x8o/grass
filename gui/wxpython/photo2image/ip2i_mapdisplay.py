"""
@package photo2image.ip2i_mapdisplay
@brief Display to manage ground control points with two toolbars, one
for various display management functions, one for manipulating GCPs.
Classes:
- mapdisplay::MapPanel
(C) 2006-2011 by the GRASS Development Team
This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.
@author Markus Metz
"""

import os
import platform

from core import globalvar
import wx
import wx.aui

from mapdisp.toolbars import MapToolbar
from gcp.toolbars import GCPDisplayToolbar, GCPManToolbar
from mapdisp.gprint import PrintOptions
from core.gcmd import GMessage
from gui_core.dialogs import GetImageHandlers, ImageSizeDialog
from gui_core.mapdisp import SingleMapPanel
from gui_core.wrap import Menu
from mapwin.buffered import BufferedMapWindow

import mapdisp.statusbar as sb
import gcp.statusbar as sbgcp

# for standalone app
cmdfilename = None


class MapPanel(SingleMapPanel):
    """Main panel for map display window. Drawing takes place in
    child double buffered drawing window.
    """

    def __init__(
        self,
        parent,
        giface,
        title=_("GRASS GIS Manage Location of Tick Points on a Scanned Photo"),
        toolbars=["gcpdisp"],
        Map=None,
        auimgr=None,
        name="GCPMapWindow",
        **kwargs,
    ):
        """Main map display window with toolbars, statusbar and
        DrawWindow
        :param giface: GRASS interface instance
        :param title: window title
        :param toolbars: array of activated toolbars, e.g. ['map', 'digit']
        :param map: instance of render.Map
        :param auimgs: AUI manager
        :param kwargs: wx.Frame attributes
        """

        SingleMapPanel.__init__(
            self,
            parent=parent,
            giface=giface,
            title=title,
            Map=Map,
            auimgr=auimgr,
            name=name,
            **kwargs,
        )

        self._giface = giface

        self.mapWindowProperties.alignExtent = True

        #
        # Add toolbars
        #
        for toolb in toolbars:
            self.AddToolbar(toolb)

        self.activemap = self.toolbars["gcpdisp"].togglemap
        self.activemap.SetSelection(0)

        self.SrcMap = self.grwiz.SrcMap  # instance of render.Map
        self.TgtMap = self.grwiz.TgtMap  # instance of render.Map
        self._mgr.SetDockSizeConstraint(0.5, 0.5)

        #
        # Add statusbar
        #

        # items for choice
        statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sbgcp.SbGoToGCP,
            sbgcp.SbRMSError,
        ]

        # create statusbar and its manager
        self.statusbar = self.CreateStatusbar(statusbarItems)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 149493a965 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4e96740dbd (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9890cdb67e (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 010ce4879d (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 621bf8524c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3af5373555 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de32f09541 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2c6590ffd (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 74f41ca644 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f83f32f68c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 008d590ac9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 693b38ddef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> cb67a2190f (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
=======
=======
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 96263f4797 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 96263f4797 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 085d58c6be (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c7bce671b (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 96263f4797 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> osgeo-main
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c7bce671b (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 2f9dd78a3c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 008d590ac9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 693b38ddef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> e7579ce5b9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> a26da7d1f7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 524f6f69f9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 0b789a422a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 8c3ec54d26 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 149493a965 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 8d52a1c863 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 4e96740dbd (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> ce9d75290d (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 9890cdb67e (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> c46a4c7962 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 010ce4879d (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 90ad523f8c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 621bf8524c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 5dad4218c6 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 3af5373555 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cb67a2190f (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> db5e75f509 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> d26895c7cf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> de32f09541 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> d62b25491c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> f2c6590ffd (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 5c7bce671b (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 74f41ca644 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> f83f32f68c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 96263f4797 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 008d590ac9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 693b38ddef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))

        #
        # Init map display (buffered DC & set default cursor)
        #
        self.grwiz.SwitchEnv("source")
        self.SrcMapWindow = BufferedMapWindow(
            parent=self,
            giface=self._giface,
            id=wx.ID_ANY,
            properties=self.mapWindowProperties,
            Map=self.SrcMap,
        )

        self.grwiz.SwitchEnv("target")
        self.TgtMapWindow = BufferedMapWindow(
            parent=self,
            giface=self._giface,
            id=wx.ID_ANY,
            properties=self.mapWindowProperties,
            Map=self.TgtMap,
        )
        self.MapWindow = self.SrcMapWindow
        self.Map = self.SrcMap
        self._setUpMapWindow(self.SrcMapWindow)
        self._setUpMapWindow(self.TgtMapWindow)
        self.SrcMapWindow.SetNamedCursor("cross")
        self.TgtMapWindow.SetNamedCursor("cross")
        # used to switch current map (combo box in toolbar)
        self.SrcMapWindow.mouseEntered.connect(
            lambda: self._setActiveMapWindow(self.SrcMapWindow)
        )
        self.TgtMapWindow.mouseEntered.connect(
            lambda: self._setActiveMapWindow(self.TgtMapWindow)
        )

        #
        # initialize region values
        #
        self._initMap(Map=self.SrcMap)
        self._initMap(Map=self.TgtMap)

        self.GetMapToolbar().SelectDefault()

        #
        # Bind various events
        #
        self.activemap.Bind(wx.EVT_CHOICE, self.OnUpdateActive)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        #
        # Update fancy gui style
        #
        # AuiManager wants a CentrePane, workaround to get two equally sized
        # windows
        self.list = self.CreateGCPList()

        # set Go To GCP item as active in statusbar
        self.mapWindowProperties.sbItem = 5

        # self.SrcMapWindow.SetSize((300, 300))
        # self.TgtMapWindow.SetSize((300, 300))
        self.list.SetSize((100, 150))
        self._addPanes()

        srcwidth, srcheight = self.SrcMapWindow.GetSize()
        tgtwidth, tgtheight = self.TgtMapWindow.GetSize()
        srcwidth = (srcwidth + tgtwidth) / 2
        self._mgr.GetPane("target").Hide()
        self._mgr.Update()
        self._mgr.GetPane("source").BestSize((srcwidth, srcheight))
        self._mgr.GetPane("target").BestSize((srcwidth, srcheight))
        if self.show_target:
            self._mgr.GetPane("target").Show()
        else:
            self.activemap.Enable(False)
        # needed by Mac OS, does not harm on Linux, breaks display on Windows
        if platform.system() != "Windows":
            self._mgr.Update()

        #
        # Init print module and classes
        #
        self.printopt = PrintOptions(self, self.MapWindow)

        #
        # Initialization of digitization tool
        #
        self.digit = None

        # set active map
        self.MapWindow = self.SrcMapWindow
        self.Map = self.SrcMap

        # do not init zoom history here, that happens when zooming to map(s)

        #
        # Re-use dialogs
        #
        self.dialogs = {}
        self.dialogs["attributes"] = None
        self.dialogs["category"] = None
        self.dialogs["barscale"] = None
        self.dialogs["legend"] = None

        self.decorationDialog = None  # decoration/overlays

    def _setUpMapWindow(self, mapWindow):
        # TODO: almost the same implementation as for MapPanelBase (only names differ)
        # enable or disable zoom history tool
        mapWindow.zoomHistoryAvailable.connect(
            lambda: self.GetMapToolbar().Enable("zoomback", enable=True)
        )
        mapWindow.zoomHistoryUnavailable.connect(
            lambda: self.GetMapToolbar().Enable("zoomback", enable=False)
        )
        mapWindow.mouseMoving.connect(self.CoordinatesChanged)

    def AddToolbar(self, name):
        """Add defined toolbar to the window
        Currently known toolbars are:
         - 'map'     - basic map toolbar
         - 'gcpdisp' - GCP Manager, Display
         - 'gcpman'  - GCP Manager, points management
         - 'nviz'    - 3D view mode
        """
        # default toolbar
        if name == "map":
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 149493a965 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4e96740dbd (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 9890cdb67e (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 010ce4879d (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 621bf8524c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3af5373555 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> db5e75f509 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> de32f09541 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f2c6590ffd (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cb67a2190f (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
=======
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
=======
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 008d590ac9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f814ffff83 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 693b38ddef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 085d58c6be (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5c7bce671b (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 74f41ca644 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f83f32f68c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 5c7bce671b (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 74f41ca644 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> f83f32f68c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 96263f4797 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 2f9dd78a3c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 008d590ac9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> e7579ce5b9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> a26da7d1f7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 524f6f69f9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 0b789a422a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 8c3ec54d26 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 149493a965 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 8d52a1c863 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 4e96740dbd (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> ce9d75290d (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 9890cdb67e (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> c46a4c7962 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 010ce4879d (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 90ad523f8c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 621bf8524c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 5dad4218c6 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 3af5373555 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cb67a2190f (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> db5e75f509 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> d26895c7cf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> de32f09541 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> d62b25491c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> f2c6590ffd (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 085d58c6be (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5c7bce671b (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 74f41ca644 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f83f32f68c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 96263f4797 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 008d590ac9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> f814ffff83 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 693b38ddef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
            if "map" not in self.toolbars:
                self.toolbars["map"] = MapToolbar(
                    self, self._toolSwitcher, self._giface
                )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb67a2190f (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
=======
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 74f41ca644 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f83f32f68c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> main
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 524f6f69f9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0b789a422a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8c3ec54d26 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 149493a965 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d52a1c863 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 4e96740dbd (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ce9d75290d (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 9890cdb67e (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c46a4c7962 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 010ce4879d (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90ad523f8c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 621bf8524c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5dad4218c6 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 3af5373555 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d26895c7cf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> de32f09541 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d62b25491c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> f2c6590ffd (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 085d58c6be (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 5c7bce671b (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 5c7bce671b (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 74f41ca644 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f83f32f68c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 008d590ac9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 693b38ddef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> osgeo-main
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 2f9dd78a3c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> e7579ce5b9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> a26da7d1f7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 524f6f69f9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 0b789a422a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8c3ec54d26 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 149493a965 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8d52a1c863 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 4e96740dbd (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> ce9d75290d (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 9890cdb67e (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c46a4c7962 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 010ce4879d (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 90ad523f8c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 621bf8524c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 5dad4218c6 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 3af5373555 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cb67a2190f (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> db5e75f509 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> d26895c7cf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> de32f09541 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> d62b25491c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> f2c6590ffd (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 085d58c6be (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 5c7bce671b (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 74f41ca644 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> f83f32f68c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 96263f4797 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 008d590ac9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> f814ffff83 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 693b38ddef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))

            self._mgr.AddPane(
                self.toolbars["map"],
                wx.aui.AuiPaneInfo()
                .Name("maptoolbar")
                .Caption(_("Map Toolbar"))
                .ToolbarPane()
                .Top()
                .LeftDockable(False)
                .RightDockable(False)
                .BottomDockable(False)
                .TopDockable(True)
                .CloseButton(False)
                .Layer(2)
                .BestSize(self.toolbars["map"].GetSize()),
            )

        # GCP display
        elif name == "gcpdisp":
            if "gcpdisp" not in self.toolbars:
                self.toolbars["gcpdisp"] = GCPDisplayToolbar(self, self._toolSwitcher)

            self._mgr.AddPane(
                self.toolbars["gcpdisp"],
                wx.aui.AuiPaneInfo()
                .Name("gcpdisplaytoolbar")
                .Caption(_("GCP Display toolbar"))
                .ToolbarPane()
                .Top()
                .LeftDockable(False)
                .RightDockable(False)
                .BottomDockable(False)
                .TopDockable(True)
                .CloseButton(False)
                .Layer(2),
            )

            if self.show_target is False:
                self.toolbars["gcpdisp"].Enable("zoommenu", enable=False)

            if "gcpman" not in self.toolbars:
                self.toolbars["gcpman"] = GCPManToolbar(self)

            self._mgr.AddPane(
                self.toolbars["gcpman"],
                wx.aui.AuiPaneInfo()
                .Name("gcpmanagertoolbar")
                .Caption(_("GCP Manager toolbar"))
                .ToolbarPane()
                .Top()
                .Row(1)
                .LeftDockable(False)
                .RightDockable(False)
                .BottomDockable(False)
                .TopDockable(True)
                .CloseButton(False)
                .Layer(2),
            )

        self._mgr.Update()

    def _addPanes(self):
        """Add mapwindows, toolbars and statusbar to aui manager"""
        self._mgr.AddPane(
            self.list,
            wx.aui.AuiPaneInfo()
            .Name("gcplist")
            .Caption(_("GCP List"))
            .LeftDockable(False)
            .RightDockable(False)
            .PinButton()
            .FloatingSize((600, 200))
            .CloseButton(False)
            .DestroyOnClose(True)
            .Top()
            .Layer(1)
            .MinSize((200, 100)),
        )
        self._mgr.AddPane(
            self.SrcMapWindow,
            wx.aui.AuiPaneInfo()
            .Name("source")
            .Caption(_("Source Display"))
            .Dockable(False)
            .CloseButton(False)
            .DestroyOnClose(True)
            .Floatable(False)
            .Centre(),
        )
        self._mgr.AddPane(
            self.TgtMapWindow,
            wx.aui.AuiPaneInfo()
            .Name("target")
            .Caption(_("Target Display"))
            .Dockable(False)
            .CloseButton(False)
            .DestroyOnClose(True)
            .Floatable(False)
            .Right()
            .Layer(0),
        )
        # statusbar
        self.AddStatusbarPane()

    def OnUpdateProgress(self, event):
        """
        Update progress bar info
        """
        self.GetProgressBar().UpdateProgress(event.layer, event.map)

        event.Skip()

    def OnFocus(self, event):
        """
        Change choicebook page to match display.
        Or set display for georectifying
        """
        # was in if layer manager but considering the state it was executed
        # always, moreover, there is no layer manager dependent code

        # in GCP Management, set focus to current MapWindow for mouse actions
        self.OnPointer(event)
        self.MapWindow.SetFocus()

        event.Skip()

    def OnDraw(self, event):
        """Re-display current map composition"""
        self.MapWindow.UpdateMap(render=False)

    def OnRender(self, event):
        """Re-render map composition (each map layer)"""
        # FIXME: remove qlayer code or use RemoveQueryLayer() now in mapdisp.frame
        # delete tmp map layers (queries)
        qlayer = self.Map.GetListOfLayers(name=globalvar.QUERYLAYER)
        for layer in qlayer:
            self.Map.DeleteLayer(layer)

        self.SrcMapWindow.UpdateMap(render=True)
        if self.show_target:
            self.TgtMapWindow.UpdateMap(render=True)

        # update statusbar
        self.StatusbarUpdate()

    def OnPointer(self, event):
        """Pointer button clicked"""
        self.SrcMapWindow.SetModePointer()
        self.TgtMapWindow.SetModePointer()
        # change the default cursor
        self.SrcMapWindow.SetNamedCursor("cross")
        self.TgtMapWindow.SetNamedCursor("cross")

    def OnZoomIn(self, event):
        """Zoom in the map."""
        self.SrcMapWindow.SetModeZoomIn()
        self.TgtMapWindow.SetModeZoomIn()

    def OnZoomOut(self, event):
        """Zoom out the map."""
        self.SrcMapWindow.SetModeZoomOut()
        self.TgtMapWindow.SetModeZoomOut()

    def OnPan(self, event):
        """Panning, set mouse to drag"""
        self.SrcMapWindow.SetModePan()
        self.TgtMapWindow.SetModePan()

    def OnErase(self, event):
        """
        Erase the canvas
        """
        self.MapWindow.EraseMap()

        if self.MapWindow == self.SrcMapWindow:
            win = self.TgtMapWindow
        elif self.MapWindow == self.TgtMapWindow:
            win = self.SrcMapWindow

        win.EraseMap()

    def SaveToFile(self, event):
        """Save map to image"""
        img = self.MapWindow.img
        if not img:
            GMessage(
                parent=self,
                message=_("Nothing to render (empty map). Operation canceled."),
            )
            return
        filetype, ltype = GetImageHandlers(img)

        # get size
        dlg = ImageSizeDialog(self)
        dlg.CentreOnParent()
        if dlg.ShowModal() != wx.ID_OK:
            dlg.Destroy()
            return
        width, height = dlg.GetValues()
        dlg.Destroy()

        # get filename
        dlg = wx.FileDialog(
            parent=self,
            message=_(
                "Choose a file name to save the image (no need to add extension)"
            ),
            wildcard=filetype,
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
        )

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            if not path:
                dlg.Destroy()
                return

            base, ext = os.path.splitext(path)
            fileType = ltype[dlg.GetFilterIndex()]["type"]
            extType = ltype[dlg.GetFilterIndex()]["ext"]
            if ext != extType:
                path = base + "." + extType

            self.MapWindow.SaveToFile(path, fileType, width, height)

        dlg.Destroy()

    def PrintMenu(self, event):
        """
        Print options and output menu for map display
        """
        printmenu = Menu()
        # Add items to the menu
        setup = wx.MenuItem(printmenu, wx.ID_ANY, _("Page setup"))
        printmenu.AppendItem(setup)
        self.Bind(wx.EVT_MENU, self.printopt.OnPageSetup, setup)

        preview = wx.MenuItem(printmenu, wx.ID_ANY, _("Print preview"))
        printmenu.AppendItem(preview)
        self.Bind(wx.EVT_MENU, self.printopt.OnPrintPreview, preview)

        doprint = wx.MenuItem(printmenu, wx.ID_ANY, _("Print display"))
        printmenu.AppendItem(doprint)
        self.Bind(wx.EVT_MENU, self.printopt.OnDoPrint, doprint)

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(printmenu)
        printmenu.Destroy()

    def OnZoomToRaster(self, event):
        """
        Set display extents to match selected raster map (ignore NULLs)
        """
        self.MapWindow.ZoomToMap(ignoreNulls=True)

    def OnZoomToSaved(self, event):
        """Set display geometry to match extents in
        saved region file
        """
        self.MapWindow.SetRegion(zoomOnly=True)

    def OnDisplayToWind(self, event):
        """Set computational region (WIND file) to match display
        extents
        """
        self.MapWindow.DisplayToWind()

    def SaveDisplayRegion(self, event):
        """Save display extents to named region file."""
        self.MapWindow.SaveDisplayRegion()

    def OnZoomMenu(self, event):
        """Popup Zoom menu"""
        zoommenu = Menu()
        # Add items to the menu

        zoomwind = wx.MenuItem(
            zoommenu, wx.ID_ANY, _("Zoom to computational region (set with g.region)")
        )
        zoommenu.AppendItem(zoomwind)
        self.Bind(wx.EVT_MENU, self.OnZoomToWind, zoomwind)

        zoomdefault = wx.MenuItem(zoommenu, wx.ID_ANY, _("Zoom to default region"))
        zoommenu.AppendItem(zoomdefault)
        self.Bind(wx.EVT_MENU, self.OnZoomToDefault, zoomdefault)

        zoomsaved = wx.MenuItem(zoommenu, wx.ID_ANY, _("Zoom to saved region"))
        zoommenu.AppendItem(zoomsaved)
        self.Bind(wx.EVT_MENU, self.OnZoomToSaved, zoomsaved)

        savewind = wx.MenuItem(
            zoommenu, wx.ID_ANY, _("Set computational region from display")
        )
        zoommenu.AppendItem(savewind)
        self.Bind(wx.EVT_MENU, self.OnDisplayToWind, savewind)

        savezoom = wx.MenuItem(
            zoommenu, wx.ID_ANY, _("Save display geometry to named region")
        )
        zoommenu.AppendItem(savezoom)
        self.Bind(wx.EVT_MENU, self.SaveDisplayRegion, savezoom)

        # Popup the menu. If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(zoommenu)
        zoommenu.Destroy()

    def GetSrcWindow(self):
        return self.SrcMapWindow

    def GetTgtWindow(self):
        return self.TgtMapWindow

    def GetShowTarget(self):
        return self.show_target

    def GetMapToolbar(self):
        """Returns toolbar with zooming tools"""
        return self.toolbars["gcpdisp"]

    def _setActiveMapWindow(self, mapWindow):
        if self.MapWindow != mapWindow:
            self.MapWindow = mapWindow
            self.Map = mapWindow.Map
            self.UpdateActive(mapWindow)
            # needed for wingrass
            self.SetFocus()
