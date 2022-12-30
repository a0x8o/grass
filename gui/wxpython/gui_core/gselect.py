"""
@package gui_core.gselect

@brief Custom control that selects elements

Classes:
 - :class:`Select`
 - :class:`VectorSelect`
 - :class:`ListCtrlComboPopup`
 - :class:`TreeCrtlComboPopup`
 - :class:`VectorDBInfo`
 - :class:`LayerSelect`
 - :class:`DriverSelect`
 - :class:`DatabaseSelect`
 - :class:`TableSelect`
 - :class:`ColumnSelect`
 - :class:`DbaseSelect`
 - :class:`LocationSelect`
 - :class:`MapsetSelect`
 - :class:`SubGroupSelect`
 - :class:`FormatSelect`
 - :class:`GdalSelect`
 - :class:`ProjSelect`
 - :class:`ElementSelect`
 - :class:`OgrTypeSelect`
 - :class:`CoordinatesSelect`
 - :class:`VectorCategorySelect`
 - :class:`SignatureSelect`
 - :class:`SignatureTypeSelect`
 - :class:`SeparatorSelect`
 - :class:`SqlWhereSelect`

(C) 2007-2023 by the GRASS Development Team

This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.

@author Michael Barton
@author Martin Landa <landa.martin gmail.com>
@author Vaclav Petras <wenzeslaus gmail.com> (menu customization)
@author Stepan Turek <stepan.turek seznam.cz> (CoordinatesSelect, ListCtrlComboPopup)
@author Matej Krejci <matejkrejci gmail.com> (VectorCategorySelect)
"""

