#!/usr/bin/env python3

############################################################################
#
# MODULE:	t.vect.univar
# AUTHOR(S):	Soeren Gebbert
#
# PURPOSE:	Calculates univariate statistics of attributes for each registered vector map of a space time vector dataset
# COPYRIGHT:	(C) 2011-2017 by the GRASS Development Team
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
# % description: Calculates univariate statistics of attributes for each registered vector map of a space time vector dataset
# % keyword: temporal
# % keyword: statistics
# % keyword: vector
# % keyword: time
# %end

# %option G_OPT_STVDS_INPUT
# %end

# %option G_OPT_F_OUTPUT
# % required: no
# %end

# %option G_OPT_V_FIELD
# %end

# %option G_OPT_DB_COLUMN
# % required: yes
# %end

# %option G_OPT_T_WHERE
# % guisection: Selection
# % key: twhere
# %end

# %option G_OPT_DB_WHERE
# % guisection: Selection
# %end

# %option G_OPT_V_TYPE
# % options: point,line,boundary,centroid,area
# % multiple: no
# % answer: point
# %end

# %option G_OPT_F_SEP
# % label: Field separator character between the output columns
# % guisection: Formatting
# %end

# %flag
# % key: e
# % description: Calculate extended statistics
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
    output = options["output"]
    twhere = options["twhere"]
    layer = options["layer"]
    type = options["type"]
    column = options["column"]
    where = options["where"]
    extended = flags["e"]
    header = flags["u"]
    separator = gs.separator(options["separator"])

    # Make sure the temporal database exists
    tgis.init()

    if not output:
        output = None
    if output == "-":
        output = None

    tgis.print_vector_dataset_univar_statistics(
        input, output, twhere, layer, type, column, where, extended, header, separator
    )


if __name__ == "__main__":
    options, flags = gs.parser()
    main()
