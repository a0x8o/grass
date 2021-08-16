"""
@package mapdisp.frame

@brief Map display with toolbar for various display management
functions, and additional toolbars (vector digitizer, 3d view).

Can be used either from Layer Manager or as d.mon backend.

Classes:
 - mapdisp::MapPanel

(C) 2006-2016 by the GRASS Development Team

This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.

@author Michael Barton
@author Jachym Cepicky
@author Martin Landa <landa.martin gmail.com>
@author Vaclav Petras <wenzeslaus gmail.com> (SingleMapPanel, handlers support)
@author Anna Kratochvilova <kratochanna gmail.com> (SingleMapPanel)
@author Stepan Turek <stepan.turek seznam.cz> (handlers support)
"""

import os
import copy

from core import globalvar
import wx
import wx.aui

from mapdisp.toolbars import MapToolbar, NvizIcons
from mapdisp.gprint import PrintOptions
from core.gcmd import GError, GMessage, RunCommand
from core.utils import ListOfCatsToRange, GetLayerNameFromCmd
from gui_core.dialogs import GetImageHandlers, ImageSizeDialog
from core.debug import Debug
from core.settings import UserSettings
from gui_core.mapdisp import SingleMapPanel, FrameMixin
from gui_core.query import QueryDialog, PrepareQueryResults
from mapwin.buffered import BufferedMapWindow
from mapwin.decorations import (
    LegendController,
    BarscaleController,
    ArrowController,
    DtextController,
    LegendVectController,
)
from mapwin.analysis import (
    ProfileController,
    MeasureDistanceController,
    MeasureAreaController,
)
from gui_core.forms import GUI
from core.giface import Notification
from gui_core.vselect import VectorSelectBase, VectorSelectHighlighter
from gui_core.wrap import Menu
from mapdisp import statusbar as sb
from main_window.page import MainPageBase

import grass.script as gs

from grass.pydispatch.signal import Signal


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
class MapPanel(SingleMapPanel):
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
class MapPanel(SingleMapPanel):
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
class MapPanel(SingleMapPanel, MainPageBase):
=======
class MapPanel(SingleMapPanel):
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
class MapPanel(SingleMapPanel):
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
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
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
class MapPanel(SingleMapPanel):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
    """Main panel for map display window. Drawing takes place in
    child double buffered drawing window.
    """

    def __init__(
        self,
        parent,
        giface,
        title=_("Map Display"),
        toolbars=["map"],
        statusbar=True,
        tree=None,
        lmgr=None,
        Map=None,
        auimgr=None,
        dockable=False,
        name="MapWindow",
        **kwargs,
    ):
        """Main map display window with toolbars, statusbar and
        2D map window, 3D map window and digitizer.

        :param toolbars: array of activated toolbars, e.g. ['map', 'digit']
        :param statusbar: True to add statusbar
        :param tree: reference to layer tree
        :param lmgr: Layer Manager
        :param map: instance of render.Map
        :param auimgr: AUI manager
        :param name: panel name
        :param kwargs: wx.Panel attributes
        """
        SingleMapPanel.__init__(
            self,
            parent=parent,
            title=title,
            Map=Map,
            auimgr=auimgr,
            name=name,
            **kwargs,
        )
        MainPageBase.__init__(self, dockable)

        self._giface = giface
        # Layer Manager object
        # need by GLWindow (a lot), VDigitWindow (a little bit)
        self._layerManager = lmgr
        # Layer Manager layer tree object
        # used for VDigit toolbar and window and GLWindow
        self.tree = tree
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # checks for saving workspace
        self.canCloseDisplayCallback = None
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
        # checks for saving workspace
        self.canCloseDisplayCallback = None
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))

        # Saved Map Display output img size
        self._saved_output_img_size = None
=======
        # checks for saving workspace
        self.canCloseDisplayCallback = None
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
=======
        # checks for saving workspace
        self.canCloseDisplayCallback = None
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> main

        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
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

        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))

        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")
=======
        # checks for saving workspace
        self.canCloseDisplayCallback = None
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
        # checks for saving workspace
        self.canCloseDisplayCallback = None
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD

        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))

=======
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))

<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))

<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

<<<<<<< HEAD
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))

<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d4beced40f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b58199776 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
        # Emitted when switching map notebook tabs (Single-Window)
        self.onFocus = Signal("MapPanel.onFocus")

>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 057ade7c94 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        # Emitted when starting (switching to) 3D mode.
<<<<<<< HEAD
        # Parameter firstTime specifies if 3D was already activated.
=======
        # Parameter firstTime specifies if 3D was already actived.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
        self.starting3dMode = Signal("MapPanel.starting3dMode")

        # Emitted when ending (switching from) 3D mode.
        self.ending3dMode = Signal("MapPanel.ending3dMode")

        # Emitted when closing display by closing its window.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        self.closingDisplay = Signal("MapPanel.closingDisplay")

        # Emitted when closing display by closing its window.
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
        self.closingDisplay = Signal("MapPanel.closingDisplay")

        # Emitted when closing display by closing its window.
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
        self.closingDisplay = Signal("MapPanel.closingDisplay")

        # Emitted when closing display by closing its window.
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
        self.closingDisplay = Signal("MapPanel.closingDisplay")

        # Emitted when closing display by closing its window.
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        self.closingDisplay = Signal("MapPanel.closingDisplay")

        # Emitted when closing display by closing its window.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
        self.closingDisplay = Signal("MapPanel.closingDisplay")

        # Emitted when closing display by closing its window.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
        self.closingVNETDialog = Signal("MapPanel.closingVNETDialog")

        #
        # Add toolbars
        #
        for toolb in toolbars:
            self.AddToolbar(toolb)

        #
        # Add statusbar
        #
        self.statusbar = None
        self.statusbarManager = None
        if statusbar:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6d10bb4d89 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 922eb0ee2b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 073cd3f76c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> d95da6adeb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c104fc60dc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c6d94bdfdc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 2a2fae8c22 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 36d43bcb43 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 82879813d8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b3a8e05232 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> ce2336a470 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 239ace486a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 073cd3f76c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e2cdbc7bf5 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d95da6adeb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
>>>>>>> d6e9b6bb9c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c104fc60dc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
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
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 31b55bff37 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe652fab2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c6d94bdfdc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> c7d3c75e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 2a2fae8c22 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> cbf5dacd51 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 36d43bcb43 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> e8c04688ee (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 82879813d8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
            # items for choice
            statusbarItems = [
                sb.SbCoordinates,
                sb.SbRegionExtent,
                sb.SbCompRegionExtent,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
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
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 2f9dd78a3c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
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
>>>>>>> osgeo-main
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
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
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
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
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
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
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
>>>>>>> 524f6f69f9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
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
>>>>>>> 0b789a422a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
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
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 524f6f69f9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 0b789a422a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
                sb.SbShowRegion,
                sb.SbAlignExtent,
                sb.SbResolution,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
                sb.SbShowRegion,
                sb.SbAlignExtent,
                sb.SbResolution,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
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
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
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
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
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
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
                sb.SbShowRegion,
                sb.SbAlignExtent,
                sb.SbResolution,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
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
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
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
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> e7579ce5b9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
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
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> a26da7d1f7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
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
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
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
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 524f6f69f9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
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
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
            ]
            self.statusbarItemsDisabledInNviz = (
                sb.SbDisplayGeometry,
<<<<<<< HEAD
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 0b789a422a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
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
                sb.SbDisplayGeometry,
                sb.SbMapScale,
                sb.SbGoTo,
                sb.SbProjection,
            ]
            self.statusbarItemsHiddenInNviz = (
                sb.SbAlignExtent,
                sb.SbDisplayGeometry,
                sb.SbShowRegion,
                sb.SbResolution,
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
                sb.SbMapScale,
            )
            self.statusbar = self.CreateStatusbar(statusbarItems)

            self.Map.GetRenderMgr().updateProgress.connect(
                self.statusbarManager.SetProgress
            )

        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                % {"command": " ".join(cmd), "error": error}
            )
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
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
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
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 524f6f69f9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 0b789a422a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
            self.statusbar = self.CreateStatusbar()
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
            self.statusbar = self.CreateStatusbar()
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
            self.statusbar = self.CreateStatusbar()
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
            self.statusbar = self.CreateStatusbar()
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
            self.statusbar = self.CreateStatusbar()
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 6d10bb4d89 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
            self.statusbar = self.CreateStatusbar()
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 922eb0ee2b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
                % dict(command=" ".join(cmd), error=error)
=======
                % {"command": " ".join(cmd), "error": error}