import os
import sys
import glob
<<<<<<< HEAD
=======
import six
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> d1e0f3a451 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1b62444dcb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5b7ab488c3 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 101a8cef7f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c621983a87 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67d74ea5b0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0ba4fb709f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f440f5d30 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c940746c7a (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> db3baef4a0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 42e8aaeeb9 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 998dac8c79 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 273146cb7f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> d1e0f3a451 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 228be75788 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1b62444dcb (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 94afdfdae9 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 5b7ab488c3 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> e435dd0d3f (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 101a8cef7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 0873fb5a66 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c621983a87 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> af0cda6849 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 67d74ea5b0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> cd2a15c8d0 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 0ba4fb709f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12e7124573 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 7f440f5d30 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> a74c224a9d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c940746c7a (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 210c8f3c49 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> db3baef4a0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 998dac8c79 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 273146cb7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 72d2bd2407 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 42e8aaeeb9 (ci: Ignore paths in CodeQL (#1778))
import ctypes

from pathlib import Path
=======
import ctypes
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
import ctypes
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

import wx

from core import globalvar
from wx.lib import buttons
import wx.lib.filebrowsebutton as filebrowse


import grass.script as gs
from grass.script import task as gtask
from grass.exceptions import CalledModuleError

from gui_core.widgets import ManageSettingsWidget, CoordinatesValidator

from core.gcmd import RunCommand, GError, GMessage, GWarning, GException
from core.utils import (
    GetListOfLocations,
    GetListOfMapsets,
    GetFormats,
    rasterFormatExtension,
    vectorFormatExtension,
)
from core.utils import GetSettingsPath, GetValidLayerName, ListSortLower
from core.utils import GetVectorNumberOfLayers
from core.settings import UserSettings
from core.debug import Debug
from gui_core.vselect import VectorSelectBase
from gui_core.wrap import (
    TreeCtrl,
    Button,
    StaticText,
    StaticBox,
    TextCtrl,
    Panel,
    ComboPopup,
    ComboCtrl,
)

from grass.pydispatch.signal import Signal


class Select(ComboCtrl):
    def __init__(
        self,
        parent,
        id=wx.ID_ANY,
        size=globalvar.DIALOG_GSELECT_SIZE,
        type=None,
        multiple=False,
        nmaps=1,
        mapsets=None,
        updateOnPopup=True,
        onPopup=None,
        fullyQualified=True,
        extraItems={},
        layerTree=None,
        validator=wx.DefaultValidator,
    ):
        """Custom control to create a ComboBox with a tree control to
        display and select GIS elements within accessible mapsets.
        Elements can be selected with mouse. Can allow multiple
        selections, when argument <em>multiple</em> is True. Multiple
        selections are separated by commas.

        :param type: type of GIS elements ('raster, 'vector', ...)
        :param multiple: True for multiple input
        :param nmaps: number of maps to be entered
        :param mapsets: force list of mapsets (otherwise search path)
        :param updateOnPopup: True for updating list of elements on popup
        :param onPopup: function to be called on Popup
        :param fullyQualified: True to provide fully qualified names (map@mapset)
        :param extraItems: extra items to add (given as dictionary)
                           - see gmodeler for usage
        :param layerTree: show only elements from given layer tree if not None
        :param validator: validator for TextCtrl
        """
        ComboCtrl.__init__(self, parent=parent, id=id, size=size, validator=validator)
        if globalvar.CheckWxVersion([3]):
            self.SetName("Select")
        else:
            self.GetChildren()[0].SetName("Select")

        self.GetChildren()[0].type = type

        self.tcp = TreeCtrlComboPopup()
        self.SetPopupControl(self.tcp)
        self.SetPopupExtents(0, 100)
        if type:
            self.tcp.SetData(
                type=type,
                mapsets=mapsets,
                multiple=multiple,
                nmaps=nmaps,
                updateOnPopup=updateOnPopup,
                onPopup=onPopup,
                fullyQualified=fullyQualified,
                extraItems=extraItems,
                layerTree=layerTree,
            )
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

    def OnKeyDown(self, event):
        """Open popup and send key events to the tree."""
        if self.IsPopupShown():
            # on some configurations we get key down, with some only key up
            # so we are trying to catch either key up or down
            # this mess shouldn't be necessary with wxPython 3
            self.tcp.OnKeyUp(event)
        else:
            if event.GetKeyCode() == wx.WXK_DOWN:
                self.ShowPopup()
            event.Skip()

    def SetElementList(self, type, mapsets=None):
        """Set element list

        :param type: GIS element type
        :param mapsets: list of acceptable mapsets (None for all in search path)
        """
        self.tcp.SetData(type=type, mapsets=mapsets)

    def GetElementList(self):
        """Load elements"""
        self.tcp.GetElementList()

    def SetType(
        self,
        etype,
        multiple=False,
        nmaps=1,
        mapsets=None,
        updateOnPopup=True,
        onPopup=None,
    ):
        """Param set element type for widget

        :param etype: element type, see gselect.ElementSelect
        """
        self.tcp.SetData(
            type=etype,
            mapsets=mapsets,
            multiple=multiple,
            nmaps=nmaps,
            updateOnPopup=updateOnPopup,
            onPopup=onPopup,
        )


class VectorSelect(Select):
    def __init__(self, parent, ftype, **kwargs):
        """Custom to create a ComboBox with a tree control to display and
        select vector maps. You can filter the vector maps. If you
        don't need this feature use Select class instead

        :param ftype: filter vector maps based on feature type
        """
        Select.__init__(self, parent=parent, id=wx.ID_ANY, type="vector", **kwargs)

        self.ftype = ftype

        # remove vector maps which do not contain given feature type
        self.tcp.SetFilter(self._isElement)

    def _isElement(self, vectorName):
        """Check if element should be filtered out"""
        try:
            if int(gs.vector_info_topo(vectorName)[self.ftype]) < 1:
                return False
        except KeyError:
            return False

        return True


class ListCtrlComboPopup(ComboPopup):
    """Create a list ComboBox using TreeCtrl with hidden root.

    .. todo::

        use event.EventObject instead of hardcoding (see forms.py)
        https://groups.google.com/forum/#!topic/wxpython-users/pRz6bi0k0XY

    """

    # overridden ComboPopup methods

    def Init(self):
        self.value = []  # for multiple is False ->
        # len(self.value) in [0,1]
        self.curitem = None
        self.multiple = False
        self.updateOnPopup = True
        self.filterItems = []  # limit items based on this list,
        # see layerTree parameter

    def Create(self, parent):
        self.seltree = TreeCtrl(
            parent,
            style=wx.TR_HIDE_ROOT
            | wx.TR_HAS_BUTTONS
            | wx.TR_SINGLE
            | wx.TR_LINES_AT_ROOT
            | wx.SIMPLE_BORDER
            | wx.TR_FULL_ROW_HIGHLIGHT,
        )
        self.seltree.Bind(wx.EVT_MOTION, self.OnMotion)
        self.seltree.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        # the following dummy handler are needed to keep tree events
        # from propagating up to the parent GIS Manager layer tree
        self.seltree.Bind(wx.EVT_TREE_ITEM_EXPANDING, lambda x: None)
        self.seltree.Bind(wx.EVT_TREE_ITEM_COLLAPSED, lambda x: None)
        self.seltree.Bind(wx.EVT_TREE_SEL_CHANGED, lambda x: None)
        self.seltree.Bind(wx.EVT_TREE_DELETE_ITEM, lambda x: None)
        self.seltree.Bind(wx.EVT_TREE_BEGIN_DRAG, lambda x: None)
        self.seltree.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, lambda x: None)
        # navigation in list/tree is handled automatically since wxPython 3
        # for older versions, we have to workaround it and write our own
        # navigation
        if globalvar.CheckWxVersion(version=[3]):
            self.seltree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self._onItemConfirmed)
            self.seltree.Bind(wx.EVT_TREE_KEY_DOWN, self._onDismissPopup)
        else:
            self.seltree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, lambda x: None)
            self.seltree.Bind(wx.EVT_KEY_UP, self.OnKeyUp)

        return True

    def GetControl(self):
        return self.seltree

    def GetComboCtrl(self):
        if globalvar.wxPythonPhoenix:
            return super().GetComboCtrl()
        return self.GetCombo()

    def GetStringValue(self):
        """Get value as a string separated by commas"""
        return ",".join(self.value)

    def SetStringValue(self, value):
        # this assumes that item strings are unique...
        root = self.seltree.GetRootItem()
        if not root:
            return
        winValue = self.GetComboCtrl().GetValue().strip(",")
        self.value = []
        if winValue:
            self.value = winValue.split(",")

    def OnPopup(self, force=False):
        """Limited only for first selected"""
        if not force and not self.updateOnPopup:
            return

        # selects map starting according to written text
        inputText = self.GetComboCtrl().GetValue().strip()
        if inputText:
            root = self.seltree.GetRootItem()
            match = self.FindItem(root, inputText, startLetters=True)
            if match.IsOk():
                self.seltree.EnsureVisible(match)
                self.seltree.SelectItem(match)

    def GetAdjustedSize(self, minWidth, prefHeight, maxHeight):
        """Reads UserSettings to get height (which was 200 in old implementation)."""
        height = UserSettings.Get(
            group="appearance", key="gSelectPopupHeight", subkey="value"
        )
        return wx.Size(minWidth, min(height, maxHeight))

    def FindItem(self, parentItem, text, startLetters=False):
        """Finds item with given name or starting with given text"""
        startletters = startLetters
        item, cookie = self.seltree.GetFirstChild(parentItem)
        while wx.TreeItemId.IsOk(item):
            if self.seltree.GetItemText(item) == text:
                return item
            if self.seltree.ItemHasChildren(item):
                item = self.FindItem(item, text, startLetters=startletters)
                if wx.TreeItemId.IsOk(item):
                    return item
            elif startletters and self.seltree.GetItemText(item).startswith(
                text.split("@", 1)[0]
            ):
                return item
            item, cookie = self.seltree.GetNextChild(parentItem, cookie)
        return wx.TreeItemId()

    def AddItem(self, value):
        root = self.seltree.GetRootItem()
        if not root:
            root = self.seltree.AddRoot("<hidden root>")
        self.seltree.AppendItem(root, text=value)

    def SetItems(self, items):
        root = self.seltree.GetRootItem()
        if not root:
            root = self.seltree.AddRoot("<hidden root>")
        for item in items:
            self.seltree.AppendItem(root, text=item)

    def OnKeyUp(self, event):
        """Enable to select items using keyboard.

        Unused with wxPython 3, can be removed in the future.
        """
        item = self.seltree.GetSelection()
        if event.GetKeyCode() == wx.WXK_DOWN:
            self.seltree.SelectItem(self.seltree.GetNextVisible(item))

        elif event.GetKeyCode() == wx.WXK_UP:
            itemPrev = self.seltree.GetPrevSibling(item)
            self.seltree.SelectItem(itemPrev)

        elif event.GetKeyCode() == wx.WXK_ESCAPE:
            self.Dismiss()

        elif event.GetKeyCode() == wx.WXK_RETURN:
            self.seltree.SelectItem(item)
            self.curitem = item
            self._selectTreeItem(item)
            self.Dismiss()

    def _onDismissPopup(self, event):
        """Hide popup without selecting item on Esc"""
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.Dismiss()
        else:
            event.Skip()

    def _selectTreeItem(self, item):
        item_str = self.seltree.GetItemText(item)
        if self.multiple:
            if item_str not in self.value:
                self.value.append(item_str)
        else:
            self.value = [item_str]

    def _onItemConfirmed(self, event):
        item = event.GetItem()
        self._selectTreeItem(item)
        self.Dismiss()

    def OnMotion(self, evt):
        """Have the selection follow the mouse, like in a real combobox"""
        item, flags = self.seltree.HitTest(evt.GetPosition())
        if item and flags & wx.TREE_HITTEST_ONITEMLABEL:
            self.seltree.SelectItem(item)
            self.curitem = item
        evt.Skip()

    def OnLeftDown(self, evt):
        """Do the combobox selection"""
        if self.curitem is None:
            return

        self._selectTreeItem(self.curitem)
        self.Dismiss()

        evt.Skip()

    def SetData(self, **kargs):
        """Set object properties"""
        if "multiple" in kargs:
            self.multiple = kargs["multiple"]
        if "onPopup" in kargs:
            self.onPopup = kargs["onPopup"]
        if kargs.get("layerTree"):
            self.filterItems = []  # reset
            ltype = kargs["type"]
            for layer in kargs["layerTree"].GetVisibleLayers(skipDigitized=True):
                if layer.GetType() != ltype:
                    continue
                self.filterItems.append(layer.GetName())

    def DeleteAllItems(self):
        """Delete all items in popup"""
        self.seltree.DeleteAllItems()


class TreeCtrlComboPopup(ListCtrlComboPopup):
    """Create a tree ComboBox for selecting maps and other GIS elements
    in accessible mapsets within the current location
    """

    # overridden ComboPopup methods

    def Init(self):
        ListCtrlComboPopup.Init(self)
        self.nmaps = 1
        self.type = None
        self.mapsets = None
        self.onPopup = None
        self.fullyQualified = True
        self.extraItems = {}

        self.SetFilter(None)
        self.tgis_error = False

    def SetFilter(self, filter):
        """Set filter for GIS elements, see e.g. VectorSelect"""
        self.filterElements = filter

    def OnPopup(self, force=False):
        """Limited only for first selected"""
        if not force and not self.updateOnPopup:
            return
        if self.onPopup:
            selected, exclude = self.onPopup(self.type)
        else:
            selected = None
            exclude = False

        self.GetElementList(selected, exclude)

        ListCtrlComboPopup.OnPopup(self, force)

    def GetElementList(self, elements=None, exclude=False):
        """Get filtered list of GIS elements in accessible mapsets
        and display as tree with all relevant elements displayed
        beneath each mapset branch
        """
        # update list
        self.seltree.DeleteAllItems()
        if self.type:
            self._getElementList(self.type, self.mapsets, elements, exclude)

        if len(self.value) > 0:
            root = self.seltree.GetRootItem()
            if not root:
                return
            item = self.FindItem(root, self.value[0])
            try:
                self.seltree.EnsureVisible(item)
                self.seltree.SelectItem(item)
            except Exception:
                pass

    def _getElementList(self, element, mapsets=None, elements=None, exclude=False):
        """Get list of GIS elements in accessible mapsets and display as tree
        with all relevant elements displayed beneath each mapset branch

        :param element: GIS element
        :param mapsets: list of acceptable mapsets (None for all mapsets in search path)
        :param elements: list of forced GIS elements
        :param exclude: True to exclude, False for forcing the list (elements)
        """
        # get current mapset
        curr_mapset = gs.gisenv()["MAPSET"]

        # map element types to g.list types
        elementdict = {
            "cell": "raster",
            "raster": "raster",
            "grid3": "raster_3d",
            "raster_3d": "raster_3d",
            "vector": "vector",
            "paint/labels": "label",
            "label": "label",
            "windows": "region",
            "region": "region",
            "group": "group",
            "stds": "stds",
            "strds": "strds",
            "str3ds": "str3ds",
            "stvds": "stvds",
        }

        # to support multiple elements
        element_list = element.split(",")
        renamed_elements = []
        for elem in element_list:
            if elem not in elementdict:
                self.AddItem(_("Not selectable element"), node=False)
                return
            renamed_elements.append(elementdict[elem])

        if element in {"stds", "strds", "str3ds", "stvds"}:
            if not self.tgis_error:
                import grass.temporal as tgis

                filesdict = tgis.tlist_grouped(elementdict[element], element == "stds")
            else:
                filesdict = None
        else:
            filesdict = gs.list_grouped(renamed_elements, check_search_path=False)

        # add extra items first
        if self.extraItems:
            for group, items in self.extraItems.items():
                node = self.AddItem(group, node=True)
                self.seltree.SetItemTextColour(node, wx.Colour(50, 50, 200))
                for item in items:
                    self.AddItem(item, node=False, parent=node)
                self.seltree.ExpandAllChildren(node)

        # list of mapsets in current location
        if mapsets is None:
            mapsets = gs.mapsets(search_path=True)

        # current mapset first
        if curr_mapset in mapsets and mapsets[0] != curr_mapset:
            mapsets.remove(curr_mapset)
            mapsets.insert(0, curr_mapset)

        first_mapset = None
        for mapset in mapsets:
            mapset_node = self.AddItem(
                _("Mapset") + ": " + mapset, node=True, mapset=mapset
            )
            node = mapset_node
            if not first_mapset:
                first_mapset = mapset_node

            self.seltree.SetItemTextColour(mapset_node, wx.Colour(50, 50, 200))
            if mapset not in filesdict:
                continue
            try:
                if isinstance(filesdict[mapset], dict):
                    for elementType in filesdict[mapset].keys():
                        node = self.AddItem(
                            _("Type: ") + elementType,
                            mapset=mapset,
                            node=True,
                            parent=mapset_node,
                        )
                        self.seltree.SetItemTextColour(node, wx.Colour(50, 50, 200))
                        elem_list = filesdict[mapset][elementType]
                        self._addItems(
                            elist=elem_list,
                            elements=elements,
                            mapset=mapset,
                            exclude=exclude,
                            node=node,
                        )
                else:
                    elem_list = filesdict[mapset]
                    self._addItems(
                        elist=elem_list,
                        elements=elements,
                        mapset=mapset,
                        exclude=exclude,
                        node=node,
                    )
            except Exception as e:
                sys.stderr.write(_("GSelect: invalid item: %s") % e)
                continue

            if self.seltree.ItemHasChildren(mapset_node):
                sel = UserSettings.Get(
                    group="appearance", key="elementListExpand", subkey="selection"
                )
                collapse = True

                if sel == 0:  # collapse all except PERMANENT and current
                    if mapset in {"PERMANENT", curr_mapset}:
                        collapse = False
                elif sel == 1:  # collapse all except PERMANENT
                    if mapset == "PERMANENT":
                        collapse = False
                elif sel == 2:  # collapse all except current
                    if mapset == curr_mapset:
                        collapse = False
                elif sel == 3:  # collapse all
                    pass
                elif sel == 4:  # expand all
                    collapse = False

                if collapse:
                    self.seltree.CollapseAllChildren(mapset_node)
                else:
                    self.seltree.ExpandAllChildren(mapset_node)

        if first_mapset:
            # select first mapset (MSW hack)
            self.seltree.SelectItem(first_mapset)

    # helpers
    def _addItems(self, elist, elements, mapset, exclude, node):
        """Helper function for adding multiple items (maps, stds).

        :param list elist: list of map/stds names
        :param list elements: list of forced elements
        :param str mapset:  mapset name
        :param exclude: True to exclude, False for forcing the list
        :param node: parent node
        """
        elist = gs.naturally_sorted(elist)
        for elem in elist:
            if elem != "":
                fullqElem = elem + "@" + mapset
                if self.filterItems and fullqElem not in self.filterItems:
                    continue  # skip items missed in self.filterItems

                if elements is not None:
                    if (exclude and fullqElem in elements) or (
                        not exclude and fullqElem not in elements
                    ):
                        continue

                if self.filterElements:
                    if self.filterElements(fullqElem):
                        self.AddItem(elem, mapset=mapset, node=False, parent=node)
                else:
                    self.AddItem(elem, mapset=mapset, node=False, parent=node)

    def AddItem(self, value, mapset=None, node=True, parent=None):
        if not parent:
            root = self.seltree.GetRootItem()
            if not root:
                root = self.seltree.AddRoot("<hidden root>")
            parent = root

        data = {"node": node, "mapset": mapset}

        return self.seltree.AppendItem(parent, text=value, data=data)

    def OnKeyUp(self, event):
        """Enables to select items using keyboard

        Unused with wxPython 3, can be removed in the future.
        """

        item = self.seltree.GetSelection()
        if event.GetKeyCode() == wx.WXK_DOWN:
            self.seltree.SelectItem(self.seltree.GetNextVisible(item))

        # problem with GetPrevVisible
        elif event.GetKeyCode() == wx.WXK_UP:
            if self.seltree.ItemHasChildren(item) and self.seltree.IsExpanded(
                self.seltree.GetPrevSibling(item)
            ):
                itemPrev = self.seltree.GetLastChild(self.seltree.GetPrevSibling(item))
            else:
                itemPrev = self.seltree.GetPrevSibling(item)
                if not wx.TreeItemId.IsOk(itemPrev):
                    itemPrev = self.seltree.GetItemParent(item)
                    if (
                        item
                        == self.seltree.GetFirstChild(self.seltree.GetRootItem())[0]
                    ):
                        itemPrev = item
            self.seltree.SelectItem(itemPrev)

        # selects first item starting with the written text in next mapset
        elif event.GetKeyCode() == wx.WXK_TAB:
            selected = self.seltree.GetSelection()
            if self.seltree.ItemHasChildren(selected):
                parent = selected
            else:
                parent = self.seltree.GetItemParent(selected)
            nextSibling = self.seltree.GetNextSibling(parent)
            if wx.TreeItemId.IsOk(nextSibling):
                match = self.FindItem(
                    nextSibling, self.GetCombo().GetValue().strip(), True
                )
            else:
                match = self.FindItem(
                    self.seltree.GetFirstChild(self.seltree.GetItemParent(parent))[0],
                    self.GetCombo().GetValue().strip(),
                    True,
                )
            self.seltree.SelectItem(match)

        elif event.GetKeyCode() == wx.WXK_RIGHT:
            if self.seltree.ItemHasChildren(item):
                self.seltree.Expand(item)

        elif event.GetKeyCode() == wx.WXK_LEFT:
            if self.seltree.ItemHasChildren(item):
                self.seltree.Collapse(item)

        elif event.GetKeyCode() == wx.WXK_ESCAPE:
            self.Dismiss()

        elif event.GetKeyCode() == wx.WXK_RETURN:
            if self.seltree.GetItemData(item)["node"]:
                self.value = []
            else:
                self._selectTreeItem(item)

            self.Dismiss()

    def OnLeftDown(self, evt):
        """Do the combobox selection"""
        item, flags = self.seltree.HitTest(evt.GetPosition())
        if item and flags & wx.TREE_HITTEST_ONITEMLABEL:
            self.curitem = item

            if self.seltree.GetItemData(item)["node"]:
                evt.Skip()
                return

            self._selectTreeItem(item)
            self.Dismiss()

        evt.Skip()

    def _selectTreeItem(self, item):
        fullName = self.seltree.GetItemText(item)
        if self.fullyQualified and self.seltree.GetItemData(item)["mapset"]:
            fullName += "@" + self.seltree.GetItemData(item)["mapset"]

        if self.multiple:
            self.value.append(fullName)
        elif self.nmaps > 1:  # see key_desc
            if len(self.value) >= self.nmaps:
                self.value = [fullName]
            else:
                self.value.append(fullName)
        else:
            self.value = [fullName]

    def _onItemConfirmed(self, event):
        item = event.GetItem()
        if self.seltree.GetItemData(item)["node"]:
            self.value = []
        else:
            self._selectTreeItem(item)
        self.Dismiss()

    def SetData(self, **kargs):
        """Set object properties"""
        ListCtrlComboPopup.SetData(self, **kargs)
        if "type" in kargs:
            self.type = kargs["type"]
            if self.type in {"stds", "strds", "str3ds", "stvds"}:
                # Initiate the temporal framework. Catch database error
                # and set the error flag for the stds listing.
                try:
                    import grass.temporal as tgis
                    from grass.pygrass import messages

                    try:
                        tgis.init(True)
                    except messages.FatalError as e:
                        sys.stderr.write(_("Temporal GIS error:\n%s") % e)
                        self.tgis_error = True
                except ImportError as e:
                    # PyGRASS (ctypes) is the likely cause
                    sys.stderr.write(
                        _(
                            "Unable to import pyGRASS: %s\n"
                            "Some functionality will be not accessible"
                        )
                        % e
                    )
                    self.tgis_error = True
        if "mapsets" in kargs:
            self.mapsets = kargs["mapsets"]
        if "nmaps" in kargs:
            self.nmaps = kargs["nmaps"]
        if "updateOnPopup" in kargs:
            self.updateOnPopup = kargs["updateOnPopup"]
        if "fullyQualified" in kargs:
            self.fullyQualified = kargs["fullyQualified"]
        if "extraItems" in kargs:
            self.extraItems = kargs["extraItems"]

    def GetType(self):
        """Get element type"""
        return self.type


class VectorDBInfo:
    """Class providing information about attribute tables
    linked to a vector map"""

    def __init__(self, map):
        self.map = map

        # dictionary of layer number and associated (driver, database, table)
        self.layers = {}
        # dictionary of table and associated columns (type, length, values,
        # ids)
        self.tables = {}

        if not self._CheckDBConnection():  # -> self.layers
            return

        self._DescribeTables()  # -> self.tables

    def _CheckDBConnection(self):
        """Check DB connection"""
        nuldev = open(os.devnull, "w+")
        # if map is not defined (happens with vnet initialization) or it
        # doesn't exist
        try:
            self.layers = gs.vector_db(map=self.map, stderr=nuldev)
        except CalledModuleError:
            return False
        finally:  # always close nuldev
            nuldev.close()

        return bool(len(self.layers.keys()) > 0)

    def _DescribeTables(self):
        """Describe linked tables"""
        for layer in self.layers.keys():
            # determine column names and types
            table = self.layers[layer]["table"]
            columns = {}  # {name: {type, length, [values], [ids]}}
            i = 0
            Debug.msg(
                1,
                "gselect.VectorDBInfo._DescribeTables(): table=%s driver=%s database=%s"
                % (
                    self.layers[layer]["table"],
                    self.layers[layer]["driver"],
                    self.layers[layer]["database"],
                ),
            )
            for item in gs.db_describe(
                table=self.layers[layer]["table"],
                driver=self.layers[layer]["driver"],
                database=self.layers[layer]["database"],
            )["cols"]:
                name, type, length = item
                # FIXME: support more datatypes
                if type.lower() == "integer":
                    ctype = int
                elif type.lower() == "double precision":
                    ctype = float
                else:
                    ctype = str

                columns[name.strip()] = {
                    "index": i,
                    "type": type.lower(),
                    "ctype": ctype,
                    "length": int(length),
                    "values": [],
                    "ids": [],
                }
                i += 1

            # check for key column
            # v.db.connect -g/p returns always key column name lowercase
            if self.layers[layer]["key"] not in columns.keys():
                for col in columns.keys():
                    if col.lower() == self.layers[layer]["key"]:
                        self.layers[layer]["key"] = col.upper()
                        break

            self.tables[table] = columns

        return True

    def Reset(self):
        """Reset"""
        for layer in self.layers:
            table = self.layers[layer]["table"]  # get table desc
            for name in self.tables[table].keys():
                self.tables[table][name]["values"] = []
                self.tables[table][name]["ids"] = []

    def GetName(self):
        """Get vector name"""
        return self.map

    def GetKeyColumn(self, layer):
        """Get key column of given layer

        :param layer: vector layer number
        """
        return str(self.layers[layer]["key"])

    def GetTable(self, layer):
        """Get table name of given layer

        :param layer: vector layer number
        """
        if layer not in self.layers:
            raise GException(_("No table linked to layer <{}>.").format(layer))
        return self.layers[layer]["table"]

    def GetDbSettings(self, layer):
        """Get database settings

        :param layer: layer number

        :return: (driver, database)
        """
        return self.layers[layer]["driver"], self.layers[layer]["database"]

    def GetTableDesc(self, table):
        """Get table columns

        :param table: table name
        """
        return self.tables[table]


class LayerSelect(wx.ComboBox):
    def __init__(
        self,
        parent,
        id=wx.ID_ANY,
        size=globalvar.DIALOG_COMBOBOX_SIZE,
        vector=None,
        dsn=None,
        choices=[],
        all=False,
        default=None,
    ):
        """Creates combo box for selecting vector map layer names

        :param str vector: vector map name (native or connected via v.external)
        :param str dsn: OGR data source name
        """
        super().__init__(parent, id, size=size, choices=choices)

        self.all = all

        self.SetName("LayerSelect")

        # default value
        self.default = default

        self.InsertLayers(vector=vector, dsn=dsn)

    def InsertLayers(self, vector=None, dsn=None):
        """Insert layers for a vector into the layer combobox

        :param str vector: vector map name (native or connected via v.external)
        :param str dsn: OGR data source name
        """
        layers = []

        if vector:
            layers = GetVectorNumberOfLayers(vector)
        elif dsn:
            ret = RunCommand("v.in.ogr", read=True, quiet=True, flags="l", input=dsn)
            if ret:
                layers = ret.splitlines()

        if self.default:
            if len(layers) == 0:
                layers.insert(0, str(self.default))
            elif self.default not in layers:
                layers.append(self.default)

        if self.all:
            layers.insert(0, "-1")

        if len(layers) > 0:
            self.SetItems(layers)
        else:
            self.Clear()

        self.SetValue("")

        if self.default and self.default in layers:
            self.SetValue(self.default)


class DriverSelect(wx.ComboBox):
    """Creates combo box for selecting database driver."""

    def __init__(
        self,
        parent,
        choices,
        value,
        id=wx.ID_ANY,
        pos=wx.DefaultPosition,
        size=globalvar.DIALOG_LAYER_SIZE,
        **kargs,
    ):
        super().__init__(parent, id, value, pos, size, choices, style=wx.CB_READONLY)

        self.SetName("DriverSelect")

        self.SetStringSelection(value)


class DatabaseSelect(TextCtrl):
    """Creates combo box for selecting database driver."""

    def __init__(
        self,
        parent,
        value="",
        id=wx.ID_ANY,
        size=globalvar.DIALOG_TEXTCTRL_SIZE,
        **kargs,
    ):
        super().__init__(parent, id, value, size=size, **kargs)
        self.SetName("DatabaseSelect")


class TableSelect(wx.ComboBox):
    """Creates combo box for selecting attribute tables from the database"""

    def __init__(
        self,
        parent,
        id=wx.ID_ANY,
        value="",
        size=globalvar.DIALOG_COMBOBOX_SIZE,
        choices=[],
        **kargs,
    ):
        super().__init__(
            parent, id, value, size=size, choices=choices, style=wx.CB_READONLY, **kargs
        )
        self.SetName("TableSelect")

        if not choices:
            self.InsertTables()

    def InsertTables(self, driver=None, database=None):
        """Insert attribute tables into combobox"""
        items = []

        if not driver or not database:
            connect = gs.db_connection()

            driver = connect["driver"]
            database = connect["database"]

        ret = RunCommand(
            "db.tables", flags="p", read=True, driver=driver, database=database
        )

        if ret:
            for table in ret.splitlines():
                items.append(table)

        self.SetItems(items)
        self.SetValue("")


class ColumnSelect(ComboCtrl):
    """Creates combo box for selecting columns in the attribute table
    for a vector map.

    :param parent: window parent
    :param id: window id
    :param value: default value
    :param size: window size
    :param str vector: vector map name
    :param layer: layer number
    :param multiple: True if it is possible to add multiple columns
    :param param: parameters list (see menuform.py)
    :param kwags: wx.ComboBox parameters
    """

    def __init__(
        self,
        parent,
        id=wx.ID_ANY,
        value="",
        size=globalvar.DIALOG_COMBOBOX_SIZE,
        vector=None,
        layer=1,
        multiple=False,
        param=None,
        **kwargs,
    ):
        self.defaultValue = value
        self.param = param
        self.columns = []

        ComboCtrl.__init__(self, parent, id, size=size, **kwargs)
        self.GetChildren()[0].SetName("ColumnSelect")
        self.GetChildren()[0].type = type

        self.tcp = ListCtrlComboPopup()
        self.SetPopupControl(self.tcp)
        self.tcp.SetData(multiple=multiple)

        if vector:
            self.InsertColumns(vector, layer)
        self.GetChildren()[0].Bind(wx.EVT_KEY_UP, self.OnKeyUp)

    def GetColumns(self):
        return self.columns

    def OnKeyUp(self, event):
        """Shows popupwindow if down arrow key is released"""
        if event.GetKeyCode() == wx.WXK_DOWN and not self.IsPopupShown():
            self.ShowPopup()
        else:
            event.Skip()

    def Clear(self):
        self.tcp.DeleteAllItems()
        self.SetValue("")

    def InsertColumns(
        self, vector, layer, excludeKey=False, excludeCols=None, type=None, dbInfo=None
    ):
        """Insert columns for a vector attribute table into the columns combobox

        :param str vector: vector name
        :param int layer: vector layer number
        :param excludeKey: exclude key column from the list?
        :param excludeCols: list of columns to be removed from the list
        :param type: only columns of given type (given as list)
        """
        if not dbInfo:
            dbInfo = VectorDBInfo(vector)

        try:
            try:
                layer = int(layer)
            except TypeError:
                # assuming layer 1
                layer = 1
            table = dbInfo.GetTable(layer)
            columnchoices = dbInfo.GetTableDesc(table)
            keyColumn = dbInfo.GetKeyColumn(layer)
            self.columns = len(columnchoices.keys()) * [""]
            for key, val in columnchoices.items():
                self.columns[val["index"]] = key
            if excludeKey:  # exclude key column
                self.columns.remove(keyColumn)
            if excludeCols:  # exclude key column
                for key in columnchoices.keys():
                    if key in excludeCols:
                        self.columns.remove(key)
            if type:  # only selected column types
                for key, value in columnchoices.items():
                    if value["type"] not in type:
                        try:
                            self.columns.remove(key)
                        except ValueError:
                            pass
        except (KeyError, ValueError, GException):
            self.columns[:] = []

        # update list
        self.tcp.DeleteAllItems()
        for col in self.columns:
            self.tcp.AddItem(col)

        self.SetValue(self.defaultValue)

        if self.param:
            value = self.param.get("value", "")
            if value != "" and value in self.columns:
                self.SetValue(value)

    def InsertTableColumns(self, table, driver=None, database=None):
        """Insert table columns

        :param str table: table name
        :param str driver: driver name
        :param str database: database name
        """
        self.columns[:] = []

        ret = RunCommand(
            "db.columns", read=True, driver=driver, database=database, table=table
        )

        if ret:
            self.columns = ret.splitlines()

        # update list
        self.tcp.DeleteAllItems()
        self.SetValue(self.defaultValue)

        for col in self.columns:
            self.tcp.AddItem(col)
        if self.param:
            value = self.param.get("value", "")
            if value != "" and value in self.columns:
                self.SetValue(value)


class DbaseSelect(wx.lib.filebrowsebutton.DirBrowseButton):
    """Widget for selecting GRASS Database"""

    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            id=wx.ID_ANY,
            size=globalvar.DIALOG_GSELECT_SIZE,
            labelText="",
            dialogTitle=_("Choose GIS Data Directory"),
            buttonText=_("Browse"),
            startDirectory=gs.gisenv()["GISDBASE"],
            **kwargs,
        )


class LocationSelect(wx.ComboBox):
    """Widget for selecting GRASS location"""

    def __init__(
        self,
        parent,
        id=wx.ID_ANY,
        size=globalvar.DIALOG_COMBOBOX_SIZE,
        gisdbase=None,
        **kwargs,
    ):
        super().__init__(parent, id, size=size, **kwargs)
        self.SetName("LocationSelect")

        if not gisdbase:
            self.gisdbase = gs.gisenv()["GISDBASE"]
        else:
            self.gisdbase = gisdbase

        self.SetItems(GetListOfLocations(self.gisdbase))

    def UpdateItems(self, dbase):
        """Update list of locations

        :param str dbase: path to GIS database
        """
        self.gisdbase = dbase
        if dbase:
            self.SetItems(GetListOfLocations(self.gisdbase))
        else:
            self.SetItems([])


class MapsetSelect(wx.ComboBox):
    """Widget for selecting GRASS mapset"""

    def __init__(
        self,
        parent,
        id=wx.ID_ANY,
        size=globalvar.DIALOG_COMBOBOX_SIZE,
        gisdbase=None,
        location=None,
        setItems=True,
        searchPath=False,
        new=False,
        skipCurrent=False,
        multiple=False,
        **kwargs,
    ):
        style = 0
        # disabled, read-only widget has no TextCtrl children (TODO: rewrite)
        # if not new and not multiple:
        #     style = wx.CB_READONLY

        wx.ComboBox.__init__(self, parent, id, size=size, style=style, **kwargs)
        self.searchPath = searchPath
        self.skipCurrent = skipCurrent
        self.SetName("MapsetSelect")
        self.value = ""
        self.multiple = multiple
        if not gisdbase:
            self.gisdbase = gs.gisenv()["GISDBASE"]
        else:
            self.gisdbase = gisdbase

        if not location:
            self.location = gs.gisenv()["LOCATION_NAME"]
        else:
            self.location = location

        if setItems:
            self.SetItems(self._getMapsets())

        if self.multiple:
            self.Bind(wx.EVT_COMBOBOX, self._onSelection)
            self.Bind(wx.EVT_TEXT, self._onSelection)

    def _onSelection(self, event):
        value = self.GetValue()
        if value:
            if self.value:
                self.value += ","
            self.value += value
            self.SetValue(self.value)
        else:
            self.value = value
        event.Skip()

    def UpdateItems(self, location, dbase=None):
        """Update list of mapsets for given location

        :param str dbase: path to GIS database (None to use currently
                          selected)
        :param str location: name of location
        """
        if dbase:
            self.gisdbase = dbase
        self.location = location

        if location:
            self.SetItems(self._getMapsets())
        else:
            self.SetItems([])

    def _getMapsets(self):
        if self.searchPath:
            mlist = RunCommand(
                "g.mapsets", read=True, flags="p", sep="newline"
            ).splitlines()
        else:
            mlist = GetListOfMapsets(self.gisdbase, self.location, selectable=False)

        gisenv = gs.gisenv()
        if (
            self.skipCurrent
            and gisenv["LOCATION_NAME"] == self.location
            and gisenv["MAPSET"] in mlist
        ):
            mlist.remove(gisenv["MAPSET"])

        return mlist


class SubGroupSelect(wx.ComboBox):
    """Widget for selecting subgroups"""

    def __init__(
        self, parent, id=wx.ID_ANY, size=globalvar.DIALOG_GSELECT_SIZE, **kwargs
    ):
        super().__init__(parent, id, size=size, **kwargs)
        self.SetName("SubGroupSelect")

    def Insert(self, group):
        """Insert subgroups for defined group"""
        if not group:
            return
<<<<<<< HEAD
=======
        gisenv = gs.gisenv()
        try:
            name, mapset = group.split("@", 1)
        except ValueError:
            name = group
            mapset = gisenv["MAPSET"]
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))

        mlist = RunCommand("i.group", group=group, read=True, flags="sg").splitlines()
        try:
            self.SetItems(mlist)
        except OSError:
            self.SetItems([])


