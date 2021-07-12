# MODULE:    grass.benchmark
#
# AUTHOR(S): Aaron Saw Min Sern <aaronsms u nus edu>
#            Vaclav Petras <wenzeslaus gmail com>
#
# PURPOSE:   Benchmarking for GRASS GIS modules
#
# COPYRIGHT: (C) 2021 Vaclav Petras, and by the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.


"""Basic functions for benchmarking modules"""

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
import random
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import random
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
import random
=======
>>>>>>> osgeo-main
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
import random
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
import random
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import random
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
import random
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
import random
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
=======
import random
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
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
import random
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
import random
=======
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
import random
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
import random
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
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
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
import random
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
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
import random
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
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
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
import random
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
=======
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
import random
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
import random
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
import random
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
import random
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
import shutil
from types import SimpleNamespace

import grass.script as gs


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
def benchmark_single(module, label, repeat=5):
    """Benchmark module as is without chaning anything.
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
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
def benchmark_single(module, label, repeat=5):
    """Benchmark module as is without chaning anything.
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
<<<<<<< HEAD
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
def benchmark_single(module, label, repeat=5):
    """Benchmark module as is without changing anything.
=======
def benchmark_single(module, label, repeat=5):
    """Benchmark module as is without chaning anything.
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
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
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
def benchmark_single(module, label, repeat=5):
    """Benchmark module as is without chaning anything.
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
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
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
def benchmark_single(module, label, repeat=5):
    """Benchmark module as is without chaning anything.
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
def benchmark_single(module, label, repeat=5):
    """Benchmark module as is without chaning anything.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
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
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))

    *module* is an instance of PyGRASS Module class or any object which
    has a *run* method which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    *repeat* sets how many times the each run is repeated.
    *label* is a text to add to the result (for user-facing display).

    Returns an object with attributes *time* (an average execution time),
    *all_times* (list of measured execution times),
    and *label* (the provided parameter as is).
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")

    print("\u2500" * term_size.columns)
    time_sum = 0
    measured_times = []
    for _ in range(repeat):
        module.run()
        print(f"{module.time}s")
        time_sum += module.time
        measured_times.append(module.time)

    avg = time_sum / repeat
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    min_avg = min(avg, min_avg)
=======
    if avg < min_avg:
        min_avg = avg
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    if avg < min_avg:
        min_avg = avg
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    min_avg = min(avg, min_avg)
>>>>>>> e9b8764134 (style: Fixes if-stmt-min-max (PLR1730) (#3950))
    print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
    print(f"Best average time - {min_avg}s\n")

    return SimpleNamespace(
        all_times=measured_times,
        time=avg,
        label=label,
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
def benchmark_nprocs(module, label, max_nprocs, repeat=5, shuffle=True):
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
    Runs are executed in random order, set *shuffle* to false if they
    need to be executed in order based on number of threads.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
def benchmark_nprocs(module, label, max_nprocs, repeat):
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
=======
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
def benchmark_nprocs(module, label, max_nprocs, repeat):
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class.
    The module is executed  used to generate range of values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))

    *label* is a text to add to the result (for user-facing display).
    Optional *nprocs* is passed to the module if present.

    Returns an object with attributes *times* (list of average execution times),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
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
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
    result = SimpleNamespace(times=[], all_times=[], speedup=[], efficiency=[])
    result.nprocs = list(range(1, max_nprocs + 1))
    result.label = label
    nprocs_list_shuffled = sorted(result.nprocs * repeat)
<<<<<<< HEAD
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
        avg_times.append(avg)
        all_times.append(times[nprocs])
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
<<<<<<< HEAD
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
        result.times.append(avg)
        result.all_times.append(times[nprocs])
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
        avg_times.append(avg)
        all_times.append(times[nprocs])
<<<<<<< HEAD
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
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
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
        avg_times.append(avg)
        all_times.append(times[nprocs])
<<<<<<< HEAD
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
        avg_times.append(avg)
        all_times.append(times[nprocs])
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
=======
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
        avg_times.append(avg)
<<<<<<< HEAD
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        all_times.append(times[nprocs])
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
        avg_times.append(avg)
        all_times.append(times[nprocs])
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        all_times.append(times[nprocs])
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
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
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        all_times.append(times[nprocs])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
>>>>>>> cc3c0468f2 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
        avg_times.append(avg)
        all_times.append(times[nprocs])
<<<<<<< HEAD
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
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
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
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
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
        avg_times.append(avg)
        all_times.append(times[nprocs])
<<<<<<< HEAD
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
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
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
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
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
        avg_times.append(avg)
        all_times.append(times[nprocs])
<<<<<<< HEAD
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
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
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
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
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
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
=======
<<<<<<< HEAD
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
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
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
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
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
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
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
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
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
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
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
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
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
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
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
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
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
        avg_times.append(avg)
        all_times.append(times[nprocs])
<<<<<<< HEAD
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
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
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
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
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
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
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
        avg_times.append(avg)
        all_times.append(times[nprocs])
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
    """
    term_size = shutil.get_terminal_size()
    print(module.get_bash())

    min_avg = float("inf")
    min_time = 1
    avg_times = []
    all_times = []
    nprocs_list = list(range(1, max_nprocs + 1))
    for nprocs in nprocs_list:
        print("\u2500" * term_size.columns)
        print(f"Benchmark with {nprocs} thread(s)...\n")
        time_sum = 0
        measured_times = []
        for _ in range(repeat):
            module(nprocs=nprocs).run()
            print(f"{module.time}s")
            time_sum += module.time
            measured_times.append(module.time)

        avg = time_sum / repeat
