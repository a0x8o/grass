#!/usr/bin/env python3
############################################################################
#
# MODULE:    Map Swipe
# AUTHOR(S): Anna Kratochvilova
# PURPOSE:   The Map Swipe is a wxGUI component which allows the user to
#            interactively compare two maps
# COPYRIGHT: (C) 2012 by Anna Kratochvilova, and the GRASS Development Team
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
############################################################################

# %module
# % description: Interactively compares two maps by swiping a visibility bar.
# % keyword: general
# % keyword: GUI
# % keyword: display
# %end
# %option G_OPT_R_INPUT
# % key: first
# % description: First (top/right) raster map
# % required: no
# %end
# %option G_OPT_R_INPUT
# % key: second
# % description: Second (bottom/left) raster map
# % required: no
# %end
# %option
# % key: mode
# % description: View mode
# % options: swipe,mirror
# % descriptions:swipe;swiping the upper map layer to show the map layer below ;mirror;synchronized maps side by side
# % answer: swipe
# % required: no
# %end

import os
import grass.script as gs


def main():
    options, flags = gs.parser()

    import wx

    from grass.script.setup import set_gui_path

    set_gui_path()

    from core.settings import UserSettings
    from core.giface import StandaloneGrassInterface
    from core import globalvar
    from mapswipe.frame import SwipeMapDisplay

    driver = UserSettings.Get(group="display", key="driver", subkey="type")
    if driver == "png":
        os.environ["GRASS_RENDER_IMMEDIATE"] = "png"
    else:
        os.environ["GRASS_RENDER_IMMEDIATE"] = "cairo"

    first = options["first"]
    second = options["second"]
    mode = options["mode"]

    for mapName in [first, second]:
        if mapName:
            gfile = gs.find_file(name=mapName)
            if not gfile["name"]:
                gs.fatal(_("Raster map <%s> not found") % mapName)

    app = wx.App()

    # show main frame
    frame = wx.Frame(
        parent=None,
        size=globalvar.MAP_WINDOW_SIZE,
        title=_("Map Swipe Tool - GRASS GIS"),
    )
    frame = SwipeMapDisplay(
        parent=frame,
        giface=StandaloneGrassInterface(),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        title=_("Map Swipe Tool - GRASS GIS"),
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
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
=======
        title=_("Map Swipe Tool - GRASS GIS"),
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
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
        title=_("Map Swipe Tool - GRASS GIS"),
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
        title=_("Map Swipe Tool - GRASS GIS"),
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
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
    )

    if first:
        frame.SetFirstRaster(first)
    if second:
        frame.SetSecondRaster(second)
    if first or second:
        frame.SetRasterNames()

    frame.SetViewMode(mode)
    frame.Show()

    app.MainLoop()


if __name__ == "__main__":
    main()
