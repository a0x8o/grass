"""
Univariate statistic function for space time datasets

Usage:

.. code-block:: python

    import grass.temporal as tgis

    tgis.print_gridded_dataset_univar_statistics(
        type, input, output, where, extended, no_header, fs, rast_region
    )

..

(C) 2012-2024 by the GRASS Development Team
This program is free software under the GNU General Public
License (>=v2). Read the file COPYING that comes with GRASS
for details.

:authors: Soeren Gebbert
"""
<<<<<<< HEAD

from multiprocessing import Pool
from subprocess import PIPE

import grass.script as gs
from grass.pygrass.modules import Module
=======
from __future__ import print_function
from multiprocessing import Pool
from subprocess import PIPE
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
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
=======
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))

from .core import SQLDatabaseInterfaceConnection, get_current_mapset
from .factory import dataset_factory
from .open_stds import open_old_stds
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import grass.script as gs
from grass.pygrass.modules import Module
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
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
import grass.script as gs
from grass.pygrass.modules import Module
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
import grass.script as gs
from grass.pygrass.modules import Module
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
import grass.script as gs
from grass.pygrass.modules import Module
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
import grass.script as gs
from grass.pygrass.modules import Module
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
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
import grass.script as gs
from grass.pygrass.modules import Module
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
import grass.script as gs
from grass.pygrass.modules import Module
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
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
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
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
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
import grass.script as gs
from grass.pygrass.modules import Module
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
import grass.script as gs
from grass.pygrass.modules import Module
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))

###############################################################################


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def compute_univar_stats(
    registered_map_info, stats_module, fs, rast_region: bool = False
=======
def compute_univar_stats(registered_map_info, stats_module, fs, rast_region=False):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
def compute_univar_stats(registered_map_info, stats_module, fs, rast_region=False):
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
def compute_univar_stats(
    registered_map_info, stats_module, fs, rast_region: bool = False
=======
def compute_univar_stats(registered_map_info, stats_module, fs, rast_region=False):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
def compute_univar_stats(registered_map_info, stats_module, fs, rast_region=False):
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
    """Compute univariate statistics for a map of a space time raster or raster3d
    dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics
                        with
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
    :param fs: Field separator
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    """
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}'
            if stats_module.inputs.percentile:
                for perc in stats_module.inputs.percentile:
                    perc_value = stats[
                        "percentile_"
                        f"{str(perc).rstrip('0').rstrip('.').replace('.','_')}"
                    ]
                    string += f"{fs}{perc_value}"
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
):
=======
def compute_univar_stats(registered_map_info, stats_module, fs, rast_region=False):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d
    dataset

<<<<<<< HEAD
    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics
                        with
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
<<<<<<< HEAD
<<<<<<< HEAD
    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region and (stats_module.inputs.zones or stats_module.name == "r3.univar"):
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}'
            if stats_module.inputs.percentile:
                for perc in stats_module.inputs.percentile:
                    perc_value = stats[
                        "percentile_"
                        f"{str(perc).rstrip('0').rstrip('.').replace('.','_')}"
                    ]
                    string += f"{fs}{perc_value}"
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
):
=======
def compute_univar_stats(registered_map_info, stats_module, fs, rast_region=False):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
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
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d
    dataset

<<<<<<< HEAD
    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics
                        with
