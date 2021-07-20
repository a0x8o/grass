# MODULE:    grass.benchmark
#
# AUTHOR(S): Vaclav Petras <wenzeslaus gmail com>
#
# PURPOSE:   Benchmarking for GRASS GIS modules
#
# COPYRIGHT: (C) 2021 Vaclav Petras, and by the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.


"""CLI for the benchmark package"""

import argparse
import sys
from pathlib import Path

from grass.benchmark import (
    join_results_from_files,
    load_results_from_file,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    nprocs_plot,
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    nprocs_plot,
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    nprocs_plot,
=======
>>>>>>> osgeo-main
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
    nprocs_plot,
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
    nprocs_plot,
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    nprocs_plot,
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> osgeo-main
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
    nprocs_plot,
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
=======
<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
    nprocs_plot,
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    nprocs_plot,
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> osgeo-main
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
<<<<<<< HEAD
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    nprocs_plot,
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
    nprocs_plot,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    nprocs_plot,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
    num_cells_plot,
    save_results_to_file,
)


class CliUsageError(ValueError):
    """Raised when error is in the command line arguments.

    Used when the error is discovered only after argparse parsed the arguments.
    """

    # ArgumentError from argparse may work too, but it is not documented and
    # takes a reference argument which we don't have access to after the parse step.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> osgeo-main
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
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
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
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
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> osgeo-main
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    pass
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))


def join_results_cli(args):
    """Translate CLI parser result to API calls."""
    if args.prefixes and len(args.results) != len(args.prefixes):
        raise CliUsageError(
            f"Number of prefixes ({len(args.prefixes)}) needs to be the same"
            f" as the number of input result files ({len(args.results)})"
        )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> osgeo-main
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))

    def select_only(result):
        return result.label == args.only

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    select_function = select_only if args.only else None
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    select_function = select_only if args.only else None
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
    select_function = select_only if args.only else None
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
    select_function = select_only if args.only else None
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    if args.only:
        select_function = select_only
    else:
        select_function = None

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> osgeo-main
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> osgeo-main
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> osgeo-main
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
>>>>>>> 340827d0ae (Merge branch 'a0x8o' into stag0)
        metric=args.metric,
    )


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
    )


>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
        select=select_function,
        prefixes_as_labels=args.re_label,
    )

    save_results_to_file(results, args.output)


<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
def plot_nprocs_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    nprocs_plot(
        results.results,
        filename=args.output,
        title=args.title,
    )


>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    results = join_results_from_files(
        source_filenames=args.results,
        prefixes=args.prefixes,
    )
    save_results_to_file(results, args.output)


>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
def plot_cells_cli(args):
    """Translate CLI parser result to API calls."""
    results = load_results_from_file(args.input)
    num_cells_plot(
        results.results,
        filename=args.output,
        title=args.title,
        show_resolution=args.resolutions,
    )


def get_executable_name():
    """Get name of the executable and module.

    This is a workaround for Python issue:
    argparse support for "python -m module" in help
    https://bugs.python.org/issue22240
    """
    executable = Path(sys.executable).stem
    return f"{executable} -m grass.benchmark"


class ExtendAction(argparse.Action):
    """Support for agrparse action="extend" before Python 3.8

    Each parser instance needs the action to be registered.
    """

    # pylint: disable=too-few-public-methods
    def __call__(self, parser, namespace, values, option_string=None):
        items = getattr(namespace, self.dest) or []
        items.extend(values)
        setattr(namespace, self.dest, items)


def add_subcommand_parser(subparsers, name, description):
    """Add parser for a subcommand into subparsers."""
    # help is in parent's help, description in subcommand's help.
    return subparsers.add_parser(name, help=description, description=description)


def add_subparsers(parser, dest):
    """Add subparsers in a unified way.

    Uses title 'subcommands' for the list of commands
    (instead of the 'positional' which is the default).

    The *dest* should be 'command', 'subcommand', etc. with appropriate nesting.
    """
    if sys.version_info < (3, 7):
        # required as parameter is only in >=3.7.
        return parser.add_subparsers(title="subcommands", dest=dest)
    return parser.add_subparsers(title="subcommands", required=True, dest=dest)


def add_results_subcommand(parent_subparsers):
    """Add results subcommand."""
    main_parser = add_subcommand_parser(
        parent_subparsers, "results", description="Manipulate results"
    )
    main_subparsers = add_subparsers(main_parser, dest="subcommand")

    join = main_subparsers.add_parser("join", help="Join results")
    join.add_argument("results", help="Files with results", nargs="*", metavar="file")
    join.add_argument("output", help="Output file", metavar="output_file")
    if sys.version_info < (3, 8):
        join.register("action", "extend", ExtendAction)
    join.add_argument(
        "--prefixes",
        help="Add prefixes to result labels per file",
        action="extend",
        nargs="*",
        metavar="text",
    )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> osgeo-main
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
    join.add_argument(
        "--only",
        help="Select only results with matching label",
        metavar="label",
    )
    join.add_argument(
        "--re-label",
        help="Use prefixes as the new labels",
        action="store_true",
    )
    join.set_defaults(handler=join_results_cli)