<<<<<<< HEAD
=======
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
        avg_times.append(avg)
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
        if nprocs == 1:
            serial_avg = avg
        if avg < min_avg:
            min_avg = avg
            min_time = nprocs
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
        efficiency.append(serial_avg / (nprocs * avg))
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
=======
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
=======
<<<<<<< HEAD
>>>>>>> cc3c0468f2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
<<<<<<< HEAD
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
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
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))

    print("\u2500" * term_size.columns)
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))

    print("\u2500" * term_size.columns)
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
=======
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
=======
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> main
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
>>>>>>> osgeo-main
>>>>>>> main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
    return SimpleNamespace(
        all_times=all_times,
        times=avg_times,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> main
<<<<<<< HEAD
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
        efficiency=efficiency,
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        efficiency=efficiency,
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
        efficiency=efficiency,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        efficiency=efficiency,
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
        nprocs=nprocs_list,
        label=label,
    )
=======
    return result
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
    return SimpleNamespace(
        all_times=all_times,
        times=avg_times,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
        efficiency=efficiency,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
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
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
        nprocs=nprocs_list,
        label=label,
    )
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
        nprocs=nprocs_list,
        label=label,
    )
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
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
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
        print(f"\nResult - {avg}s")
=======
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))

    print("\u2500" * term_size.columns)
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
<<<<<<< HEAD
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
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
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
    return SimpleNamespace(
        all_times=all_times,
        times=avg_times,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
        efficiency=efficiency,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        nprocs=nprocs_list,
        label=label,
    )
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    return result
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
>>>>>>> effa23168e (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
<<<<<<< HEAD
>>>>>>> cc3c0468f2 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
    return SimpleNamespace(
        all_times=all_times,
        times=avg_times,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
        efficiency=efficiency,
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
        nprocs=nprocs_list,
        label=label,
    )
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
        nprocs=nprocs_list,
        label=label,
    )
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> osgeo-main
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
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
    print(f"\nSerial average time - {serial_avg}s")
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

    return SimpleNamespace(
        all_times=all_times,
        times=avg_times,
        nprocs=nprocs_list,
        label=label,
    )
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))