>>>>>>> 898113134f (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
            )
        )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
            self.statusbar = self.CreateStatusbar()
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 2f9dd78a3c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e7579ce5b9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a26da7d1f7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                % dict(command=" ".join(cmd), error=error)
            )
        )
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b3a8e05232 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> ce2336a470 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 239ace486a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 073cd3f76c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
            self.statusbar = self.CreateStatusbar()
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e2cdbc7bf5 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d95da6adeb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> d6e9b6bb9c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c104fc60dc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
            self.statusbar = self.CreateStatusbar()
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 31b55bff37 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
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
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
            self.statusbar = self.CreateStatusbar()
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe652fab2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
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
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c6d94bdfdc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> c7d3c75e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 2a2fae8c22 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> cbf5dacd51 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 36d43bcb43 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
            self.statusbar = self.CreateStatusbar()
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> e8c04688ee (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 82879813d8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))

        # init decoration objects
        self.decorations = {}
        self._decorationWindows = {}

        self.mapWindowProperties.autoRenderChanged.connect(
            lambda value: self.OnRender(None) if value else None
        )

        #
        # Init map display (buffered DC & set default cursor)
        #
        self.MapWindow2D = BufferedMapWindow(
            self,
            giface=self._giface,
            Map=self.Map,
            properties=self.mapWindowProperties,
            overlays=self.decorations,
        )
        self.MapWindow2D.mapQueried.connect(self.Query)
        self.MapWindow2D.overlayActivated.connect(self._activateOverlay)
        self.MapWindow2D.overlayRemoved.connect(self.RemoveOverlay)
        self._setUpMapWindow(self.MapWindow2D)

        self.MapWindow2D.mouseHandlerUnregistered.connect(self.ResetPointer)

        self.MapWindow2D.InitZoomHistory()
        self.MapWindow2D.zoomChanged.connect(self.StatusbarUpdate)

        # register context menu actions
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
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
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
        if self.statusbar:
            self._registerContextMenuActions()
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if self.statusbar:
            self._registerContextMenuActions()
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> osgeo-main
        self._registerContextMenuActions()
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
        if self.statusbar:
            self._registerContextMenuActions()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        if self.statusbar:
            self._registerContextMenuActions()
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
        if self.statusbar:
            self._registerContextMenuActions()
=======
        self._registerContextMenuActions()
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
        if self.statusbar:
            self._registerContextMenuActions()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
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
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
        if self.statusbar:
            self._registerContextMenuActions()
=======
        self._registerContextMenuActions()
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
        if self.statusbar:
            self._registerContextMenuActions()
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
        if self.statusbar:
            self._registerContextMenuActions()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        if self.statusbar:
            self._registerContextMenuActions()
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
        self._registerContextMenuActions()
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
        if self.statusbar:
            self._registerContextMenuActions()
=======
        self._registerContextMenuActions()
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
        if self.statusbar:
            self._registerContextMenuActions()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        self._registerContextMenuActions()
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
        if self.statusbar:
            self._registerContextMenuActions()
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
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
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
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
        if self.statusbar:
            self._registerContextMenuActions()
=======
        self._registerContextMenuActions()
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
        if self.statusbar:
            self._registerContextMenuActions()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
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
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
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
        if self.statusbar:
            self._registerContextMenuActions()
=======
        self._registerContextMenuActions()
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        if self.statusbar:
            self._registerContextMenuActions()
=======
        self._registerContextMenuActions()
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
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
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
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
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
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
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))

        self._giface.updateMap.connect(self.MapWindow2D.UpdateMap)
        # default is 2D display mode
        self.MapWindow = self.MapWindow2D
        self.MapWindow.SetNamedCursor("default")
        # used by vector digitizer
        self.MapWindowVDigit = None
        # used by Nviz (3D display mode)
        self.MapWindow3D = None

        if "map" in self.toolbars:
            self.toolbars["map"].SelectDefault()

        #
        # Bind various events
        #
        self.Bind(wx.EVT_SIZE, self.OnSize)

        #
        # Update fancy gui style
        #
        self._mgr.AddPane(
            self.MapWindow,
            wx.aui.AuiPaneInfo()
            .CentrePane()
            .Dockable(False)
            .BestSize((-1, -1))
            .Name("2d")
            .CloseButton(False)
            .DestroyOnClose(True)
            .Layer(0),
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
<<<<<<< HEAD
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
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> 6d10bb4d89 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 922eb0ee2b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 073cd3f76c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
<<<<<<< HEAD
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b3a8e05232 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> ce2336a470 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 239ace486a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 073cd3f76c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> osgeo-main
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e2cdbc7bf5 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d95da6adeb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> d6e9b6bb9c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c104fc60dc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 31b55bff37 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
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
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe652fab2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
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
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c6d94bdfdc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> c7d3c75e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 2a2fae8c22 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> cbf5dacd51 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 36d43bcb43 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> e8c04688ee (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 82879813d8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
        # statusbar
        if self.statusbar:
            self.AddStatusbarPane()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6d10bb4d89 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 922eb0ee2b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b3a8e05232 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> ce2336a470 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 239ace486a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 073cd3f76c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e2cdbc7bf5 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d95da6adeb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d6e9b6bb9c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c104fc60dc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 31b55bff37 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe652fab2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c6d94bdfdc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c7d3c75e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 2a2fae8c22 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> cbf5dacd51 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 36d43bcb43 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e8c04688ee (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 82879813d8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
        self._mgr.AddPane(
            self.statusbar,
            wx.aui.AuiPaneInfo()
            .Bottom()
            .MinSize(30, 30)
            .Fixed()
            .Name("statusbar")
            .CloseButton(False)
            .DestroyOnClose(True)
            .ToolbarPane()
            .Dockable(False)
            .PaneBorder(False)
            .Gripper(False),
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 31b55bff37 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fe652fab2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c6d94bdfdc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 2a2fae8c22 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 36d43bcb43 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 82879813d8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6d10bb4d89 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 922eb0ee2b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 073cd3f76c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e2cdbc7bf5 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> d95da6adeb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c104fc60dc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
        # statusbar
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
        if self.statusbar:
            self.AddStatusbarPane()

>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e7579ce5b9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a26da7d1f7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
        if self.statusbar:
            self.AddStatusbarPane()

>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))

>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))

>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))

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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))

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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 6d10bb4d89 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 922eb0ee2b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
        # statusbar
<<<<<<< HEAD
<<<<<<< HEAD
        if self.statusbar:
            self.AddStatusbarPane()

>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b3a8e05232 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))

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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> ce2336a470 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))

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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 239ace486a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 073cd3f76c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))

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
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e2cdbc7bf5 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))

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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d95da6adeb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))

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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> d6e9b6bb9c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c104fc60dc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))

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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 31b55bff37 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))

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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe652fab2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))

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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c6d94bdfdc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))

>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c7d3c75e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 2a2fae8c22 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))

>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 524f6f69f9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> cbf5dacd51 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 36d43bcb43 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
        self.AddStatusbarPane()
=======
        if self.statusbar:
            self.AddStatusbarPane()
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))

>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 0b789a422a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e8c04688ee (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 82879813d8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
        self.AddStatusbarPane()

>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
        self._mgr.Update()

        #
        # Init print module and classes
        #
        self.printopt = PrintOptions(self, self.MapWindow)

        #
        # Re-use dialogs
        #
        self.dialogs = {}
        self.dialogs["attributes"] = None
        self.dialogs["category"] = None
        self.dialogs["vnet"] = None
        self.dialogs["query"] = None
        self.dialogs["vselect"] = None

        # initialize layers to query (d.what.vect/rast)
        self._vectQueryLayers = []
        self._rastQueryLayers = []
        # initialize highlighter for vector features
        self._highlighter_layer = None

        self.measureController = None

        self._resize()

    def _registerContextMenuActions(self):
        """Register show/hide toolbars and statusbar context menu actions"""
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
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
=======
=======
=======
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
=======
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
=======
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
<<<<<<< HEAD
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======
=======
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
<<<<<<< HEAD
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
=======
=======
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======

        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
            )

        def on_show_hide_toolbar(event):
            self.ShowAllToolbars(not self.AreAllToolbarsShown())

        self.MapWindow2D.RegisterContextAction(
            name="showAllToolbars",
            label=show_hide_toolbar_label,
            action=on_show_hide_toolbar,
        )

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
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
        return statusbar
=======
        return statusbar
=======
        return statusbar
=======
        return statusbar
=======
        return statusbar

<<<<<<< HEAD
    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))

<<<<<<< HEAD
    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))

<<<<<<< HEAD
    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))

<<<<<<< HEAD
    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))

    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)

<<<<<<< HEAD
=======

>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======

>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======

>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======

>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======

>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
=======

>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
    def CreateStatusbar(self):
        if self.statusbarManager:
            return
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
=======
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======

        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            )

        def on_show_hide_toolbar(event):
            self.ShowAllToolbars(not self.AreAllToolbarsShown())

        self.MapWindow2D.RegisterContextAction(
            name="showAllToolbars",
            label=show_hide_toolbar_label,
            action=on_show_hide_toolbar,
        )
        return statusbar

    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
        )

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
        )
        return statusbar

    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)

<<<<<<< HEAD
<<<<<<< HEAD
    def CreateStatusbar(self):
        if self.statusbarManager:
            return
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
=======
<<<<<<< HEAD
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======

        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
            )

        def on_show_hide_toolbar(event):
            self.ShowAllToolbars(not self.AreAllToolbarsShown())

        self.MapWindow2D.RegisterContextAction(
            name="showAllToolbars",
            label=show_hide_toolbar_label,
            action=on_show_hide_toolbar,
        )
        return statusbar

    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
        )
        return statusbar

    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)

<<<<<<< HEAD
        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
        )
        return statusbar

    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)

<<<<<<< HEAD
<<<<<<< HEAD
    def CreateStatusbar(self):
        if self.statusbarManager:
            return
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
=======
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======

        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======

        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
            )

        def on_show_hide_toolbar(event):
            self.ShowAllToolbars(not self.AreAllToolbarsShown())

        self.MapWindow2D.RegisterContextAction(
            name="showAllToolbars",
            label=show_hide_toolbar_label,
            action=on_show_hide_toolbar,
        )

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
        )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        return statusbar
=======
        return statusbar

<<<<<<< HEAD
    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))

<<<<<<< HEAD
    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)

<<<<<<< HEAD
<<<<<<< HEAD
        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
        )
        return statusbar

    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======

>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======

