#!/usr/bin/env python3

############################################################################
#
# MODULE:       d.rast.leg
# AUTHOR(S):
#               Jianping Xu and Scott Madry, Rutgers University. October 19, 1993
#               Markus Neteler 8/2002: added simple d.legend logic
#               Markus Neteler 10/2003: added g.parser
#               Michael Barton 12/2004: remove reference to (null)
#               Glynn Clements 10/2008: converted to Python
#
# PURPOSE:      Displays a raster map and its legend on a graphics window.
#
# Description:  d.rast.leg clears the entire screen, divides it into a main
#               (left) and a minor (right) frames, and then display a raster
#               map in the main frame and the map legend in the minor frame.
#               The user can run the program interactively or
#               non-interactively.
#
# See also:     d.rast, d.legend.
#
# COPYRIGHT:	(C) 1993-2014 by the GRASS Development Team
#
#               This program is free software under the GNU General Public
#               License (>=v2). Read the file COPYING that comes with GRASS
#               for details.
#
#############################################################################

# %module
# % description: Displays a raster map and its legend on a graphics window
# % keyword: display
# % keyword: cartography
# % keyword: legend
# %end
# %flag
# %  key: f
# %  description: Flip legend
# %end
# %flag
# %  key: n
# %  description: Omit entries with missing label
# %end
# %option G_OPT_R_MAP
# % description: Name of raster map to display
# %end
# %flag
# %  key: s
# %  description: Draw smooth gradient
# %end
# %option
# % key: lines
# % type: integer
# % description: Number of lines to appear in the legend
# % required: no
# %end
# %option G_OPT_R_INPUT
# % key: raster
# % description: Name of input raster map to generate legend from
# % required: no
# %end

import sys
import os
import grass.script as gs


def make_frame(f, b, t, l, r):  # noqa: E741
    (fl, fr, ft, fb) = f

    t /= 100.0
    b /= 100.0
    l /= 100.0
    r /= 100.0

    rt = fb + t * (ft - fb)
    rb = fb + b * (ft - fb)
    rl = fl + l * (fr - fl)
    rr = fl + r * (fr - fl)
    s = "%f,%f,%f,%f" % (rt, rb, rl, rr)
    os.environ["GRASS_RENDER_FRAME"] = s


def main():
    map = options["map"]
    nlines = options["lines"]
    rast = options["raster"]
    omit = flags["n"]
    flip = flags["f"]
    smooth = flags["s"]

    # for -n flag of d.legend
    if not gs.find_file(map)["file"]:
        gs.fatal(_("Raster map <%s> not found") % map)

    # for rast=
    if rast and not gs.find_file(rast)["file"]:
        gs.fatal(_("Raster map <%s> not found") % rast)

    s = gs.read_command("d.info", flags="f")
    if not s:
        sys.exit(1)

    # fixes trunk r64459
    s = s.split(":")[1]
    f = tuple(float(x) for x in s.split())

    gs.run_command("d.erase")
    os.environ["GRASS_RENDER_FILE_READ"] = "TRUE"

    # draw title

    # set vertical divide at 65 instead of 80 if real labels in cats/ file??
    make_frame(f, 90, 100, 70, 100)
    # use map name without mapset suffix
    mapname = map.split("@")[0]
    gs.run_command("d.text", color="black", size=5, at="5,97", align="cl", text=mapname)

    # draw legend

    # set legend vertical position and size based on number of categories
    cats = gs.read_command("r.describe", map=map, flags="1n")
    ncats = len(cats.strip().split("\n"))

    # Only need to adjust legend size if number of categories is between 1 and 10
    ncats = max(ncats, 2)
    ncats = min(ncats, 10)

    VSpacing = 100 - (ncats * 10) + 10

    if not nlines:
        nlines = None

    lmap = rast or map

    kv = gs.raster_info(map=lmap)
<<<<<<< HEAD
    leg_at = None if kv["datatype"] == "CELL" else "%f,95,5,10" % VSpacing
=======
    if kv["datatype"] == "CELL":
        leg_at = None
    else:
        leg_at = "%f,95,5,10" % VSpacing
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))

    # checking for histogram causes more problems than it solves
    #    histfiledir = grass.find_file(lmap, 'cell_misc')['file']
    #    has_hist = os.path.isfile(os.path.join(histfiledir, 'histogram'))

    lflags = ""
    if flip:
        lflags += "f"
    if omit:
        lflags += "n"
    if smooth:
        lflags += "s"

    #    if has_hist or omit:
    #        lflags += 'n'

    make_frame(f, 0, 90, 70, 100)
    gs.run_command("d.legend", flags=lflags, raster=lmap, lines=nlines, at=leg_at)

    # draw map
    make_frame(f, 0, 100, 0, 70)
    gs.run_command("d.rast", map=map)


if __name__ == "__main__":
    options, flags = gs.parser()
    main()
