#!/usr/bin/env python3

############################################################################
#
# MODULE:       t.rast.out.vtk
# AUTHOR(S):    Soeren Gebbert
#
# PURPOSE:      Export space time raster dataset as VTK time series
# COPYRIGHT:    (C) 2011-2017 by the GRASS Development Team
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
#############################################################################

# %module
# % description: Exports space time raster dataset as VTK time series.
# % keyword: temporal
# % keyword: export
# % keyword: output
# % keyword: raster
# % keyword: VTK
# % keyword: time
# %end

# %option G_OPT_STRDS_INPUT
# %end

# %option
# % key: directory
# % type: string
# % description: Path to the export directory
# % required: yes
# % multiple: no
# %end

# %option G_OPT_R_ELEV
# % required: no
# %end

# %option G_OPT_T_WHERE
# %end

# %option
# % key: null
# % type: double
# % description: Value to represent no data cell
# % required: no
# % multiple: no
# % answer: -99999.99
# %end

# %flag
# % key: p
# % description: Create VTK point data instead of VTK cell data (if no elevation map is given)
# %end

# %flag
# % key: c
# % description: Correct the coordinates to fit the VTK-OpenGL precision
# %end

# %flag
# % key: g
# % description: Export files using the space time dataset granularity for equidistant time between maps, where statement will be ignored
# %end

import os

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import grass.script as gs
=======
<<<<<<< HEAD
<<<<<<< HEAD
import grass.script as grass
=======
import grass.script as gs
>>>>>>> osgeo-main
>>>>>>> main
=======
import grass.script as grass
>>>>>>> 0c13ccda1f (style(temporal): Sort and group imports (#3959))
<<<<<<< HEAD
>>>>>>> c8cd2d055b (style(temporal): Sort and group imports (#3959))
=======
=======
import grass.script as gs
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
>>>>>>> cc1bb01ea7 (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
=======
=======
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
import grass.script as gs
=======
import grass.script as grass
>>>>>>> 0c13ccda1f (style(temporal): Sort and group imports (#3959))
<<<<<<< HEAD
>>>>>>> 3fa16d2bea (style(temporal): Sort and group imports (#3959))
=======
=======
import grass.script as gs
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
from grass.exceptions import CalledModuleError

############################################################################


def main():
    # lazy imports
    import grass.temporal as tgis

    # Get the options
    input = options["input"]
    elevation = options["elevation"]
    expdir = options["directory"]
    where = options["where"]
    null = options["null"]
    use_pdata = flags["p"]
    coorcorr = flags["c"]
    use_granularity = flags["g"]

    # Make sure the temporal database exists
    tgis.init()

    if not os.path.exists(expdir):
        gs.fatal(_("Export directory <%s> not found.") % expdir)

    os.chdir(expdir)

    sp = tgis.open_old_stds(input, "strds")

    if use_granularity:
        # Attention: A list of lists of maps will be returned
        maps = sp.get_registered_maps_as_objects_by_granularity()
        # Create a NULL map in case of granularity support
        null_map = "temporary_null_map_%i" % os.getpid()
        gs.mapcalc("%s = null()" % (null_map))
    else:
        maps = sp.get_registered_maps_as_objects(where, "start_time", None)

    # To have scalar values with the same name, we need to copy the
    # raster maps using a single name
    map_name = "%s_%i" % (sp.base.get_name(), os.getpid())

    count = 0
    if maps is not None:
        for map in maps:
            if use_granularity:
                if map and len(map) > 0:
                    id = map[0].get_map_id()
            else:
                id = map.get_map_id()
            # None ids will be replaced by NULL maps
            if id is None:
                id = null_map

            gs.run_command("g.copy", raster="%s,%s" % (id, map_name), overwrite=True)
            out_name = "%6.6i_%s.vtk" % (count, sp.base.get_name())

            mflags = ""
            if use_pdata:
                mflags += "p"
            if coorcorr:
                mflags += "c"

            # Export the raster map with r.out.vtk
            try:
                if elevation:
                    gs.run_command(
                        "r.out.vtk",
                        flags=mflags,
                        null=null,
                        input=map_name,
                        elevation=elevation,
                        output=out_name,
                        overwrite=gs.overwrite(),
                    )
                else:
                    gs.run_command(
                        "r.out.vtk",
                        flags=mflags,
                        null=null,
                        input=map_name,
                        output=out_name,
                        overwrite=gs.overwrite(),
                    )
            except CalledModuleError:
<<<<<<< HEAD
                gs.fatal(_("Unable to export raster map <%s>") % map_name)
=======
                gs.fatal(_("Unable to export raster map <%s>" % map_name))
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))

            count += 1

    if use_granularity:
        gs.run_command("g.remove", flags="f", type="raster", name=null_map)
    gs.run_command("g.remove", flags="f", type="raster", name=map_name)


if __name__ == "__main__":
    options, flags = gs.parser()
    main()
