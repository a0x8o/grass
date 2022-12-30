"""
@package gui_core.toolbars

@brief Base classes toolbar widgets

Classes:
 - toolbars::BaseToolbar

(C) 2007-2011 by the GRASS Development Team

This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.

@author Michael Barton
@author Jachym Cepicky
@author Martin Landa <landa.martin gmail.com>
"""

import platform
import os

import wx
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
from wx.lib.agw import aui
=======
import wx.lib.agw.aui as aui
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
import wx.lib.agw.aui as aui
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
from wx.lib.agw import aui
>>>>>>> d59d1faa34 (style: Fixes manual-from-import (PLR0402) (#3949))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
import wx.lib.agw.aui as aui
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

from core import globalvar
from core.debug import Debug
from icons.icon import MetaIcon
from collections import defaultdict
from core.globalvar import IMGDIR
from gui_core.wrap import ToolBar, Menu, BitmapButton, NewId

from grass.pydispatch.signal import Signal


BaseIcons = {
    "display": MetaIcon(
        img="show", label=_("Display map"), desc=_("Re-render modified map layers only")
    ),
    "render": MetaIcon(
        img="layer-redraw",
        label=_("Render map"),
        desc=_("Force re-rendering all map layers"),
    ),
    "erase": MetaIcon(
        img="erase",
        label=_("Erase display"),
        desc=_("Erase display canvas with given background color"),
    ),
    "pointer": MetaIcon(img="pointer", label=_("Pointer")),
    "zoomIn": MetaIcon(
        img="zoom-in", label=_("Zoom in"), desc=_("Drag or click mouse to zoom")
    ),
    "zoomOut": MetaIcon(
        img="zoom-out", label=_("Zoom out"), desc=_("Drag or click mouse to unzoom")
    ),
    "zoomBack": MetaIcon(img="zoom-last", label=_("Return to previous zoom")),
    "zoomMenu": MetaIcon(
        img="zoom-more",
        label=_("Various zoom options"),
        desc=_("Zoom to default or saved region, save to named region, ..."),
    ),
    "zoomExtent": MetaIcon(img="zoom-extent", label=_("Zoom to selected map layer(s)")),
    "zoomRegion": MetaIcon(
        img="zoom-region", label=_("Zoom to computational region extent")
    ),
    "pan": MetaIcon(img="pan", label=_("Pan"), desc=_("Drag with mouse to pan")),
    "saveFile": MetaIcon(img="map-export", label=_("Save display to file")),
    "print": MetaIcon(img="print", label=_("Print display")),
    "font": MetaIcon(img="font", label=_("Select font")),
    "help": MetaIcon(img="help", label=_("Show manual")),
    "quit": MetaIcon(img="quit", label=_("Quit")),
    "addRast": MetaIcon(img="layer-raster-add", label=_("Add raster map layer")),
    "addVect": MetaIcon(img="layer-vector-add", label=_("Add vector map layer")),
    "overlay": MetaIcon(
        img="overlay-add",
        label=_("Add map elements"),
        desc=_("Overlay elements like scale and legend onto map"),
    ),
    "histogram": MetaIcon(
        img="layer-raster-histogram", label=_("Create histogram with d.histogram")
    ),
    "settings": MetaIcon(img="settings", label=_("Settings")),
    "mapDispSettings": MetaIcon(
        img="monitor-settings", label=_("Map Display Settings")
    ),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
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
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    "docking": MetaIcon(img="monitor-dock", label=_("(Un)dock")),
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
}


class ToolbarController:
    """Controller specialized for wx.ToolBar subclass.

    Toolbar subclasses must delegate methods to controller.
    Methods inherited from toolbar class must be delegated explicitly
    and other methods can be delegated by @c __getattr__.
    """

    def __init__(self, classObject, widget, parent, toolSwitcher):
        """
        :param classObject: toolbar class name (object, i.e. wx.Toolbar)
        :param widget: toolbar instance
        """
        self.classObject = classObject
        self.widget = widget
        self.parent = parent
        self.toolSwitcher = toolSwitcher
        self.handlers = {}
        self.data = None

    def InitToolbar(self, toolData):
        """Initialize toolbar, add tools to the toolbar"""
        for tool in toolData:
            self.CreateTool(*tool)

        self.data = toolData

    def CreateTool(self, label, bitmap, kind, shortHelp, longHelp, handler, pos=-1):
        """Add tool to the toolbar

        :param pos: if -1 add tool, if > 0 insert at given pos
        :return: id of tool
        """
        bmpDisabled = wx.NullBitmap
        tool = -1

        if isinstance(label, tuple):
            internal_label, label = label[0], label[1]
        else:
            internal_label = label

        if label:
            tool = vars(self.widget)[internal_label] = NewId()
            Debug.msg(
                3, "CreateTool(): tool=%d, label=%s bitmap=%s" % (tool, label, bitmap)
            )
            if pos < 0:
                toolWin = self.classObject.AddTool(
                    self.widget,
                    tool,
                    label,
                    bitmap,
                    bmpDisabled,
                    kind,
                    shortHelp,
                    longHelp,
                )
            else:
                toolWin = self.classObject.InsertTool(
                    self.widget,
                    pos,
                    tool,
                    label,
                    bitmap,
                    bmpDisabled,
                    kind,
                    shortHelp,
                    longHelp,
                )
            self.handlers[tool] = handler
            self.widget.Bind(wx.EVT_TOOL, handler, toolWin)
            self.widget.Bind(wx.EVT_TOOL, self.OnTool, toolWin)
        else:  # separator
            self.classObject.AddSeparator(self.widget)

        return tool

    def EnableLongHelp(self, enable):
        """Enable/disable long help

        :param enable: True for enable otherwise disable
        """
        for tool in self.data:
            if isinstance(tool[0], tuple):
                if tool[0][0] == "":  # separator
                    continue
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
                internal_label = tool[0][0]
            else:
                if tool[0] == "":  # separator
                    continue
                internal_label = tool[0]
=======
                else:
                    internal_label = tool[0][0]
            else:
                if tool[0] == "":  # separator
                    continue
                else:
                    internal_label = tool[0]
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
                else:
                    internal_label = tool[0][0]
            else:
                if tool[0] == "":  # separator
                    continue
                else:
                    internal_label = tool[0]
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

            label = vars(self.widget)[internal_label]
            if enable:
                self.classObject.SetToolLongHelp(self.widget, label, tool[4])
            else:
                self.classObject.SetToolLongHelp(self.widget, label, "")

    def OnTool(self, event):
        """Tool selected"""
        if self.toolSwitcher:
            Debug.msg(3, "BaseToolbar.OnTool(): id = %s" % event.GetId())
            self.toolSwitcher.ToolChanged(event.GetId())
        event.Skip()

    def SelectTool(self, id):
        self.classObject.ToggleTool(self.widget, id, True)
        self.toolSwitcher.ToolChanged(id)

        self.handlers[id](event=None)

    def SelectDefault(self):
        """Select default tool"""
        self.SelectTool(self.widget._default)

    def FixSize(self, width):
        """Fix toolbar width on Windows

        .. todo::
            Determine why combobox causes problems here
        """
        if platform.system() == "Windows":
            size = self.classObject.GetBestSize(self.widget)
            self.classObject.SetSize(self.widget, (size[0] + width, size[1]))

    def Enable(self, tool, enable=True):
        """Enable/Disable defined tool

        :param str/tuple tool: name
        :param enable: True to enable otherwise disable tool
        """
        try:
            if isinstance(tool, tuple):
                id = getattr(self.widget, tool[0])
            else:
                id = getattr(self.widget, tool)
        except AttributeError:
            # TODO: test everything that this is not raised
            # this error was ignored for a long time
            raise AttributeError("Toolbar does not have a tool %s." % tool)
            return

        self.classObject.EnableTool(self.widget, id, enable)

    def EnableAll(self, enable=True):
        """Enable/Disable all tools

        :param enable: True to enable otherwise disable tool
        """
        for item in self.widget._toolbarData():
            if not item[0]:
                continue
            self.Enable(item[0], enable)

    def _getToolbarData(self, data):
        """Define tool"""
        retData = []
        for args in data:
            retData.append(self._defineTool(*args))
        return retData

    def _defineTool(
        self, name=None, icon=None, handler=None, item=wx.ITEM_NORMAL, pos=-1
    ):
        """Define tool"""
        if name:
            return (
                name,
                icon.GetBitmap(),
                item,
                icon.GetLabel(),
                icon.GetDesc(),
                handler,
                pos,
            )
        return ("", "", "", "", "", "")  # separator

    def _onMenu(self, data):
        """Toolbar pop-up menu"""
        menu = Menu()

        for icon, handler in data:
            item = wx.MenuItem(menu, wx.ID_ANY, icon.GetLabel())
            item.SetBitmap(icon.GetBitmap(self.parent.iconsize))
            menu.AppendItem(item)
            self.widget.Bind(wx.EVT_MENU, handler, item)

        self.classObject.PopupMenu(self.widget, menu)
        menu.Destroy()

    def CreateSelectionButton(self, tooltip):
        """Add button to toolbar for selection of graphics drawing mode.

        Button must be custom (not toolbar tool) to set smaller width.
        """
        arrowPath = os.path.join(IMGDIR, "small_down_arrow.png")
        if os.path.isfile(arrowPath) and os.path.getsize(arrowPath):
            bitmap = wx.Bitmap(name=arrowPath)
        else:
            bitmap = wx.ArtProvider.GetBitmap(
                id=wx.ART_MISSING_IMAGE, client=wx.ART_TOOLBAR
            )
        button = BitmapButton(
            parent=self.widget,
            id=wx.ID_ANY,
            size=((-1, self.classObject.GetToolSize(self.widget)[1])),
            bitmap=bitmap,
            style=wx.NO_BORDER,
        )
        button.SetToolTip(tooltip)

        return button


class AuiToolbarController(ToolbarController):
    """Controller specialized for wx.lib.agw.aui.auibar.AuiToolBar subclass"""

    def _defineTool(self, name=None, icon=None, handler=None, item=wx.ITEM_NORMAL):
        """Define tool. Position is not needed since wx.lib.agw.aui.auibar.AuiToolBar
        does not have InsertTool method."""
        if name:
            return (
                name,
                icon.GetBitmap(),
                item,
                icon.GetLabel(),
                icon.GetDesc(),
                handler,
            )
        return ("", "", "", "", "", "")  # separator

    def CreateTool(self, label, bitmap, kind, shortHelp, longHelp, handler):
        """Add tool to the toolbar"""
        return super().CreateTool(label, bitmap, kind, shortHelp, longHelp, handler)


class BaseToolbar(ToolBar):
    """Abstract basic toolbar class.

    Following code shows how to create new basic toolbar:


        class MyToolbar(BaseToolbar):
            def __init__(self, parent):
                BaseToolbar.__init__(self, parent)
                self.InitToolbar(self._toolbarData())
                self.Realize()

            def _toolbarData(self):
                # e.g. ("help", _("Help")) tool short label (triangle/arrow
                # at the right side of the toolbar)
                return self._getToolbarData(
                    (
                        ("help", Icons["help"].label),
                        Icons["help"],
                        self.parent.OnHelp
                    ),
                )
    """

    def __init__(
        self, parent, toolSwitcher=None, style=wx.NO_BORDER | wx.TB_HORIZONTAL
    ):
        self.parent = parent
        wx.ToolBar.__init__(self, parent=self.parent, id=wx.ID_ANY, style=style)

        self._default = None
        self.SetToolBitmapSize(globalvar.toolbarSize)

        self.toolSwitcher = toolSwitcher
        self.controller = ToolbarController(
            classObject=ToolBar,
            widget=self,
            parent=self.parent,
            toolSwitcher=toolSwitcher,
        )

    def _toolbarData(self):
        """Toolbar data (virtual)"""
        return None

    def Enable(self, tool, enable=True):
        """@copydoc ToolbarController::Enable()"""
        self.controller.Enable(tool, enable)

    def CreateTool(self, *args, **kwargs):
        """@copydoc ToolbarController::CreateTool()"""
        self.controller.CreateTool(*args, **kwargs)

    def OnTool(self, event):
        """@copydoc ToolbarController::OnTool()"""
        self.controller.OnTool(event)

    def __getattr__(self, name):
        return getattr(self.controller, name)


class AuiToolbar(aui.AuiToolBar):
    """Abstract AUI toolbar class.

    Toolbar for integration with the AUI layout system."""

    def __init__(
        self,
        parent,
        toolSwitcher=None,
        style=wx.NO_BORDER | wx.TB_HORIZONTAL,
        agwStyle=aui.AUI_TB_PLAIN_BACKGROUND | aui.AUI_TB_GRIPPER,
    ):
        self.parent = parent
        super().__init__(
            parent=self.parent, id=wx.ID_ANY, style=style, agwStyle=agwStyle
        )

        self._default = None
        self.SetToolBitmapSize(globalvar.toolbarSize)

        self.toolSwitcher = toolSwitcher
        self.controller = AuiToolbarController(
            classObject=aui.AuiToolBar,
            widget=self,
            parent=self.parent,
            toolSwitcher=toolSwitcher,
        )

    def _toolbarData(self):
        """Toolbar data (virtual)"""
        return None

    def Enable(self, tool, enable=True):
        """@copydoc ToolbarController::Enable()"""
        self.controller.Enable(tool, enable)

    def CreateTool(self, *args, **kwargs):
        """@copydoc ToolbarController::CreateTool()"""
        self.controller.CreateTool(*args, **kwargs)

    def OnTool(self, event):
        """@copydoc ToolbarController::OnTool()"""
        self.controller.OnTool(event)

    def __getattr__(self, name):
        return getattr(self.controller, name)


class ToolSwitcher:
    """Class handling switching tools in toolbar and custom toggle buttons."""

    def __init__(self):
        self._groups = defaultdict(lambda: defaultdict(list))
        self._toolsGroups = defaultdict(list)

        # emitted when tool is changed
        self.toggleToolChanged = Signal("ToolSwitcher.toggleToolChanged")

    def AddToolToGroup(self, group, toolbar, tool):
        """Adds tool from toolbar to group of exclusive tools.

        :param group: name of group (e.g. 'mouseUse')
        :param toolbar: instance of toolbar
        :param tool: id of a tool from the toolbar
        """
        self._groups[group][toolbar].append(tool)
        self._toolsGroups[tool].append(group)

    def AddCustomToolToGroup(self, group, btnId, toggleHandler):
        """Adds custom tool from to group of exclusive tools (some toggle button).

        :param group: name of group (e.g. 'mouseUse')
        :param btnId: id of a tool (typically button)
        :param toggleHandler: handler to be called to switch the button
        """
        self._groups[group]["custom"].append((btnId, toggleHandler))
        self._toolsGroups[btnId].append(group)

    def RemoveCustomToolFromGroup(self, tool):
        """Removes custom tool from group.

        :param tool: id of the button
        """
        if tool not in self._toolsGroups:
            return
        for group in self._toolsGroups[tool]:
            self._groups[group]["custom"] = [
                (bid, hdlr)
                for (bid, hdlr) in self._groups[group]["custom"]
                if bid != tool
            ]

    def RemoveToolbarFromGroup(self, group, toolbar):
        """Removes toolbar from group.

        Before toolbar is destroyed, it must be removed from group, too.
        Otherwise we can expect some DeadObject errors.

        :param group: name of group (e.g. 'mouseUse')
        :param toolbar: instance of toolbar
        """
        for tb in self._groups[group]:
            if tb == toolbar:
                del self._groups[group][tb]
                break

    def IsToolInGroup(self, tool, group):
        """Checks whether a tool is in a specified group.

        :param tool: tool id
        :param group: name of group (e.g. 'mouseUse')
        """
        for group in self._toolsGroups[tool]:
            for tb in self._groups[group]:
                if tb == "custom":
                    for bid, handler in self._groups[group][tb]:
                        if tool == bid:
                            return True
                elif tb.FindById(tool):
                    return True
        return False

    def ToolChanged(self, tool):
        """When any tool/button is pressed, other tools from group must be unchecked.

        :param tool: id of a tool/button
        """
        for group in self._toolsGroups[tool]:
            for tb in self._groups[group]:
                if tb == "custom":
                    for btnId, handler in self._groups[group][tb]:
                        if btnId != tool:
                            handler(False)
                else:
                    for tl in self._groups[group][tb]:
                        if tb.FindById(tl):  # check if still exists
                            if tl != tool:
                                tb.ToggleTool(tl, False)
                            else:
                                tb.ToggleTool(tool, True)

        self.toggleToolChanged.emit(id=tool)