>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
    def CreateStatusbar(self):
        if self.statusbarManager:
            return
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======

        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
            )

        def on_show_hide_toolbar(event):
            self.ShowAllToolbars(not self.AreAllToolbarsShown())

        self.MapWindow2D.RegisterContextAction(
            name="showAllToolbars",
            label=show_hide_toolbar_label,
            action=on_show_hide_toolbar,
        )
<<<<<<< HEAD

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
        )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        return statusbar
=======
        return statusbar
=======
        return statusbar
=======
        return statusbar
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

<<<<<<< HEAD
    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)

<<<<<<< HEAD
=======

>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD

>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
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

>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
    def CreateStatusbar(self):
        if self.statusbarManager:
            return
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
=======
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======

        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======

        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            )

        def on_show_hide_toolbar(event):
            self.ShowAllToolbars(not self.AreAllToolbarsShown())

        self.MapWindow2D.RegisterContextAction(
            name="showAllToolbars",
            label=show_hide_toolbar_label,
            action=on_show_hide_toolbar,
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
=======
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 6d10bb4d89 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
        return statusbar
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
        return statusbar

    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 31b55bff37 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
>>>>>>> fe652fab2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
>>>>>>> c6d94bdfdc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
>>>>>>> 2a2fae8c22 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
>>>>>>> 36d43bcb43 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
>>>>>>> 82879813d8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

<<<<<<< HEAD
    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6d10bb4d89 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
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
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
        return statusbar

    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> fe652fab2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c7d3c75e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 2a2fae8c22 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> cbf5dacd51 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 36d43bcb43 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> e8c04688ee (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 82879813d8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
        )
        return statusbar

    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
<<<<<<< HEAD
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
<<<<<<< HEAD
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
<<<<<<< HEAD
>>>>>>> 524f6f69f9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
<<<<<<< HEAD
>>>>>>> 0b789a422a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
<<<<<<< HEAD
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
    def CreateStatusbar(self):
        if self.statusbarManager:
            return
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
=======
        # items for choice
        self.statusbarItems = [
            sb.SbCoordinates,
            sb.SbRegionExtent,
            sb.SbCompRegionExtent,
            sb.SbShowRegion,
            sb.SbAlignExtent,
            sb.SbResolution,
            sb.SbDisplayGeometry,
            sb.SbMapScale,
            sb.SbGoTo,
            sb.SbProjection,
        ]

        self.statusbarItemsHiddenInNviz = (
            sb.SbAlignExtent,
            sb.SbDisplayGeometry,
            sb.SbShowRegion,
            sb.SbResolution,
            sb.SbMapScale,
        )

        statusbar = wx.StatusBar(self, id=wx.ID_ANY)
        statusbar.SetMinHeight(24)
        statusbar.SetFieldsCount(4)
        statusbar.SetStatusWidths([-5, -2, -1, -1])
        self.statusbarManager = sb.SbManager(mapframe=self, statusbar=statusbar)

        # fill statusbar manager
        self.statusbarManager.AddStatusbarItemsByClass(
            self.statusbarItems, mapframe=self, statusbar=statusbar
        )
        self.statusbarManager.AddStatusbarItem(
            sb.SbMask(self, statusbar=statusbar, position=2)
        )
        sbRender = sb.SbRender(self, statusbar=statusbar, position=3)
        self.statusbarManager.AddStatusbarItem(sbRender)

        self.statusbarManager.Update()

        #
        self.Map.GetRenderMgr().updateProgress.connect(
            self.statusbarManager.SetProgress
        )
        self.Map.GetRenderMgr().renderingFailed.connect(
            lambda cmd, error: self._giface.WriteError(
                _("Failed to run command '%(command)s'. Details:\n%(error)s")
                % dict(command=" ".join(cmd), error=error)
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======

        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======

        def show_hide_toolbar_label():
            return (
                _("Hide toolbars") if self.AreAllToolbarsShown() else _("Show toolbars")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
            )

        def on_show_hide_toolbar(event):
            self.ShowAllToolbars(not self.AreAllToolbarsShown())

        self.MapWindow2D.RegisterContextAction(
            name="showAllToolbars",
            label=show_hide_toolbar_label,
            action=on_show_hide_toolbar,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        )

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
        )
        return statusbar
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        )
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
        )
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
        )
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
        )
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        )
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
        )
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

        def show_hide_statusbar_label():
            return (
                _("Hide statusbar") if self.IsStatusbarShown() else _("Show statusbar")
            )

        def on_show_hide_statusbar(event):
            self.ShowStatusbar(not self.IsStatusbarShown())

        self.MapWindow2D.RegisterContextAction(
            name="showStatusbar",
            label=show_hide_statusbar_label,
            action=on_show_hide_statusbar,
        )
        return statusbar

    def ShowStatusbar(self, show):
        """Show/hide statusbar and associated pane"""
        self._mgr.GetPane("statusbar").Show(show)
        self._mgr.Update()

    def IsStatusbarShown(self):
        """Check if statusbar is shown"""
        return self._mgr.GetPane("statusbar").IsShown()

    def SetStatusText(self, *args):
        """Overide wx.StatusBar method"""
        self.statusbar.SetStatusText(*args)

