#!/usr/bin/env python3
############################################################################
#
# MODULE:    g.gui.vdigit
# AUTHOR(S): Martin Landa <landa.martin gmail.com>
# PURPOSE:   wxGUI Vector Digitizer
# COPYRIGHT: (C) 2007-2013 by Martin Landa, and the GRASS Development Team
#
#  This program is free software; you can 1redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 2 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
############################################################################

# %module
# % description: Interactive editing and digitization of vector maps.
# % keyword: general
# % keyword: GUI
# % keyword: vector
# % keyword: editing
# % keyword: digitizer
# %end
# %flag
# % key: c
# % description: Create new vector map if doesn't exist
# %end
# %option G_OPT_V_MAP
# % label: Name of vector map to edit
# %end

import os
import grass.script as gs


def main():
    gs.set_raise_on_error(False)

    options, flags = gs.parser()

    # import wx only after running parser
    # to avoid issues with complex imports when only interface is needed
    import wx

    from grass.script.setup import set_gui_path

    set_gui_path()

    from core.render import Map
    from core.globalvar import ICONDIR
    from mapdisp.frame import MapPanel
    from gui_core.mapdisp import FrameMixin
    from mapdisp.main import DMonGrassInterface
    from core.settings import UserSettings
    from vdigit.main import haveVDigit, errorMsg
    from grass.exceptions import CalledModuleError

    # define classes which needs imports as local
    # for longer definitions, a separate file would be a better option
    class VDigitMapDisplay(FrameMixin, MapPanel):
        """Map display for wrapping map panel with v.digit mathods and frame methods"""

        def __init__(self, parent, vectorMap):
            MapPanel.__init__(
                self, parent=parent, Map=Map(), giface=DMonGrassInterface(None)
            )

            # set system icon
            parent.SetIcon(
                wx.Icon(os.path.join(ICONDIR, "grass_map.ico"), wx.BITMAP_TYPE_ICO)
            )

            # bindings
            parent.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

            # extend shortcuts and create frame accelerator table
            self.shortcuts_table.append(
                (self.OnFullScreen, wx.ACCEL_NORMAL, wx.WXK_F11)
            )
            self._initShortcuts()

            # this giface issue not solved yet, we must set mapframe afterwards
            self._giface._mapframe = self
            # load vector map
            mapLayer = self.GetMap().AddLayer(
                ltype="vector",
                name=vectorMap,
                command=["d.vect", "map=%s" % vectorMap],
                active=True,
                hidden=False,
                opacity=1.0,
                render=True,
            )

            # switch toolbar
            self.AddToolbar("vdigit", fixed=True)

            # start editing
            self.toolbars["vdigit"].StartEditing(mapLayer)
            # use Close instead of QuitVDigit for standalone tool
            self.toolbars["vdigit"].quitDigitizer.disconnect(self.QuitVDigit)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0292214bb (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
>>>>>>> 192a521175 (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
=======
>>>>>>> c0e1e1a5b1 (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
>>>>>>> 6c2a690d2a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 9e87022bce (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 346ac2b69f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 93504623ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5d165f4019 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d60db92912 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> bbd5e9b440 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f508af7b6f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 341119ec87 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3d8b9dcee3 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3b9f6cedaf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6e84cf14b2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fab0494fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 37d73e31b1 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b0292214bb (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> bcbb587500 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 502e49ed0a (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
<<<<<<< HEAD
>>>>>>> c0e1e1a5b1 (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 6c2a690d2a (wxGUI: fix layout flag assert in wms dialog (#1764))
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
<<<<<<< HEAD
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b0292214bb (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
>>>>>>> 8135f68d14 (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
=======
>>>>>>> 90e532a7f7 (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b0292214bb (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 502e49ed0a (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
<<<<<<< HEAD
>>>>>>> 90e532a7f7 (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 6e84cf14b2 (wxGUI: fix layout flag assert in wms dialog (#1764))
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
>>>>>>> 9e87022bce (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9e87022bce (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 346ac2b69f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
>>>>>>> 0cc7cbf610 (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
>>>>>>> osgeo-main
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
>>>>>>> osgeo-main
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
>>>>>>> osgeo-main
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> osgeo-main
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> osgeo-main
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
=======
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
>>>>>>> osgeo-main
=======
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
>>>>>>> osgeo-main
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
>>>>>>> 0cc7cbf610 (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> osgeo-main
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> osgeo-main
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> osgeo-main
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
>>>>>>> osgeo-main
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
>>>>>>> osgeo-main
=======
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bbd5e9b440 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f508af7b6f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 341119ec87 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3d8b9dcee3 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3b9f6cedaf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
<<<<<<< HEAD
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
>>>>>>> 0cc7cbf610 (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
>>>>>>> 0cc7cbf610 (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
=======
>>>>>>> d60db92912 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> bbd5e9b440 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f508af7b6f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 341119ec87 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3d8b9dcee3 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3b9f6cedaf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 6e84cf14b2 (wxGUI: fix layout flag assert in wms dialog (#1764))
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> fab0494fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 37d73e31b1 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
>>>>>>> 0cc7cbf610 (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
>>>>>>> 0cc7cbf610 (style: Fixes some unnecessary-lambda (PLW0108) (#3956))
=======
            self.toolbars["vdigit"].quitDigitizer.connect(self.Close)
=======
            self.toolbars["vdigit"].quitDigitizer.connect(lambda: self.Close())
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 6e84cf14b2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fab0494fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 37d73e31b1 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

            # add Map Display panel to Map Display frame
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self, proportion=1, flag=wx.EXPAND)
            parent.SetSizer(sizer)
            parent.Layout()

    if not haveVDigit:
        gs.fatal(_("Vector digitizer not available. %s") % errorMsg)

    if not gs.find_file(
        name=options["map"], element="vector", mapset=gs.gisenv()["MAPSET"]
    )["fullname"]:
        if not flags["c"]:
            gs.fatal(
                _(
                    "Vector map <%s> not found in current mapset. "
                    "New vector map can be created by providing '-c' flag."
                )
                % options["map"]
            )
        else:
            gs.verbose(_("New vector map <%s> created") % options["map"])
            try:
                gs.run_command("v.edit", map=options["map"], tool="create", quiet=True)
            except CalledModuleError:
                gs.fatal(_("Unable to create new vector map <%s>") % options["map"])

    # allow immediate rendering
    driver = UserSettings.Get(group="display", key="driver", subkey="type")
    if driver == "png":
        os.environ["GRASS_RENDER_IMMEDIATE"] = "png"
    else:
        os.environ["GRASS_RENDER_IMMEDIATE"] = "cairo"

    app = wx.App()
    frame = wx.Frame(
        None,
        id=wx.ID_ANY,
        size=(850, 600),
        style=wx.DEFAULT_FRAME_STYLE,
        title=_("Vector Digitizer - GRASS GIS"),
    )
    frame = VDigitMapDisplay(parent=frame, vectorMap=options["map"])
    frame.Show()

    app.MainLoop()


if __name__ == "__main__":
    main()
