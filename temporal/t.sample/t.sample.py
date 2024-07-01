#!/usr/bin/env python3

############################################################################
#
# MODULE:	t.sample
# AUTHOR(S):	Soeren Gebbert
#
# PURPOSE:	Sample the input space time dataset(s) with a sample space time dataset and print the result to stdout
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
# % description: Samples the input space time dataset(s) with a sample space time dataset and print the result to stdout.
# % keyword: temporal
# % keyword: sampling
# % keyword: time
# %end

# %option G_OPT_STDS_INPUTS
# %end

# %option G_OPT_STDS_INPUT
# % key: sample
# % description: Name of the sample space time dataset
# %end

# %option G_OPT_STDS_TYPE
# % key: intype
# % guisection: Required
# %end

# %option G_OPT_STDS_TYPE
# % key: samtype
# % guisection: Required
# % description: Type of the sample space time dataset
# %end

# %option G_OPT_T_SAMPLE
# % key: method
# % answer: during,overlap,contain,equal
# %end

# %option G_OPT_F_SEP
# % description: Field separator between output columns, default is tabular " | "
# % label: Do not use "," as this char is reserved to list several map ids in a sample granule
# %end

# %flag
# % key: c
# % description: Print the column names as first row
# %end

# %flag
# % key: s
# % description: Check for spatial topological overlap
# %end

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
import grass.script as gs
=======
import grass.script as grass
>>>>>>> 0c13ccda1f (style(temporal): Sort and group imports (#3959))
>>>>>>> 3fa16d2bea (style(temporal): Sort and group imports (#3959))

############################################################################


def main():
    # lazy imports
    import grass.temporal as tgis

    # Get the options
    inputs = options["inputs"]
    sampler = options["sample"]
    samtype = options["samtype"]
    intype = options["intype"]
    separator = gs.separator(options["separator"])
    method = options["method"]
    header = flags["c"]
    spatial = flags["s"]

    # Make sure the temporal database exists
    tgis.init()

    tgis.sample_stds_by_stds_topology(
        intype, samtype, inputs, sampler, header, separator, method, spatial, True
    )


if __name__ == "__main__":
    options, flags = gs.parser()
    main()
