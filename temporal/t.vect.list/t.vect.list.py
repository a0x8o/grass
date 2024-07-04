#!/usr/bin/env python3

############################################################################
#
# MODULE:	t.vect.list
# AUTHOR(S):	Soeren Gebbert
#
# PURPOSE:	List registered maps of a space time vector dataset
# COPYRIGHT:	(C) 2011-2017, Soeren Gebbert and the GRASS Development Team
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
# % description: Lists registered maps of a space time vector dataset.
# % keyword: temporal
# % keyword: map management
# % keyword: vector
# % keyword: list
# % keyword: time
# %end

# %option G_OPT_STVDS_INPUT
# %end

# %option
# % key: order
# % type: string
# % description: Sort the space time dataset by category
# % guisection: Formatting
# % required: no
# % multiple: yes
# % options: id,name,layer,creator,mapset,temporal_type,creation_time,start_time,end_time,north,south,west,east,points,lines,boundaries,centroids,faces,kernels,primitives,nodes,areas,islands,holes,volumes
# % answer: start_time
# %end

# %option
# % key: columns
# % type: string
# % description: Columns to be printed to stdout
# % guisection: Selection
# % required: no
# % multiple: yes
# % options: id,name,layer,creator,mapset,temporal_type,creation_time,start_time,end_time,north,south,west,east,points,lines,boundaries,centroids,faces,kernels,primitives,nodes,areas,islands,holes,volumes
# % answer: name,layer,mapset,start_time,end_time
# %end

# %option G_OPT_T_WHERE
# % guisection: Selection
# %end

# %option
# % key: method
# % type: string
# % description: Method used for data listing
# % required: no
# % multiple: no
# % options: cols,comma,delta,deltagaps,gran
# % answer: cols
# %end

# %option G_OPT_F_SEP
# % label: Field separator character between the output columns
# % guisection: Formatting
# %end

# %option G_OPT_F_OUTPUT
# % required: no
# %end

# %flag
# % key: u
# % description: Suppress printing of column names
# % guisection: Formatting
# %end

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

############################################################################


def main():
    # lazy imports
    import grass.temporal as tgis

    # Get the options
    input = options["input"]
    columns = options["columns"]
    order = options["order"]
    where = options["where"]
    separator = gs.separator(options["separator"])
    method = options["method"]
    header = flags["u"]
    output = options["output"]

    # Make sure the temporal database exists
    tgis.init()

    tgis.list_maps_of_stds(
        "stvds", input, columns, order, where, separator, method, header, outpath=output
    )


if __name__ == "__main__":
    options, flags = gs.parser()
    main()
