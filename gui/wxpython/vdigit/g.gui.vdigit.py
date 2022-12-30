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

            # this giface issue not solved yet, we must set mapframe aferwards
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
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
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