class FormatSelect(wx.Choice):
    def __init__(
        self, parent, srcType, ogr=False, size=globalvar.DIALOG_SPIN_SIZE, **kwargs
    ):
        """Widget for selecting external (GDAL/OGR) format

        :param parent: parent window
        :param srcType: source type ('file', 'database', 'protocol')
        :param ogr: True for OGR otherwise GDAL
        """
        super().__init__(parent, id=wx.ID_ANY, size=size, **kwargs)
        self.SetName("FormatSelect")

        ftype = "ogr" if ogr else "gdal"

<<<<<<< HEAD
<<<<<<< HEAD
        formats = []
=======
        formats = list()
<<<<<<< HEAD
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        formats = []
>>>>>>> 962f525ded (style: Fixes unnecessary-collection-call (C408) for empty collections (#3945))
        for f in GetFormats()[ftype][srcType].items():
            formats += f
        self.SetItems(formats)

    def GetExtension(self, name):
        """Get file extension by format name"""
        formatToExt = {}
        formatToExt.update(rasterFormatExtension)
        formatToExt.update(vectorFormatExtension)

        return formatToExt.get(name, "")


class GdalSelect(wx.Panel):
    def __init__(
        self,
        parent,
        panel,
        ogr=False,
        link=False,
        dest=False,
        exclude=None,
        settings=True,
    ):
        """Widget for selecting GDAL/OGR datasource, format

        .. todo::
             Split into GdalSelect and OgrSelect and optionally to
             GdalSelectOutput, OgrSelectOutput

        :param parent: parent window
        :param bool ogr: use OGR selector instead of GDAL
        :param bool dest: True for output (destination)
        :param default: default type (ignored when dest == True)
        :param exclude: list of types to be excluded
        """
        self.parent = parent
        self.ogr = ogr
        self.link = link
        self.dest = dest
        self._sourceType = None
        self._psql = "psql"

        wx.Panel.__init__(self, parent=panel, name="GdalSelect")

        self.reloadDataRequired = Signal("GdalSelect.reloadDataRequired")

        self.inputBox = StaticBox(parent=self)
        if dest:
            self.inputBox.SetLabel(" %s " % _("Output settings"))
        else:
            self.inputBox.SetLabel(" %s " % _("Source input"))

        # source type
        sources = []
        self.sourceMap = {"file": -1, "dir": -1, "db": -1, "pro": -1, "native": -1}
        idx = 0
        if dest:
            sources.append(_("Native"))
            self.sourceMap["native"] = idx
            idx += 1
        if exclude is None:
            exclude = []
        if "file" not in exclude:
            sources.append(_("File"))
            self.sourceMap["file"] = idx
            idx += 1
        if "directory" not in exclude:
            sources.append(_("Directory"))
            self.sourceMap["dir"] = idx
            idx += 1
        if "database" not in exclude:
            sources.append(_("Database"))
            self.sourceMap["db"] = idx
            idx += 1
        if "protocol" not in exclude:
            sources.append(_("Protocol"))
            self.sourceMap["pro"] = idx
            idx += 1
        self.sourceMapByIdx = {}
        for name, idx in self.sourceMap.items():
            self.sourceMapByIdx[idx] = name

        self.source = wx.RadioBox(
            parent=self, id=wx.ID_ANY, style=wx.RA_SPECIFY_COLS, choices=sources
        )
        if dest:
            self.source.SetLabel(" %s " % _("Output type"))
        else:
            self.source.SetLabel(" %s " % _("Source type"))

        self.source.SetSelection(0)
        self.source.Bind(
            wx.EVT_RADIOBOX,
            lambda evt: self.SetSourceType(self.sourceMapByIdx[evt.GetInt()]),
        )

        self.nativeWidgets = {}
        self.fileWidgets = {}
        self.dirWidgets = {}
        self.dbWidgets = {}
        self.protocolWidgets = {}
        self.pgWidgets = {}

        fType = "ogr" if ogr else "gdal"

        # file
        fileMask = "%(all)s (*)|*|" % {"all": _("All files")}
        if not ogr:
            extList = rasterFormatExtension
            fileMask += (
                "%(name)s (*.%(low1)s;*.%(low2)s;*.%(up1)s;*.%(up2)s)|"
                "*.%(low1)s;*.%(low2)s;*.%(up1)s;*.%(up2)s|"
                % {
                    "name": "GeoTIFF",
                    "low1": "tif",
                    "low2": "tiff",
                    "up1": "TIF",
                    "up2": "TIFF",
                }
            )
        else:
            extList = vectorFormatExtension
            fileMask += "%(name)s (*.%(low)s;*.%(up)s)|*.%(low)s;*.%(up)s|" % {
                "name": "ESRI Shapefile",
                "low": "shp",
                "up": "SHP",
            }

        for name, ext in sorted(extList.items()):
            if name in {"ESRI Shapefile", "GeoTIFF"}:
                continue
            fileMask += "%(name)s (*.%(low)s;*.%(up)s)|*.%(low)s;*.%(up)s|" % {
                "name": name,
                "low": ext.lower(),
                "up": ext.upper(),
            }
        fileMask += "%s (*.zip;*.ZIP)|*.zip;*.ZIP|" % _("ZIP files")
        fileMask += "%s (*.gz;*.GZ)|*.gz;*.GZ|" % _("GZIP files")
        fileMask += "%s (*.tar;*.TAR)|*.tar;*.TAR|" % _("TAR files")
        # don't include last '|' - windows and mac throw error
        fileMask += (
            "%s (*.tar.gz;*.TAR.GZ;*.tgz;*.TGZ)|*.tar.gz;*.TAR.GZ;*.tgz;*.TGZ"
            % _("TARGZ files")
        )
        # only contains formats with extensions hardcoded

        self.filePanel = wx.Panel(parent=self)
        browse = filebrowse.FileBrowseButton(
            parent=self.filePanel,
            id=wx.ID_ANY,
            size=globalvar.DIALOG_GSELECT_SIZE,
            labelText=_("File:"),
            dialogTitle=_("Choose file to import"),
            buttonText=_("Browse"),
            startDirectory=str(Path.cwd()),
            changeCallback=self.OnUpdate,
            fileMask=fileMask,
        )
        browse.GetChildren()[1].SetName("GdalSelectDataSource")
        self.fileWidgets["browse"] = browse
        self.fileWidgets["options"] = TextCtrl(parent=self.filePanel)

        # directory
        self.dirPanel = wx.Panel(parent=self)
        browse = filebrowse.DirBrowseButton(
            parent=self.dirPanel,
            id=wx.ID_ANY,
            size=globalvar.DIALOG_GSELECT_SIZE,
            labelText=_("Directory:"),
            dialogTitle=_("Choose input directory"),
            buttonText=_("Browse"),
            startDirectory=str(Path.cwd()),
            changeCallback=self.OnUpdate,
        )
        browse.GetChildren()[1].SetName("GdalSelectDataSource")

        self.dirWidgets["browse"] = browse
        formatSelect = wx.Choice(parent=self.dirPanel)
        self.dirWidgets["format"] = formatSelect
        self.fileFormats = GetFormats(writableOnly=dest)[fType]["file"]
        formatSelect.SetItems(sorted(list(self.fileFormats.values())))
        formatSelect.Bind(
            wx.EVT_CHOICE,
            lambda evt: self.SetExtension(
                self.dirWidgets["format"].GetStringSelection()
            ),
        )
        formatSelect.Bind(wx.EVT_CHOICE, self.OnUpdate)

        self.dirWidgets["extensionLabel"] = StaticText(
            parent=self.dirPanel, label=_("Extension:")
        )
        self.dirWidgets["extension"] = TextCtrl(parent=self.dirPanel)
        self.dirWidgets["extension"].Bind(wx.EVT_TEXT, self.ExtensionChanged)
        self.dirWidgets["options"] = TextCtrl(parent=self.dirPanel)
        if self.ogr:
            shapefile = "ESRI Shapefile"
            if shapefile in self.fileFormats:
                formatSelect.SetStringSelection(shapefile)
                self.SetExtension(shapefile)
        else:
            tiff = "GeoTIFF"
            if tiff in self.fileFormats:
                formatSelect.SetStringSelection(tiff)
                self.SetExtension(tiff)

        # database
        self.dbPanel = wx.Panel(parent=self)

        self.dbFormats = GetFormats(writableOnly=dest)[fType]["database"]
        dbChoice = wx.Choice(parent=self.dbPanel, choices=list(self.dbFormats.values()))
        dbChoice.Bind(
            wx.EVT_CHOICE,
            lambda evt: self.SetDatabase(db=dbChoice.GetStringSelection()),
        )
        self.dbWidgets["format"] = dbChoice

        browse = filebrowse.FileBrowseButton(
            parent=self.dbPanel,
            id=wx.ID_ANY,
            size=globalvar.DIALOG_GSELECT_SIZE,
            labelText=_("Name:"),
            dialogTitle=_("Choose file"),
            buttonText=_("Browse"),
            startDirectory=str(Path.cwd()),
            changeCallback=self.OnUpdate,
        )
        browse.GetChildren()[1].SetName("GdalSelectDataSource")

        self.dbWidgets["browse"] = browse
        self.dbWidgets["choice"] = wx.Choice(
            parent=self.dbPanel, name="GdalSelectDataSource"
        )
        self.dbWidgets["choice"].Bind(wx.EVT_CHOICE, self.OnUpdate)
        self.dbWidgets["text"] = TextCtrl(
            parent=self.dbPanel, name="GdalSelectDataSource"
        )
        self.dbWidgets["text"].Bind(wx.EVT_TEXT, self.OnUpdate)
        self.dbWidgets["textLabel1"] = StaticText(parent=self.dbPanel, label=_("Name:"))
        self.dbWidgets["textLabel2"] = StaticText(parent=self.dbPanel, label=_("Name:"))
        self.dbWidgets["featType"] = wx.RadioBox(
            parent=self.dbPanel,
            id=wx.ID_ANY,
            label=" %s " % _("Feature type:"),
            choices=[_("simple features"), _("topological")],
            majorDimension=2,
            style=wx.RA_SPECIFY_COLS,
        )
        if dest:
            self.dbWidgets["featType"].Disable()
        else:
            self.dbWidgets["featType"].Hide()
        browse = filebrowse.DirBrowseButton(
            parent=self.dbPanel,
            id=wx.ID_ANY,
            size=globalvar.DIALOG_GSELECT_SIZE,
            labelText=_("Directory:"),
            dialogTitle=_("Choose input directory"),
            buttonText=_("Browse"),
            startDirectory=str(Path.cwd()),
            changeCallback=self.OnUpdate,
        )
        self.dbWidgets["dirbrowse"] = browse
        self.dbWidgets["options"] = TextCtrl(parent=self.dbPanel)

        # protocol
        self.protocolPanel = wx.Panel(parent=self)
        self.protocolFormats = GetFormats(writableOnly=self.dest)[fType]["protocol"]
        protocolChoice = wx.Choice(
            parent=self.protocolPanel, choices=list(self.protocolFormats.values())
        )
        self.protocolWidgets["format"] = protocolChoice

        self.protocolWidgets["text"] = TextCtrl(parent=self.protocolPanel)
        self.protocolWidgets["text"].Bind(wx.EVT_TEXT, self.OnUpdate)
        self.protocolWidgets["options"] = TextCtrl(parent=self.protocolPanel)

        # native
        self.nativePanel = wx.Panel(parent=self)

        self._layout()
        sourceType = "file"
        self.SetSourceType(sourceType)  # needed always to fit dialog size
        if self.dest:
            current = RunCommand(
                "v.external.out",
                parent=self,
                read=True,
                parse=gs.parse_key_val,
                flags="g",
            )
            if current["format"] == "native":
                sourceType = "native"
            elif current["format"] in GetFormats()["ogr"]["database"].values():
                sourceType = "db"
            else:
                sourceType = "dir"

        if self.dest:
            wx.CallAfter(self._postInit, sourceType, current)

    def _postInit(self, sourceType, data):
        """Fill in default values."""
        format = data.get("format", "")
        pg = "conninfo" in data.keys()
        if pg:
            dsn = ""
            for item in data.get("conninfo").split(" "):
                k, v = item.split("=")
                if k == "dbname":
                    dsn = v
                    break
            optList = []
            for k, v in data.items():
                if k in {"format", "conninfo", "topology"}:
                    continue
                optList.append("%s=%s" % (k, v))
            options = ",".join(optList)
        else:
            dsn = data.get("dsn")
            options = data.get("options", "")

        self.SetSourceType(sourceType)
        self.source.SetSelection(self.sourceMap[sourceType])

        # v.external.out does not return dsn for the native format
        if dsn:
            dsn = os.path.expandvars(dsn)  # v.external.out uses $HOME
            # fill in default values
            if sourceType == "dir":
                self.dirWidgets["format"].SetStringSelection(format)
                self.dirWidgets["browse"].SetValue(dsn)
                self.dirWidgets["options"].SetValue(options)
            elif sourceType == "db":
                self.dbWidgets["format"].SetStringSelection(format)
                self.dbWidgets["options"].SetValue(options)
                name = self._getCurrentDbWidgetName()
                if name == "choice":
                    if dsn in self.dbWidgets[name].GetItems():
                        self.dbWidgets[name].SetStringSelection(dsn)
                    if "topology" in data.keys():
                        self.dbWidgets["featType"].SetSelection(1)
                else:
                    self.dbWidgets[name].SetValue(dsn)

    def _layout(self):
        """Layout"""
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.changingSizer = wx.StaticBoxSizer(self.inputBox, wx.VERTICAL)

        # file
        paddingSizer = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.GridBagSizer(vgap=5, hgap=10)
        paddingSizer.Add(
            self.fileWidgets["browse"], flag=wx.BOTTOM | wx.EXPAND, border=35
        )
        sizer.Add(paddingSizer, flag=wx.EXPAND, pos=(0, 0), span=(1, 2))
        sizer.AddGrowableCol(0)
        if self.dest:
            sizer.Add(
                StaticText(parent=self.filePanel, label=_("Creation options:")),
                flag=wx.ALIGN_CENTER_VERTICAL,
                pos=(1, 0),
            )
            sizer.Add(
                self.fileWidgets["options"],
                flag=wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
                pos=(1, 1),
            )

        else:
            self.fileWidgets["options"].Hide()
        self.filePanel.SetSizer(sizer)

        # directory
        sizer = wx.GridBagSizer(vgap=3, hgap=10)
        sizer.Add(
            StaticText(parent=self.dirPanel, label=_("Format:")),
            flag=wx.ALIGN_CENTER_VERTICAL,
            pos=(0, 0),
        )
        sizer.Add(
            self.dirWidgets["format"],
            flag=wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
            pos=(0, 1),
        )
        sizer.Add(
            self.dirWidgets["extensionLabel"], flag=wx.ALIGN_CENTER_VERTICAL, pos=(0, 2)
        )
        sizer.Add(
            self.dirWidgets["extension"], flag=wx.ALIGN_CENTER_VERTICAL, pos=(0, 3)
        )
        sizer.Add(
            self.dirWidgets["browse"],
            flag=wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
            pos=(1, 0),
            span=(1, 4),
        )
        if self.dest:
            sizer.Add(
                StaticText(parent=self.dirPanel, label=_("Creation options:")),
                flag=wx.ALIGN_CENTER_VERTICAL,
                pos=(2, 0),
            )
            sizer.Add(
                self.dirWidgets["options"],
                flag=wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
                pos=(2, 1),
            )
            helpBtn = Button(parent=self.dirPanel, id=wx.ID_HELP)
            helpBtn.Bind(wx.EVT_BUTTON, self.OnHelp)
            sizer.Add(helpBtn, flag=wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, pos=(2, 2))

            self.dirWidgets["extensionLabel"].Hide()
            self.dirWidgets["extension"].Hide()
        else:
            self.dirWidgets["options"].Hide()
        sizer.AddGrowableCol(1)
        self.dirPanel.SetSizer(sizer)

        # database
        sizer = wx.GridBagSizer(vgap=1, hgap=5)
        sizer.Add(
            StaticText(parent=self.dbPanel, label=_("Format:")),
            flag=wx.ALIGN_CENTER_VERTICAL,
            pos=(0, 0),
        )
        sizer.Add(self.dbWidgets["format"], flag=wx.ALIGN_CENTER_VERTICAL, pos=(0, 1))
        sizer.Add(
            self.dbWidgets["textLabel1"], flag=wx.ALIGN_CENTER_VERTICAL, pos=(1, 0)
        )
        sizer.Add(
            self.dbWidgets["text"],
            flag=wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
            pos=(1, 1),
            span=(1, 2),
        )
        sizer.Add(
            self.dbWidgets["browse"],
            flag=wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
            pos=(2, 0),
            span=(1, 3),
        )
        sizer.Add(
            self.dbWidgets["dirbrowse"],
            flag=wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
            pos=(3, 0),
            span=(1, 2),
        )
        sizer.Add(
            self.dbWidgets["textLabel2"], flag=wx.ALIGN_CENTER_VERTICAL, pos=(4, 0)
        )
        sizer.Add(
            self.dbWidgets["choice"],
            flag=wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
            pos=(4, 1),
            span=(1, 2),
        )
        if self.dest:
            sizer.Add(self.dbWidgets["featType"], pos=(0, 2), flag=wx.EXPAND)

            sizer.Add(
                StaticText(parent=self.dbPanel, label=_("Creation options:")),
                flag=wx.ALIGN_CENTER_VERTICAL,
                pos=(5, 0),
            )
            sizer.Add(
                self.dbWidgets["options"],
                flag=wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
                pos=(5, 1),
                span=(1, 2),
            )

            # help button
            helpBtn = Button(parent=self.dbPanel, id=wx.ID_HELP)
            helpBtn.Bind(wx.EVT_BUTTON, self.OnHelp)
            sizer.Add(helpBtn, pos=(5, 3))

        else:
            self.dbWidgets["options"].Hide()

        self.dbPanel.SetSizer(sizer)
        sizer.SetEmptyCellSize((0, 0))
        sizer.AddGrowableCol(1)

        # protocol
        sizer = wx.GridBagSizer(vgap=3, hgap=3)
        sizer.Add(
            StaticText(parent=self.protocolPanel, label=_("Format:")),
            flag=wx.ALIGN_CENTER_VERTICAL,
            pos=(0, 0),
        )
        sizer.Add(
            self.protocolWidgets["format"], flag=wx.ALIGN_CENTER_VERTICAL, pos=(0, 1)
        )
        sizer.Add(
            StaticText(parent=self.protocolPanel, label=_("Protocol:")),
            flag=wx.ALIGN_CENTER_VERTICAL,
            pos=(1, 0),
        )
        sizer.Add(
            self.protocolWidgets["text"],
            flag=wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
            pos=(1, 1),
        )
        if self.dest:
            sizer.Add(
                StaticText(parent=self.protocolPanel, label=_("Creation options:")),
                flag=wx.ALIGN_CENTER_VERTICAL,
                pos=(2, 0),
            )
            sizer.Add(
                self.protocolWidgets["options"],
                flag=wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
                pos=(2, 1),
            )

        else:
            self.protocolWidgets["options"].Hide()
        sizer.AddGrowableCol(1)
        self.protocolPanel.SetSizer(sizer)

        # native
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(
            StaticText(parent=self.nativePanel, label=_("No settings available")),
            flag=wx.ALL | wx.EXPAND,
            border=5,
        )
        self.nativePanel.SetSizer(sizer)

        for panel in (
            self.nativePanel,
            self.filePanel,
            self.dirPanel,
            self.dbPanel,
            self.protocolPanel,
        ):
            self.changingSizer.Add(panel, proportion=1, flag=wx.EXPAND)

        self.mainSizer.Add(
            self.source, proportion=0, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=5
        )
        self.mainSizer.Add(
            self.changingSizer, proportion=1, flag=wx.ALL | wx.EXPAND, border=5
        )
        self.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self)

    def _getExtension(self, name):
        """Get file extension by format name"""
        formatToExt = {}
        formatToExt.update(rasterFormatExtension)
        formatToExt.update(vectorFormatExtension)

        return formatToExt.get(name, "")

    def _getFormatAbbreviation(self, formats, formatName):
        """Get format abbreviation

        :param dict formats: {formatAbbreviation: formatLongName}
        :param str formatName: long format name

        return str: return format abbreviation
        """
        for key, value in formats.items():
            if formatName == value:
                return key

    def SetSourceType(self, sourceType):
        """Set source type (db, file, dir, ...).
        Does not switch radioboxes."""
        self._sourceType = sourceType
        self.changingSizer.Show(self.filePanel, show=(sourceType == "file"))
        self.changingSizer.Show(self.nativePanel, show=(sourceType == "native"))
        self.changingSizer.Show(self.dirPanel, show=(sourceType == "dir"))
        self.changingSizer.Show(self.protocolPanel, show=(sourceType == "pro"))
        self.changingSizer.Show(self.dbPanel, show=(sourceType == "db"))

        self.changingSizer.Layout()

        if sourceType == "db":
            self.dbWidgets["format"].SetItems(list(self.dbFormats.values()))
            if self.dbFormats:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 1cb35c2fc8 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 793ee713c5 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
>>>>>>> a09cd63835 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 565c97946b (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 150ef7b78e (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f5fb4923c (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3229dc2622 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9d1090ec82 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 83a2bf0c85 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 19273bf354 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> deaca750c4 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ea1bcfd13 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d2b40d15ca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 667b6aa79a (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e4f4950cae (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3be45bfb5 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 744c99be79 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 024f004a0e (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 724bccdb58 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e502e3849e (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> e2b92fe11f (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 946be2ff7b (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
>>>>>>> 1eade8c933 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 793ee713c5 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> b8162a916c (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 565c97946b (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> a05b13298f (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 150ef7b78e (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> 6433ad1296 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 6f5fb4923c (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> c4d1702fe7 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4625684fca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 3229dc2622 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> 02f32ae2d4 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 9d1090ec82 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> osgeo-main
                if "PostgreSQL" in self.dbFormats.values():
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
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
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
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
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
                if "PostgreSQL" in self.dbFormats.values():
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4625684fca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
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
>>>>>>> 7eeb1e86e5 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9e134ec08d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> deaca750c4 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 75f1063afc (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b479d694c0 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> d2b40d15ca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> 8b762d062b (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 667b6aa79a (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
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
>>>>>>> b621c8b780 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> e4f4950cae (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
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
>>>>>>> 2942a2fdfb (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> d3be45bfb5 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
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
>>>>>>> 9051310ffd (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 744c99be79 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
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
>>>>>>> 510052984c (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 024f004a0e (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
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
>>>>>>> 095dc4def6 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 724bccdb58 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
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
>>>>>>> 45a066d418 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> e502e3849e (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
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
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fa3a181fb0 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> e2b92fe11f (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
                if "PostgreSQL" in self.dbFormats.values():
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40118f6d63 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> deaca750c4 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
                if "PostgreSQL" in self.dbFormats.values():
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
>>>>>>> 9e134ec08d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> 75f1063afc (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 4ea1bcfd13 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
                if "PostgreSQL" in self.dbFormats.values():
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 05e3f88683 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ea1bcfd13 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                if "PostgreSQL" in self.dbFormats.values():
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
>>>>>>> 1cb35c2fc8 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
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
>>>>>>> 793ee713c5 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> a09cd63835 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b8162a916c (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 565c97946b (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> a05b13298f (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 150ef7b78e (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
                if "PostgreSQL" in self.dbFormats.values():
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4625684fca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 6433ad1296 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 6f5fb4923c (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4625684fca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 3229dc2622 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> 02f32ae2d4 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 9d1090ec82 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
                if "PostgreSQL" in self.dbFormats.values():
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
>>>>>>> 40118f6d63 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> c4d1702fe7 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 83a2bf0c85 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
                if "PostgreSQL" in self.dbFormats.values():
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
>>>>>>> 9e134ec08d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 7eeb1e86e5 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 19273bf354 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> 9e134ec08d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> deaca750c4 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> 75f1063afc (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 4ea1bcfd13 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> b479d694c0 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> d2b40d15ca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> 8b762d062b (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 667b6aa79a (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
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
>>>>>>> b621c8b780 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> e4f4950cae (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
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
>>>>>>> 2942a2fdfb (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> d3be45bfb5 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
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
>>>>>>> 9051310ffd (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 744c99be79 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
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
>>>>>>> 510052984c (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 024f004a0e (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
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
>>>>>>> 095dc4def6 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 724bccdb58 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
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
>>>>>>> 45a066d418 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> e502e3849e (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
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
>>>>>>> osgeo-main
=======
                db_formats = self.dbFormats.values()
                if "PostgreSQL" in db_formats:
=======
                if "PostgreSQL" in self.dbFormats.values():
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
>>>>>>> 05e3f88683 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 946be2ff7b (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 1eade8c933 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fa3a181fb0 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> e2b92fe11f (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
                    self.dbWidgets["format"].SetStringSelection("PostgreSQL")
                elif "PostgreSQL/PostGIS" in db_formats:
                    self.dbWidgets["format"].SetStringSelection("PostgreSQL/PostGIS")
                else:
                    self.dbWidgets["format"].SetSelection(0)
            self.dbWidgets["format"].Enable()

        if sourceType == "db":
            db = self.dbWidgets["format"].GetStringSelection()
            self.SetDatabase(db)

        if not self.dest:
            self.reloadDataRequired.emit(listData=None, data=None)
            self._reloadLayers()

    def OnSettingsChanged(self, data):
        """User changed setting"""
        # data list: [type, dsn, format, options]
        if len(data) == 3:
            data.append("")
        elif len(data) < 3:
            return

        self.source.SetSelection(self.sourceMap[data[0]])
        self.SetSourceType(data[0])
        if data[0] == "file":
            self.fileWidgets["browse"].SetValue(data[1])
            self.fileWidgets["options"].SetValue(data[3])
        elif data[0] == "dir":
            self.dirWidgets["browse"].SetValue(data[1])
            self.dirWidgets["format"].SetStringSelection(data[2])
            self.dirWidgets["options"].SetValue(data[3])
            self.SetExtension(data[2])
        elif data[0] == "pro":
            self.protocolWidgets["text"].SetValue(data[2])
            self.protocolWidgets["options"].SetValue(data[3])
        elif data[0] == "db":
            name = self._getCurrentDbWidgetName()
            if name == "choice":
                if len(data[1].split(":", 1)) > 1:
                    for item in data[1].split(":", 1)[1].split(","):
                        key, value = item.split("=", 1)
                        if key == "dbname":
                            self.dbWidgets[name].SetStringSelection(value)
                            break
                else:
                    self.dbWidgets[name].SetStringSelection(data[1])
            else:
                self.dbWidgets[name].SetValue(data[1])
            self.dbWidgets["options"].SetValue(data[3])

        if not self.dest:
            self.reloadDataRequired.emit(listData=None, data=None)
            self._reloadLayers()

    def AttachSettings(self):
        if self.ogr:
            settingsFile = os.path.join(GetSettingsPath(), "wxOGR")
        else:
            settingsFile = os.path.join(GetSettingsPath(), "wxGDAL")

        self.settsManager = ManageSettingsWidget(parent=self, settingsFile=settingsFile)
        self.settsManager.settingsChanged.connect(self.OnSettingsChanged)
        self.settsManager.settingsSaving.connect(self.OnSettingsSaving)

        # do layout
        self.mainSizer.Insert(0, self.settsManager, flag=wx.ALL | wx.EXPAND, border=5)

    def OnSettingsSaving(self, name):
        """Saving data"""
        if not self.GetDsn():
            GMessage(
                parent=self,
                message=_("No data source defined, settings are not saved."),
            )
            return

        self.settsManager.SetDataToSave(
            (self._sourceType, self.GetDsn(), self.GetFormat(), self.GetOptions())
        )
        self.settsManager.SaveSettings(name)

    def _getExtPatternGlob(self, ext):
        """Get pattern for case-insensitive globing"""
        pattern = "*."
        for c in ext:
            pattern += "[%s%s]" % (c.lower(), c.upper())
        return pattern

    def _getCurrentDbWidgetName(self):
        """Returns active dns database widget name."""
        for widget in ("browse", "dirbrowse", "text", "choice"):
            if self.dbWidgets[widget].IsShown():
                return widget

    def GetDsn(self):
        """Get datasource name"""
        if self._sourceType == "db":
            if self.dbWidgets["format"].GetStringSelection() in {
                "PostgreSQL",
                "PostgreSQL/PostGIS",
                "PostGIS Raster driver",
<<<<<<< HEAD
<<<<<<< HEAD
            }:
=======
            ):
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            }:
>>>>>>> 6bd0f720cb (style(gui): Fixes literal-membership (PLR6201) (#3952))
                ret = RunCommand("db.login", read=True, quiet=True, flags="p")
                message = _(
                    "PostgreSQL/PostGIS login was not set."
                    " Set it via <db.login> module, please."
                )
                if not ret:
                    GError(parent=self, message=message)
                    return

                connection_string = None
                for conn in ret.splitlines():
                    db_login = conn.split("|")
                    if db_login[0] == "pg":
                        user, password, host, port = db_login[2:]
                        connection_string = (
                            f"PG:dbname={self.dbWidgets['choice'].GetStringSelection()}"
                        )
                        if user:
                            connection_string += f" user={user}"
                        if password:
                            connection_string += f" password={password}"
                        if host:
                            connection_string += f" host={host}"
                        if port:
                            connection_string += f" port={port}"
                        return connection_string
                if not connection_string:
                    GError(parent=self, message=message)
                    return
            else:
                name = self._getCurrentDbWidgetName()
                if name == "choice":
                    dsn = self.dbWidgets[name].GetStringSelection()
                else:
                    dsn = self.dbWidgets[name].GetValue()

        else:
            if self._sourceType == "file":
                dsn = self.fileWidgets["browse"].GetValue()
            elif self._sourceType == "dir":
                dsn = self.dirWidgets["browse"].GetValue()
            elif self._sourceType == "pro":
                dsn = self.protocolWidgets["text"].GetValue()
            else:
                dsn = ""
            # check compressed files
            try:
                ext = os.path.splitext(dsn)[1].lower()
            except KeyError:
                ext = None

            if ext == ".zip":
                dsn = "/vsizip/" + dsn
            elif ext == ".gzip":
                dsn = "/vsigzip/" + dsn
            elif ext in {".tar", ".tar.gz", ".tgz"}:
                dsn = "/vsitar/" + dsn

        return dsn

    def SetDatabase(self, db):
        """Update database panel."""
        sizer = self.dbPanel.GetSizer()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        showBrowse = db in {"SQLite", "SQLite / Spatialite", "Rasterlite"}
=======
        showBrowse = db in ("SQLite", "SQLite / Spatialite", "Rasterlite")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        showBrowse = db in ("SQLite", "SQLite / Spatialite", "Rasterlite")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        showBrowse = db in {"SQLite", "SQLite / Spatialite", "Rasterlite"}
>>>>>>> 6bd0f720cb (style(gui): Fixes literal-membership (PLR6201) (#3952))
        showDirbrowse = db in ("FileGDB")
        showChoice = db in {
            "PostgreSQL",
            "PostgreSQL/PostGIS",
            "PostGIS WKT Raster driver",
            "PostGIS Raster driver",
        }
<<<<<<< HEAD
        enableFeatType = (
            self.dest
            and self.ogr
            and db
            in {
                "PostgreSQL",
                "PostgreSQL/PostGIS",
            }
        )
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6bd0f720cb (style(gui): Fixes literal-membership (PLR6201) (#3952))
        enableFeatType = (
            self.dest
            and self.ogr
            and db
            in {
                "PostgreSQL",
                "PostgreSQL/PostGIS",
            }
        )
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        showText = not (showBrowse or showChoice or showDirbrowse)

        sizer.Show(self.dbWidgets["browse"], show=showBrowse)
        sizer.Show(self.dbWidgets["dirbrowse"], show=showDirbrowse)
        sizer.Show(self.dbWidgets["choice"], show=showChoice)
        sizer.Show(self.dbWidgets["textLabel2"], show=showChoice)
        sizer.Show(self.dbWidgets["text"], show=showText)
        sizer.Show(self.dbWidgets["textLabel1"], show=showText)
        self.dbWidgets["featType"].Enable(enableFeatType)
        if showChoice:
            # try to get list of PG databases
            dbNames = RunCommand(
                "db.databases", parent=self, quiet=True, read=True, driver="pg"
            ).splitlines()
            if dbNames is not None:
                self.dbWidgets["choice"].SetItems(sorted(dbNames))
                self.dbWidgets["choice"].SetSelection(0)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            elif gs.find_program(self._psql, "--help"):
                if not self.dbWidgets["choice"].GetItems():
                    p = gs.Popen([self._psql, "-ltA"], stdout=gs.PIPE)
=======
            elif grass.find_program(self._psql, "--help"):
                if not self.dbWidgets["choice"].GetItems():
                    p = grass.Popen([self._psql, "-ltA"], stdout=grass.PIPE)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            elif grass.find_program(self._psql, "--help"):
                if not self.dbWidgets["choice"].GetItems():
                    p = grass.Popen([self._psql, "-ltA"], stdout=grass.PIPE)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            elif gs.find_program(self._psql, "--help"):
                if not self.dbWidgets["choice"].GetItems():
                    p = gs.Popen([self._psql, "-ltA"], stdout=gs.PIPE)
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
                    ret = p.communicate()[0]
                    if ret:
                        dbNames = []
                        for line in ret.splitlines():
                            sline = line.split("|")
                            if len(sline) < 2:
                                continue
                            dbname = sline[0]
                            if dbname:
                                dbNames.append(dbname)
                        self.dbWidgets["choice"].SetItems(db)
                        self.dbWidgets["choice"].SetSelection(0)
            else:
                sizer.Show(self.dbWidgets["text"])
                sizer.Show(self.dbWidgets["choice"], False)

        sizer.Layout()

    def OnUpdate(self, event):
        """Update required - load layers."""
        if not self.dest:
            self._reloadLayers()

        event.Skip()

    def _reloadLayers(self):
        """Reload list of layers"""

        def hasRastSameProjAsLocation(dsn, table=None):
            """Check if raster has same projection as location

            :param str dsn: data source name
            :param str table: PG DB table name, default value is None

            :return str: 1 if raster projection match location
                         projection else 0
            """
            projectionMatch = "0"

            if "PG:" in dsn:
                dsn = dsn.replace("PG:", "")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                p = gs.Popen(
=======
                p = grass.Popen(
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                p = grass.Popen(
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                p = gs.Popen(
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
                    [
                        self._psql,
                        "-t",
                        "-A",
                        dsn,
                        "-c",
                        f"SELECT ST_SRID(rast) AS srid FROM {table} WHERE rid=1;",
                    ],
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    stdout=gs.PIPE,
=======
                    stdout=grass.PIPE,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                    stdout=grass.PIPE,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                    stdout=gs.PIPE,
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
                )
                ret, error = p.communicate()
                if error:
                    GError(
                        parent=self,
                        message=_(
                            "Getting raster <{table}> SRID from PostgreSQL"
                            " DB <{db}>, host <{host}> failed."
<<<<<<< HEAD
<<<<<<< HEAD
                            " {error}."
                        ).format(
                            table=table,
                            db=self._getPDDBConnectionParam(
                                dsn,
                                conn_param="dbname",
                            ),
                            host=self._getPDDBConnectionParam(
                                dsn,
                                conn_param="host",
                            ),
                            error=gs.utils.decode(error),
                        ),
                    )
                if ret:
                    raster_srid = gs.utils.decode(ret).replace(os.linesep, "")
                    location_srid = gs.parse_command("g.proj", flags="g")
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                            " {error}.".format(
                                table=table,
                                db=self._getPDDBConnectionParam(
                                    dsn,
                                    conn_param="dbname",
                                ),
                                host=self._getPDDBConnectionParam(
                                    dsn,
                                    conn_param="host",
                                ),
                                error=gs.utils.decode(error),
                            ),
                        ),
                    )
                if ret:
<<<<<<< HEAD
                    raster_srid = grass.utils.decode(ret).replace(os.linesep, "")
                    location_srid = grass.parse_command("g.proj", flags="g")
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                    raster_srid = gs.utils.decode(ret).replace(os.linesep, "")
                    location_srid = gs.parse_command("g.proj", flags="g")
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
                    if raster_srid == location_srid["srid"].split(":")[-1]:
                        projectionMatch = "1"
            else:
                ret = RunCommand(
                    "r.external", quiet=True, read=True, flags="t", input=dsn
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                # v.external returns info for individual bands, however projection is shared by all bands ->
                # (it is possible to take first line)
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
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
                # v.external returns info for individual bands, however projection is shared by all bands ->
                # (it is possible to take first line)
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
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> osgeo-main
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
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
                # v.external returns info for individual bands, however projection is
                # shared by all bands -> (it is possible to take first line)
=======
                # v.external returns info for individual bands, however projection is shared by all bands ->
                # (it is possible to take first line)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
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
                # v.external returns info for individual bands, however projection is shared by all bands ->
                # (it is possible to take first line)
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
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
                # v.external returns info for individual bands, however projection is shared by all bands ->
                # (it is possible to take first line)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
                # v.external returns info for individual bands, however projection is shared by all bands ->
                # (it is possible to take first line)
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> osgeo-main
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
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))

                lines = ret.splitlines()
                projectionMatch = "0"
                if lines:
<<<<<<< HEAD
<<<<<<< HEAD
                    bandNumber, bandType, projectionMatch = (
                        x.strip() for x in lines[0].split(",")
=======
                    bandNumber, bandType, projectionMatch = map(
                        lambda x: x.strip(), lines[0].split(",")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                    bandNumber, bandType, projectionMatch = map(
                        lambda x: x.strip(), lines[0].split(",")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    )

            return projectionMatch

        def getProjMatchCaption(projectionMatch):
            return _("No") if projectionMatch == "0" else _("Yes")

        dsn = self.GetDsn()
        if not dsn:
            return

        data = []
        listData = []
        layerId = 1

        if self.ogr:
            ret = RunCommand("v.external", quiet=True, read=True, flags="t", input=dsn)
            if not ret:
                self.reloadDataRequired.emit(listData=None, data=None)
                return

            layerId = 1
            for line in ret.splitlines():
                layerName, featureType, projectionMatch, geometryColumn = (
                    x.strip() for x in line.split(",")
                )
                projectionMatchCaption = getProjMatchCaption(projectionMatch)
                grassName = GetValidLayerName(layerName)
                if geometryColumn:
                    featureType = geometryColumn + "/" + featureType
                listData.append(
                    (layerId, layerName, featureType, projectionMatchCaption, grassName)
                )
                data.append(
                    (layerId, layerName, featureType, int(projectionMatch), grassName)
                )
                layerId += 1
        elif self._sourceType == "file":
            baseName = os.path.basename(dsn)
            grassName = GetValidLayerName(baseName.split(".", -1)[0])
            projectionMatch = hasRastSameProjAsLocation(dsn)
            projectionMatchCaption = getProjMatchCaption(projectionMatch)
            listData.append((layerId, baseName, projectionMatchCaption, grassName))
            data.append((layerId, baseName, int(projectionMatch), grassName))
        elif self._sourceType == "dir":
            ext = self.dirWidgets["extension"].GetValue()
            for filename in glob.glob(
                os.path.join(dsn, "%s") % self._getExtPatternGlob(ext)
            ):
                baseName = os.path.basename(filename)
                grassName = GetValidLayerName(baseName.split(".", -1)[0])
                projectionMatch = hasRastSameProjAsLocation(filename)
                projectionMatchCaption = getProjMatchCaption(projectionMatch)
                listData.append((layerId, baseName, projectionMatchCaption, grassName))
                data.append((layerId, baseName, int(projectionMatch), grassName))
<<<<<<< HEAD
                layerId += 1
        elif self.dbWidgets["format"].GetStringSelection() == "PostGIS Raster driver":
            rasters = self._getPGDBRasters(dsn)
            for raster in rasters:
                grassName = GetValidLayerName(raster)
                projectionMatch = hasRastSameProjAsLocation(dsn, table=raster)
                projectionMatchCaption = getProjMatchCaption(projectionMatch)
                listData.append((layerId, raster, projectionMatchCaption, grassName))
                data.append((layerId, raster, int(projectionMatch), grassName))
                layerId += 1
        elif self.dbWidgets["format"].GetStringSelection() == "Rasterlite":
            rasters = self._getRasterliteDBRasters(dsn)
            for raster in rasters:
                grassName = GetValidLayerName(raster)
                projectionMatch = hasRastSameProjAsLocation(dsn)
                projectionMatchCaption = getProjMatchCaption(projectionMatch)
                listData.append((layerId, raster, projectionMatchCaption, grassName))
                data.append((layerId, raster, int(projectionMatch), grassName))
                layerId += 1
=======
            elif self._sourceType == "dir":
                ext = self.dirWidgets["extension"].GetValue()
                for filename in glob.glob(
                    os.path.join(dsn, "%s") % self._getExtPatternGlob(ext)
                ):
                    baseName = os.path.basename(filename)
                    grassName = GetValidLayerName(baseName.split(".", -1)[0])
                    projectionMatch = hasRastSameProjAsLocation(filename)
                    projectionMatchCaption = getProjMatchCaption(projectionMatch)
                    listData.append(
                        (layerId, baseName, projectionMatchCaption, grassName)
                    )
                    data.append((layerId, baseName, int(projectionMatch), grassName))
                    layerId += 1
            elif (
                self.dbWidgets["format"].GetStringSelection() == "PostGIS Raster driver"
            ):
                rasters = self._getPGDBRasters(dsn)
                for raster in rasters:
                    grassName = GetValidLayerName(raster)
                    projectionMatch = hasRastSameProjAsLocation(dsn, table=raster)
                    projectionMatchCaption = getProjMatchCaption(projectionMatch)
                    listData.append(
                        (layerId, raster, projectionMatchCaption, grassName)
                    )
                    data.append((layerId, raster, int(projectionMatch), grassName))
                    layerId += 1
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

        # emit signal
        self.reloadDataRequired.emit(listData=listData, data=data)

    def ExtensionChanged(self, event):
        if not self.dest:
            # reload layers
            self._reloadLayers()

    def SetExtension(self, name):
        """Extension changed"""
        ext = self._getExtension(name)
        self.dirWidgets["extension"].SetValue(ext)

    def GetType(self):
        """Get source type"""
        return self._sourceType

    def GetFormat(self, getFormatAbbreviation=False):
        """Get format as string"""

        def _getFormat(getFormatAbbreviation, format_group):
            """Get format long name or format abbreviation

            :param bool getFormatAbbreviation: get format abbreviation
            :param dict format_group: formats dict {formatAbbreviation: formatLongName}
            for 'file', 'protocol', 'database' group

            return str: long format name or format abbreviation
            """
            format = self.dirWidgets["format"].GetStringSelection()
            if getFormatAbbreviation:
                return self._getFormatAbbreviation(
                    formats=self.fileFormats,
                    formatName=format,
                )
            return format

        if self._sourceType == "dir":
            format = _getFormat(getFormatAbbreviation, format_group=self.fileFormats)
        elif self._sourceType == "pro":
            format = _getFormat(
                getFormatAbbreviation, format_group=self.protocolFormats
            )
        elif self._sourceType == "db":
            format = _getFormat(getFormatAbbreviation, format_group=self.dbFormats)
        else:
            format = ""

        return format.replace(" ", "_")

    def GetFormatExt(self):
        """Get format extension"""
        return self._getExtension(self.GetFormat())

    def GetOptions(self):
        """Get creation options"""
        if self._sourceType == "file":
            options = self.fileWidgets["options"].GetValue()
        elif self._sourceType == "dir":
            options = self.dirWidgets["options"].GetValue()
        elif self._sourceType == "pro":
            options = self.protocolWidgets["options"].GetValue()
        elif self._sourceType == "db":
            if self.dbWidgets["featType"].GetSelection() == 1:
                options = "topology=yes "
            else:
                options = ""
            options += self.dbWidgets["options"].GetValue()

        return options.strip()

    def OnHelp(self, event):
        """Show related manual page"""
        cmd = ""
        if self.dest:
            cmd = "v.external.out" if self.ogr else "r.external.out"
        elif self.link:
            cmd = "v.external" if self.ogr else "r.external"
        elif self.ogr:
            cmd = "v.in.ogr"
        else:
            cmd = "r.in.gdal"

        RunCommand("g.manual", entry=cmd)

    def _getPGDBConnectionParam(self, dsn, conn_param):
        """Get PostgreSQL DB connection parameter value

        :param str dsn: PG DB connection string "dbname=<your_db_name>
                        user=<your_user_name> password=<your_db_password>
                        host=<your_host_name> port=<yor_port_number>"
        :param str connn_param: PG DB connection string
                                connection param name
                                (dbname|user|password|host|port)

        :return str: PG DB connection param value
        """
        Debug.msg(
            3,
            f"GdalSelect._getPGDBConnectionParam(): dsn='{dsn}'"
            f" conn_param='{conn_param}'",
        )
        conn_param_val = [i for i in dsn.split(" ") if conn_param in i]
        if conn_param_val:
            Debug.msg(
                3,
                f"GdalSelect._getPGDBConnectionParam(): return"
                f" {conn_param_val[0].split('=')[-1]}",
            )
            return conn_param_val[0].split("=")[-1]

    def _getPGDBtables(self, dsn):
        """Get PostgreSQL DB list of tables

        :param str dsn: PG DB connection string "dbname=<your_db_name>
                        user=<your_user_name> password=<your_db_password>
                        host=<your_host_name> port=<yor_port_number>"

        :return list tables: list of PG db tables
        """
        Debug.msg(3, f"GdalSelect._getPGDBtables(): dsn='{dsn}'")
        tables = []
        tables_list_sql = """
            SELECT tablename FROM pg_catalog.pg_tables
            WHERE schemaname != 'information_schema'
              AND schemaname != 'pg_catalog';
        """
        # Get tables list
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        p = gs.Popen(
=======
        p = grass.Popen(
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        p = grass.Popen(
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        p = gs.Popen(
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
            [
                self._psql,
                "-t",
                "-A",
                dsn,
                "-c",
                f"{tables_list_sql}",
            ],
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            stdout=gs.PIPE,
=======
            stdout=grass.PIPE,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            stdout=grass.PIPE,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            stdout=gs.PIPE,
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
        )
        ret, error = p.communicate()
        if error:
            GError(
                parent=self,
                message=_(
                    "Getting list of tables from PostgreSQL DB <{db}>,"
<<<<<<< HEAD
<<<<<<< HEAD
                    " host <{host}> failed. {error}."
                ).format(
                    db=self._getPGDBConnectionParam(
                        dsn,
                        conn_param="dbname",
                    ),
                    host=self._getPGDBConnectionParam(
                        dsn,
                        conn_param="host",
                    ),
                    error=gs.utils.decode(error),
                ),
            )
        if ret:
            ret = gs.utils.decode(ret)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    " host <{host}> failed. {error}.".format(
                        db=self._getPGDBConnectionParam(
                            dsn,
                            conn_param="dbname",
                        ),
                        host=self._getPGDBConnectionParam(
                            dsn,
                            conn_param="host",
                        ),
                        error=gs.utils.decode(error),
                    ),
                ),
            )
        if ret:
<<<<<<< HEAD
            ret = grass.utils.decode(ret)
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            ret = gs.utils.decode(ret)
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
            tables = [i.strip() for i in ret.split(os.linesep) if i]
        Debug.msg(3, f"GdalSelect._getPGDBtables(): return {tables}")
        return tables

    def _getPGDBTablesColumnsTypesSql(self, tables):
        """Get PostGIS DB tables columns data type SQL command

        :param list tables: list of PG DB tables with
                            simple quotes ["'table'", ...]
        :return str: SQL string for query all PG DB tables with
                     columns data types
        """
        return f"""
            SELECT
              relname as name,
              a.attname AS column,
              pg_catalog.format_type(a.atttypid, a.atttypmod) AS datatype
            FROM
              pg_catalog.pg_attribute a
              LEFT JOIN (
                SELECT
                  c.oid,
                  relname
                FROM
                  pg_catalog.pg_class c
                  LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
                WHERE
                  pg_catalog.pg_table_is_visible(c.oid)
              ) AS o ON a.attrelid = o.oid
            WHERE
              relname IN ({', '.join(tables)})
              AND NOT a.attisdropped;
        """

    def _getPGDBRasters(self, dsn):
        """Get PostGIS DB rasters

        :param str dsn: PG DB connection string "dbname=<your_db_name>
                        user=<your_user_name> password=<your_db_password>
                        host=<your_host_name> port=<yor_port_number>"

        :return list: list of PostGIS DB rasters
        """
        Debug.msg(3, f"GdalSelect._getPGDBRasters(): dsn='{dsn}'")
        rasters = []
        raster_col_type = "raster"
        field_sep = ","

        dsn = dsn.replace("PG:", "")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if gs.find_program(self._psql, "--help"):
=======
        if grass.find_program(self._psql, "--help"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        if grass.find_program(self._psql, "--help"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        if gs.find_program(self._psql, "--help"):
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
            tables = self._getPGDBtables(dsn)
            # Get tables columns data types list
            if tables:
                tables_with_quotes = [f"'{t}'" for t in tables]
                tables_cols_data_types_sql = self._getPGDBTablesColumnsTypesSql(
                    tables=tables_with_quotes,
                )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                p = gs.Popen(
=======
                p = grass.Popen(
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                p = grass.Popen(
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                p = gs.Popen(
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
                    [
                        self._psql,
                        "-t",
                        "-A",
                        "-F",
                        field_sep,
                        dsn,
                        "-c",
                        f"{tables_cols_data_types_sql}",
                    ],
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    stdout=gs.PIPE,
=======
                    stdout=grass.PIPE,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                    stdout=grass.PIPE,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                    stdout=gs.PIPE,
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
                )
                ret, error = p.communicate()
                if error:
                    GError(
                        parent=self,
                        message=_(
                            "Getting list of tables columns data types"
                            " from PostGIS DB <{db}>, host <{host}> failed."
<<<<<<< HEAD
<<<<<<< HEAD
                            " {error}."
                        ).format(
                            db=self._getPGDBConnectionParam(
                                dsn,
                                conn_param="dbname",
                            ),
                            host=self._getPGDBConnectionParam(
                                dsn,
                                conn_param="host",
                            ),
                            error=gs.utils.decode(error),
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                            " {error}.".format(
                                db=self._getPGDBConnectionParam(
                                    dsn,
                                    conn_param="dbname",
                                ),
                                host=self._getPGDBConnectionParam(
                                    dsn,
                                    conn_param="host",
                                ),
                                error=gs.utils.decode(error),
                            ),
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                        ),
                    )
                if ret:
                    import re

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    tables_cols = gs.utils.decode(ret)
=======
                    tables_cols = grass.utils.decode(ret)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                    tables_cols = grass.utils.decode(ret)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                    tables_cols = gs.utils.decode(ret)
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
                    rasters_cols = re.findall(
                        rf".*.{raster_col_type}",
                        tables_cols,
                    )
                    for col in rasters_cols:
                        table, col_, col_type = col.split(field_sep)
                        if col_type == raster_col_type:
                            rasters.append(table)
        else:
            GError(
                parent=self,
                message=_(
                    "PostgreSQL DB <{psql}> program was not found."
<<<<<<< HEAD
<<<<<<< HEAD
                    " Please, install it."
                ).format(psql=self._psql),
=======
                    " Please, install it.".format(psql=self._psql)
                ),
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                    " Please, install it.".format(psql=self._psql)
                ),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            )
        Debug.msg(3, f"GdalSelect._getPGDBRasters(): return {rasters}")
        return rasters

<<<<<<< HEAD
<<<<<<< HEAD
    def _getRasterliteDBRasters(self, dsn):
        """Get Rasterlite DB rasters

        :param str dsn: Rasterlite DB data source name

        :return list: list of Rasterlite DB rasters
        """
        try:
            from osgeo import gdal
        except ImportError:
            GError(
                parent=self,
                message=_("The Python GDAL package is missing. Please install it."),
            )
            return []
        rasterlite = gdal.Open(dsn)
        rasters = rasterlite.GetSubDatasets()
        if rasters:
            return [r[0].rsplit("table=")[-1] for r in rasters]
        return [os.path.basename(rasterlite.GetFileList()[0]).rsplit(".")[0]]

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

class ProjSelect(wx.ComboBox):
    """Widget for selecting input raster/vector map used by
    r.proj/v.proj modules."""

    def __init__(
        self,
        parent,
        isRaster,
        id=wx.ID_ANY,
        size=globalvar.DIALOG_COMBOBOX_SIZE,
        **kwargs,
    ):
        super().__init__(parent, id, size=size, **kwargs)
        self.SetName("ProjSelect")
        self.isRaster = isRaster

    def UpdateItems(self, dbase, location, mapset):
        """Update list of maps"""
        if not dbase:
            dbase = gs.gisenv()["GISDBASE"]
        if not mapset:
            mapset = gs.gisenv()["MAPSET"]
        if self.isRaster:
            ret = RunCommand(
                "r.proj",
                quiet=True,
                read=True,
                flags="l",
                dbase=dbase,
                project=location,
                mapset=mapset,
            )
        else:
            ret = RunCommand(
                "v.proj",
                quiet=True,
                read=True,
                flags="l",
                dbase=dbase,
                project=location,
                mapset=mapset,
            )
        listMaps = []
        if ret:
            for line in ret.splitlines():
                listMaps.append(line.strip())
        ListSortLower(listMaps)

        self.SetItems(listMaps)
        self.SetValue("")


class ElementSelect(wx.Choice):
    def __init__(
        self,
        parent,
        id=wx.ID_ANY,
        elements=None,
        size=globalvar.DIALOG_COMBOBOX_SIZE,
        **kwargs,
    ):
        """Widget for selecting GIS element

        :param parent: parent window
        :param elements: filter elements
        """
        super().__init__(parent, id, size=size, **kwargs)
        self.SetName("ElementSelect")

        task = gtask.parse_interface("g.list")
        p = task.get_param(value="type")
        self.values = p.get("values", [])
        self.valuesDesc = p.get("values_desc", [])

        if elements:
            values = []
            valuesDesc = []
            for idx in range(len(self.values)):
                value = self.values[idx]
                if value in elements:
                    values.append(value)
                    valuesDesc.append(self.valuesDesc[idx])
            self.values = values
            self.valuesDesc = valuesDesc

        self.SetItems(self.valuesDesc)

    def GetValue(self, name):
        """Translate value

        :param name: element name
        """
        idx = self.valuesDesc.index(name)
        if idx > -1:
            return self.values[idx]
        return ""


class OgrTypeSelect(wx.Panel):
    def __init__(self, parent, panel, **kwargs):
        """Widget to choose OGR feature type

        :param parent: parent window
        :param panel: wx.Panel instance used as parent window
        """
        wx.Panel.__init__(self, parent=panel, id=wx.ID_ANY)

        self.ftype = wx.Choice(
            parent=self,
            id=wx.ID_ANY,
            size=(200, -1),
            choices=(_("Point"), _("LineString"), _("Polygon")),
        )
        self._layout()

    def _layout(self):
        """Do layout"""
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(
            StaticText(parent=self, id=wx.ID_ANY, label=_("Feature type:")),
            proportion=1,
            flag=wx.ALIGN_CENTER_VERTICAL,
            border=5,
        )
        sizer.Add(self.ftype, proportion=0, flag=wx.EXPAND | wx.ALIGN_RIGHT)

        self.SetSizer(sizer)
        sizer.Fit(self)

    def GetType(self):
        """Get selected type as string

        :return: feature type as string
        """
        sel = self.ftype.GetSelection()
        if sel == 0:
            return "point"
        if sel == 1:
            return "line"
        if sel == 2:
            return "boundary"


class CoordinatesSelect(Panel):
    def __init__(self, parent, giface, multiple=False, **kwargs):
        """Widget to get coordinates from map window  by mouse click

        :param parent: parent window
        :param giface: GRASS interface
        :param multiple: - True if it is possible to insert more coordinates
        """
        self._giface = giface
        self.multiple = multiple
        self.mapWin = None
        self.drawMapWin = None

        super().__init__(parent=parent, id=wx.ID_ANY)

        self.coordsField = TextCtrl(
            parent=self,
            id=wx.ID_ANY,
            size=globalvar.DIALOG_TEXTCTRL_SIZE,
            validator=CoordinatesValidator(),
        )

        icon = wx.Bitmap(os.path.join(globalvar.ICONDIR, "grass", "pointer.png"))
        self.buttonInsCoords = buttons.ThemedGenBitmapToggleButton(
            parent=self, id=wx.ID_ANY, bitmap=icon, size=globalvar.DIALOG_COLOR_SIZE
        )
        self.registered = False
        self.buttonInsCoords.Bind(wx.EVT_BUTTON, self._onClick)

        mapdisp = self._giface.GetMapDisplay()
        if mapdisp:
            switcher = mapdisp.GetToolSwitcher()
            switcher.AddCustomToolToGroup(
                group="mouseUse",
                btnId=self.buttonInsCoords.GetId(),
                toggleHandler=self.buttonInsCoords.SetValue,
            )
        self._doLayout()
        self.coordsField.Bind(wx.EVT_TEXT, lambda event: self._draw(delay=1))

    def _doLayout(self):
        self.dialogSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.dialogSizer.Add(self.coordsField, proportion=1, flag=wx.EXPAND)
        self.dialogSizer.Add(self.buttonInsCoords)
        self.SetSizer(self.dialogSizer)

    def _onClick(self, event):
        """Button for interacitve inserting of coordinates clicked"""

        self.mapWin = self._giface.GetMapWindow()
        if self.buttonInsCoords.GetToggle() and self.mapWin:
            switcher = self._giface.GetMapDisplay().GetToolSwitcher()
            switcher.ToolChanged(self.buttonInsCoords.GetId())
            if not self.mapWin.RegisterMouseEventHandler(
                wx.EVT_LEFT_DOWN, self._onMapClickHandler, "cross"
            ):
                return

            self.registered = True
            self._giface.GetMapDisplay().Raise()
        elif self.mapWin and self.mapWin.UnregisterMouseEventHandler(
            wx.EVT_LEFT_DOWN, self._onMapClickHandler
        ):
            self.registered = False
            return

    def drawCleanUp(self):
        if self.drawMapWin:
            self.drawMapWin.UnregisterGraphicsToDraw(self.pointsToDraw)

    def _draw(self, delay):
        """Draws points representing inserted coordinates in mapwindow."""
        if self.drawMapWin != self.mapWin:
            self.drawCleanUp()
            if self.mapWin:
                self.drawMapWin = self.mapWin
                self.pointsToDraw = self.drawMapWin.RegisterGraphicsToDraw(
                    graphicsType="point"
                )

        if self.drawMapWin:
            items = self.pointsToDraw.GetAllItems()
            for i in items:
                self.pointsToDraw.DeleteItem(i)

            coords = self._getCoords()
            if coords is not None:
                for i in range(len(coords) // 2):
                    i *= 2
                    self.pointsToDraw.AddItem(coords=(coords[i], coords[i + 1]))

            self._giface.updateMap.emit(render=False, renderVector=False, delay=delay)

    def _getCoords(self):
        """Get list of coordinates.

        :return: None if values are not valid
        """
        if self.coordsField.GetValidator().Validate(self):
            return self.coordsField.GetValue().split(",")

        return None

    def _onMapClickHandler(self, event):
        """Gets coordinates from mapwindow"""
        if event == "unregistered":
            return

        e, n = self.mapWin.GetLastEN()
        prevCoords = ""

        if self.multiple:
            prevCoords = self.coordsField.GetValue().strip()
            if prevCoords != "":
                prevCoords += ","

        value = prevCoords + str(e) + "," + str(n)
        self.coordsField.SetValue(value)

        self._draw(delay=0)

    def OnClose(self):
        """Unregistrates _onMapClickHandler from mapWin"""
        self.drawCleanUp()
        self._giface.updateMap.emit(render=False, renderVector=False)

        mapdisp = self._giface.GetMapDisplay()
        if mapdisp:
            switcher = mapdisp.GetToolSwitcher()
            switcher.RemoveCustomToolFromGroup(self.buttonInsCoords.GetId())

        if self.mapWin and self.registered:
            self.mapWin.UnregisterMouseEventHandler(
                wx.EVT_LEFT_DOWN, self._onMapClickHandler
            )

    def GetTextWin(self):
        """Get TextCtrl widget"""
        return self.coordsField


class VectorCategorySelect(wx.Panel):
    """Widget that allows interactive selection of vector features"""

    def __init__(self, parent, giface, task=None):
        super().__init__(parent=parent, id=wx.ID_ANY)
        self.task = task
        self.parent = parent
        self.giface = giface

        self.selectedFeatures = None
        self.registered = False
        self._vectorSelect = None

        self.mapdisp = self.giface.GetMapDisplay()

        self.catsField = TextCtrl(
            parent=self, id=wx.ID_ANY, size=globalvar.DIALOG_TEXTCTRL_SIZE
        )

        icon = wx.Bitmap(os.path.join(globalvar.ICONDIR, "grass", "select.png"))
        self.buttonVecSelect = buttons.ThemedGenBitmapToggleButton(
            parent=self, id=wx.ID_ANY, bitmap=icon, size=globalvar.DIALOG_COLOR_SIZE
        )
        self.buttonVecSelect.Bind(wx.EVT_BUTTON, self._onClick)

        if self.mapdisp:
            switcher = self.mapdisp.GetToolSwitcher()
            switcher.AddCustomToolToGroup(
                group="mouseUse",
                btnId=self.buttonVecSelect.GetId(),
                toggleHandler=self.buttonVecSelect.SetValue,
            )

        self._layout()

    def _isMapSelected(self):
        """Check if layer list contains at least one selected map"""
        layerList = self.giface.GetLayerList()
        layerSelected = layerList.GetSelectedLayer()
        if layerSelected is None:
            GWarning(_("No vector map selected in layer manager. Operation canceled."))
            return False

        return True

    def _chckMap(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
        """Check if selected map in 'input' widget is the same as selected map in
        lmgr"""
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Check if selected map in 'input' widget is the same as selected map in lmgr"""
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
        if self._isMapSelected():
            layerList = self.giface.GetLayerList()
            layerSelected = layerList.GetSelectedLayer()
            # d.vect module
            inputName = self.task.get_param(value="map", raiseError=False)
            if not inputName:
                inputName = self.task.get_param("input")
            if inputName["value"] != str(layerSelected):
                if inputName["value"] == "" or inputName["value"] is None:
                    GWarning(_("Input vector map is not selected"))
                    return False
                GWarning(
                    _(
                        "Input vector map <%s> and selected map <%s> in layer manager "
                        "are different. Operation canceled."
                    )
                    % (inputName["value"], str(layerSelected))
                )
                return False
            return True
        return False

    def _onClick(self, evt=None):
        if (self.task is not None and not self._chckMap()) or not self._isMapSelected():
            self.buttonVecSelect.SetValue(False)
            return

        if self._vectorSelect is None and self.mapdisp:
            if self.buttonVecSelect.IsEnabled():
                switcher = self.mapdisp.GetToolSwitcher()
                switcher.ToolChanged(self.buttonVecSelect.GetId())

            self._vectorSelect = VectorSelectBase(self.mapdisp, self.giface)
            if not self.mapdisp.GetWindow().RegisterMouseEventHandler(
                wx.EVT_LEFT_DOWN, self._onMapClickHandler, "cross"
            ):
                return
            self.registered = True
            self.mapdisp.Raise()
        else:
            self.OnClose()

    def OnClose(self, event=None):
        if not self.mapdisp:
            return

        switcher = self.mapdisp.GetToolSwitcher()
        switcher.RemoveCustomToolFromGroup(self.buttonVecSelect.GetId())
        if self._vectorSelect is not None:
            tmp = self._vectorSelect.GetLineStringSelectedCats()
            self._vectorSelect.OnClose()
            self.catsField.SetValue(tmp)
        self._vectorSelect = None

    def _onMapClickHandler(self, event):
        """Update category text input widget"""
        if event == "unregistered":
            return

        if (self.task is None and not self._isMapSelected()) or not self._chckMap():
            self.OnClose()
        else:
            self.catsField.SetValue(self._vectorSelect.GetLineStringSelectedCats())

    def GetTextWin(self):
        return self.catsField

    def GetValue(self):
        return self.catsField.GetValue()

    def SetValue(self, value):
        self.catsField.SetValue(value)

    def _layout(self):
        self.dialogSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.dialogSizer.Add(self.catsField, proportion=1, flag=wx.EXPAND)

        self.dialogSizer.Add(self.buttonVecSelect)
        self.SetSizer(self.dialogSizer)


class SignatureSelect(wx.ComboBox):
    """Widget for selecting signatures"""

    def __init__(
        self,
        parent,
        element,
        mapsets,
        id=wx.ID_ANY,
        size=globalvar.DIALOG_GSELECT_SIZE,
        **kwargs,
    ):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        super(SignatureSelect, self).__init__(parent, id, size=size, **kwargs)

        items = []
        if mapsets:
            for mapset in mapsets:
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d1e0f3a451 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1b62444dcb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5b7ab488c3 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 101a8cef7f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c621983a87 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67d74ea5b0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0ba4fb709f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f440f5d30 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c940746c7a (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> db3baef4a0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 273146cb7f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 42e8aaeeb9 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 998dac8c79 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
        super(SignatureSelect, self).__init__(parent, id, size=size, **kwargs)

        items = []
        if mapsets:
            for mapset in mapsets:
=======
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> d1e0f3a451 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 228be75788 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1b62444dcb (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 94afdfdae9 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 5b7ab488c3 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e435dd0d3f (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 101a8cef7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0873fb5a66 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c621983a87 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> af0cda6849 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 67d74ea5b0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cd2a15c8d0 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 0ba4fb709f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12e7124573 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 7f440f5d30 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a74c224a9d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c940746c7a (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 210c8f3c49 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> db3baef4a0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 998dac8c79 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 273146cb7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 72d2bd2407 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 42e8aaeeb9 (ci: Ignore paths in CodeQL (#1778))
        super().__init__(parent, id, size=size, **kwargs)
        self.SetName("SignatureSelect")
        self.mapsets = mapsets
        self.UpdateItems(element)

    def UpdateItems(self, element):
        """Update list of signature files for given element

        :param str element: signatures/sig, signatures/sigset or signatures/libsvm
        """
        items = []
        if self.mapsets:
            for mapset in self.mapsets:
=======
        super(SignatureSelect, self).__init__(parent, id, size=size, **kwargs)

        items = []
        if mapsets:
            for mapset in mapsets:
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
        super(SignatureSelect, self).__init__(parent, id, size=size, **kwargs)

        items = []
        if mapsets:
            for mapset in mapsets:
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
        # A workaround to list signature files before a separate
        # signature management module is developed
        try:
            from grass.lib.gis import G_gisinit
=======
        super(SignatureSelect, self).__init__(parent, id, size=size, **kwargs)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 998dac8c79 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
        sig_type = None
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======

>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======

<<<<<<< HEAD
        sig_type = None
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======

<<<<<<< HEAD
        sig_type = None
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD

<<<<<<< HEAD
        sig_type = None
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
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

<<<<<<< HEAD
        sig_type = None
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======

<<<<<<< HEAD
        sig_type = None
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======

<<<<<<< HEAD
        sig_type = None
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

<<<<<<< HEAD
        sig_type = None
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

<<<<<<< HEAD
        sig_type = None
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======

<<<<<<< HEAD
        sig_type = None
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
=======
<<<<<<< HEAD
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
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

<<<<<<< HEAD
        sig_type = None
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======

<<<<<<< HEAD
        sig_type = None
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> d1e0f3a451 (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======

<<<<<<< HEAD
        sig_type = None
>>>>>>> 228be75788 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1b62444dcb (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
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

<<<<<<< HEAD
        sig_type = None
>>>>>>> 94afdfdae9 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 5b7ab488c3 (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
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

<<<<<<< HEAD
        sig_type = None
>>>>>>> e435dd0d3f (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 101a8cef7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
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

<<<<<<< HEAD
        sig_type = None
>>>>>>> 0873fb5a66 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c621983a87 (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
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

<<<<<<< HEAD
        sig_type = None
>>>>>>> af0cda6849 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 67d74ea5b0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
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

<<<<<<< HEAD
        sig_type = None
>>>>>>> cd2a15c8d0 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 0ba4fb709f (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
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

<<<<<<< HEAD
        sig_type = None
>>>>>>> 12e7124573 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 7f440f5d30 (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
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

<<<<<<< HEAD
        sig_type = None
>>>>>>> a74c224a9d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c940746c7a (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
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

<<<<<<< HEAD
        sig_type = None
>>>>>>> 210c8f3c49 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> db3baef4a0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
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
>>>>>>> osgeo-main
=======

<<<<<<< HEAD
        sig_type = None
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 998dac8c79 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 273146cb7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
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

<<<<<<< HEAD
        sig_type = None
>>>>>>> 72d2bd2407 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 42e8aaeeb9 (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
        # Extend here if a new signature type is introduced
        if element == "signatures/sig":
            sig_type = I_SIGFILE_TYPE_SIG
        elif element == "signatures/sigset":
            sig_type = I_SIGFILE_TYPE_SIGSET
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> 42e8aaeeb9 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 998dac8c79 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 273146cb7f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> db3baef4a0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c940746c7a (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f440f5d30 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0ba4fb709f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67d74ea5b0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c621983a87 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 101a8cef7f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5b7ab488c3 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1b62444dcb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d1e0f3a451 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
=======
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
=======
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
        else:
            return
<<<<<<< HEAD
=======
        super(SignatureSelect, self).__init__(parent, id, size=size, **kwargs)
=======
=======
        else:
            return
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
        else:
            return
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
        else:
            return
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
        else:
            return
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
        else:
            return
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
        else:
            return
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
        else:
            return
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
        else:
            return
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
        else:
            return
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
        else:
            return
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
        else:
            return
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
        else:
            return
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
        list_ptr = ctypes.POINTER(ctypes.c_char_p)
        sig_list = list_ptr()
        count = I_signatures_list_by_type(sig_type, mapset, ctypes.byref(sig_list))
        for n in range(count):
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
<<<<<<< HEAD
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))

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

        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======

<<<<<<< HEAD
        sig_type = None
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======

<<<<<<< HEAD
        sig_type = None
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
=======
=======
        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
        # Extend here if a new signature type is introduced
        if element == "signatures/sig":
            sig_type = I_SIGFILE_TYPE_SIG
        elif element == "signatures/sigset":
            sig_type = I_SIGFILE_TYPE_SIGSET
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 228be75788 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 94afdfdae9 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> e435dd0d3f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 0873fb5a66 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> af0cda6849 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> cd2a15c8d0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 12e7124573 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a74c224a9d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 210c8f3c49 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 72d2bd2407 (ci: Ignore paths in CodeQL (#1778))
        items = []
        if sig_type is not None:
            if mapsets:
                for mapset in mapsets:
                    self._append_mapset_signatures(mapset, sig_type, items)
            else:
                self._append_mapset_signatures(None, sig_type, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, sig_type, items):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
        else:
            return
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
        else:
            return
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
        else:
            return
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
        else:
            return
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 228be75788 (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 94afdfdae9 (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e435dd0d3f (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0873fb5a66 (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af0cda6849 (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd2a15c8d0 (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12e7124573 (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a74c224a9d (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 210c8f3c49 (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 72d2bd2407 (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
        list_ptr = ctypes.POINTER(ctypes.c_char_p)
        sig_list = list_ptr()
        count = I_signatures_list_by_type(sig_type, mapset, ctypes.byref(sig_list))
        for n in range(count):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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

=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))

>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> osgeo-main
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
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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

        items = []
        if mapsets:
            for mapset in mapsets:
                self._append_mapset_signatures(mapset, element, items)
        else:
            self._append_mapset_signatures(None, element, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, element, items):
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
        # Extend here if a new signature type is introduced
        if element == "signatures/sig":
            sig_type = I_SIGFILE_TYPE_SIG
        elif element == "signatures/sigset":
            sig_type = I_SIGFILE_TYPE_SIGSET
        else:
            return
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
=======
=======
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 273146cb7f (ci: Ignore paths in CodeQL (#1778))
        items = []
        if sig_type is not None:
            if mapsets:
                for mapset in mapsets:
                    self._append_mapset_signatures(mapset, sig_type, items)
            else:
                self._append_mapset_signatures(None, sig_type, items)
        self.SetItems(items)
        self.SetValue("")

    def _append_mapset_signatures(self, mapset, sig_type, items):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 273146cb7f (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
=======
        else:
            return
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
        else:
            return
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
=======
=======
        else:
            return
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
        else:
            return
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 998dac8c79 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 273146cb7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
        else:
            return
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
        list_ptr = ctypes.POINTER(ctypes.c_char_p)
        sig_list = list_ptr()
        count = I_signatures_list_by_type(sig_type, mapset, ctypes.byref(sig_list))
        for n in range(count):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 998dac8c79 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 273146cb7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> osgeo-main
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> osgeo-main
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> osgeo-main
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> osgeo-main
>>>>>>> main
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> osgeo-main
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> osgeo-main
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> osgeo-main
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> osgeo-main
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> osgeo-main
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> osgeo-main
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> osgeo-main
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> osgeo-main
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> osgeo-main
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> osgeo-main
=======
=======
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> d1e0f3a451 (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 228be75788 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1b62444dcb (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 94afdfdae9 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 5b7ab488c3 (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> e435dd0d3f (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 101a8cef7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 0873fb5a66 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c621983a87 (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> af0cda6849 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 67d74ea5b0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> cd2a15c8d0 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 0ba4fb709f (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 12e7124573 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 7f440f5d30 (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> a74c224a9d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c940746c7a (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 210c8f3c49 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> db3baef4a0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 998dac8c79 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 273146cb7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            items.append(decode(sig_list[n]))
        I_free_signatures_list(count, sig_list)
>>>>>>> 72d2bd2407 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 42e8aaeeb9 (ci: Ignore paths in CodeQL (#1778))
=======
=======
            items.append(grass.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))

>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))

            G_gisinit("")
        except Exception:
            return
        try:
            from grass.lib.imagery import (
                I_SIGFILE_TYPE_SIG,
                I_SIGFILE_TYPE_SIGSET,
                I_SIGFILE_TYPE_LIBSVM,
                I_signatures_list_by_type,
                I_free_signatures_list,
            )
        except ImportError as e:
            sys.stderr.write(
                _("Unable to import C imagery library functions: %s\n") % e
            )
            return
        # Extend here if a new signature type is introduced
        if element == "signatures/sig":
            sig_type = I_SIGFILE_TYPE_SIG
        elif element == "signatures/sigset":
            sig_type = I_SIGFILE_TYPE_SIGSET
        elif element == "signatures/libsvm":
            sig_type = I_SIGFILE_TYPE_LIBSVM
        else:
            return
        list_ptr = ctypes.POINTER(ctypes.c_char_p)
        sig_list = list_ptr()
        count = I_signatures_list_by_type(sig_type, mapset, ctypes.byref(sig_list))
        for n in range(count):
            items.append(gs.decode(sig_list[n]))
        I_free_signatures_list(count, ctypes.byref(sig_list))


class SignatureTypeSelect(wx.ComboBox):
    """Widget for selecting signature type"""

    def __init__(
        self, parent, id=wx.ID_ANY, size=globalvar.DIALOG_GSELECT_SIZE, **kwargs
    ):
        super().__init__(parent, id, size=size, **kwargs)
        self.SetName("SignatureTypeSelect")
        self.SetItems(["sig", "sigset", "libsvm"])


class SeparatorSelect(wx.ComboBox):
    """Widget for selecting separator"""

    def __init__(
        self, parent, id=wx.ID_ANY, size=globalvar.DIALOG_GSELECT_SIZE, **kwargs
    ):
        super().__init__(parent, id, size=size, **kwargs)
        self.SetName("SeparatorSelect")
        self.SetItems(["pipe", "comma", "space", "tab", "newline"])


class SqlWhereSelect(wx.Panel):
    def __init__(self, parent, **kwargs):
        """Widget to define SQL WHERE condition.

        :param parent: parent window
        """
        super().__init__(parent=parent, id=wx.ID_ANY)
        self.parent = parent
        self.vector_map = None

        self.sqlField = TextCtrl(
            parent=self, id=wx.ID_ANY, size=globalvar.DIALOG_TEXTCTRL_SIZE
        )
        self.GetChildren()[0].SetName("SqlWhereSelect")
        icon = wx.Bitmap(os.path.join(globalvar.ICONDIR, "grass", "table.png"))
        self.buttonInsSql = buttons.ThemedGenBitmapButton(
            parent=self, id=wx.ID_ANY, bitmap=icon, size=globalvar.DIALOG_COLOR_SIZE
        )
        self.buttonInsSql.Bind(wx.EVT_BUTTON, self._onClick)

        self._doLayout()

    def _doLayout(self):
        self.dialogSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.dialogSizer.Add(self.sqlField, proportion=1, flag=wx.EXPAND)
        self.dialogSizer.Add(self.buttonInsSql)
        self.SetSizer(self.dialogSizer)

    def GetTextWin(self):
        return self.sqlField

    def _onClick(self, event):
        from dbmgr.sqlbuilder import SQLBuilderWhere

        try:
            if not self.vector_map:
                raise GException(_("No vector map selected"))
            win = SQLBuilderWhere(
                parent=self, vectmap=self.vector_map, layer=self.vector_layer
            )
            win.Show()
        except GException as e:
            GMessage(parent=self.parent, message="{}".format(e))

    def SetData(self, vector, layer):
        self.vector_map = vector
        self.vector_layer = int(layer)  # TODO: support layer names

    def SetValue(self, value):
        self.sqlField.SetValue(value)