=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> osgeo-main
=======
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
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> e7579ce5b9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> a26da7d1f7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 524f6f69f9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 0b789a422a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
    def GetMapWindow(self):
        return self.MapWindow

    def _addToolbarVDigit(self):
        """Add vector digitizer toolbar"""
        from vdigit.main import haveVDigit, VDigit
        from vdigit.toolbars import VDigitToolbar

        if not haveVDigit:
            from vdigit import errorMsg

            self.toolbars["map"].combo.SetValue(_("2D view"))

            GError(
                _("Unable to start wxGUI vector digitizer.\nDetails: %s") % errorMsg,
                parent=self,
            )
            return

        if not self.MapWindowVDigit:
            from vdigit.mapwindow import VDigitWindow

            self.MapWindowVDigit = VDigitWindow(
                parent=self,
                giface=self._giface,
                properties=self.mapWindowProperties,
                Map=self.Map,
                tree=self.tree,
                lmgr=self._layerManager,
                overlays=self.decorations,
            )
            self._setUpMapWindow(self.MapWindowVDigit)
            self.MapWindowVDigit.digitizingInfo.connect(
                self.statusbarManager.statusbarItems["coordinates"].SetAdditionalInfo
            )
            self.MapWindowVDigit.digitizingInfoUnavailable.connect(
                lambda: self.statusbarManager.statusbarItems[
                    "coordinates"
                ].SetAdditionalInfo(None)
            )
            self.MapWindowVDigit.Show()
            self._mgr.AddPane(
                self.MapWindowVDigit,
                wx.aui.AuiPaneInfo()
                .CentrePane()
                .Dockable(False)
                .BestSize((-1, -1))
                .Name("vdigit")
                .CloseButton(False)
                .DestroyOnClose(True)
                .Layer(0),
            )

        self._switchMapWindow(self.MapWindowVDigit)

        if self._mgr.GetPane("2d").IsShown():
            self._mgr.GetPane("2d").Hide()
        elif self._mgr.GetPane("3d").IsShown():
            self._mgr.GetPane("3d").Hide()
        self._mgr.GetPane("vdigit").Show()
        if "vdigit" not in self.toolbars:
            self.toolbars["vdigit"] = VDigitToolbar(
                parent=self,
                toolSwitcher=self._toolSwitcher,
                MapWindow=self.MapWindow,
                digitClass=VDigit,
                giface=self._giface,
            )
            self.toolbars["vdigit"].quitDigitizer.connect(self.QuitVDigit)

            def openATM(selection):
                self._layerManager.OnShowAttributeTable(None, selection=selection)

            self.toolbars["vdigit"].openATM.connect(openATM)
            self.Map.layerAdded.connect(self._updateVDigitLayers)
        self.MapWindowVDigit.SetToolbar(self.toolbars["vdigit"])

        self._mgr.AddPane(
            self.toolbars["vdigit"],
            wx.aui.AuiPaneInfo()
            .Name("vdigittoolbar")
            .Caption(_("Vector Digitizer Toolbar"))
            .ToolbarPane()
            .Top()
            .Row(1)
            .LeftDockable(False)
            .RightDockable(False)
            .BottomDockable(False)
            .TopDockable(True)
            .CloseButton(False)
            .Layer(2)
            .BestSize(self.toolbars["vdigit"].GetBestSize()),
        )
        # change mouse to draw digitized line
        self.MapWindow.mouse["box"] = "point"
        self.MapWindow.zoomtype = 0
        self.MapWindow.pen = wx.Pen(colour="red", width=2, style=wx.SOLID)
        self.MapWindow.polypen = wx.Pen(colour="green", width=2, style=wx.SOLID)

    def _updateVDigitLayers(self, layer):
        """Update vdigit layers"""
        if "vdigit" in self.toolbars:
            self.toolbars["vdigit"].UpdateListOfLayers(updateTool=True)

    def AddNviz(self):
        """Add 3D view mode window"""
        from nviz.main import haveNviz, GLWindow, errorMsg

        # check for GLCanvas and OpenGL
        if not haveNviz:
            self.toolbars["map"].combo.SetValue(_("2D view"))
            GError(
                parent=self,
                message=_(
                    "Unable to switch to 3D display mode.\nThe Nviz python extension "
                    "was not found or loaded properly.\n"
                    "Switching back to 2D display mode.\n\nDetails: %s"
                )
                % errorMsg,
            )
            return

        # here was disabling 3D for other displays, now done on starting3dMode

        self.toolbars["map"].Enable2D(False)
        # add rotate tool to map toolbar
        self.toolbars["map"].InsertTool(
            (("rotate", NvizIcons["rotate"], self.OnRotate, wx.ITEM_CHECK, 7),)
        )  # 7 is position
        self._toolSwitcher.AddToolToGroup(
            group="mouseUse",
            toolbar=self.toolbars["map"],
            tool=self.toolbars["map"].rotate,
        )
        self.toolbars["map"].InsertTool(
            (
                (
                    "flyThrough",
                    NvizIcons["flyThrough"],
                    self.OnFlyThrough,
                    wx.ITEM_CHECK,
                    8,
                ),
            )
        )
        self._toolSwitcher.AddToolToGroup(
            group="mouseUse",
            toolbar=self.toolbars["map"],
            tool=self.toolbars["map"].flyThrough,
        )
        # update status bar

        self.statusbarManager.DisableStatusbarItemsByClass(
            self.statusbarItemsDisabledInNviz
        )
        self.mapWindowProperties.sbItem = 0

        # erase map window
        self.MapWindow.EraseMap()

        self._giface.WriteCmdLog(
            _("Starting 3D view mode..."), notification=Notification.HIGHLIGHT
        )
        self.SetStatusText(_("Please wait, loading data..."), 0)

        # create GL window
        if not self.MapWindow3D:
            self.MapWindow3D = GLWindow(
                self,
                giface=self._giface,
                id=wx.ID_ANY,
                frame=self,
                Map=self.Map,
                tree=self.tree,
                lmgr=self._layerManager,
            )
            self._setUpMapWindow(self.MapWindow3D)
            self.MapWindow3D.mapQueried.connect(self.Query)
            self._switchMapWindow(self.MapWindow3D)
            self.MapWindow.SetNamedCursor("default")

            # here was AddNvizTools in lmgr
            self.starting3dMode.emit(firstTime=True)

            # switch from MapWindow to MapWindowGL
            self._mgr.GetPane("2d").Hide()
            self._mgr.AddPane(
                self.MapWindow3D,
                wx.aui.AuiPaneInfo()
                .CentrePane()
                .Dockable(False)
                .BestSize((-1, -1))
                .Name("3d")
                .CloseButton(False)
                .DestroyOnClose(True)
                .Layer(0),
            )

            self.MapWindow3D.Show()
            self.MapWindow3D.ResetViewHistory()
            self.MapWindow3D.UpdateView(None)
            self.MapWindow3D.overlayActivated.connect(self._activateOverlay)
            self.MapWindow3D.overlayRemoved.connect(self.RemoveOverlay)
        else:
            self._switchMapWindow(self.MapWindow3D)
            os.environ["GRASS_REGION"] = self.Map.SetRegion(windres=True, windres3=True)
            self.MapWindow3D.GetDisplay().Init()
            self.MapWindow3D.LoadDataLayers()
            del os.environ["GRASS_REGION"]

            # switch from MapWindow to MapWindowGL
            self._mgr.GetPane("2d").Hide()
            self._mgr.GetPane("3d").Show()

            # here was AddNvizTools in lmgr and updating of pages
            self.starting3dMode.emit(firstTime=False)

            self.MapWindow3D.ResetViewHistory()

        # connect signals for updating overlays
        for overlay in self.decorations.values():
            overlay.overlayChanged.connect(self.MapWindow3D.UpdateOverlays)
        self.Map.GetRenderMgr().renderDone.connect(self.MapWindow3D._onUpdateOverlays)

        self._giface.updateMap.disconnect(self.MapWindow2D.UpdateMap)
        self._giface.updateMap.connect(self.MapWindow3D.UpdateMap)
        self.MapWindow3D.overlays = self.MapWindow2D.overlays
        # update overlays needs to be called after because getClientSize
        # is called during update and it must give reasonable values
        wx.CallAfter(self.MapWindow3D.UpdateOverlays)

        self.SetStatusText("", 0)
        self._mgr.Update()

    def Disable3dMode(self):
        """Disables 3D mode (NVIZ) in user interface."""
        # TODO: this is broken since item is removed but switch is drived by
        # index
        if "3D" in self.toolbars["map"].combo.GetString(1):
            self.toolbars["map"].combo.Delete(1)

    def RemoveNviz(self):
        """Restore 2D view. Can be called even if 3D is not active."""
        if not self.IsPaneShown("3d"):
            return
        try:
            self.toolbars["map"].RemoveTool(self.toolbars["map"].rotate)
            self.toolbars["map"].RemoveTool(self.toolbars["map"].flyThrough)
        except AttributeError:
            pass

        # update status bar
        self.SetStatusText(_("Please wait, unloading data..."), 0)
        self.statusbarManager.disabledItems = {}
        self.mapWindowProperties.sbItem = UserSettings.Get(
            group="display", key="statusbarMode", subkey="selection"
        )

        # unloading messages from library cause highlight anyway
        self._giface.WriteCmdLog(
            _("Switching back to 2D view mode..."),
            notification=Notification.NO_NOTIFICATION,
        )
        if self.MapWindow3D:
            self.MapWindow3D.OnClose(event=None)
        # switch from MapWindowGL to MapWindow
        self._mgr.GetPane("2d").Show()
        self._mgr.GetPane("3d").Hide()

        self._switchMapWindow(self.MapWindow2D)
        # here was RemoveNvizTools form lmgr
        self.ending3dMode.emit()
        try:
            self.MapWindow2D.overlays = self.MapWindow3D.overlays
        except AttributeError:
            pass
        # TODO: here we end because self.MapWindow3D is None for a while
        self._giface.updateMap.disconnect(self.MapWindow3D.UpdateMap)
        self._giface.updateMap.connect(self.MapWindow2D.UpdateMap)
        # disconnect overlays
        for overlay in self.decorations.values():
            overlay.overlayChanged.disconnect(self.MapWindow3D.UpdateOverlays)
        self.Map.GetRenderMgr().renderDone.disconnect(
            self.MapWindow3D._onUpdateOverlays
        )
        self.MapWindow3D.ClearTextures()

        self.MapWindow.UpdateMap()
        self._mgr.Update()
        self.GetMapToolbar().SelectDefault()

    def AddToolbar(self, name, fixed=False):
        """Add defined toolbar to the window

        Currently recognized toolbars are:
         - 'map'     - basic map toolbar
         - 'vdigit'  - vector digitizer

        :param name: toolbar to add
        :param fixed: fixed toolbar
        """
        # default toolbar
        if name == "map":
            if "map" not in self.toolbars:
                self.toolbars["map"] = MapToolbar(
                    self, toolSwitcher=self._toolSwitcher, giface=self._giface
                )

            self._mgr.AddPane(
                self.toolbars["map"],
                wx.aui.AuiPaneInfo()
                .Name("maptoolbar")
                .Caption(_("Map Toolbar"))
                .ToolbarPane()
                .Top()
                .Name("mapToolbar")
                .LeftDockable(False)
                .RightDockable(False)
                .BottomDockable(False)
                .TopDockable(True)
                .CloseButton(False)
                .Layer(2)
                .BestSize(self.toolbars["map"].GetBestSize()),
            )

        # nviz
        elif name == "nviz":
            self.toolbars["map"].combo.SetValue(_("3D view"))
            self.AddNviz()

        # vector digitizer
        elif name == "vdigit":
            self.toolbars["map"].combo.SetValue(_("Vector digitizer"))
            self._addToolbarVDigit()

        # raster digitizer
        elif name == "rdigit":
            self.toolbars["map"].combo.SetValue(_("Raster digitizer"))
            self.AddRDigit()

        if fixed:
            self.toolbars["map"].combo.Disable()

        self._mgr.Update()

    def RemoveToolbar(self, name, destroy=False):
        """Removes defined toolbar from the window

        :param name toolbar to remove
        :param destroy True to destroy otherwise toolbar is only hidden
        """
        super().RemoveToolbar(name, destroy)

        if name == "vdigit":
            self._mgr.GetPane("vdigit").Hide()
            self._mgr.GetPane("2d").Show()
            self._switchMapWindow(self.MapWindow2D)

        self.toolbars["map"].Enable2D(True)

        self._mgr.Update()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0b789a422a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 524f6f69f9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0b0d6e2ba7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b35238645a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
<<<<<<< HEAD
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self.RemoveToolbar
        else:
            action = self.AddToolbar
        for toolbar in self.GetToolbarNames():
            action(toolbar)

    def AreAllToolbarsShown(self):
        return self.GetMapToolbar().IsShown()

    def IsPaneShown(self, name):
        """Check if pane (toolbar, mapWindow ...) of given name is currently shown"""
        if self._mgr.GetPane(name).IsOk():
            return self._mgr.GetPane(name).IsShown()
        return False

