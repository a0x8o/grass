"""
@package web_services.dialogs

@brief Dialogs for web services.

List of classes:
 - dialogs::WSDialogBase
 - dialogs::AddWSDialog
 - dialogs::WSPropertiesDialog
 - dialogs::SaveWMSLayerDialog

(C) 2009-2021 by the GRASS Development Team

This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.

@author Martin Landa <landa.martin gmail.com>
@author Stepan Turek <stepan.turek seznam.cz>
"""

import wx

import os
import shutil

from copy import deepcopy

import grass.script as gs
from grass.script.task import cmdlist_to_tuple, cmdtuple_to_list

from core import globalvar
from core.debug import Debug
from core.gcmd import GMessage, GWarning, GError
from core.utils import GetSettingsPath
from core.gconsole import CmdThread, GStderr, EVT_CMD_DONE, EVT_CMD_OUTPUT

from gui_core.gselect import Select
from gui_core.wrap import Button, StaticText, StaticBox, TextCtrl, RadioButton

from web_services.widgets import WSPanel, WSManageSettingsWidget


class WSDialogBase(wx.Dialog):
    """Base class for web service dialogs."""

    def __init__(
        self,
        parent,
        id=wx.ID_ANY,
        style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
        **kwargs,
    ):
        wx.Dialog.__init__(self, parent, id, style=style, **kwargs)

        self.parent = parent

        # contains panel for every web service on server
        self.ws_panels = {
            "WMS_1.1.1": {"panel": None, "label": "WMS 1.1.1"},
            "WMS_1.3.0": {"panel": None, "label": "WMS 1.3.0"},
            "WMTS": {"panel": None, "label": "WMTS"},
            "OnEarth": {"panel": None, "label": "OnEarth"},
        }

        # TODO: should be in file
        self.default_servers = {
            "OSM-WMS": [
                "https://ows.terrestris.de/osm/service?",
                "",
                "",
            ],
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8d63674c88 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a1f29aef40 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8cdf2763b4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8b5db77cc8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 897ec22b89 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 84365c60c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7a02ec5519 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 179aa8f0a6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bd05168e52 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 515877a709 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aac8b57eb9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 721df60534 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 61c229caa3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 516c6402fb (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4972a560dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
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
<<<<<<< HEAD
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d63674c88 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a1f29aef40 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 8cdf2763b4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8b5db77cc8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 897ec22b89 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84365c60c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7a02ec5519 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 179aa8f0a6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd05168e52 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 515877a709 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aac8b57eb9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 721df60534 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 61c229caa3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 516c6402fb (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4972a560dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
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
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
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
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
                "",
                "",
            ],
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8d63674c88 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a1f29aef40 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 61c229caa3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
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
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8d63674c88 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a1f29aef40 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8cdf2763b4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8b5db77cc8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 897ec22b89 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 84365c60c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7a02ec5519 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 179aa8f0a6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bd05168e52 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 515877a709 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aac8b57eb9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 721df60534 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 61c229caa3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 516c6402fb (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
=======
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4972a560dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            "NASA GIBS WMTS": [
                "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi",
                "",
                "",
            ],
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
            "tiles.maps.eox.at (Sentinel-2)": [
                "https://tiles.maps.eox.at/wms",
                "",
                "",
            ],
        }

        # holds reference to web service panel which is showed
        self.active_ws_panel = None

        # buttons which are disabled when the dialog is not connected
        self.run_btns = []

        # stores error messages for GError dialog showed when all web service
        # connections were unsuccessful
        self.error_msgs = ""

        self._createWidgets()
        self._doLayout()

    def _createWidgets(self):
        settingsFile = os.path.join(GetSettingsPath(), "wxWS")

        self.settsManager = WSManageSettingsWidget(
            parent=self, settingsFile=settingsFile, default_servers=self.default_servers
        )

        self.settingsBox = StaticBox(
            parent=self, id=wx.ID_ANY, label=_(" Server settings ")
        )

        self.serverText = StaticText(parent=self, id=wx.ID_ANY, label=_("Server:"))
        self.server = TextCtrl(parent=self, id=wx.ID_ANY)

        self.btn_connect = Button(parent=self, id=wx.ID_ANY, label=_("&Connect"))
        self.btn_connect.SetToolTip(_("Connect to the server"))
        if not self.server.GetValue():
            self.btn_connect.Enable(False)

        self.infoCollapseLabelExp = _("Show advanced connection settings")
        self.infoCollapseLabelCol = _("Hide advanced connection settings")

        self.adv_conn = wx.CollapsiblePane(
            parent=self,
            label=self.infoCollapseLabelExp,
            style=wx.CP_DEFAULT_STYLE | wx.CP_NO_TLW_RESIZE | wx.EXPAND,
        )

        self.MakeAdvConnPane(pane=self.adv_conn.GetPane())
        self.adv_conn.Collapse(True)
        self.Bind(
            wx.EVT_COLLAPSIBLEPANE_CHANGED, self.OnAdvConnPaneChanged, self.adv_conn
        )

        self.reqDataPanel = wx.Panel(parent=self, id=wx.ID_ANY)

        self.layerNameBox = StaticBox(
            parent=self.reqDataPanel, id=wx.ID_ANY, label=_(" Layer Manager Settings ")
        )

        self.layerNameText = StaticText(
            parent=self.reqDataPanel, id=wx.ID_ANY, label=_("Output layer name:")
        )
        self.layerName = TextCtrl(parent=self.reqDataPanel, id=wx.ID_ANY)

        for ws in self.ws_panels.keys():
            # set class WSPanel argument layerNameTxtCtrl
            self.ws_panels[ws]["panel"] = WSPanel(
                parent=self.reqDataPanel, web_service=ws
            )
            self.ws_panels[ws]["panel"].capParsed.connect(self.OnPanelCapParsed)
            self.ws_panels[ws]["panel"].layerSelected.connect(self.OnLayerSelected)

        # buttons
        self.btn_close = Button(parent=self, id=wx.ID_CLOSE)
        self.btn_close.SetToolTip(_("Close dialog"))

        # statusbar
        self.statusbar = wx.StatusBar(parent=self, id=wx.ID_ANY)

        # bindings
        self.btn_close.Bind(wx.EVT_BUTTON, self.OnClose)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.btn_connect.Bind(wx.EVT_BUTTON, self.OnConnect)

        self.server.Bind(wx.EVT_TEXT, self.OnServer)
        self.layerName.Bind(wx.EVT_TEXT, self.OnOutputLayerName)

        self.settsManager.settingsChanged.connect(self.OnSettingsChanged)
        self.settsManager.settingsSaving.connect(self.OnSettingsSaving)

    def OnLayerSelected(self, title):
        self.layerName.SetValue(title)

    def _doLayout(self):
        dialogSizer = wx.BoxSizer(wx.VERTICAL)

        dialogSizer.Add(
            self.settsManager,
            proportion=0,
            flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT,
            border=5,
        )

        # connection settings
        settingsSizer = wx.StaticBoxSizer(self.settingsBox, wx.VERTICAL)

        serverSizer = wx.FlexGridSizer(cols=3, vgap=5, hgap=5)

        serverSizer.Add(self.serverText, flag=wx.ALIGN_CENTER_VERTICAL)
        serverSizer.AddGrowableCol(1)
        serverSizer.Add(self.server, flag=wx.EXPAND | wx.ALL)

        serverSizer.Add(self.btn_connect)

        settingsSizer.Add(
            serverSizer, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5
        )

        settingsSizer.Add(self.adv_conn, flag=wx.ALL | wx.EXPAND, border=5)

        dialogSizer.Add(
            settingsSizer,
            proportion=0,
            flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT,
            border=5,
        )

        # layer name, parsed capabilities

        reqDataSizer = wx.BoxSizer(wx.VERTICAL)

        layerNameSizer = wx.StaticBoxSizer(self.layerNameBox, wx.HORIZONTAL)

        layerNameSizer.Add(
            self.layerNameText, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL, border=5
        )

        layerNameSizer.Add(self.layerName, flag=wx.EXPAND, proportion=1)

        reqDataSizer.Add(
            layerNameSizer, flag=wx.TOP | wx.LEFT | wx.RIGHT | wx.EXPAND, border=5
        )

        self.ch_ws_sizer = wx.BoxSizer(wx.VERTICAL)

        reqDataSizer.Add(
            self.ch_ws_sizer, proportion=0, flag=wx.TOP | wx.EXPAND, border=5
        )

        for ws in self.ws_panels.keys():
            reqDataSizer.Add(
                self.ws_panels[ws]["panel"],
                proportion=1,
                flag=wx.TOP | wx.LEFT | wx.RIGHT | wx.EXPAND,
                border=5,
            )
            self.ws_panels[ws]["panel"].Hide()

        dialogSizer.Add(self.reqDataPanel, proportion=1, flag=wx.EXPAND)

        self.reqDataPanel.SetSizer(reqDataSizer)
        self.reqDataPanel.Hide()

        # buttons
        self.btnsizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.btnsizer.Add(
            self.btn_close, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER, border=10
        )

        dialogSizer.Add(self.btnsizer, proportion=0, flag=wx.ALIGN_CENTER)

        # expand wxWidget wx.StatusBar
        statusbarSizer = wx.BoxSizer(wx.HORIZONTAL)
        statusbarSizer.Add(self.statusbar, proportion=1, flag=wx.EXPAND)
        dialogSizer.Add(statusbarSizer, proportion=0, flag=wx.EXPAND)

        self.SetSizer(dialogSizer)
        self.Layout()

        self.SetMinSize((550, -1))
        self.SetMaxSize((-1, self.GetBestSize()[1]))
        self.Fit()

    def MakeAdvConnPane(self, pane):
        """Create advanced connection settings pane"""
        self.usernameText = StaticText(parent=pane, id=wx.ID_ANY, label=_("Username:"))
        self.username = TextCtrl(parent=pane, id=wx.ID_ANY)

        self.passwText = StaticText(parent=pane, id=wx.ID_ANY, label=_("Password:"))
        self.password = TextCtrl(parent=pane, id=wx.ID_ANY, style=wx.TE_PASSWORD)

        # pane layout
        adv_conn_sizer = wx.BoxSizer(wx.VERTICAL)

        usernameSizer = wx.BoxSizer(wx.HORIZONTAL)

        usernameSizer.Add(self.usernameText, flag=wx.ALIGN_CENTER_VERTICAL, border=5)

        usernameSizer.Add(self.username, proportion=1, flag=wx.EXPAND, border=5)

        adv_conn_sizer.Add(usernameSizer, flag=wx.ALL | wx.EXPAND, border=5)

        passwSizer = wx.BoxSizer(wx.HORIZONTAL)

        passwSizer.Add(self.passwText, flag=wx.ALIGN_CENTER_VERTICAL, border=5)

        passwSizer.Add(self.password, proportion=1, flag=wx.EXPAND, border=5)

        adv_conn_sizer.Add(passwSizer, flag=wx.ALL | wx.EXPAND, border=5)

        pane.SetSizer(adv_conn_sizer)
        adv_conn_sizer.Fit(pane)

        pane.SetSizer(adv_conn_sizer)
        adv_conn_sizer.Fit(pane)

    def OnSettingsSaving(self, name):
        """Check if required data are filled before setting save is performed."""
        server = self.server.GetValue().strip()
        if not server:
            GMessage(
                parent=self,
                message=_("No data source defined, settings are not saved."),
            )
            return

        self.settsManager.SetDataToSave(
            (server, self.username.GetValue(), self.password.GetValue())
        )
        self.settsManager.SaveSettings(name)

    def OnSettingsChanged(self, data):
        """Update widgets according to chosen settings"""
        # data list: [server, username, password]
        if len(data) < 3:
            return

        self.server.SetValue(data[0])

        self.username.SetValue(data[1])
        self.password.SetValue(data[2])

        if data[1] or data[2]:
            self.adv_conn.Expand()
        else:
            self.adv_conn.Collapse(True)

        # clear content of the wxWidget wx.TextCtrl (Output layer
        # name:), based on changing default server selection in the
        # wxWidget wx.Choice
        if len(self.layerName.GetValue()) > 0:
            self.layerName.Clear()

    def OnClose(self, event):
        """Close the dialog"""
        if not self.IsModal():
            self.Destroy()
        event.Skip()

    def _getCapFiles(self):
        ws_cap_files = {}
        for v in self.ws_panels.values():
            ws_cap_files[v["panel"].GetWebService()] = v["panel"].GetCapFile()

        return ws_cap_files

    def OnServer(self, event):
        """Server settings edited"""
        value = event.GetString()
        if value:
            self.btn_connect.Enable(True)
        else:
            self.btn_connect.Enable(False)

        # clear content of the wxWidget wx.TextCtrl (Output Layer
        # name:), based on changing content of the wxWidget
        # wx.TextCtrl (Server:)
        self.layerName.Clear()

    def OnOutputLayerName(self, event):
        """Update layer name to web service panel"""
        lname = event.GetString()
        for v in self.ws_panels.values():
            v["panel"].SetOutputLayerName(lname.strip())

    def OnConnect(self, event):
        """Connect to the server"""
        server = self.server.GetValue().strip()

        self.ch_ws_sizer.Clear(True)

        if self.active_ws_panel is not None:
            self.reqDataPanel.Hide()
            for btn in self.run_btns:
                btn.Enable(False)
            self.active_ws_panel = None

            self.Layout()
            self.Fit()

        self.statusbar.SetStatusText(
            _("Connecting to <$s>...") % self.server.GetValue().strip()
        )

        # number of panels already connected
        self.finished_panels_num = 0
        for ws in self.ws_panels.keys():
            self.ws_panels[ws]["panel"].ConnectToServer(
                url=server,
                username=self.username.GetValue(),
                password=self.password.GetValue(),
            )
            self.ws_panels[ws]["panel"].Hide()

    def OnPanelCapParsed(self, error_msg):
        """Called when panel has downloaded and parsed capabilities file."""
        # how many web service panels are finished
        self.finished_panels_num += 1

        if error_msg:
            self.error_msgs += "\n" + error_msg

        # if all are finished, show panels, which succeeded in connection
        if self.finished_panels_num == len(self.ws_panels):
            self.UpdateDialogAfterConnection()

            # show error dialog only if connections to all web services were
            # unsuccessful
            if not self._getConnectedWS() and self.error_msgs:
                GError(self.error_msgs, parent=self)
            self.error_msgs = ""

            self.Layout()
            self.Fit()

    def _getConnectedWS(self):
        """
        :return: list of found web services on server (identified as keys in
                 self.ws_panels)
        """
        conn_ws = []
        for ws, data in self.ws_panels.items():
            if data["panel"].IsConnected():
                conn_ws.append(ws)

        return conn_ws

    def UpdateDialogAfterConnection(self):
        """Update dialog after all web service panels downloaded and parsed
        capabilities data."""
        avail_ws = {}
        conn_ws = self._getConnectedWS()

        for ws in conn_ws:
            avail_ws[ws] = self.ws_panels[ws]

        self.web_service_sel = []
        self.rb_choices = []

        # at least one web service found on server
        if len(avail_ws) > 0:
            self.reqDataPanel.Show()
            self.rb_order = ["WMS_1.1.1", "WMS_1.3.0", "WMTS", "OnEarth"]

            for ws in self.rb_order:
                if ws in avail_ws:
                    self.web_service_sel.append(ws)
                    self.rb_choices.append(avail_ws[ws]["label"])

            self.choose_ws_rb = wx.RadioBox(
                parent=self.reqDataPanel,
                id=wx.ID_ANY,
                label=_("Available web services"),
                pos=wx.DefaultPosition,
                choices=self.rb_choices,
                majorDimension=1,
                style=wx.RA_SPECIFY_ROWS,
            )

            self.Bind(wx.EVT_RADIOBOX, self.OnChooseWs, self.choose_ws_rb)
            self.ch_ws_sizer.Add(
                self.choose_ws_rb,
                flag=wx.TOP | wx.LEFT | wx.RIGHT | wx.EXPAND,
                border=5,
            )
            self._showWsPanel(self.web_service_sel[self.choose_ws_rb.GetSelection()])
            self.statusbar.SetStatusText(
                _("Connected to <%s>") % self.server.GetValue().strip()
            )
            for btn in self.run_btns:
                btn.Enable(True)
        # no web service found on server
        else:
            self.statusbar.SetStatusText(
                _("Unable to connect to <%s>") % self.server.GetValue().strip()
            )
            for btn in self.run_btns:
                btn.Enable(False)
            self.reqDataPanel.Hide()
            self.active_ws_panel = None

    def OnChooseWs(self, event):
        """Show panel corresponding to selected web service."""
        chosen_r = event.GetInt()
        self._showWsPanel(self.web_service_sel[chosen_r])

    def _showWsPanel(self, ws):
        """Helper function"""
        if self.active_ws_panel is not None:
            self.active_ws_panel.Hide()

        self.active_ws_panel = self.ws_panels[ws]["panel"]
        if not self.active_ws_panel.IsShown():
            self.active_ws_panel.Show()
            self.SetMaxSize((-1, -1))
            self.active_ws_panel.GetContainingSizer().Layout()

    def OnAdvConnPaneChanged(self, event):
        """Collapse search module box"""
        if self.adv_conn.IsExpanded():
            self.adv_conn.SetLabel(self.infoCollapseLabelCol)
        else:
            self.adv_conn.SetLabel(self.infoCollapseLabelExp)

        self.Layout()
        self.SetMaxSize((-1, self.GetBestSize()[1]))
        self.SendSizeEvent()
        self.Fit()


class AddWSDialog(WSDialogBase):
    """Dialog for adding web service layer."""

    def __init__(
        self,
        parent,
        giface,
        id=wx.ID_ANY,
        style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
        **kwargs,
    ):
        WSDialogBase.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
            **kwargs,
        )

        self.SetTitle(_("Add web service layer"))

        self.parent = parent
        self.giface = giface
        self.btn_connect.SetDefault()

    def _createWidgets(self):
        WSDialogBase._createWidgets(self)

        self.btn_add = Button(parent=self, id=wx.ID_ANY, label=_("&Add layer"))
        self.btn_add.SetToolTip(
            _("Add selected web service layers as map layer into layer tree")
        )
        self.btn_add.Enable(False)

        self.run_btns.append(self.btn_add)

    def _doLayout(self):
        WSDialogBase._doLayout(self)

        self.btnsizer.Add(
            self.btn_add, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER, border=10
        )

        # bindings
        self.btn_add.Bind(wx.EVT_BUTTON, self.OnAddLayer)

    def UpdateDialogAfterConnection(self):
        """Connect to the server"""
        WSDialogBase.UpdateDialogAfterConnection(self)

        if self._getConnectedWS():
            self.btn_add.SetDefault()
        else:
            self.btn_connect.SetDefault()

    def OnAddLayer(self, event):
        """Add web service layer."""
        # add layer
        if self.active_ws_panel is None:
            return

        lcmd = self.active_ws_panel.CreateCmd()
        if not lcmd:
            return None

        # TODO: It is not clear how to do GetOptData in giface
        # knowing what GetOptData is doing might help
        # (maybe Get... is not the right name)
        # please fix giface if you know
        # tree -> giface
        # GetLayerTree -> GetLayerList
        # AddLayer -> AddLayer (but tree ones returns some layer,
        # giface ones nothing)
        # GetLayerInfo -> Layer object can by used instead
        # GetOptData -> unknown
        ltree = self.giface.GetLayerTree()

        active_ws = self.active_ws_panel.GetWebService()
        if "WMS" not in active_ws:
            cap_file = self.active_ws_panel.GetCapFile()
            cmd_cap_file = gs.tempfile()
            shutil.copyfile(cap_file, cmd_cap_file)
            lcmd.append("capfile=" + cmd_cap_file)

        layer = ltree.AddLayer(
            ltype="wms",
            lname=self.active_ws_panel.GetOutputLayerName(),
            lchecked=True,
            lcmd=lcmd,
        )

        ws_cap_files = self._getCapFiles()
        # create properties dialog
        cmd_list = ltree.GetLayerInfo(layer, "cmd")
        cmd = cmdlist_to_tuple(cmd_list)

        prop_win = WSPropertiesDialog(
            parent=self.parent,
            giface=self.giface,
            id=wx.ID_ANY,
            layer=layer,
            ws_cap_files=ws_cap_files,
            cmd=cmd,
        )

        prop_win.Hide()
        ltree.GetOptData(dcmd=None, layer=layer, params=None, propwin=prop_win)


class WSPropertiesDialog(WSDialogBase):
    """Dialog for editing web service properties."""

    def __init__(
        self,
        parent,
        giface,
        layer,
        ws_cap_files,
        cmd,
        id=wx.ID_ANY,
        style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
        **kwargs,
    ):
        """
        :param giface: grass interface
        :param layer: layer tree item
        :param ws_cap_files: dict web service('WMS_1.1.1', 'WMS_1.3.0',
        'WMTS', 'OnEarth') : cap file path cap files, which will be parsed
        :param cmd: cmd to which dialog widgets will be initialized if
        it is possible (cmp parameters exists in parsed web service cap_file)
        """

        WSDialogBase.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
            **kwargs,
        )

        self.SetTitle(_("Web service layer properties"))

        self.layer = layer
        self.giface = giface

        # after web service panels are connected, set dialog widgets
        # according to cmd in this variable (if it is not None)
        self.cmd_to_set = None

        # store data needed for reverting
        self.revert_ws_cap_files = {}
        self.revert_cmd = cmd

        ws_cap = self._getWSfromCmd(cmd)
        for ws in self.ws_panels.keys():
            # cap file used in cmd will be deleted, thanks to the dialogs
            # destructor
            if ws == ws_cap and "capfile" in cmd[1]:
                self.revert_ws_cap_files[ws] = cmd[1]["capfile"]
                del ws_cap_files[ws]
            else:
                self.revert_ws_cap_files[ws] = gs.tempfile()

        self._setRevertCapFiles(ws_cap_files)

        self.LoadCapFiles(ws_cap_files=self.revert_ws_cap_files, cmd=cmd)
        self.btn_ok.SetDefault()

    def __del__(self):
        for f in self.revert_ws_cap_files.values():
            gs.try_remove(f)

    def _setRevertCapFiles(self, ws_cap_files):
        for ws, f in ws_cap_files.items():
            if os.path.isfile(f):
                shutil.copyfile(f, self.revert_ws_cap_files[ws])
            else:
                # delete file content
                f_o = open(f, "w")
                f_o.close()

    def _createWidgets(self):
        WSDialogBase._createWidgets(self)

        self.btn_apply = Button(parent=self, id=wx.ID_ANY, label=_("&Apply"))
        self.btn_apply.SetToolTip(_("Apply changes"))
        self.btn_apply.Enable(False)
        self.run_btns.append(self.btn_apply)

        self.btn_ok = Button(parent=self, id=wx.ID_ANY, label=_("&OK"))
        self.btn_ok.SetToolTip(_("Apply changes and close dialog"))
        self.btn_ok.Enable(False)
        self.run_btns.append(self.btn_ok)

    def _doLayout(self):
        WSDialogBase._doLayout(self)

        self.btnsizer.Add(
            self.btn_apply, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER, border=10
        )

        self.btnsizer.Add(
            self.btn_ok, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER, border=10
        )

        # bindings
        self.btn_apply.Bind(wx.EVT_BUTTON, self.OnApply)
        self.btn_ok.Bind(wx.EVT_BUTTON, self.OnSave)

    def LoadCapFiles(self, ws_cap_files, cmd):
        """Parse cap files and update dialog.

        For parameters description, see the constructor.
        """
        self.ch_ws_sizer.Clear(True)

        self.cmd_to_set = cmd

        self.finished_panels_num = 0

        conn = self._getServerConnFromCmd(cmd)

        self.server.SetValue(conn["url"])
        self.password.SetValue(conn["password"])
        self.username.SetValue(conn["username"])

        self.layerName.SetValue(cmd[1]["map"])

        for ws, data in self.ws_panels.items():
            cap_file = None

            if ws in ws_cap_files:
                cap_file = ws_cap_files[ws]

            data["panel"].ParseCapFile(
                url=conn["url"],
                username=conn["password"],
                password=conn["username"],
                cap_file=cap_file,
            )

    def _getServerConnFromCmd(self, cmd):
        """Get url/server/password from cmd tuple"""
        conn = {"url": "", "username": "", "password": ""}

        for k in conn.keys():
            if k in cmd[1]:
                conn[k] = cmd[1][k]
        return conn

    def _apply(self):
        """Apply chosen values from widgets to web service layer."""
        lcmd = self.active_ws_panel.CreateCmd()
        if not lcmd:
            return

        active_ws = self.active_ws_panel.GetWebService()
        if "WMS" not in active_ws:
            lcmd.append("capfile=" + self.revert_ws_cap_files[active_ws])

        self.giface.GetLayerTree().GetOptData(
            dcmd=lcmd, layer=self.layer, params=True, propwin=self
        )

        # TODO use just list or tuple
        cmd = cmdlist_to_tuple(lcmd)
        self.revert_cmd = cmd
        self._setRevertCapFiles(self._getCapFiles())

        self.giface.updateMap.emit()

    def UpdateDialogAfterConnection(self):
        """Connect to the server"""
        WSDialogBase.UpdateDialogAfterConnection(self)
        if self._getConnectedWS():
            self.btn_ok.SetDefault()
        else:
            self.btn_connect.SetDefault()

    def OnApply(self, event):
        self._apply()

    def OnSave(self, event):
        self._apply()
        self._close()

    def OnClose(self, event):
        """Close dialog"""
        self._close()

    def _close(self):
        """Hide dialog"""
        self.Hide()
        self.LoadCapFiles(cmd=self.revert_cmd, ws_cap_files=self.revert_ws_cap_files)

    def OnPanelCapParsed(self, error_msg):
        """Called when panel has downloaded and parsed capabilities file."""
        WSDialogBase.OnPanelCapParsed(self, error_msg)

        if self.finished_panels_num == len(self.ws_panels):
            if self.cmd_to_set:
                self._updateWsPanelWidgetsByCmd(self.cmd_to_set)
                self.cmd_to_set = None

    def _updateWsPanelWidgetsByCmd(self, cmd):
        """Set values of  widgets according to parameters in cmd."""

        ws = self._getWSfromCmd(cmd)
        if self.ws_panels[ws]["panel"].IsConnected():
            self.choose_ws_rb.SetStringSelection(self.ws_panels[ws]["label"])
            self._showWsPanel(ws)
            self.ws_panels[ws]["panel"].UpdateWidgetsByCmd(cmd)

    def _getWSfromCmd(self, cmd):
        driver = cmd[1]["driver"]
        ws = driver.split("_")[0]

        if ws == "WMS":
            ws += "_" + cmd[1]["wms_version"]
        return ws