=======
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
>>>>>>> osgeo-main
=======
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
>>>>>>> osgeo-main
=======
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region and (stats_module.inputs.zones or stats_module.name == "r3.univar"):
<<<<<<< HEAD
=======
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _("Unable to get statistics for raster map <%s>") % id
            if stats_module.name == "r.univar"
            else _("Unable to get statistics for 3d raster map <%s>") % id
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}'
            if stats_module.inputs.percentile:
                for perc in stats_module.inputs.percentile:
                    perc_value = stats[
                        "percentile_"
                        f"{str(perc).rstrip('0').rstrip('.').replace('.','_')}"
                    ]
                    string += f"{fs}{perc_value}"
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}'
            if stats_module.inputs.percentile:
                for perc in stats_module.inputs.percentile:
                    perc_value = stats[
                        "percentile_"
                        f"{str(perc).rstrip('0').rstrip('.').replace('.','_')}"
                    ]
                    string += f"{fs}{perc_value}"
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
<<<<<<< HEAD
>>>>>>> osgeo-main
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
<<<<<<< HEAD
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
=======
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
    """Compute univariate statistics for a map of a space time raster or raster3d
    dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics
                        with
=======
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
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
    """Compute univariate statistics for a map of a space time raster or raster3d dataset

    :param registered_map_info: dict or db row with tgis info for a registered map
    :param stats_module: Pre-configured PyGRASS Module to compute univariate statistics with
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
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
=======
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
<<<<<<< HEAD
<<<<<<< HEAD
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
=======
>>>>>>> osgeo-main
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
=======
>>>>>>> osgeo-main
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
<<<<<<< HEAD
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
=======
>>>>>>> osgeo-main
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
<<<<<<< HEAD
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
<<<<<<< HEAD
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
            string += f'{fs}{stats["third_quartile"]}{fs}{stats["percentile_90"]}'
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header=False,
    fs="|",
    rast_region=False,
    zones=None,
    nprocs=1,
):
    """Print univariate statistics for a space time raster or raster3d dataset

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
           Only available for strds.
    :param zones: raster map with zones to calculate statistics for
    """
<<<<<<< HEAD
    string = ""
    id = registered_map_info["id"]
    start = registered_map_info["start_time"]
    end = registered_map_info["end_time"]
    semantic_label = (
        ""
        if stats_module.name == "r3.univar" or not registered_map_info["semantic_label"]
        else registered_map_info["semantic_label"]
    )

    stats_module.inputs.map = id
    if rast_region:
        stats_module.env = gs.region_env(raster=id)
    stats_module.run()

    univar_stats = stats_module.outputs.stdout

    if not univar_stats:
        gs.warning(
            _(
                "Unable to get statistics for {voxel}raster map "
                "<{rmap}>".format(
                    rmap=id, voxel="" if stats_module.name == "r.univar" else "3d "
                )
            )
        )
        return None
    eol = ""

    for idx, stats_kv in enumerate(univar_stats.split(";")):
        stats = gs.utils.parse_key_val(stats_kv)
        string += (
            f"{id}{fs}{semantic_label}{fs}{start}{fs}{end}"
            if stats_module.name == "r.univar"
            else f"{id}{fs}{start}{fs}{end}"
        )
        if stats_module.inputs.zones:
            if idx == 0:
                zone = str(stats["zone"])
                string = ""
                continue
            string += f"{fs}{zone}"
            if "zone" in stats:
                zone = str(stats["zone"])
                eol = "\n"
            else:
                eol = ""
        string += f'{fs}{stats["mean"]}{fs}{stats["min"]}'
        string += f'{fs}{stats["max"]}{fs}{stats["mean_of_abs"]}'
        string += f'{fs}{stats["stddev"]}{fs}{stats["variance"]}'
        string += f'{fs}{stats["coeff_var"]}{fs}{stats["sum"]}'
        string += f'{fs}{stats["null_cells"]}{fs}{stats["n"]}'
        string += f'{fs}{stats["n"]}'
        if "median" in stats:
            string += f'{fs}{stats["first_quartile"]}{fs}{stats["median"]}'
<<<<<<< HEAD
=======
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
            string += f'{fs}{stats["third_quartile"]}'
            if stats_module.inputs.percentile:
                for perc in stats_module.inputs.percentile:
                    perc_value = stats[
                        "percentile_"
                        f"{str(perc).rstrip('0').rstrip('.').replace('.', '_')}"
                    ]
                    string += f"{fs}{perc_value}"
        string += eol
    return string


