"""
@package gcp.mapdisplay

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
    """Main frame for map display window. Drawing takes place in
    child double buffered drawing window.
    """

    def __init__(
        self,
        parent,
        giface,
        title=_("Manage Ground Control Points"),
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
        self.mapWindowProperties.autoRenderChanged.connect(self.OnAutoRenderChanged)

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
        # Create statusbar
        #
        statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sbgcp.SbGoToGCP,
            sbgcp.SbRMSError,
        ]
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
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
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
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
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
        self.statusbarManager.SetMode(8)  # goto GCP
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))

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
         - 'vdigit'  - vector digitizer
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
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
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
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 2f9dd78a3c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
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
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
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
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.toolbars["map"] = MapToolbar(self, self._toolSwitcher, self._giface)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))

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

            if not self.show_target:
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
        kwargs = {}
        # Handle display map event (mouse click on toolbar Display map
        # tool)
        if event and event.GetEventType() == wx.EVT_TOOL.typeId:
            kwargs = {"reRenderTool": True}
        self.MapWindow.UpdateMap(render=False, **kwargs)

    def OnRender(self, event):
        """Re-render map composition (each map layer)"""
        kwargs = {}
        # Handle re-render map event (mouse click on toolbar Render map
        # tool, F5/Ctrl+R keyboard shortcut)
        if event and event.GetEventType() == wx.EVT_TOOL.typeId:
            kwargs = {"reRenderTool": True}
        # FIXME: remove qlayer code or use RemoveQueryLayer() now in mapdisp.frame
        # delete tmp map layers (queries)
        qlayer = self.Map.GetListOfLayers(name=globalvar.QUERYLAYER)
        for layer in qlayer:
            self.Map.DeleteLayer(layer)

        self.SrcMapWindow.UpdateMap(render=True, **kwargs)
        if self.show_target:
            self.TgtMapWindow.UpdateMap(render=True, **kwargs)

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

    def OnAutoRenderChanged(self, value):
        self.OnRender(event=None)

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