class SaveWMSLayerDialog(wx.Dialog):
    """Dialog for saving web service layer into GRASS vector/raster layer.

    .. todo::
        Implement saving data in region of map display.
    """

    def __init__(self, parent, layer, giface):
        wx.Dialog.__init__(
            self,
            parent=parent,
            title=("Save web service layer as raster map"),
            id=wx.ID_ANY,
        )

        self.layer = layer
        self._giface = giface

        self.cmd = self.layer.GetCmd()

        self.thread = CmdThread(self)
        self.cmdStdErr = GStderr(self)

        self._createWidgets()

    def _createWidgets(self):
        self.labels = {}
        self.params = {}

        self.labels["output"] = StaticText(
            parent=self, id=wx.ID_ANY, label=_("Name for output raster map:")
        )

        self.params["output"] = Select(
            parent=self,
            type="raster",
            mapsets=[gs.gisenv()["MAPSET"]],
            size=globalvar.DIALOG_GSELECT_SIZE,
        )

        self.regionStBoxLabel = StaticBox(
            parent=self, id=wx.ID_ANY, label=" %s " % _("Export region")
        )

        self.region_types_order = ["display", "comp", "named"]
        self.region_types = {}
        self.region_types["display"] = RadioButton(
            parent=self, label=_("Map display"), style=wx.RB_GROUP
        )
        self.region_types["comp"] = RadioButton(
            parent=self, label=_("Computational region")
        )
        self.region_types["named"] = RadioButton(parent=self, label=_("Named region"))
        self.region_types["display"].SetToolTip(
            _("Extent and resolution are based on Map Display geometry.")
        )
        self.region_types["comp"].SetToolTip(
            _("Extent and resolution are based on computational region.")
        )
        self.region_types["named"].SetToolTip(
            _("Extent and resolution are based on named region.")
        )
        self.region_types["display"].SetValue(True)  # set default as map display

        self.overwrite = wx.CheckBox(
            parent=self, id=wx.ID_ANY, label=_("Overwrite existing raster map")
        )

        self.named_reg_panel = wx.Panel(parent=self, id=wx.ID_ANY)
        self.labels["region"] = StaticText(
            parent=self.named_reg_panel, id=wx.ID_ANY, label=_("Choose named region:")
        )

        self.params["region"] = Select(
            parent=self.named_reg_panel,
            type="region",
            size=globalvar.DIALOG_GSELECT_SIZE,
        )

        # buttons
        self.btn_close = Button(parent=self, id=wx.ID_CLOSE)
        self.SetEscapeId(self.btn_close.GetId())
        self.btn_close.SetToolTip(_("Close dialog"))

        self.btn_ok = Button(parent=self, label=_("&Save layer"))
        self.btn_ok.SetToolTip(_("Save web service layer as raster map"))

        # statusbar
        self.statusbar = wx.StatusBar(parent=self, id=wx.ID_ANY)

        self._layout()

    def _layout(self):
        self._border = wx.BoxSizer(wx.VERTICAL)
        dialogSizer = wx.BoxSizer(wx.VERTICAL)

        regionSizer = wx.BoxSizer(wx.HORIZONTAL)

        dialogSizer.Add(
            self._addSelectSizer(title=self.labels["output"], sel=self.params["output"])
        )

        regionSizer = wx.StaticBoxSizer(self.regionStBoxLabel, wx.VERTICAL)

        regionTypeSizer = wx.BoxSizer(wx.HORIZONTAL)
        for r_type in self.region_types_order:
            regionTypeSizer.Add(self.region_types[r_type], flag=wx.RIGHT, border=8)

        regionSizer.Add(regionTypeSizer)

        self.named_reg_panel.SetSizer(
            self._addSelectSizer(title=self.labels["region"], sel=self.params["region"])
        )
        regionSizer.Add(self.named_reg_panel)
        self.named_reg_panel.Hide()

        dialogSizer.Add(regionSizer, flag=wx.EXPAND)

        dialogSizer.Add(self.overwrite, flag=wx.TOP, border=10)

        # buttons
        self.btnsizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.btnsizer.Add(
            self.btn_close, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER, border=10
        )

        self.btnsizer.Add(
            self.btn_ok, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER, border=10
        )

        dialogSizer.Add(self.btnsizer, proportion=0, flag=wx.ALIGN_CENTER)

        self._border.Add(dialogSizer, proportion=0, flag=wx.ALL, border=5)

        self._border.Add(self.statusbar, proportion=0)

        self.SetSizer(self._border)
        self.Layout()
        self.Fit()

        # bindings
        self.btn_ok.Bind(wx.EVT_BUTTON, self.OnSave)

        self.Bind(EVT_CMD_DONE, self.OnCmdDone)
        self.Bind(EVT_CMD_OUTPUT, self.OnCmdOutput)

        for r_type in self.region_types_order:
            self.Bind(wx.EVT_RADIOBUTTON, self.OnRegionType, self.region_types[r_type])

    def _addSelectSizer(self, title, sel):
        """Helper layout function."""
        selSizer = wx.BoxSizer(orient=wx.VERTICAL)

        selTitleSizer = wx.BoxSizer(wx.HORIZONTAL)
        selTitleSizer.Add(
            title, proportion=1, flag=wx.LEFT | wx.TOP | wx.EXPAND, border=5
        )

        selSizer.Add(selTitleSizer, proportion=0, flag=wx.EXPAND)

        selSizer.Add(
            sel,
            proportion=1,
            flag=wx.EXPAND | wx.ALL,
            border=5,
        )

        return selSizer

    def OnRegionType(self, event):
        selected = event.GetEventObject()
        if selected == self.region_types["named"]:
            self.named_reg_panel.Show()
        else:
            self.named_reg_panel.Hide()

        self._border.Layout()
        self.Fit()

    def OnSave(self, event):
        """Import WMS raster data into GRASS as raster layer."""
        self.thread.abort(abortall=True)
        currmapset = gs.gisenv()["MAPSET"]

        self.output = self.params["output"].GetValue().strip()
        l_spl = self.output.strip().split("@")

        # check output layer
        msg = None
        if not self.output:
            msg = _("Missing output raster.")

        elif len(l_spl) > 1 and l_spl[1] != currmapset:
            msg = _("Output map can be added only to current mapset.")

        elif (
            not self.overwrite.IsChecked()
            and gs.find_file(self.output, "cell", ".")["fullname"]
        ):
            msg = _("Output map <%s> already exists") % self.output

        if msg:
            GMessage(parent=self, message=msg)
            return

        self.output = l_spl[0]

        # check region
        region = self.params["region"].GetValue().strip()
        reg_spl = region.strip().split("@")

        reg_mapset = "."
        if len(reg_spl) > 1:
            reg_mapset = reg_spl[1]

        if self.region_types["named"].GetValue():
            if not gs.find_file(reg_spl[0], "windows", reg_mapset)["fullname"]:
