#!/usr/bin/env python3

############################################################################
#
# MODULE:       t.vect.what.strds
# AUTHOR(S):    Soeren Gebbert
#
# PURPOSE:      Store raster map values at spatial and temporal positions of vector points as vector attributes.
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
# % description: Stores raster map values at spatial and temporal positions of vector points as vector attributes.
# % keyword: temporal
# % keyword: sampling
# % keyword: vector
# % keyword: time
# %end

# %option G_OPT_STVDS_INPUT
# %end

# %option G_OPT_STRDS_INPUT
# % key: strds
# %end

# %option
# % key: column
# % type: string
# % label: Name of the vector column to be created and to store sampled raster values
# % description: The use of a column name forces t.vect.what.rast to sample only values from the first map found in an interval. Otherwise the raster map names are used as column names
# % required: no
# % multiple: no
# %end

# %option
# % key: method
# % type: string
# % description: Aggregate operation to be performed on the raster maps
# % required: yes
# % multiple: no
# % options: disabled,average,count,median,mode,minimum,min_raster,maximum,max_raster,stddev,range,sum,variance,diversity,slope,offset,detcoeff,quart1,quart3,perc90,quantile,skewness,kurtosis
# % answer: disabled
# %end

# %option G_OPT_DB_WHERE
# %end

# %option G_OPT_T_WHERE
# % key: t_where
# %end

# %option G_OPT_T_SAMPLE
# %end