def add_plot_io_arguments(parser):
    """Add input and output arguments to *parser*."""
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 340827d0ae (Merge branch 'a0x8o' into stag0)
    parser.add_argument(
        "input", help="file with results (e.g. results.json)", metavar="input_file"
    )
    parser.add_argument(
        "output",
        help=(
            "output file with extension (e.g., figure.png)."
            " If not provided, the plot will be opened in a new window."
        ),
        nargs="?",
        metavar="output_file",
=======
    parser.add_argument("input", help="file with results (JSON)", metavar="input_file")
    parser.add_argument(
        "output", help="output file (e.g., PNG)", nargs="?", metavar="output_file"
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
    parser.add_argument("input", help="file with results (JSON)", metavar="input_file")
    parser.add_argument(
        "output", help="output file (e.g., PNG)", nargs="?", metavar="output_file"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 340827d0ae (Merge branch 'a0x8o' into stag0)
=======
    parser.add_argument(
        "input", help="file with results (e.g. results.json)", metavar="input_file"
    )
    parser.add_argument(
        "output",
        help=(
            "output file with extension (e.g., figure.png)."
            " If not provided, the plot will be opened in a new window."
        ),
        nargs="?",
        metavar="output_file",
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 340827d0ae (Merge branch 'a0x8o' into stag0)
    )


def add_plot_title_argument(parser):
    """Add title argument to *parser*."""
    parser.add_argument(
        "--title",
        help="Title for the plot",
        metavar="text",
    )


<<<<<<< HEAD
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
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
    join.set_defaults(handler=join_results_cli)


>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
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
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
def add_plot_metric_argument(parser):
    """Add metric argument to *parser*."""
    parser.add_argument(
        "--metric",
        help="Metric for the plot (default: time)",
        default="time",
        choices=["time", "speedup", "efficiency"],
    )


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
=======
=======
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
    join.set_defaults(handler=join_results_cli)


>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
    join.set_defaults(handler=join_results_cli)


>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
    join.set_defaults(handler=join_results_cli)


>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
def add_plot_metric_argument(parser):
    """Add metric argument to *parser*."""
    parser.add_argument(
        "--metric",
        help="Metric for the plot (default: time)",
        default="time",
        choices=["time", "speedup", "efficiency"],
    )


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
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
>>>>>>> cc3c0468f2 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
    join.set_defaults(handler=join_results_cli)


>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
    join.set_defaults(handler=join_results_cli)


>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
def add_plot_metric_argument(parser):
    """Add metric argument to *parser*."""
    parser.add_argument(
        "--metric",
        help="Metric for the plot (default: time)",
        default="time",
        choices=["time", "speedup", "efficiency"],
    )


<<<<<<< HEAD
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
>>>>>>> 340827d0ae (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
    join.set_defaults(handler=join_results_cli)


>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
def add_plot_subcommand(parent_subparsers):
    """Add plot subcommand."""
    main_parser = add_subcommand_parser(
        parent_subparsers, "plot", description="Plot results"
    )
    main_subparsers = add_subparsers(main_parser, dest="subcommand")

    join = main_subparsers.add_parser("cells", help="Plot for variable number of cells")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> osgeo-main
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
<<<<<<< HEAD
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
<<<<<<< HEAD
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> osgeo-main
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> osgeo-main
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
    join.add_argument("input", help="file with results (JSON)", metavar="input_file")
    join.add_argument(
        "output", help="output file (e.g., PNG)", nargs="?", metavar="output_file"
    )
    join.add_argument(
        "--title",
        help="Title for the plot",
        metavar="text",
    )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> osgeo-main
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
    add_plot_io_arguments(join)
    add_plot_title_argument(join)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
    join.add_argument(
        "--resolutions",
        help="Use resolutions for x axis instead of cell count",
        action="store_true",
    )
    join.set_defaults(handler=plot_cells_cli)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> osgeo-main
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
    nprocs = main_subparsers.add_parser(
        "nprocs", help="Plot for variable number of processing elements"
    )
    add_plot_io_arguments(nprocs)
    add_plot_title_argument(nprocs)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
>>>>>>> 340827d0ae (Merge branch 'a0x8o' into stag0)
    add_plot_metric_argument(nprocs)
    nprocs.set_defaults(handler=plot_nprocs_cli)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> main
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
    nprocs.set_defaults(handler=plot_nprocs_cli)

>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
    nprocs.set_defaults(handler=plot_nprocs_cli)

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 89623f244e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0f77eb70a6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 383842366e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 01d8181620 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b5b02a4bab (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 885cbae99b (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> da97348a02 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b661c10652 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5bdb91a7d7 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 0221192d22 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 99dbae4f6d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    nprocs.set_defaults(handler=plot_nprocs_cli)

>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
    nprocs.set_defaults(handler=plot_nprocs_cli)

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> cf2f0afab7 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5c1ab471ac (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))

def define_arguments():
    """Define top level parser and create subparsers."""
    parser = argparse.ArgumentParser(
        description="Process results from module benchmarks.",
        prog=get_executable_name(),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 340827d0ae (Merge branch 'a0x8o' into stag0)
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
=======
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
>>>>>>> 340827d0ae (Merge branch 'a0x8o' into stag0)
    )
    subparsers = add_subparsers(parser, dest="command")

    add_results_subcommand(subparsers)
    add_plot_subcommand(subparsers)

    return parser


def main(args=None):
    """Define and parse command line parameters then run the appropriate handler."""
    parser = define_arguments()
    args = parser.parse_args(args)
    try:
        args.handler(args)
    except CliUsageError as error:
        # Report a usage error and exit.
        sys.exit(f"ERROR: {error}")


if __name__ == "__main__":
    main()