def benchmark_resolutions(module, resolutions, label, repeat=5, nprocs=None):
    """Benchmark module using different resolutions.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8d4a4cbf97 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 11243252e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ad14dca817 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c68c553712 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2ba6ea4638 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d2deec5b99 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 62d0febf95 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> e9d37a972c (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fdbfa0cdb6 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 18cf7b413d (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f2a5fffa6c (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb51144890 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6e4511d349 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d047b12a28 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd9ee76548 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ca553cee6d (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> defcd4d416 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aa770628e6 (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> 84b0de4a0b (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8d4a4cbf97 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 11243252e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 252e8801e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> ad14dca817 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 7b6920a07b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> c68c553712 (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 92d65cd4a6 (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 84b0de4a0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> f75642e9e3 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
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
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 2ba6ea4638 (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 5eabce4769 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> d2deec5b99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 799750b257 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 62d0febf95 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
<<<<<<< HEAD
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> b4ca4c9a56 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> e9d37a972c (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 4f7a1fd8f9 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> fdbfa0cdb6 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> c428d906c4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 18cf7b413d (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> de793b6ebf (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> f2a5fffa6c (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 7f529ced08 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> fb51144890 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 0110f9a6c3 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 6e4511d349 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 790e05082d (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> d047b12a28 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> aa770628e6 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> dd9ee76548 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> c0f0b4ecd0 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> ca553cee6d (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> aa257e5504 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> defcd4d416 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
    *module* is an instance of PyGRASS Module class or any object
    with attributes as specified in :func:`benchmark_nprocs`
    except that the *update* method is required only when *nprocs* is set.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> aa770628e6 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> 84b0de4a0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 11243252e9 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d4a4cbf97 (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> ad14dca817 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7b6920a07b (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> c68c553712 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> 2ba6ea4638 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5eabce4769 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> d2deec5b99 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 799750b257 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> 62d0febf95 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b4ca4c9a56 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> e9d37a972c (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f7a1fd8f9 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> fdbfa0cdb6 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c428d906c4 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> 18cf7b413d (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de793b6ebf (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> f2a5fffa6c (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f529ced08 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> fb51144890 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0110f9a6c3 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> 6e4511d349 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 790e05082d (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> d047b12a28 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c0f0b4ecd0 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> ca553cee6d (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aa257e5504 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> defcd4d416 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8d4a4cbf97 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 11243252e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 252e8801e9 (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> ad14dca817 (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 7b6920a07b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> c68c553712 (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 92d65cd4a6 (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 84b0de4a0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> f75642e9e3 (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 2ba6ea4638 (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 5eabce4769 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> d2deec5b99 (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 799750b257 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 62d0febf95 (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> osgeo-main
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> b4ca4c9a56 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> e9d37a972c (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 4f7a1fd8f9 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> fdbfa0cdb6 (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> c428d906c4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 18cf7b413d (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> de793b6ebf (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> f2a5fffa6c (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 7f529ced08 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> fb51144890 (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 0110f9a6c3 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 6e4511d349 (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 790e05082d (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> d047b12a28 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> aa770628e6 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> dd9ee76548 (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> c0f0b4ecd0 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> ca553cee6d (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> aa257e5504 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> defcd4d416 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
    *resolutions* is a list of resolutions to set (current region is currently
    used and changed but that may change in the future).
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``len(resolutions) * repeat`` times.

    *label* is a text to add to the result (for user-facing display).
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
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
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
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
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
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
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
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
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
=======
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
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
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
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
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
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
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
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
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
<<<<<<< HEAD
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))

    Returns an object with attributes *times* (list of average execution times),
    *all_times* (list of lists of measured execution times), *resolutions*
    (the provided parameter as is), *cells* (number of cells in the region),
    and *label* (the provided parameter as is).
    """
    term_size = shutil.get_terminal_size()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
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
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
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
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 86d855a90b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 547913387f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9deecba858 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> aada9378f8 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1b9dd510b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> de0e6aa50e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
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
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
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
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
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
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
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
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
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
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    print(module.get_bash())
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
    print(module.get_bash())
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
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
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> osgeo-main
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> da95805ca1 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 63045de622 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2a88dad128 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> fb1415d5b7 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> bcd8260293 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 5a369c18ab (libpython: Support benchmarks of non-parallel runs better (#1733))
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
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 58f65d161b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 8e09c28a9a (libpython: Support benchmarks of non-parallel runs better (#1733))
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
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 196a20892e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ff508b1907 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2e712c25e8 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 479bcc2525 (libpython: Support benchmarks of non-parallel runs better (#1733))
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
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 84a0683221 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a5bc7458b9 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
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
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    print(module.get_bash())
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    print(module.get_bash())
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))

    avg_times = []
    all_times = []
    n_cells = []
    for resolution in resolutions:
        gs.run_command("g.region", res=resolution)
        region = gs.region()
        n_cells.append(region["cells"])
        print("\u2500" * term_size.columns)
        print(f"Benchmark with {resolution} resolution...\n")
        time_sum = 0
        measured_times = []
        for _ in range(repeat):
            if nprocs:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8d4a4cbf97 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 252e8801e9 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ad14dca817 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c68c553712 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 92d65cd4a6 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f75642e9e3 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2ba6ea4638 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d2deec5b99 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 62d0febf95 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> e9d37a972c (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fdbfa0cdb6 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 18cf7b413d (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f2a5fffa6c (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb51144890 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6e4511d349 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d047b12a28 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ca553cee6d (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> defcd4d416 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aa770628e6 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dd9ee76548 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 11243252e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 252e8801e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
=======
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
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> ad14dca817 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> 7b6920a07b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> c68c553712 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
                module.update(nprocs=nprocs)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                module.update(nprocs=nprocs)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
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
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
                module.update(nprocs=nprocs)
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
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
                module.update(nprocs=nprocs)
=======
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 84b0de4a0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 2ba6ea4638 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
                module.update(nprocs=nprocs)
=======
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
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
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2ba6ea4638 (pygrass: Add update parameters method to Module (#1712))
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
                module.update(nprocs=nprocs)
=======
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
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
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 5eabce4769 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> d2deec5b99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> 799750b257 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 62d0febf95 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> b4ca4c9a56 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> e9d37a972c (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> 4f7a1fd8f9 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> fdbfa0cdb6 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> c428d906c4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 18cf7b413d (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> de793b6ebf (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> f2a5fffa6c (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> 7f529ced08 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> fb51144890 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> 0110f9a6c3 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 6e4511d349 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
>>>>>>> 790e05082d (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> d047b12a28 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> c0f0b4ecd0 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> ca553cee6d (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> aa257e5504 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> defcd4d416 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
                module.update(nprocs=nprocs)
=======
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d2deec5b99 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 62d0febf95 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> e9d37a972c (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fdbfa0cdb6 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 18cf7b413d (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f2a5fffa6c (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb51144890 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6e4511d349 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d047b12a28 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ca553cee6d (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> defcd4d416 (pygrass: Add update parameters method to Module (#1712))
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8d4a4cbf97 (pygrass: Add update parameters method to Module (#1712))
=======
=======
                module.update(nprocs=nprocs)
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
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 11243252e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
                module.update(nprocs=nprocs)
=======
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 252e8801e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
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
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> ad14dca817 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 7b6920a07b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> c68c553712 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 92d65cd4a6 (pygrass: Add update parameters method to Module (#1712))
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
                module.update(nprocs=nprocs)
=======
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 84b0de4a0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> f75642e9e3 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
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
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 2ba6ea4638 (pygrass: Add update parameters method to Module (#1712))
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
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 5eabce4769 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> d2deec5b99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 799750b257 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 62d0febf95 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
<<<<<<< HEAD
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> b4ca4c9a56 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> e9d37a972c (pygrass: Add update parameters method to Module (#1712))
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
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 4f7a1fd8f9 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> fdbfa0cdb6 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> c428d906c4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 18cf7b413d (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> de793b6ebf (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> f2a5fffa6c (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 7f529ced08 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> fb51144890 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 0110f9a6c3 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 6e4511d349 (pygrass: Add update parameters method to Module (#1712))
=======
=======
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
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 790e05082d (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> d047b12a28 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> aa770628e6 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> dd9ee76548 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> c0f0b4ecd0 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> ca553cee6d (pygrass: Add update parameters method to Module (#1712))
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
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> aa257e5504 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> defcd4d416 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
                module.update(nprocs=nprocs)
=======
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
=======
                module.update(nprocs=nprocs)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
            module.run()
            print(f"{module.time}s")
            time_sum += module.time
            measured_times.append(module.time)

        avg = time_sum / repeat
        avg_times.append(avg)
        all_times.append(measured_times)
        print(f"\nResult - {avg}s")

    return SimpleNamespace(
        all_times=all_times,
        times=avg_times,
        resolutions=resolutions,
        cells=n_cells,
        label=label,
    )