import os
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4ad9c8a13e (style: Fixes manual-from-import (PLR0402) (#3949))
=======
>>>>>>> 3fa16d2bea (style(temporal): Sort and group imports (#3959))

<<<<<<< HEAD
import grass.script as grass
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
from grass.script import raster
>>>>>>> 85b047f439 (style: Fixes manual-from-import (PLR0402) (#3949))
=======
>>>>>>> 4f1b897788 (style(temporal): Sort and group imports (#3959))
=======
import grass.script as gs
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d880ec0a6d (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
=======
=======
import grass.script as gs
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 4ad9c8a13e (style: Fixes manual-from-import (PLR0402) (#3949))
=======
import grass.script as grass
from grass.script import raster
>>>>>>> d59d1faa34 (style: Fixes manual-from-import (PLR0402) (#3949))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebb6f8a179 (style: Fixes manual-from-import (PLR0402) (#3949))
=======
=======

<<<<<<< HEAD
import grass.script as grass
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0c13ccda1f (style(temporal): Sort and group imports (#3959))
<<<<<<< HEAD
>>>>>>> c8cd2d055b (style(temporal): Sort and group imports (#3959))
=======
=======
=======
>>>>>>> 8433de61b2 (style(temporal): Sort and group imports (#3959))
<<<<<<< HEAD
=======
from grass.script import raster
>>>>>>> 85b047f439 (style: Fixes manual-from-import (PLR0402) (#3949))
<<<<<<< HEAD
>>>>>>> ea07a210df (style: Fixes manual-from-import (PLR0402) (#3949))
<<<<<<< HEAD
>>>>>>> aec0b58ff8 (style: Fixes manual-from-import (PLR0402) (#3949))
=======
=======
=======
>>>>>>> 4f1b897788 (style(temporal): Sort and group imports (#3959))
<<<<<<< HEAD
>>>>>>> 8433de61b2 (style(temporal): Sort and group imports (#3959))
<<<<<<< HEAD
>>>>>>> 80e24e5298 (style(temporal): Sort and group imports (#3959))
=======
=======
=======
import grass.script as gs
>>>>>>> d880ec0a6d (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
>>>>>>> cc1bb01ea7 (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
=======
>>>>>>> 4ad9c8a13e (style: Fixes manual-from-import (PLR0402) (#3949))
=======
=======

import grass.script as grass
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0c13ccda1f (style(temporal): Sort and group imports (#3959))
<<<<<<< HEAD
>>>>>>> 3fa16d2bea (style(temporal): Sort and group imports (#3959))
=======
=======
=======
>>>>>>> 8433de61b2 (style(temporal): Sort and group imports (#3959))
<<<<<<< HEAD
=======
from grass.script import raster
>>>>>>> 85b047f439 (style: Fixes manual-from-import (PLR0402) (#3949))
<<<<<<< HEAD
>>>>>>> ea07a210df (style: Fixes manual-from-import (PLR0402) (#3949))
<<<<<<< HEAD
>>>>>>> 5b625e12f4 (style: Fixes manual-from-import (PLR0402) (#3949))
=======
=======
=======
>>>>>>> 4f1b897788 (style(temporal): Sort and group imports (#3959))
<<<<<<< HEAD
>>>>>>> 8433de61b2 (style(temporal): Sort and group imports (#3959))
<<<<<<< HEAD
>>>>>>> 07a13705fd (style(temporal): Sort and group imports (#3959))
=======
=======
=======
import grass.script as gs
>>>>>>> d880ec0a6d (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
from grass.exceptions import CalledModuleError
from grass.script import raster

############################################################################


def main():
    # lazy imports
    import grass.temporal as tgis

    # Get the options
    input = options["input"]
    strds = options["strds"]
    where = options["where"]
    column = options["column"]
    method = options["method"]
    tempwhere = options["t_where"]
    sampling = options["sampling"]

    if where in {"", " ", "\n"}:
        where = None

    # Make sure the temporal database exists
    tgis.init()
    # We need a database interface
    dbif = tgis.SQLDatabaseInterfaceConnection()
    dbif.connect()

    sp = tgis.open_old_stds(input, "stvds", dbif)
    strds_sp = tgis.open_old_stds(strds, "strds", dbif)

    if strds_sp.get_temporal_type() != sp.get_temporal_type():
        dbif.close()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        gs.fatal(_("Input and aggregation dataset must have the same temporal type"))
=======
<<<<<<< HEAD
<<<<<<< HEAD
        grass.fatal(_("Input and aggregation dataset must have the same temporal type"))
=======
        gs.fatal(_("Input and aggregation dataset must have the same temporal type"))
>>>>>>> osgeo-main
>>>>>>> main
=======
        grass.fatal(_("Input and aggregation dataset must have the same temporal type"))
>>>>>>> fb2b1e4ce2 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
<<<<<<< HEAD
>>>>>>> c866535f04 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
        gs.fatal(_("Input and aggregation dataset must have the same temporal type"))
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
>>>>>>> cc1bb01ea7 (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
=======
=======
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
        gs.fatal(_("Input and aggregation dataset must have the same temporal type"))
=======
        grass.fatal(_("Input and aggregation dataset must have the same temporal type"))
>>>>>>> fb2b1e4ce2 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
<<<<<<< HEAD
>>>>>>> d10220bba4 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
        gs.fatal(_("Input and aggregation dataset must have the same temporal type"))
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))

    # Check if intervals are present in the sample dataset
    if sp.get_temporal_type() == "absolute":
        map_time = sp.absolute_time.get_map_time()
    else:
        map_time = sp.relative_time.get_map_time()

    if map_time != "interval":
        dbif.close()
        gs.fatal(
            _(
                "All registered maps of the space time vector "
                "dataset must have time intervals"
            )
        )

    rows = sp.get_registered_maps(
        "name,layer,mapset,start_time,end_time", tempwhere, "start_time", dbif
    )

    if not rows:
        dbif.close()
        gs.fatal(_("Space time vector dataset <%s> is empty") % sp.get_id())

    # Sample the raster dataset with the vector dataset and run v.what.rast
    for row in rows:
        start = row["start_time"]
        end = row["end_time"]
        vectmap = row["name"] + "@" + row["mapset"]
        layer = row["layer"]

        raster_maps = tgis.collect_map_names(strds_sp, dbif, start, end, sampling)

        aggreagated_map_name = None

        if raster_maps:
            # Aggregation
            if method != "disabled" and len(raster_maps) > 1:
                # Generate the temporary map name
                aggreagated_map_name = "aggreagated_map_name_" + str(os.getpid())
                new_map = tgis.aggregate_raster_maps(
                    raster_maps,
                    aggreagated_map_name,
                    start,
                    end,
                    0,
                    method,
                    False,
                    dbif,
                )
                aggreagated_map_name += "_0"
                if new_map is None:
                    continue
                # We overwrite the raster_maps list
                raster_maps = (new_map.get_id(),)

            for rastermap in raster_maps:
                # Create a new column with the SQL compliant
                # name of the sampled raster map if not column
                col_name = column or rastermap.split("@")[0].replace(".", "_")

                coltype = "DOUBLE PRECISION"
                # Get raster type
                rasterinfo = raster.raster_info(rastermap)
                if rasterinfo["datatype"] == "CELL":
                    coltype = "INT"

                try:
                    if layer:
                        gs.run_command(
                            "v.db.addcolumn",
                            map=vectmap,
                            layer=layer,
                            column="%s %s" % (col_name, coltype),
                            overwrite=gs.overwrite(),
                        )
                    else:
                        gs.run_command(
                            "v.db.addcolumn",
                            map=vectmap,
                            column="%s %s" % (col_name, coltype),
                            overwrite=gs.overwrite(),
                        )
                except CalledModuleError:
                    dbif.close()
                    gs.fatal(
                        _("Unable to add column %s to vector map <%s>")
                        % (col_name, vectmap)
                    )

                # Call v.what.rast
                try:
                    if layer:
                        gs.run_command(
                            "v.what.rast",
                            map=vectmap,
                            layer=layer,
                            raster=rastermap,
                            column=col_name,
                            where=where,
                        )
                    else:
                        gs.run_command(
                            "v.what.rast",
                            map=vectmap,
                            raster=rastermap,
                            column=col_name,
                            where=where,
                        )
                except CalledModuleError:
                    dbif.close()
                    gs.fatal(
                        _(
                            "Unable to run v.what.rast for vector map "
                            "<%s> and raster map <%s>"
                        )
                        % (vectmap, rastermap)
                    )

                if aggreagated_map_name:
                    try:
                        gs.run_command(
                            "g.remove",
                            flags="f",
                            type="raster",
                            name=aggreagated_map_name,
                        )
                    except CalledModuleError:
                        dbif.close()
                        gs.fatal(
                            _("Unable to remove raster map <%s>")
                            % (aggreagated_map_name)
                        )

                # Use the first map in case a column names was provided
                if column:
                    break

    dbif.close()


if __name__ == "__main__":
    options, flags = gs.parser()
    main()