>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 54529c0b40 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 2f9dd78a3c (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b2b55251f8 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 769e5b1bf2 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
=======
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 38efcb69af (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> cb9a071273 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 96abfa32e7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 7293916d97 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> a26da7d1f7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fa4688f918 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> e7579ce5b9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> cfd421bf4a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
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
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 54821cb4b4 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 8f67182ef7 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
    def RemoveQueryLayer(self):
        """Removes temporary map layers (queries)"""
        qlayer = self.GetMap().GetListOfLayers(name=globalvar.QUERYLAYER)
        for layer in qlayer:
            self.GetMap().DeleteLayer(layer)

    def OnRender(self, event):
        """Re-render map composition (each map layer)"""
        self.RemoveQueryLayer()

        # deselect features in vdigit
        if self.GetToolbar("vdigit"):
            if self.MapWindow.digit:
                self.MapWindow.digit.GetDisplay().SetSelected([])
            self.MapWindow.UpdateMap(
                render=True,
                renderVector=True,
                reRenderTool=True,
            )
        else:
            self.MapWindow.UpdateMap(render=True, reRenderTool=True)

        # reset dialog with selected features
        if self.dialogs["vselect"]:
            self.dialogs["vselect"].Reset()

        # update statusbar
        self.StatusbarUpdate()

    def OnPointer(self, event):
        """Pointer button clicked"""
        self.MapWindow.SetModePointer()

        if self.GetToolbar("vdigit"):
            self.toolbars["vdigit"].action["id"] = -1
            self.toolbars["vdigit"].action["desc"] = ""

    def OnSelect(self, event):
        """Vector feature selection button clicked"""
        layerList = self._giface.GetLayerList()
        layerSelected = layerList.GetSelectedLayer()
        if not self.dialogs["vselect"]:
            if layerSelected is None:
                GMessage(_("No map layer selected. Operation canceled."))
                return

            self.dialogs["vselect"] = VectorSelectBase(self.parent, self._giface)
            self.dialogs["vselect"].CreateDialog(createButton=True)
            self.dialogs["vselect"].onCloseDialog.connect(
                self._onCloseVectorSelectDialog
            )

    def _onCloseVectorSelectDialog(self):
        self.dialogs["vselect"] = None

    def OnRotate(self, event):
        """Rotate 3D view"""
        self.MapWindow.mouse["use"] = "rotate"

        # change the cursor
        self.MapWindow.SetNamedCursor("hand")

    def OnFlyThrough(self, event):
        """Fly-through mode"""
        self.MapWindow.mouse["use"] = "fly"

        # change the cursor
        self.MapWindow.SetNamedCursor("hand")
        self.MapWindow.SetFocus()

    def SaveToFile(self, event):
        """Save map to image"""
        filetype, ltype = self._prepareSaveToFile()
        if not ltype:
            return

        # get size
        dlg = ImageSizeDialog(self, img_size=self._saved_output_img_size)
        dlg.CentreOnParent()
        if dlg.ShowModal() != wx.ID_OK:
            dlg.Destroy()
            return
        self._saved_output_img_size = dlg.GetValues()
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

            self.MapWindow.SaveToFile(path, fileType, *self._saved_output_img_size)

        dlg.Destroy()

    def DOutFile(self, command, callback=None):
        """Saves map to image by running d.out.file from gui or d.mon.
        Command is expected to be validated by parser.
        """
        filetype, ltype = self._prepareSaveToFile()
        if not ltype:
            return
        width, height = self.MapWindow.GetClientSize()
        for param in command[1:]:
            try:
                p, val = param.split("=")
            except ValueError:
                # --overwrite
                continue
            if p == "format":  # must be there
                extType = "ppm" if self.IsPaneShown("3d") else val
            if p == "output":  # must be there
                name = val
            elif p == "size":
                width, height = val.split(",")

        base, ext = os.path.splitext(name)
        if not ext:
            name = base + "." + extType
        elif ext[1:] != extType:
            extType = ext[1:]

        # default type is PNG
        bitmapType = "ppm" if self.IsPaneShown("3d") else wx.BITMAP_TYPE_PNG
        for each in ltype:
            if each["ext"] == extType:
                bitmapType = each["type"]
                break
        self.MapWindow.SaveToFile(name, bitmapType, int(width), int(height), callback)

    def DOutFileOptData(self, dcmd, layer, params, propwin):
        """Dummy function which is called when d.out.file is called
        and returns parsed and validated command which is then passed
        to DOutFile method."""
        if not dcmd:
            return

        self.DOutFile(dcmd)

    def DToRast(self, command):
        """Saves currently loaded composition of layers as a raster map."""

        def _DToRastDone():
            # import back as red, green, blue rasters
            returncode, messages = RunCommand(
                "r.in.gdal",
                flags="o",
                input=pngFile,
                output=tmpName,
                quiet=True,
                overwrite=overwrite,
                getErrorMsg=True,
            )
            if returncode != 0:
                self._giface.WriteError(_("Failed to run d.to.rast:\n") + messages)
                return
            # set region for composite
            gs.use_temp_region()
            returncode, messages = RunCommand(
                "g.region", raster=tmpName + ".red", quiet=True, getErrorMsg=True
            )
<<<<<<< HEAD
            if returncode != 0:
=======
            if not returncode == 0:
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
                gs.del_temp_region()
                self._giface.WriteError(_("Failed to run d.to.rast:\n") + messages)
                return
            # composite
            returncode, messages = RunCommand(
                "r.composite",
                red=tmpName + ".red",
                green=tmpName + ".green",
                blue=tmpName + ".blue",
                output=outputRaster,
                quiet=True,
                overwrite=overwrite,
                getErrorMsg=True,
            )
            gs.del_temp_region()
            RunCommand(
                "g.remove",
                type="raster",
                flags="f",
                quiet=True,
                name=[tmpName + ".red", tmpName + ".green", tmpName + ".blue"],
            )
            if returncode != 0:
                self._giface.WriteError(_("Failed to run d.to.rast:\n") + messages)
                gs.try_remove(pngFile)
                return

            # alignExtent changes only region variable
            oldRegion = self.GetMap().GetCurrentRegion().copy()
            self.GetMap().AlignExtentFromDisplay()
            region = self.GetMap().GetCurrentRegion().copy()
            self.GetMap().region.update(oldRegion)
            RunCommand(
                "r.region",
                map=outputRaster,
                n=region["n"],
                s=region["s"],
                e=region["e"],
                w=region["w"],
                quiet=True,
            )
            gs.try_remove(pngFile)

        if self.IsPaneShown("3d"):
            self._giface.WriteError(_("d.to.rast can be used only in 2D mode."))
            return
        outputRaster = None
        overwrite = False
        for param in command[1:]:
            try:
                p, val = param.split("=")
                if p == "output":
                    outputRaster = val
            except ValueError:
                if param.startswith("--overwrite"):
                    overwrite = True

        if not outputRaster:
            return
        # output file as PNG
        tmpName = "d_to_rast_tmp"
        pngFile = gs.tempfile(create=False) + ".png"
        dOutFileCmd = ["d.out.file", "output=" + pngFile, "format=png"]
        self.DOutFile(dOutFileCmd, callback=_DToRastDone)

    def DToRastOptData(self, dcmd, layer, params, propwin):
        """Dummy function which is called when d.to.rast is called
        and returns parsed and validated command which is then passed
        to DToRast method."""
        if not dcmd:
            return

        self.DToRast(dcmd)

    def _prepareSaveToFile(self):
        """Get wildcards and format extensions."""
        if self.IsPaneShown("3d"):
            filetype = "TIF file (*.tif)|*.tif|PPM file (*.ppm)|*.ppm"
            ltype = [{"ext": "tif", "type": "tif"}, {"ext": "ppm", "type": "ppm"}]
        else:
            img = self.MapWindow.img
            if not img:
                GMessage(
                    parent=self,
                    message=_("Nothing to render (empty map). Operation canceled."),
                )
                return None, None
            filetype, ltype = GetImageHandlers(img)
        return filetype, ltype

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

    def CleanUp(self):
        """Clean up before closing map display.
        End digitizer/nviz."""
        Debug.msg(2, "MapPanel.CleanUp()")
        self.Map.Clean()
        # close edited map and 3D tools properly
        if self.GetToolbar("vdigit"):
            maplayer = self.toolbars["vdigit"].GetLayer()
            if maplayer:
                self.toolbars["vdigit"].OnExit()
        self.RemoveNviz()
        if hasattr(self, "rdigit") and self.rdigit:
            self.rdigit.CleanUp()
        if self.dialogs["vnet"]:
            self.closingVNETDialog.emit()
        self._mgr.UnInit()

    def OnCloseWindow(self, event, askIfSaveWorkspace=True):
        """Window closed.
        Also close associated layer tree page
        """
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        Debug.msg(2, "MapPanel.OnCloseWindow()")
        if self.canCloseDisplayCallback:
            pgnum_dict = self.canCloseDisplayCallback(
                askIfSaveWorkspace=askIfSaveWorkspace
            )
            if pgnum_dict is not None:
                self.CleanUp()
                if pgnum_dict["layers"] > -1:
                    self.closingDisplay.emit(pgnum_dict=pgnum_dict)
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
        Debug.msg(2, "MapPanel.OnCloseWindow()")
        if self.canCloseDisplayCallback:
            pgnum_dict = self.canCloseDisplayCallback(
                askIfSaveWorkspace=askIfSaveWorkspace
            )
            if pgnum_dict is not None:
                self.CleanUp()
                if pgnum_dict["layers"] > -1:
                    self.closingDisplay.emit(pgnum_dict=pgnum_dict)
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
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
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
        Debug.msg(2, "MapPanel.OnCloseWindow()")
        if self.canCloseCallback:
            pgnum_dict = self.canCloseCallback(askIfSaveWorkspace=askIfSaveWorkspace)
            if pgnum_dict is not None:
=======
        Debug.msg(2, "MapFrame.OnCloseWindow()")
        if self.canCloseDisplayCallback:
            pgnum = self.canCloseDisplayCallback(askIfSaveWorkspace=askIfSaveWorkspace)
            if pgnum is not None:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
                self.CleanUp()
                if pgnum_dict["layers"] > -1:
                    if self.IsDockable():
                        self.closingPage.emit(
                            pgnum_dict=pgnum_dict, is_docked=self.IsDocked()
                        )
                        if not self.IsDocked():
                            frame = self.GetParent()
                            frame.Destroy()
                    else:
                        self.closingPage.emit(pgnum_dict=pgnum_dict)
=======
        Debug.msg(2, "MapPanel.OnCloseWindow()")
        if self.canCloseDisplayCallback:
            pgnum_dict = self.canCloseDisplayCallback(
                askIfSaveWorkspace=askIfSaveWorkspace
            )
            if pgnum_dict is not None:
                self.CleanUp()
                if pgnum_dict["layers"] > -1:
                    self.closingDisplay.emit(pgnum_dict=pgnum_dict)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
        Debug.msg(2, "MapPanel.OnCloseWindow()")
        if self.canCloseDisplayCallback:
            pgnum_dict = self.canCloseDisplayCallback(
                askIfSaveWorkspace=askIfSaveWorkspace
            )
            if pgnum_dict is not None:
                self.CleanUp()
                if pgnum_dict["layers"] > -1:
                    self.closingDisplay.emit(pgnum_dict=pgnum_dict)
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
        Debug.msg(2, "MapPanel.OnCloseWindow()")
        if self.canCloseDisplayCallback:
            pgnum_dict = self.canCloseDisplayCallback(
                askIfSaveWorkspace=askIfSaveWorkspace
            )
            if pgnum_dict is not None:
                self.CleanUp()
                if pgnum_dict["layers"] > -1:
                    self.closingDisplay.emit(pgnum_dict=pgnum_dict)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
<<<<<<< HEAD
        Debug.msg(2, "MapPanel.OnCloseWindow()")
        if self.canCloseDisplayCallback:
            pgnum_dict = self.canCloseDisplayCallback(
                askIfSaveWorkspace=askIfSaveWorkspace
            )
            if pgnum_dict is not None:
                self.CleanUp()
                if pgnum_dict["layers"] > -1:
                    self.closingDisplay.emit(pgnum_dict=pgnum_dict)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
                    # Destroy is called when notebook page is deleted
        else:
            self.CleanUp()
            self.Destroy()

    def Query(self, x, y):
        """Query selected layers.

        :param x,y: coordinates
        """
        if self._vectQueryLayers or self._rastQueryLayers:
            rast = self._rastQueryLayers
            vect = self._vectQueryLayers
        else:
            layers = self._giface.GetLayerList().GetSelectedLayers(checkedOnly=False)
            rast = []
            vect = []
            for layer in layers:
                if layer.type == "command":
                    continue
                name, found = GetLayerNameFromCmd(layer.cmd)
                if not found:
                    continue
                ltype = layer.maplayer.GetType()
                if ltype == "raster":
                    rast.append(name)
                elif ltype in {"rgb", "his"}:
                    for iname in name.split("\n"):
                        rast.append(iname)
                elif ltype in {"vector", "thememap", "themechart"}:
                    vect.append(name)
            if vect:
                # check for vector maps open to be edited
                digitToolbar = self.GetToolbar("vdigit")
                if digitToolbar:
                    lmap = digitToolbar.GetLayer().GetName()
                    for name in vect:
                        if lmap == name:
                            self._giface.WriteWarning(
                                _("Vector map <%s> opened for editing - skipped.")
                                % lmap
                            )
                            vect.remove(name)

        if not (rast + vect):
            GMessage(
                parent=self,
                message=_("No raster or vector map layer selected for querying."),
            )
            return

        # set query snap distance for v.what at map unit equivalent of 10
        # pixels
        qdist = 10.0 * ((self.Map.region["e"] - self.Map.region["w"]) / self.Map.width)

        # TODO: replace returning None by exception or so
        try:
            east, north = self.MapWindow.Pixel2Cell((x, y))
        except TypeError:
            return

        if not self.IsPaneShown("3d"):
            self.QueryMap(east, north, qdist, rast, vect)
        else:
            if rast:
                self.MapWindow.QuerySurface(x, y)
            if vect:
                self.QueryMap(east, north, qdist, rast=[], vect=vect)

    def SetQueryLayersAndActivate(self, ltype, maps):
        """Activate query mode and set layers to query.
        This method is used for querying in d.mon using d.what.rast/vect"""
        self.toolbars["map"].SelectTool(self.toolbars["map"].query)
        if ltype == "vector":
            self._vectQueryLayers = maps
        elif ltype == "raster":
            self._rastQueryLayers = maps

    def QueryMap(self, east, north, qdist, rast, vect):
        """Query raster or vector map layers by r/v.what

        :param east,north: coordinates
        :param qdist: query distance
        :param rast: raster map names
        :param vect: vector map names
        """
        Debug.msg(
            1, "QueryMap(): raster=%s vector=%s" % (",".join(rast), ",".join(vect))
        )
        if self._highlighter_layer is None:
            self._highlighter_layer = VectorSelectHighlighter(
                mapdisp=self._giface.GetMapDisplay(), giface=self._giface
            )

        rastQuery = []
        vectQuery = []
        env = os.environ.copy()
        for raster in rast:
            env["GRASS_REGION"] = gs.region_env(raster=raster)
            rastQuery += gs.raster_what(
                map=raster, coord=(east, north), localized=True, env=env
            )
        if vect:
            encoding = UserSettings.Get(group="atm", key="encoding", subkey="value")
            try:
                vectQuery = gs.vector_what(
                    map=vect,
                    coord=(east, north),
                    distance=qdist,
                    encoding=encoding,
                    multiple=True,
                )
            except gs.ScriptError:
                GError(
                    parent=self,
                    message=_(
                        "Failed to query vector map(s) <{maps}>. "
                        "Check database settings and topology."
                    ).format(maps=",".join(vect)),
                )

        self._highlighter_layer.Clear()
        if vectQuery and "Category" in vectQuery[0]:
            self._queryHighlight(vectQuery)

        result = rastQuery + vectQuery
        result = PrepareQueryResults(coordinates=(east, north), result=result)
        if self.dialogs["query"]:
            self.dialogs["query"].Raise()
            self.dialogs["query"].SetData(result)
        else:
            self.dialogs["query"] = QueryDialog(parent=self, data=result)
            self.dialogs["query"].Bind(wx.EVT_CLOSE, self._oncloseQueryDialog)
            self.dialogs["query"].redirectOutput.connect(self._onRedirectQueryOutput)
            self.dialogs["query"].Show()

    def _oncloseQueryDialog(self, event):
        self.dialogs["query"] = None
        self._vectQueryLayers = []
        self._rastQueryLayers = []
        self._highlighter_layer.Clear()
        self._highlighter_layer = None
        event.Skip()

    def _onRedirectQueryOutput(self, output, style="log"):
        """Writes query output into console"""
        if style == "log":
            self._giface.WriteLog(output, notification=Notification.MAKE_VISIBLE)
        elif style == "cmd":
            self._giface.WriteCmdLog(output)

    def _queryHighlight(self, vectQuery):
        """Highlight category from query."""
        if len(vectQuery) > 0:
            self._highlighter_layer.SetLayer(vectQuery[0]["Layer"])
            self._highlighter_layer.SetMap(
                vectQuery[0]["Map"] + "@" + vectQuery[0]["Mapset"]
            )
            tmp = []
            for i in vectQuery:
                tmp.append(i["Category"])

            self._highlighter_layer.SetCats(tmp)
            self._highlighter_layer.DrawSelected()

    def OnQuery(self, event):
        """Query tools menu"""
        self.MapWindow.mouse["use"] = "query"
        self.MapWindow.mouse["box"] = "point"
        self.MapWindow.zoomtype = 0

        # change the cursor
        self.MapWindow.SetNamedCursor("cross")

    def AddTmpVectorMapLayer(self, name, cats, useId=False, addLayer=True):
        """Add temporal vector map layer to map composition

        :param name: name of map layer
        :param useId: use feature id instead of category
        """
        # color settings from ATM
        color = UserSettings.Get(group="atm", key="highlight", subkey="color")
        colorStr = str(color[0]) + ":" + str(color[1]) + ":" + str(color[2])

        # icon used in vector display and its size
        icon = ""
        size = 0
        # here we know that there is one selected layer and it is vector
        layerSelected = self._giface.GetLayerList().GetSelectedLayer()
        if not layerSelected:
            return None

        vparam = layerSelected.cmd
        for p in vparam:
            if "=" in p:
                parg, pval = p.split("=", 1)
                if parg == "icon":
                    icon = pval
                elif parg == "size":
                    size = float(pval)

        pattern = [
            "d.vect",
            "map=%s" % name,
            "color=%s" % colorStr,
            "fill_color=%s" % colorStr,
            "width=%d" % UserSettings.Get(group="atm", key="highlight", subkey="width"),
        ]
        if icon != "":
            pattern.append("icon=%s" % icon)
        if size > 0:
            pattern.append("size=%i" % size)

        if useId:
            cmd = pattern
            cmd.append("-i")
            cmd.append("cats=%s" % str(cats))
        else:
            cmd = []
            for layer in cats.keys():
                cmd.append(copy.copy(pattern))
                lcats = cats[layer]
                cmd[-1].append("layer=%d" % layer)
                cmd[-1].append("cats=%s" % ListOfCatsToRange(lcats))

        if addLayer:
            args = {}
            if useId:
                args["ltype"] = "vector"
            else:
                args["ltype"] = "command"

            return self.Map.AddLayer(
                name=globalvar.QUERYLAYER,
                command=cmd,
                active=True,
                hidden=True,
                opacity=1.0,
                render=True,
                **args,
            )
        return cmd

    def OnMeasureDistance(self, event):
        self._onMeasure(MeasureDistanceController)

    def OnMeasureArea(self, event):
        self._onMeasure(MeasureAreaController)

    def _onMeasure(self, controller):
        """Starts measurement mode.

        :param controller: measurement class (MeasureDistanceController,
                           MeasureAreaController)
        """
        self.measureController = controller(self._giface, mapWindow=self.GetMapWindow())
        # assure that the mode is ended and lines are cleared whenever other
        # tool is selected
        self._toolSwitcher.toggleToolChanged.connect(self.measureController.Stop)
        self.measureController.Start()

    def OnProfile(self, event):
        """Launch profile tool"""
        rasters = []
        layers = self._giface.GetLayerList().GetSelectedLayers()
        for layer in layers:
            if layer.type == "raster":
                rasters.append(layer.maplayer.name)
        self.Profile(rasters=rasters)

    def Profile(self, rasters=None):
        """Launch profile tool"""
        from wxplot.profile import ProfileFrame

        self.profileController = ProfileController(
            self._giface, mapWindow=self.GetMapWindow()
        )
        win = ProfileFrame(
            parent=self,
            giface=self._giface,
            rasterList=rasters,
            units=self.Map.projinfo["units"],
            controller=self.profileController,
        )
        win.Show()
        # Open raster select dialog to make sure that a raster (and
        # the desired raster) is selected to be profiled
        win.OnSelectRaster(None)

    def OnHistogramPyPlot(self, event):
        """Init PyPlot histogram display canvas and tools"""
        raster = []

        for layer in self._giface.GetLayerList().GetSelectedLayers():
            if layer.maplayer.GetType() == "raster":
                raster.append(layer.maplayer.GetName())

        from wxplot.histogram import HistogramPlotFrame

        win = HistogramPlotFrame(parent=self, giface=self._giface, rasterList=raster)
        win.CentreOnParent()
        win.Show()

    def OnScatterplot(self, event):
        """Init PyPlot scatterplot display canvas and tools"""
        raster = []

        for layer in self._giface.GetLayerList().GetSelectedLayers():
            if layer.maplayer.GetType() == "raster":
                raster.append(layer.maplayer.GetName())

        from wxplot.scatter import ScatterFrame

        win = ScatterFrame(parent=self, giface=self._giface, rasterList=raster)

        win.CentreOnParent()
        win.Show()
        # Open raster select dialog to make sure that at least 2 rasters (and the
        # desired rasters) are selected to be plotted
        win.OnSelectRaster(None)

    def OnHistogram(self, event):
        """Init histogram display canvas and tools"""
        from modules.histogram import HistogramFrame

        win = HistogramFrame(self, giface=self._giface)

        win.CentreOnParent()
        win.Show()
        win.Refresh()
        win.Update()

    def _activateOverlay(self, overlayId):
        """Launch decoration dialog according to overlay id.

        :param overlayId: id of overlay
        """
        if overlayId in self.decorations:
            dlg = self.decorations[overlayId].dialog
            if dlg.IsShown():
                dlg.SetFocus()
                dlg.Raise()
            else:
                dlg.Show()

    def RemoveOverlay(self, overlayId):
        """Hide overlay.

        :param overlayId: id of overlay
        """
        del self._decorationWindows[self.decorations[overlayId].dialog]
        self.decorations[overlayId].Remove()
        del self.decorations[overlayId]

    def AddBarscale(self, cmd=None):
        """Handler for scale bar map decoration menu selection."""
        if self.IsPaneShown("3d"):
            self.MapWindow3D.SetDrawScalebar((70, 70))
            return

        if cmd:
            show = False
        else:
            show = True
            cmd = ["d.barscale"]

        # Decoration overlay control dialog
        GUI(parent=self, giface=self._giface, show=show, modal=False).ParseCommand(
            cmd, completed=(self.GetOptData, None, None)
        )

        self.MapWindow.mouse["use"] = "pointer"

    def AddLegendRast(self, cmd=None):
        """Handler for legend raster map decoration menu selection."""

        if cmd:
            show = False
        else:
            show = True
            cmd = ["d.legend"]
            layers = self._giface.GetLayerList().GetSelectedLayers()
            for layer in layers:
                if layer.type == "raster":
                    cmd.append("raster={rast}".format(rast=layer.maplayer.name))
                    break

        GUI(parent=self, giface=self._giface, show=show, modal=False).ParseCommand(
            cmd, completed=(self.GetOptData, None, None)
        )

        self.MapWindow.mouse["use"] = "pointer"

    def AddLegendVect(self, cmd=None, showDialog=None):
        """Handler for legend vector map decoration menu selection."""

        if cmd:
            show = False
        else:
            show = True
            cmd = ["d.legend.vect"]

        GUI(parent=self, giface=self._giface, show=show, modal=False).ParseCommand(
            cmd, completed=(self.GetOptData, None, None)
        )

        self.MapWindow.mouse["use"] = "pointer"

    def AddArrow(self, cmd=None):
        """Handler for north arrow menu selection."""
        if self.IsPaneShown("3d"):
            # here was opening of appearance page of nviz notebook
            # but now moved to MapWindow3D where are other problematic nviz
            # calls
            self.MapWindow3D.SetDrawArrow((70, 70))
            return

        if cmd:
            show = False
        else:
            show = True
            cmd = ["d.northarrow"]

        # Decoration overlay control dialog
        GUI(parent=self, giface=self._giface, show=show, modal=False).ParseCommand(
            cmd, completed=(self.GetOptData, None, None)
        )

        self.MapWindow.mouse["use"] = "pointer"

    def AddDtext(self, cmd=None):
        """Handler for d.text menu selection."""
        if cmd:
            show = False
        else:
            show = True
            cmd = ["d.text"]

        # Decoration overlay control dialog
        GUI(parent=self, giface=self._giface, show=show, modal=False).ParseCommand(
            cmd, completed=(self.GetOptData, None, None)
        )

        self.MapWindow.mouse["use"] = "pointer"

    def GetOptData(self, dcmd, layer, params, propwin):
        """Called after options are set through module dialog.

        :param dcmd: resulting command
        :param layer: not used
        :param params: module parameters (not used)
        :param propwin: dialog window
        """

        if not dcmd:
            return
        if propwin in self._decorationWindows:
            overlay = self._decorationWindows[propwin]
        else:
            cmd = dcmd[0]
            if cmd == "d.northarrow":
                overlay = ArrowController(self.Map, self._giface)
            elif cmd == "d.barscale":
                overlay = BarscaleController(self.Map, self._giface)
            elif cmd == "d.legend":
                overlay = LegendController(self.Map, self._giface)
            elif cmd == "d.legend.vect":
                overlay = LegendVectController(self.Map, self._giface)
            elif cmd == "d.text":
                overlay = DtextController(self.Map, self._giface)

            self.decorations[overlay.id] = overlay
            overlay.overlayChanged.connect(
                lambda: self.MapWindow2D.UpdateMap(render=False, renderVector=False)
            )
            if self.IsPaneShown("3d"):
                overlay.overlayChanged.connect(self.MapWindow3D.UpdateOverlays)

            overlay.dialog = propwin
            self._decorationWindows[propwin] = overlay

        overlay.cmd = dcmd
        overlay.Show()

    def OnZoomToMap(self, event):
        """Set display extents to match selected raster (including
        NULLs) or vector map.
        """
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
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
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
>>>>>>> osgeo-main
        Debug.msg(3, "MapFrame.OnZoomToMap()")
<<<<<<< HEAD
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
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
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
        Debug.msg(3, "MapFrame.OnZoomToMap()")
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
        Debug.msg(3, "MapFrame.OnZoomToMap()")
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
        Debug.msg(3, "MapFrame.OnZoomToMap()")
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
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
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
        Debug.msg(3, "MapFrame.OnZoomToMap()")
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
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
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
        Debug.msg(3, "MapFrame.OnZoomToMap()")
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
        Debug.msg(3, "MapFrame.OnZoomToMap()")
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
        Debug.msg(3, "MapFrame.OnZoomToMap()")
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
        Debug.msg(3, "MapFrame.OnZoomToMap()")
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
<<<<<<< HEAD
        Debug.msg(3, "MapFrame.OnZoomToMap()")
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
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
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
        Debug.msg(3, "MapFrame.OnZoomToMap()")
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
        Debug.msg(3, "MapPanel.OnZoomToMap()")
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
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
        Debug.msg(3, "MapFrame.OnZoomToMap()")
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
        Debug.msg(3, "MapPanel.OnZoomToMap()")
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
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
        Debug.msg(3, "MapFrame.OnZoomToMap()")
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
        Debug.msg(3, "MapFrame.OnZoomToMap()")
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
        Debug.msg(3, "MapFrame.OnZoomToMap()")
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        Debug.msg(3, "MapPanel.OnZoomToMap()")
=======
        Debug.msg(3, "MapFrame.OnZoomToMap()")
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
        self.MapWindow.ZoomToMap(layers=None)

    def OnZoomToRaster(self, event):
        """Set display extents to match selected raster map (ignore NULLs)"""
        self.MapWindow.ZoomToMap(ignoreNulls=True)

    def OnZoomToSaved(self, event):
        """Set display geometry to match extents in
        saved region file
        """
        self.MapWindow.SetRegion(zoomOnly=True)

    def OnSetDisplayToWind(self, event):
        """Set computational region (WIND file) to match display
        extents
        """
        self.MapWindow.DisplayToWind()

    def OnSetWindToRegion(self, event):
        """Set computational region (WIND file) from named region
        file
        """
        self.MapWindow.SetRegion(zoomOnly=False)

    def OnSetExtentToWind(self, event):
        """Set compulational region extent interactively"""
        self.MapWindow.SetModeDrawRegion()

    def OnSaveDisplayRegion(self, event):
        """Save display extents to named region file."""
        self.MapWindow.SaveRegion(display=True)

    def OnSaveWindRegion(self, event):
        """Save computational region to named region file."""
        self.MapWindow.SaveRegion(display=False)

    def OnZoomMenu(self, event):
        """Popup Zoom menu"""
        zoommenu = Menu()

        for label, handler in (
            (_("Zoom to default region"), self.OnZoomToDefault),
            (_("Zoom to saved region"), self.OnZoomToSaved),
            (None, None),
            (
                _("Set computational region extent from display"),
                self.OnSetDisplayToWind,
            ),
            (
                _("Set computational region extent interactively"),
                self.OnSetExtentToWind,
            ),
            (_("Set computational region from named region"), self.OnSetWindToRegion),
            (None, None),
            (_("Save display geometry to named region"), self.OnSaveDisplayRegion),
            (_("Save computational region to named region"), self.OnSaveWindRegion),
        ):
            if label:
                mid = wx.MenuItem(zoommenu, wx.ID_ANY, label)
                zoommenu.AppendItem(mid)
                self.Bind(wx.EVT_MENU, handler, mid)
            else:
                zoommenu.AppendSeparator()

        # Popup the menu. If an item is selected then its handler will
        # be called before PopupMenu returns.
        self.PopupMenu(zoommenu)
        zoommenu.Destroy()

    def SetProperties(
        self,
        render=False,
        mode=0,
        showCompExtent=False,
        constrainRes=False,
        projection=False,
        alignExtent=True,
    ):
        """Set properties of map display window"""
        self.mapWindowProperties.autoRender = render
        if self.statusbarManager:
            self.statusbarManager.SetMode(mode)
        self.mapWindowProperties.useDefinedProjection = projection
        self.mapWindowProperties.showRegion = showCompExtent
        self.mapWindowProperties.alignExtent = alignExtent
        self.mapWindowProperties.resolution = constrainRes

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5168f3664a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9f5464914c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d4ef6f4dbb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6036b7efea (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
    def IsStandalone(self):
        """Check if Map display is standalone

        .. deprecated:: 7.0
        """
        # TODO: once it is removed from 2 places in vdigit it can be deleted
        # here and also in base class and other classes in the tree (hopefully)
        # and one place here still uses IsStandalone
        Debug.msg(
            1,
            "MapFrame.IsStandalone(): Method IsStandalone is"
            "deprecated, use some general approach instead such as"
            " Signals or giface",
        )
        if self._layerManager:
            return False

        return True

    def GetLayerManager(self):
        """Get reference to Layer Manager

        :return: window reference
        :return: None (if standalone)

        .. deprecated:: 7.0
        """
        Debug.msg(
            1,
            "MapFrame.GetLayerManager(): Method GetLayerManager is"
            "deprecated, use some general approach instead such as"
            " Signals or giface",
        )
        return self._layerManager

>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
=======
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5168f3664a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9f5464914c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d4ef6f4dbb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6036b7efea (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
    def GetMapToolbar(self):
        """Returns toolbar with zooming tools"""
<<<<<<< HEAD
        return self.toolbars.get("map", None)
=======
        return self.toolbars["map"] if "map" in self.toolbars else None
<<<<<<< HEAD
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    def GetDialog(self, name):
        """Get selected dialog if exist"""
        return self.dialogs.get(name, None)

    def OnVNet(self, event):
        """Dialog for v.net* modules"""
        if self.dialogs["vnet"]:
            self.dialogs["vnet"].Raise()
            return

        from vnet.dialogs import VNETDialog

        self.dialogs["vnet"] = VNETDialog(parent=self, giface=self._giface)
        self.closingVNETDialog.connect(self.dialogs["vnet"].OnCloseDialog)
        self.dialogs["vnet"].CenterOnScreen()
        self.dialogs["vnet"].Show()

    def ResetPointer(self):
        """Sets pointer mode.

        Sets pointer and toggles it (e.g. after unregistration of mouse
        handler).
        """
        self.GetMapToolbar().SelectDefault()

    def _switchMapWindow(self, map_win):
        """Notifies activated and disactivated map_wins."""
        self.MapWindow.DisactivateWin()
        map_win.ActivateWin()

        self.MapWindow = map_win

    def AddRDigit(self):
        """Adds raster digitizer: creates toolbar and digitizer controller,
        binds events and signals."""
        from rdigit.controller import RDigitController, EVT_UPDATE_PROGRESS
        from rdigit.toolbars import RDigitToolbar

        self.rdigit = RDigitController(self._giface, mapWindow=self.GetMapWindow())
        self.toolbars["rdigit"] = RDigitToolbar(
            parent=self,
            giface=self._giface,
            controller=self.rdigit,
            toolSwitcher=self._toolSwitcher,
        )
        # connect signals
        self.rdigit.newRasterCreated.connect(self.toolbars["rdigit"].NewRasterAdded)
        self.rdigit.newRasterCreated.connect(
            lambda name: self._giface.mapCreated.emit(name=name, ltype="raster")
        )
        self.rdigit.newFeatureCreated.connect(self.toolbars["rdigit"].UpdateCellValues)
        self.rdigit.uploadMapCategories.connect(
            self.toolbars["rdigit"].UpdateCellValues
        )
        self.rdigit.showNotification.connect(lambda text: self.SetStatusText(text, 0))
        self.rdigit.quitDigitizer.connect(self.QuitRDigit)
        self.rdigit.Bind(
            EVT_UPDATE_PROGRESS,
            lambda evt: self.statusbarManager.SetProgress(
                evt.range, evt.value, evt.text
            ),
        )
        rasters = self.GetMap().GetListOfLayers(
            ltype="raster", mapset=gs.gisenv()["MAPSET"]
        )
        self.toolbars["rdigit"].UpdateRasterLayers(rasters)
        self.toolbars["rdigit"].SelectDefault()

        self.GetMap().layerAdded.connect(self._updateRDigitLayers)
        self.GetMap().layerRemoved.connect(self._updateRDigitLayers)
        self.GetMap().layerChanged.connect(self._updateRDigitLayers)
        self._mgr.AddPane(
            self.toolbars["rdigit"],
            wx.aui.AuiPaneInfo()
            .Name("rdigit toolbar")
            .Caption(_("Raster Digitizer Toolbar"))
            .ToolbarPane()
            .Top()
            .Row(1)
            .LeftDockable(False)
            .RightDockable(False)
            .BottomDockable(False)
            .TopDockable(True)
            .Floatable()
            .CloseButton(False)
            .Layer(2)
            .DestroyOnClose()
            .BestSize(self.toolbars["rdigit"].GetBestSize()),
        )
        self._mgr.Update()

        self.rdigit.Start()

    def _updateRDigitLayers(self, layer):
        mapset = gs.gisenv()["MAPSET"]
        self.toolbars["rdigit"].UpdateRasterLayers(
            rasters=self.GetMap().GetListOfLayers(ltype="raster", mapset=mapset)
        )

    def QuitRDigit(self):
        """Calls digitizer cleanup, removes digitizer object and disconnects
        signals from Map."""
        self.rdigit.CleanUp()
        # disconnect updating layers
        self.GetMap().layerAdded.disconnect(self._updateRDigitLayers)
        self.GetMap().layerRemoved.disconnect(self._updateRDigitLayers)
        self.GetMap().layerChanged.disconnect(self._updateRDigitLayers)
        self._toolSwitcher.toggleToolChanged.disconnect(
            self.toolbars["rdigit"].CheckSelectedTool,
        )

        self.RemoveToolbar("rdigit", destroy=True)
        self.rdigit = None

    def QuitVDigit(self):
        """Quit VDigit"""
        # disable the toolbar
        self.RemoveToolbar("vdigit", destroy=True)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
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
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
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
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
=======
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
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
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
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
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
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
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
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
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
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
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
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))


class MapDisplay(FrameMixin, MapPanel):
    """Map display for wrapping map panel with frame methods"""

    def __init__(self, parent, giface, id, tree, lmgr, idx, Map, title, **kwargs):
        # init map panel
        MapPanel.__init__(
            self,
            parent=parent,
            giface=giface,
            id=id,
            tree=tree,
            lmgr=lmgr,
            Map=Map,
            title=title,
            **kwargs,
        )
        # set system icon
        parent.SetIcon(
            wx.Icon(
                os.path.join(globalvar.ICONDIR, "grass_map.ico"), wx.BITMAP_TYPE_ICO
            )
        )
        # use default frame window layout
        client_disp = wx.ClientDisplayRect()
        if UserSettings.Get(group="general", key="defWindowPos", subkey="enabled"):
            dim = UserSettings.Get(group="general", key="defWindowPos", subkey="dim")
            idx = 4 + idx * 4
            try:
                x, y = map(int, dim.split(",")[idx : idx + 2])
                w, h = map(int, dim.split(",")[idx + 2 : idx + 4])
                if x == 1:
                    # Get client display x offset (OS panel)
                    x = client_disp[0]
                if y == 1:
                    # Get client display y offset (OS panel)
                    y = client_disp[1]
                parent.SetPosition((x, y))
                parent.SetSize((w, h))
            except Exception:
                pass
        else:
            # Set client display x, y offset (OS panel)
            parent.SetPosition((client_disp[0], client_disp[1]))

        # bindings
        parent.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        # extend shortcuts and create frame accelerator table
        self.shortcuts_table.append((self.OnFullScreen, wx.ACCEL_NORMAL, wx.WXK_F11))
        self._initShortcuts()

        # add Map Display panel to Map Display frame
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self, proportion=1, flag=wx.EXPAND)
        parent.SetSizer(sizer)
        parent.Layout()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
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
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
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
>>>>>>> osgeo-main
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
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
<<<<<<< HEAD
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
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
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
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
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
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
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
