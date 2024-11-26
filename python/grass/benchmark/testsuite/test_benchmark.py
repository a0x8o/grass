# MODULE:    Test of grass.benchmark
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

"""Basic tests of grass.benchmark"""

from pathlib import Path
from subprocess import DEVNULL
from types import SimpleNamespace

from grass.benchmark import (
    benchmark_resolutions,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    benchmark_nprocs,
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
    benchmark_single,
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    benchmark_single,
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> osgeo-main
=======
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> osgeo-main
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    benchmark_single,
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    benchmark_single,
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
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cc3c0468f2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2cf278b2b8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 9c4cb0749b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3f42bae598 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 88accbfbad (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d4bec80a1c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c41f2eb779 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6ce1ce4c0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7aeee7f0e9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> cb7d39cb66 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 73a604b96c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 808f410679 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5fbea63c8d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 28bc5c68cb (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0fd8e61114 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
    benchmark_nprocs,
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
    benchmark_single,
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
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 340827d0ae (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d4bec80a1c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> c41f2eb779 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 6ce1ce4c0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 7aeee7f0e9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> cb7d39cb66 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 73a604b96c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 808f410679 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 5fbea63c8d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 28bc5c68cb (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 0fd8e61114 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2cf278b2b8 (libpython: Support benchmarks of non-parallel runs better (#1733))
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
    benchmark_nprocs,
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
    benchmark_single,
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
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> d4bec80a1c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c41f2eb779 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6ce1ce4c0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 7aeee7f0e9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> cb7d39cb66 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 73a604b96c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 808f410679 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5fbea63c8d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 28bc5c68cb (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0fd8e61114 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2cf278b2b8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
    benchmark_single,
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
    benchmark_single,
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
    benchmark_single,
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
=======
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    benchmark_single,
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
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
=======
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    benchmark_single,
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
    benchmark_single,
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
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    benchmark_single,
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
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 9c4cb0749b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    benchmark_single,
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
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
=======
    benchmark_single,
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    benchmark_single,
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
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
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
=======
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    benchmark_single,
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3f42bae598 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
    benchmark_nprocs,
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    benchmark_single,
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 88accbfbad (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d4bec80a1c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> c41f2eb779 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 6ce1ce4c0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 7aeee7f0e9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> cb7d39cb66 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 73a604b96c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 808f410679 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 5fbea63c8d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 28bc5c68cb (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 0fd8e61114 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 9c4cb0749b (libpython: Support benchmarks of non-parallel runs better (#1733))
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    benchmark_single,
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 9c4cb0749b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    benchmark_single,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 2cf278b2b8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    benchmark_single,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
    join_results,
    load_results,
    load_results_from_file,
    num_cells_plot,
    save_results,
    save_results_to_file,
)
from grass.gunittest.case import TestCase
from grass.gunittest.main import test
from grass.pygrass.modules import Module


class TestBenchmarksRun(TestCase):
    """Tests that functions for benchmarking can run"""

    def test_resolutions(self):
        """Test that resolution tests runs without nprocs and plots to file"""
        benchmarks = [
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b120cf7523 (style: Fixes unnecessary-collection-call (C408) for testsuite (#3947))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b120cf7523 (style: Fixes unnecessary-collection-call (C408) for testsuite (#3947))
>>>>>>> 78d8f1ae80 (style: Fixes unnecessary-collection-call (C408) for testsuite (#3947))
            {
                "module": Module(
                    "r.univar", map="elevation", stdout_=DEVNULL, run_=False
                ),
                "label": "Standard output",
            },
            {
                "module": Module(
<<<<<<< HEAD
                    "r.univar", map="elevation", flags="g", stdout_=DEVNULL, run_=False
                ),
                "label": "Standard output",
            },
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
            dict(
                module=Module("r.univar", map="elevation", stdout_=DEVNULL, run_=False),
                label="Standard output",
            ),
            dict(
                module=Module(
                    "r.univar", map="elevation", flags="g", stdout_=DEVNULL, run_=False
                ),
                label="Standard output",
            ),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                    "r.univar", map="elevation", flags="g", stdout_=DEVNULL, run_=False
                ),
                "label": "Standard output",
            },
>>>>>>> b120cf7523 (style: Fixes unnecessary-collection-call (C408) for testsuite (#3947))
<<<<<<< HEAD
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78d8f1ae80 (style: Fixes unnecessary-collection-call (C408) for testsuite (#3947))
        ]
        resolutions = [300, 200, 100]
        results = []
        for benchmark in benchmarks:
            results.append(
                benchmark_resolutions(
                    **benchmark,
                    resolutions=resolutions,
                )
            )
        plot_file = "test_res_plot.png"
        num_cells_plot(results, filename=plot_file)
        self.assertTrue(Path(plot_file).is_file())

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d4bec80a1c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c41f2eb779 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6ce1ce4c0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7aeee7f0e9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> cb7d39cb66 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 73a604b96c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 808f410679 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5fbea63c8d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 28bc5c68cb (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0fd8e61114 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9c4cb0749b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2cf278b2b8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
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
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
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
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> d4bec80a1c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> c41f2eb779 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6ce1ce4c0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 73a604b96c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 808f410679 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 5fbea63c8d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 28bc5c68cb (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 0fd8e61114 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9c4cb0749b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2cf278b2b8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 824e32212e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3f42bae598 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 88accbfbad (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d4bec80a1c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c41f2eb779 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6ce1ce4c0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 7aeee7f0e9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> cb7d39cb66 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 73a604b96c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 808f410679 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5fbea63c8d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 28bc5c68cb (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0fd8e61114 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 9c4cb0749b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2cf278b2b8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
    def test_single(self):
        """Test that single benchmark function runs"""
        label = "Standard output"
        repeat = 4
        benchmarks = [
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b120cf7523 (style: Fixes unnecessary-collection-call (C408) for testsuite (#3947))
=======
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b120cf7523 (style: Fixes unnecessary-collection-call (C408) for testsuite (#3947))
>>>>>>> 78d8f1ae80 (style: Fixes unnecessary-collection-call (C408) for testsuite (#3947))
            {
                "module": Module(
                    "r.univar", map="elevation", stdout_=DEVNULL, run_=False
                ),
                "label": label,
            }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 78d8f1ae80 (style: Fixes unnecessary-collection-call (C408) for testsuite (#3947))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
            dict(
                module=Module("r.univar", map="elevation", stdout_=DEVNULL, run_=False),
                label=label,
            )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b120cf7523 (style: Fixes unnecessary-collection-call (C408) for testsuite (#3947))
<<<<<<< HEAD
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78d8f1ae80 (style: Fixes unnecessary-collection-call (C408) for testsuite (#3947))
        ]
        results = []
        for benchmark in benchmarks:
            results.append(benchmark_single(**benchmark, repeat=repeat))
        self.assertEqual(len(results), len(benchmarks))
        for result in results:
            self.assertTrue(hasattr(result, "all_times"))
            self.assertTrue(hasattr(result, "time"))
            self.assertTrue(hasattr(result, "label"))
            self.assertEqual(len(result.all_times), repeat)
        self.assertEqual(results[0].label, label)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
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
<<<<<<< HEAD
=======
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d4bec80a1c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> c41f2eb779 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 6ce1ce4c0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 7aeee7f0e9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> cb7d39cb66 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 73a604b96c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 808f410679 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 5fbea63c8d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 28bc5c68cb (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 0fd8e61114 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2cf278b2b8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
    def test_nprocs(self):
        """Test that benchmark function runs for nprocs"""
        label = "Standard output"
        repeat = 4
        benchmarks = [
            {
                "module": Module(
                    "r.univar", map="elevation", stdout_=DEVNULL, run_=False
                ),
                "label": label,
                "max_nprocs": 4,
            }
        ]
        results = []
        for benchmark in benchmarks:
            results.append(benchmark_nprocs(**benchmark, repeat=repeat, shuffle=True))
        self.assertEqual(len(results), len(benchmarks))
        for result in results:
            self.assertTrue(hasattr(result, "times"))
            self.assertTrue(hasattr(result, "all_times"))
            self.assertTrue(hasattr(result, "speedup"))
            self.assertTrue(hasattr(result, "efficiency"))
            self.assertTrue(hasattr(result, "label"))
            self.assertEqual(len(result.all_times), repeat)
        self.assertEqual(results[0].label, label)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d4bec80a1c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c41f2eb779 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6ce1ce4c0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7aeee7f0e9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> cb7d39cb66 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 73a604b96c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 808f410679 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5fbea63c8d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 28bc5c68cb (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0fd8e61114 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2cf278b2b8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 340827d0ae (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
    def test_nprocs(self):
        """Test that benchmark function runs for nprocs"""
        label = "Standard output"
        repeat = 4
        benchmarks = [
            {
                "module": Module(
                    "r.univar", map="elevation", stdout_=DEVNULL, run_=False
                ),
                "label": label,
                "max_nprocs": 4,
            }
        ]
        results = []
        for benchmark in benchmarks:
            results.append(benchmark_nprocs(**benchmark, repeat=repeat, shuffle=True))
        self.assertEqual(len(results), len(benchmarks))
        for result in results:
            self.assertTrue(hasattr(result, "times"))
            self.assertTrue(hasattr(result, "all_times"))
            self.assertTrue(hasattr(result, "speedup"))
            self.assertTrue(hasattr(result, "efficiency"))
            self.assertTrue(hasattr(result, "label"))
            self.assertEqual(len(result.all_times), repeat)
        self.assertEqual(results[0].label, label)

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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
>>>>>>> cc3c0468f2 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
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
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2ba4dbc7e5 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 85e622234d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 7393c080aa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3e81947fcf (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> d4bec80a1c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
    def test_nprocs(self):
        """Test that benchmark function runs for nprocs"""
        label = "Standard output"
        repeat = 4
        benchmarks = [
            {
                "module": Module(
                    "r.univar", map="elevation", stdout_=DEVNULL, run_=False
                ),
                "label": label,
                "max_nprocs": 4,
            }
        ]
        results = []
        for benchmark in benchmarks:
            results.append(benchmark_nprocs(**benchmark, repeat=repeat, shuffle=True))
        self.assertEqual(len(results), len(benchmarks))
        for result in results:
            self.assertTrue(hasattr(result, "times"))
            self.assertTrue(hasattr(result, "all_times"))
            self.assertTrue(hasattr(result, "speedup"))
            self.assertTrue(hasattr(result, "efficiency"))
            self.assertTrue(hasattr(result, "label"))
            self.assertEqual(len(result.all_times), repeat)
        self.assertEqual(results[0].label, label)

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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
>>>>>>> 340827d0ae (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
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
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> dad564ed48 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 256f5d81a6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3f42bae598 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 88accbfbad (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> d4bec80a1c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c41f2eb779 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 6ce1ce4c0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 7aeee7f0e9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> cb7d39cb66 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 73a604b96c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 808f410679 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5fbea63c8d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 28bc5c68cb (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 0fd8e61114 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 9c4cb0749b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 2cf278b2b8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))

class TestBenchmarkResults(TestCase):
    """Tests that saving results work"""

    def test_save_load(self):
        """Test that results can be saved and loaded"""
        resolutions = [300, 200]
        results = [
            benchmark_resolutions(
                module=Module(
                    "r.univar",
                    map="elevation",
                    stdout_=DEVNULL,
                    stderr_=DEVNULL,
                    run_=False,
                ),
                label="Standard output",
                resolutions=resolutions,
            )
        ]
        results = load_results(save_results(results))
        plot_file = "test_res_plot.png"
        num_cells_plot(results.results, filename=plot_file)
        self.assertTrue(Path(plot_file).is_file())

    def test_data_file_roundtrip(self):
        """Test functions can save and load to a file"""
        original = [SimpleNamespace(nprocs=[1, 2, 3], times=[3, 2, 1], label="Test 1")]
        filename = "test_res_file.json"

        save_results_to_file(original, filename)
        self.assertTrue(Path(filename).is_file())

        loaded = load_results_from_file(filename).results
        self.assertEqual(original, loaded)

    def test_join_results_list(self):
        """Test that we can join lists"""
        list_1 = [
            SimpleNamespace(nprocs=[1, 2, 3], times=[3, 2, 1], label="Test 1"),
            SimpleNamespace(nprocs=[1, 2, 3], times=[3, 2, 1], label="Test 2"),
        ]
        list_2 = [SimpleNamespace(nprocs=[1, 2, 3], times=[3, 2, 1], label="Test 3")]
        new_results = join_results([list_1, list_2])
        self.assertEqual(len(new_results), 3)

    def test_join_results_structure(self):
        """Test that we can join a full results structure"""
        list_1 = SimpleNamespace(
            results=[
                SimpleNamespace(nprocs=[1, 2, 3], times=[3, 2, 1], label="Test 1"),
                SimpleNamespace(nprocs=[1, 2, 3], times=[3, 2, 1], label="Test 2"),
            ]
        )
        list_2 = [SimpleNamespace(nprocs=[1, 2, 3], times=[3, 2, 1], label="Test 3")]
        new_results = join_results([list_1, list_2])
        self.assertEqual(len(new_results), 3)


if __name__ == "__main__":
    test()