<<<<<<< HEAD
                msg = (
                    _("Region <%s> does not exist.") % self.params["region"].GetValue()
=======
                msg = _(
                    "Region <%s> does not exist." % self.params["region"].GetValue()
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
                )
                GWarning(parent=self, message=msg)
                return

        # create r.in.wms command
        cmd = ("r.in.wms", deepcopy(self.cmd[1]))

        if "map" in cmd[1]:
            del cmd[1]["map"]

        cmd[1]["output"] = self.output

        if self.overwrite.IsChecked():
            cmd[1]["overwrite"] = True

        env = os.environ.copy()
        if self.region_types["named"].GetValue():
            cmd[1]["region"] = region
        elif self.region_types["display"].GetValue():
            region = self._giface.GetMapWindow().GetMap().SetRegion()
            env["GRASS_REGION"] = region

        cmdList = cmdtuple_to_list(cmd)
        self.currentPid = self.thread.GetId()

        self.thread.RunCmd(cmdList, env=env, stderr=self.cmdStdErr)

        self.statusbar.SetStatusText(_("Downloading data..."))

    def OnCmdDone(self, event):
        """When data are fetched."""
        if event.pid != self.currentPid:
            return

        self._addLayer()
        self.statusbar.SetStatusText("")

    def _addLayer(self):
        """Add layer into layer tree."""
        llist = self._giface.GetLayerList()
        if len(llist.GetLayersByName(self.output)) == 0:
            cmd = ["d.rast", "map=" + self.output]
            llist.AddLayer(ltype="raster", name=self.output, cmd=cmd, checked=True)

    def OnCmdOutput(self, event):
        """Handle cmd output according to debug level."""
        if Debug.GetLevel() == 0:
            if event.type == "error":
                msg = _("Unable to fetch data.\n")
                msg += event.text
                GWarning(parent=self, message=msg)
        else:
            Debug.msg(1, event.text)