def print_gridded_dataset_univar_statistics(
    type,
    input,
    output,
    where,
    extended,
    no_header: bool = False,
    fs: str = "|",
    rast_region: bool = False,
    region_relation=None,
    zones=None,
    percentile=None,
    nprocs: int = 1,
) -> None:
    """Print univariate statistics for a space time raster or raster3d dataset.
    Returns None if the space time raster dataset is empty or if applied
    filters (where, region_relation) do not return any maps to process.

    :param type: Type of Space-Time-Dataset, must be either strds or str3ds
    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param percentile: List of percentiles to compute
    :param no_header: Suppress the printing of column names
    :param fs: Field separator
    :param nprocs: Number of cores to use for processing
    :param rast_region: If set True ignore the current region settings
           and use the raster map regions for univar statistical calculation.
    :param region_relation: Process only maps with the given spatial relation
           to the computational region. A string with one of the following values:
           "overlaps": maps that spatially overlap ("intersect")
                       within the provided spatial extent
           "is_contained": maps that are fully within the provided spatial extent
           "contains": maps that contain (fully cover) the provided spatial extent
    :param zones: raster map with zones to calculate statistics for
    """
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
    # We need a database interface
    dbif = SQLDatabaseInterfaceConnection()
    dbif.connect()

    sp = open_old_stds(input, type, dbif)

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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> aec9c42ac4 (t.rast.univar: allow r-flag combined with zones option (#4577))
<<<<<<< HEAD
>>>>>>> ba28fbef7c (t.rast.univar: allow r-flag combined with zones option (#4577))
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
    if output is not None:
        out_file = open(output, "w")

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    strds_cols = (
        "id,start_time,end_time,semantic_label"
        if type == "strds"
        else "id,start_time,end_time"
    )
    rows = sp.get_registered_maps(strds_cols, where, "start_time", dbif)

=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
>>>>>>> osgeo-main
=======
>>>>>>> b9298093ee (t.rast.univar: allow r-flag combined with zones option (#4577))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
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
    strds_cols = (
        "id,start_time,end_time,semantic_label"
        if type == "strds"
        else "id,start_time,end_time"
    )
    rows = sp.get_registered_maps(strds_cols, where, "start_time", dbif)

>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
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
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> b9298093ee (t.rast.univar: allow r-flag combined with zones option (#4577))
<<<<<<< HEAD
>>>>>>> aec9c42ac4 (t.rast.univar: allow r-flag combined with zones option (#4577))
<<<<<<< HEAD
>>>>>>> ba28fbef7c (t.rast.univar: allow r-flag combined with zones option (#4577))
=======
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
    strds_cols = (
        "id,start_time,end_time,semantic_label"
        if type == "strds"
        else "id,start_time,end_time"
    )
    rows = sp.get_registered_maps(strds_cols, where, "start_time", dbif)

>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
    spatial_extent = None
    if region_relation:
        spatial_extent = gs.parse_command("g.region", flags="3gu")

    strds_cols = (
        "id,start_time,end_time,semantic_label"
        if type == "strds"
        else "id,start_time,end_time"
    )
    rows = sp.get_registered_maps(
        strds_cols,
        where,
        "start_time",
        dbif,
        spatial_extent=spatial_extent,
        spatial_relation=region_relation,
    )

    if not rows and rows != [""]:
        dbif.close()
        gs.verbose(
            _(
                "No maps found to process. "
                "Space time {type} dataset <{id}> is either empty "
                "or the where condition (if used) does not return any maps "
                "or no maps with the requested spatial relation to the "
                "computational region exist in the dataset."
            ).format(type=sp.get_new_map_instance(None).get_type(), id=sp.get_id())
=======
    strds_cols = (
        "id,start_time,end_time,semantic_label"
        if type == "strds"
        else "id,start_time,end_time"
    )
    rows = sp.get_registered_maps(strds_cols, where, "start_time", dbif)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
    strds_cols = (
        "id,start_time,end_time,semantic_label"
        if type == "strds"
        else "id,start_time,end_time"
    )
    rows = sp.get_registered_maps(strds_cols, where, "start_time", dbif)

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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
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
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
    strds_cols = (
        "id,start_time,end_time,semantic_label"
        if type == "strds"
        else "id,start_time,end_time"
    )
    rows = sp.get_registered_maps(strds_cols, where, "start_time", dbif)

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
    strds_cols = (
        "id,start_time,end_time,semantic_label"
        if type == "strds"
        else "id,start_time,end_time"
    )
    rows = sp.get_registered_maps(strds_cols, where, "start_time", dbif)

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
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
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
    if not rows and rows != [""]:
        dbif.close()
        err = "Space time %(sp)s dataset <%(i)s> is empty"
        if where:
            err += " or where condition is wrong"
        gs.fatal(
            _(err) % {"sp": sp.get_new_map_instance(None).get_type(), "i": sp.get_id()}
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        )

        return

    if output is not None:
        out_file = open(output, "w")

    if no_header is False:
        cols = (
            ["id", "semantic_label", "start", "end"]
            if type == "strds"
            else ["id", "start", "end"]
        )
        if zones:
            cols.append("zone")
        cols.extend(
            [
                "mean",
                "min",
                "max",
                "mean_of_abs",
                "stddev",
                "variance",
                "coeff_var",
                "sum",
                "null_cells",
                "cells",
                "non_null_cells",
            ]
        )
        if extended is True:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
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
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
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
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
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
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
            cols.extend(["first_quartile", "median", "third_quartile"])
            if percentile:
                cols.extend(
                    [
                        "percentile_"
                        f"{str(perc).rstrip('0').rstrip('.').replace('.', '_')}"
                        for perc in percentile
                    ]
                )
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
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
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
=======
            cols.extend(["first_quartile", "median", "third_quartile", "percentile_90"])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
        string = fs.join(cols)

        if output is None:
            print(string)
        else:
            out_file.write(string + "\n")

    # Define flags
    flag = "g"
    if extended is True:
        flag += "e"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    if type == "strds" and rast_region is True and not zones:
=======
    if type == "strds" and rast_region is True:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
    if type == "strds" and rast_region is True:
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    if type == "strds" and rast_region is True and not zones:
>>>>>>> aec9c42ac4 (t.rast.univar: allow r-flag combined with zones option (#4577))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
    if type == "strds" and rast_region is True:
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
        flag += "r"

    # Setup pygrass module to use for computation
    univar_module = Module(
        "r.univar" if type == "strds" else "r3.univar",
        flags=flag,
        zones=zones,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
        percentile=percentile,
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        percentile=percentile,
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        percentile=percentile,
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
        percentile=percentile,
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
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        percentile=percentile,
=======
<<<<<<< HEAD
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
        percentile=percentile,
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
        percentile=percentile,
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
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        percentile=percentile,
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
        percentile=percentile,
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
        percentile=percentile,
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
        percentile=percentile,
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
        percentile=percentile,
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
        percentile=percentile,
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
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        percentile=percentile,
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
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
        percentile=percentile,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
        stdout_=PIPE,
        run_=False,
    )

    if nprocs == 1:
        strings = [
            compute_univar_stats(
                row,
                univar_module,
                fs,
            )
            for row in rows
        ]
    else:
        with Pool(min(nprocs, len(rows))) as pool:
            strings = pool.starmap(
                compute_univar_stats, [(dict(row), univar_module, fs) for row in rows]
            )

    if output is None:
        print("\n".join(filter(None, strings)))
    else:
        out_file.write("\n".join(filter(None, strings)))

    dbif.close()

    if output is not None:
        out_file.close()


###############################################################################


def print_vector_dataset_univar_statistics(
    input,
    output,
    twhere,
    layer,
    type,
    column,
    where,
    extended,
    no_header: bool = False,
    fs: str = "|",
) -> None:
    """Print univariate statistics for a space time vector dataset

    :param input: The name of the space time dataset
    :param output: Name of the optional output file, if None stdout is used
    :param twhere: A temporal database where statement
    :param layer: The layer number used in case no layer is present
           in the temporal dataset
    :param type: options: point,line,boundary,centroid,area
    :param column: The name of the attribute column
    :param where: A temporal database where statement
    :param extended: If True compute extended statistics
    :param no_header: Suppress the printing of column names
    :param fs: Field separator
    """

    # We need a database interface
    dbif = SQLDatabaseInterfaceConnection()
    dbif.connect()

    if output is not None:
        out_file = open(output, "w")

    mapset = get_current_mapset()

    id = input if input.find("@") >= 0 else input + "@" + mapset

    sp = dataset_factory("stvds", id)

    if sp.is_in_db(dbif) is False:
        dbif.close()
        gs.fatal(
            _("Space time %(sp)s dataset <%(i)s> not found")
            % {"sp": sp.get_new_map_instance(None).get_type(), "i": id}
        )

    sp.select(dbif)

    rows = sp.get_registered_maps(
        "id,name,mapset,start_time,end_time,layer", twhere, "start_time", dbif
    )

    if not rows:
        dbif.close()
        gs.fatal(
            _("Space time %(sp)s dataset <%(i)s> is empty")
            % {"sp": sp.get_new_map_instance(None).get_type(), "i": id}
        )

    string = ""
    if no_header is False:
        string += (
            "id"
            + fs
            + "start"
            + fs
            + "end"
            + fs
            + "n"
            + fs
            + "nmissing"
            + fs
            + "nnull"
            + fs
        )
        string += "min" + fs + "max" + fs + "range"
        if type in {"point", "centroid"}:
            string += (
                fs
                + "mean"
                + fs
                + "mean_abs"
                + fs
                + "population_stddev"
                + fs
                + "population_variance"
                + fs
            )
            string += (
                "population_coeff_variation"
                + fs
                + "sample_stddev"
                + fs
                + "sample_variance"
                + fs
            )
            string += "kurtosis" + fs + "skewness"
            if extended is True:
                string += (
                    fs
                    + "first_quartile"
                    + fs
                    + "median"
                    + fs
                    + "third_quartile"
                    + fs
                    + "percentile_90"
                )

        if output is None:
            print(string)
        else:
            out_file.write(string + "\n")

    for row in rows:
        id = row["name"] + "@" + row["mapset"]
        start = row["start_time"]
        end = row["end_time"]
        mylayer = row["layer"]

        flags = "g"

        if extended is True:
            flags += "e"

        if not mylayer:
            mylayer = layer

        stats = gs.parse_command(
            "v.univar",
            map=id,
            where=where,
            column=column,
            layer=mylayer,
            type=type,
            flags=flags,
        )

        string = ""

        if not stats:
            gs.warning(_("Unable to get statistics for vector map <%s>") % id)
            continue

        string += str(id) + fs + str(start) + fs + str(end)
        string += (
            fs
            + str(stats["n"])
            + fs
            + str(stats["nmissing"])
            + fs
            + str(stats["nnull"])
        )
        if "min" in stats:
            string += (
                fs
                + str(stats["min"])
                + fs
                + str(stats["max"])
                + fs
                + str(stats["range"])
            )
        else:
            string += fs + fs + fs

        if type in {"point", "centroid"}:
            if "mean" in stats:
                string += (
                    fs
                    + str(stats["mean"])
                    + fs
                    + str(stats["mean_abs"])
                    + fs
                    + str(stats["population_stddev"])
                    + fs
                    + str(stats["population_variance"])
                )

                string += (
                    fs
                    + str(stats["population_coeff_variation"])
                    + fs
                    + str(stats["sample_stddev"])
                    + fs
                    + str(stats["sample_variance"])
                )

                string += fs + str(stats["kurtosis"]) + fs + str(stats["skewness"])
            else:
                string += fs + fs + fs + fs + fs + fs + fs + fs + fs
            if extended is True:
                if "first_quartile" in stats:
                    string += (
                        fs
                        + str(stats["first_quartile"])
                        + fs
                        + str(stats["median"])
                        + fs
                        + str(stats["third_quartile"])
                        + fs
                        + str(stats["percentile_90"])
                    )
                else:
                    string += fs + fs + fs + fs

        if output is None:
            print(string)
        else:
            out_file.write(string + "\n")

    dbif.close()

    if output is not None:
        out_file.close()
