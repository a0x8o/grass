"""
@package mapdisp.main

@brief Start Map Display as standalone application

Classes:
 - mapdisp::DMonMap
 - mapdisp::Layer
 - mapdisp::LayerList
 - mapdisp::StandaloneMapDisplayGrassInterface
 - mapdisp::DMonGrassInterface
 - mapdisp::DMonDisplay
 - mapdisp::MapApp

Usage:
python mapdisp/main.py monitor-identifier /path/to/map/file /path/to/command/file /path/to/env/file

(C) 2006-2015 by the GRASS Development Team

This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.

@author Michael Barton
@author Jachym Cepicky
@author Martin Landa <landa.martin gmail.com>
@author Vaclav Petras <wenzeslaus gmail.com> (MapPanelBase)
@author Anna Kratochvilova <kratochanna gmail.com> (MapPanelBase)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
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
"""  # noqa: E501
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
"""  # noqa: E501
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
"""  # noqa: E501
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
"""  # noqa: E501
=======
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
"""  # noqa: E501
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
"""  # noqa: E501
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
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
"""  # noqa: E501
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
"""  # noqa: E501
=======
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
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
"""  # noqa: E501
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
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
"""  # noqa: E501
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
"""  # noqa: E501
=======
<<<<<<< HEAD
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
"""  # noqa: E501
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
"""  # noqa: E501
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
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
"""  # noqa: E501
=======
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
"""  # noqa: E501
=======
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
"""  # noqa: E501
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
"""  # noqa: E501
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
<<<<<<< HEAD
"""  # noqa: E501
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
"""  # noqa: E501
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
"""  # noqa: E501
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
"""  # noqa: E501
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
"""  # noqa: E501
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
"""  # noqa: E501
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
"""  # noqa: E501
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
"""  # noqa: E501
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
"""  # noqa: E501
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
"""  # noqa: E501
=======
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
"""  # noqa: E501
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
"""  # noqa: E501
=======
<<<<<<< HEAD
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
"""  # noqa: E501
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
"""  # noqa: E501
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
"""

from __future__ import print_function
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

import os
import sys
import time
import shutil
import fileinput

from grass.script.utils import try_remove
from grass.script import core as grass
from grass.script.task import cmdtuple_to_list, cmdlist_to_tuple
from grass.pydispatch.signal import Signal

from grass.script.setup import set_gui_path

set_gui_path()

# GUI imports require path to GUI code to be set.
from core import globalvar  # noqa: E402
import wx  # noqa: E402

from core import utils  # noqa: E402
from core.giface import StandaloneGrassInterface  # noqa: E402
from core.gcmd import RunCommand  # noqa: E402
from core.render import Map, MapLayer, RenderMapMgr  # noqa: E402
from mapdisp.frame import MapPanel  # noqa: E402
from gui_core.mapdisp import FrameMixin  # noqa: E402
from core.debug import Debug  # noqa: E402
from core.settings import UserSettings  # noqa: E402

# for standalone app
monFile = {
    "cmd": None,
    "map": None,
    "env": None,
}
monName = None
monSize = list(globalvar.MAP_WINDOW_SIZE)
monDecor = False


class DMonMap(Map):
    def __init__(self, giface, cmdfile=None, mapfile=None):
        """Map composition (stack of map layers and overlays)

        :param cmdline: full path to the cmd file (defined by d.mon)
        :param mapfile: full path to the map file (defined by d.mon)
        """
        Map.__init__(self)

        self._giface = giface

        # environment settings
        self.env = {}

        self.cmdfile = cmdfile

        # list of layers for rendering added from cmd file
        # TODO temporary solution, layer management by different tools in GRASS
        # should be resolved
        self.ownedLayers = []
        self.oldOverlays = []

        if mapfile:
            self.mapfileCmd = mapfile
            self.maskfileCmd = os.path.splitext(mapfile)[0] + ".pgm"

        # generated file for g.pnmcomp output for rendering the map
        self.mapfile = monFile["map"]
        if os.path.splitext(self.mapfile)[1] != ".ppm":
            self.mapfile += ".ppm"

        # signal sent when d.out.file/d.to.rast appears in cmd file, attribute
        # is cmd
        self.saveToFile = Signal("DMonMap.saveToFile")
        self.dToRast = Signal("DMonMap.dToRast")
        # signal sent when d.what.rast/vect appears in cmd file, attribute is
        # cmd
        self.query = Signal("DMonMap.query")

        self.renderMgr = RenderMapMgr(self)

        # update legend file variable with the one d.mon uses
        with open(monFile["env"]) as f:
            lines = f.readlines()
            for line in lines:
                if "GRASS_LEGEND_FILE" in line:
                    legfile = line.split("=", 1)[1].strip()
                    self.renderMgr.UpdateRenderEnv({"GRASS_LEGEND_FILE": legfile})
                    break

    def GetLayersFromCmdFile(self):
        """Get list of map layers from cmdfile"""
        if not self.cmdfile:
            return

        nlayers = 0
        try:
            fd = open(self.cmdfile)
            lines = fd.readlines()
            fd.close()
            # detect d.out.file, delete the line from the cmd file and export
            # graphics
            if len(lines) > 0:
                if lines[-1].startswith("d.out.file") or lines[-1].startswith(
                    "d.to.rast"
                ):
                    dCmd = lines[-1].strip()
                    fd = open(self.cmdfile, "w")
                    fd.writelines(lines[:-1])
                    fd.close()
                    if lines[-1].startswith("d.out.file"):
                        self.saveToFile.emit(cmd=utils.split(dCmd))
                    else:
                        self.dToRast.emit(cmd=utils.split(dCmd))
                    return
                if lines[-1].startswith("d.what"):
                    dWhatCmd = lines[-1].strip()
                    fd = open(self.cmdfile, "w")
                    fd.writelines(lines[:-1])
                    fd.close()
                    if "=" in utils.split(dWhatCmd)[1]:
                        maps = utils.split(dWhatCmd)[1].split("=")[1].split(",")
                    else:
                        maps = utils.split(dWhatCmd)[1].split(",")
                    self.query.emit(
                        ltype=utils.split(dWhatCmd)[0].split(".")[-1], maps=maps
                    )
                    return
            else:
                # clean overlays after erase
                self.oldOverlays = []
                overlays = list(self._giface.GetMapDisplay().decorations.keys())
                for each in overlays:
                    self._giface.GetMapDisplay().RemoveOverlay(each)

            existingLayers = self.GetListOfLayers()

            # holds new rendreing order for every layer in existingLayers
            layersOrder = [-1] * len(existingLayers)

            # next number in rendering order
            next_layer = 0
            mapFile = None
            render_env = {}
            for line in lines:
                if line.startswith("#"):
                    if "GRASS_RENDER_FILE" in line:
                        mapFile = line.split("=", 1)[1].strip()
                    try:
                        k, v = line[2:].strip().split("=", 1)
                    except:
                        pass
                    render_env[k] = v
                    continue

                cmd = utils.split(line.strip())

                ltype = None
                try:
                    ltype = utils.command2ltype[cmd[0]]
                except KeyError:
                    grass.warning(_("Unsupported command %s.") % cmd[0])
                    continue

                name = utils.GetLayerNameFromCmd(
                    cmd, fullyQualified=True, layerType=ltype
                )[0]

                args = {}

                if ltype in {"barscale", "rastleg", "northarrow", "text", "vectleg"}:
                    # TODO: this is still not optimal
                    # it is there to prevent adding the same overlay multiple times
                    if cmd in self.oldOverlays:
                        continue
                    if ltype == "rastleg":
                        self._giface.GetMapDisplay().AddLegendRast(cmd=cmd)
                    elif ltype == "barscale":
                        self._giface.GetMapDisplay().AddBarscale(cmd=cmd)
                    elif ltype == "northarrow":
                        self._giface.GetMapDisplay().AddArrow(cmd=cmd)
                    elif ltype == "text":
                        self._giface.GetMapDisplay().AddDtext(cmd=cmd)
                    elif ltype == "vectleg":
                        self._giface.GetMapDisplay().AddLegendVect(cmd=cmd)
                    self.oldOverlays.append(cmd)
                    continue

                classLayer = MapLayer
                args["ltype"] = ltype

                exists = False
                for i, layer in enumerate(existingLayers):
                    if layer.GetCmd(string=True) == utils.GetCmdString(
                        cmdlist_to_tuple(cmd)
                    ):
                        exists = True

                        if layersOrder[i] == -1:
                            layersOrder[i] = next_layer
                            next_layer += 1
                        # layer must be put higher in render order (same cmd was
                        # insered more times)
                        # TODO delete rendurant cmds from cmd file?
                        else:
                            for j, l_order in enumerate(layersOrder):
                                if l_order > layersOrder[i]:
                                    layersOrder[j] -= 1
                            layersOrder[i] = next_layer - 1

                        break
                if exists:
                    continue

                mapLayer = classLayer(
                    name=name,
                    cmd=cmd,
                    Map=None,
                    hidden=True,
                    render=False,
                    mapfile=mapFile,
                    **args,
                )
                mapLayer.GetRenderMgr().updateProgress.connect(
                    self.GetRenderMgr().ReportProgress
                )
                if render_env:
                    mapLayer.GetRenderMgr().UpdateRenderEnv(render_env)
                    render_env = {}

                newLayer = self._addLayer(mapLayer)

                existingLayers.append(newLayer)
                self.ownedLayers.append(newLayer)

                layersOrder.append(next_layer)
                next_layer += 1

                nlayers += 1

            reorderedLayers = [-1] * next_layer
            for i, layer in enumerate(existingLayers):
                # owned layer was not found in cmd file -> is deleted
                if layersOrder[i] == -1 and layer in self.ownedLayers:
                    self.ownedLayers.remove(layer)
                    self.DeleteLayer(layer)

                # other layer e. g. added by wx.vnet are added to the top
                elif layersOrder[i] == -1 and layer not in self.ownedLayers:
                    reorderedLayers.append(layer)

                # owned layer found in cmd file is added into proper rendering
                # position
                else:
                    reorderedLayers[layersOrder[i]] = layer

            self.SetLayers(reorderedLayers)

        except OSError as e:
            grass.warning(
                _("Unable to read cmdfile '%(cmd)s'. Details: %(det)s")
                % {"cmd": self.cmdfile, "det": e}
            )
            return

        Debug.msg(
            1,
            "Map.GetLayersFromCmdFile(): cmdfile=%s, nlayers=%d"
            % (self.cmdfile, nlayers),
        )

        self._giface.updateMap.emit(render=False)

    def Render(self, *args, **kwargs):
        """Render layer to image.

        For input params and returned data see overridden method in Map class.
        """
        return Map.Render(self, *args, **kwargs)

    def AddLayer(self, *args, **kwargs):
        """Adds generic map layer to list of layers.

        For input params and returned data see overridden method in Map class.
        """
        driver = UserSettings.Get(group="display", key="driver", subkey="type")

        if driver == "png":
            os.environ["GRASS_RENDER_IMMEDIATE"] = "png"
        else:
            os.environ["GRASS_RENDER_IMMEDIATE"] = "cairo"

        layer = Map.AddLayer(self, *args, **kwargs)

        del os.environ["GRASS_RENDER_IMMEDIATE"]

        return layer


class Layer:
    """@implements core::giface::Layer"""

    def __init__(self, maplayer):
        self._maplayer = maplayer

    def __getattr__(self, name):
        if name == "cmd":
            return cmdtuple_to_list(self._maplayer.GetCmd())
        if hasattr(self._maplayer, name):
            return getattr(self._maplayer, name)
        if name == "maplayer":
            return self._maplayer
        if name == "type":
            return self._maplayer.GetType()
            # elif name == 'ctrl':
        if name == "label":
            return self._maplayer.GetName()
            # elif name == 'propwin':


class LayerList:
    """@implements core::giface::LayerList"""

    def __init__(self, map, giface):
        self._map = map
        self._giface = giface
        self._index = 0

    def __len__(self):
        return len(self._map.GetListOfLayers())

    def __iter__(self):
        return self

    def __next__(self):
        items = self._map.GetListOfLayers()
        try:
            result = items[self._index]
        except IndexError:
            raise StopIteration
        self._index += 1
        return result

    def next(self):
        return next(self)

    def GetSelectedLayers(self, checkedOnly=True):
        # hidden and selected vs checked and selected
        items = self._map.GetListOfLayers()
        layers = []
        for item in items:
            layer = Layer(item)
            layers.append(layer)
        return layers

    def GetSelectedLayer(self, checkedOnly=False):
        """Returns selected layer or None when there is no selected layer."""
        layers = self.GetSelectedLayers()
        if len(layers) > 0:
            return layers[0]
        return None

    def AddLayer(self, ltype, name=None, checked=None, opacity=1.0, cmd=None):
        """Adds a new layer to the layer list.

        Launches property dialog if needed (raster, vector, etc.)

        :param ltype: layer type (raster, vector, raster_3d, ...)
        :param name: layer name
        :param checked: if True layer is checked
        :param opacity: layer opacity level
        :param cmd: command (given as a list)
        """
        self._map.AddLayer(
            ltype=ltype,
            command=cmd,
            name=name,
            active=True,
            opacity=opacity,
            render=True,
            pos=-1,
        )
        # TODO: this should be solved by signal
        # (which should be introduced everywhere,
        # alternative is some observer list)
        self._giface.updateMap.emit(render=True, renderVector=True)

    def GetLayersByName(self, name):
        items = self._map.GetListOfLayers()
        layers = []
        for item in items:
            if item.GetName() == name:
                layer = Layer(item)
                layers.append(layer)
        return layers

    def GetLayerByData(self, key, value):
        # TODO: implementation was not tested
        items = self._map.GetListOfLayers()
        for item in items:
            layer = Layer(item)
            try:
                if getattr(layer, key) == value:
                    return layer
            except AttributeError:
                pass
        return None


class StandaloneMapDisplayGrassInterface(StandaloneGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneGrassInterface.__init__(self)
        self._mapframe = mapframe

    def GetLayerList(self):
        return LayerList(self._mapframe.GetMap(), giface=self)

    def GetMapWindow(self):
        return self._mapframe.GetMapWindow()

    def GetMapDisplay(self):
        return self._mapframe

    def GetProgress(self):
        return self._mapframe.GetProgressBar()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
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
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
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
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
<<<<<<< HEAD
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 794ad6ec11 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
<<<<<<< HEAD
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
<<<<<<< HEAD
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
<<<<<<< HEAD
<<<<<<< HEAD

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
<<<<<<< HEAD
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a7a7e73225 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4a9fc58c09 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c1fc87d90c (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 25e2ad2b00 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 83892d4f00 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a4c8058b1e (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e29a7cbc33 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6fa8764e3e (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a253ccf34e (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8feebafec2 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cdb2b69452 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b5d70161ed (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a08bd516ca (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
<<<<<<< HEAD
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fd058b270f (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))


<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

<<<<<<< HEAD
<<<<<<< HEAD
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
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
<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
class DMonFrame(MapFrame):
    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))

    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
        self._mapframe.ShowStatusbar(show)

    def IsStatusbarShown(self):
        if not self._mapframe.statusbarManager:
            return False

        return self._mapframe.IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self._mapframe.RemoveToolbar
        else:
            action = self._mapframe.AddToolbar
        toolbars = list(self._mapframe.GetToolbarNames())
        if not toolbars:
            toolbars.append("map")
        for toolbar in toolbars:
            action(toolbar)

    def AreAllToolbarsShown(self):
        toolbar = self._mapframe.GetMapToolbar()
        if toolbar is None:
            return False

        return toolbar.IsShown()
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

class DMonGrassInterface(StandaloneMapDisplayGrassInterface):
    """@implements GrassInterface"""

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
class DMonDisplay(FrameMixin, MapPanel):
    """Map display for wrapping map panel with d.mon mathods and frame methods"""

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

class DMonDisplay(FrameMixin, MapPanel):
    """Map display for wrapping map panel with d.mon mathods and frame methods"""

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

class DMonDisplay(FrameMixin, MapPanel):
    """Map display for wrapping map panel with d.mon mathods and frame methods"""

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

class DMonDisplay(FrameMixin, MapPanel):
    """Map display for wrapping map panel with d.mon mathods and frame methods"""

>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

class DMonDisplay(FrameMixin, MapPanel):
    """Map display for wrapping map panel with d.mon mathods and frame methods"""

>>>>>>> osgeo-main
=======
    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

class DMonDisplay(FrameMixin, MapPanel):
    """Map display for wrapping map panel with d.mon mathods and frame methods"""

>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

class DMonDisplay(FrameMixin, MapPanel):
    """Map display for wrapping map panel with d.mon mathods and frame methods"""

>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
class DMonDisplay(FrameMixin, MapPanel):
    """Map display for wrapping map panel with d.mon mathods and frame methods"""

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
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
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
<<<<<<< HEAD
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
    def __init__(self, mapframe):
        StandaloneMapDisplayGrassInterface.__init__(self, mapframe)
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))

class DMonDisplay(FrameMixin, MapPanel):
    """Map display for wrapping map panel with d.mon mathods and frame methods"""

>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
class DMonDisplay(FrameMixin, MapPanel):
    """Map display for wrapping map panel with d.mon mathods and frame methods"""

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
=======
=======
class DMonDisplay(FrameMixin, MapPanel):
    """Map display for wrapping map panel with d.mon mathods and frame methods"""

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
class DMonDisplay(FrameMixin, MapPanel):
    """Map display for wrapping map panel with d.mon mathods and frame methods"""

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
class DMonDisplay(FrameMixin, MapPanel):
    """Map display for wrapping map panel with d.mon mathods and frame methods"""

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
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
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
    def __init__(self, parent, giface, id, Map, title, toolbars, statusbar):
        # init map panel
        MapPanel.__init__(
            self,
            parent=parent,
            id=id,
            title=title,
            Map=Map,
            giface=giface,
            toolbars=toolbars,
            statusbar=statusbar,
        )
        # set system icon
        parent.SetIcon(
            wx.Icon(
                os.path.join(globalvar.ICONDIR, "grass_map.ico"), wx.BITMAP_TYPE_ICO
            )
        )

        # bindings
        parent.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        # extend shortcuts and create frame accelerator table
        self.shortcuts_table.append((self.OnFullScreen, wx.ACCEL_NORMAL, wx.WXK_F11))
        self._initShortcuts()

        # update env file
        width, height = self.MapWindow.GetClientSize()
        for line in fileinput.input(monFile["env"], inplace=True):
            if "GRASS_RENDER_WIDTH" in line:
                print("GRASS_RENDER_WIDTH={0}".format(width))
            elif "GRASS_RENDER_HEIGHT" in line:
                print("GRASS_RENDER_HEIGHT={0}".format(height))
            else:
                print(line.rstrip("\n"))

        # add Map Display panel to Map Display frame
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self, proportion=1, flag=wx.EXPAND)
        parent.SetSizer(sizer)
        parent.Layout()

    def OnZoomToMap(self, event):
        layers = self.MapWindow.GetMap().GetListOfLayers()
        self.MapWindow.ZoomToMap(layers=layers)


class MapApp(wx.App):
    def OnInit(self):
        grass.set_raise_on_error(True)
        # actual use of StandaloneGrassInterface not yet tested
        # needed for adding functionality in future
        self._giface = DMonGrassInterface(None)

        return True

    def CreateMapDisplay(self, name, decorations=True):
        toolbars = []
        if decorations:
            toolbars.append("map")

        if __name__ == "__main__":
            self.cmdTimeStamp = 0  # fake initial timestamp
            self.Map = DMonMap(
                giface=self._giface, cmdfile=monFile["cmd"], mapfile=monFile["map"]
            )

            self.timer = wx.PyTimer(self.watcher)
            # check each 0.5s
            global mtime
            mtime = 500
            self.timer.Start(mtime)
        else:
            self.Map = None

        mapframe = wx.Frame(
            None, id=wx.ID_ANY, size=monSize, style=wx.DEFAULT_FRAME_STYLE, title=name
        )

        self.mapDisplay = DMonDisplay(
            parent=mapframe,
            id=wx.ID_ANY,
            title=name,
            Map=self.Map,
            giface=self._giface,
            toolbars=toolbars,
            statusbar=decorations,
        )

        # FIXME: hack to solve dependency
        self._giface._mapframe = self.mapDisplay

        self.mapDisplay.GetMapWindow().SetAlwaysRenderEnabled(False)

        # set default properties
        self.mapDisplay.SetProperties(
            render=UserSettings.Get(
                group="display", key="autoRendering", subkey="enabled"
            ),
            mode=UserSettings.Get(
                group="display", key="statusbarMode", subkey="selection"
            ),
            alignExtent=UserSettings.Get(
                group="display", key="alignExtent", subkey="enabled"
            ),
            constrainRes=UserSettings.Get(
                group="display", key="compResolution", subkey="enabled"
            ),
            showCompExtent=UserSettings.Get(
                group="display", key="showCompExtent", subkey="enabled"
            ),
        )

        self.Map.saveToFile.connect(self.mapDisplay.DOutFile)
        self.Map.dToRast.connect(self.mapDisplay.DToRast)
        self.Map.query.connect(
            lambda ltype, maps: self.mapDisplay.SetQueryLayersAndActivate(
                ltype=ltype, maps=maps
            )
        )

        return self.mapDisplay

    def OnExit(self):
        if __name__ == "__main__":
            # stop the timer
            if self.timer.IsRunning:
                self.timer.Stop()
            # terminate thread
            for f in monFile.values():
                try_remove(f)
        return True

    def watcher(self):
        """Redraw, if new layer appears (check's timestamp of
        cmdfile)
        """
        ###
        # TODO: find a better solution
        ###
        # the check below disabled, it's too much invasive to call
        # g.gisenv in the watcher...
        # try:
        # GISBASE and other system environmental variables can not be used
        # since the process inherited them from GRASS
        # raises exception when viable does not exists
        # grass.gisenv()['GISDBASE']
        # except KeyError:
        #    self.timer.Stop()
        #    return

        # todo: events
        try:
            currentCmdFileTime = os.path.getmtime(monFile["cmd"])
            if currentCmdFileTime > self.cmdTimeStamp:
                self.timer.Stop()
                self.cmdTimeStamp = currentCmdFileTime
                self.mapDisplay.GetMap().GetLayersFromCmdFile()
                self.timer.Start(mtime)
        except OSError as e:
            grass.warning("%s" % e)
            self.timer.Stop()

    def GetMapDisplay(self):
        """Get Map Display instance"""
        return self.mapDisplay


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(__doc__)
        sys.exit(0)

    # set command variable
    monName = sys.argv[1]
    monPath = sys.argv[2]
    monFile = {
        "map": os.path.join(monPath, "map.ppm"),
        "cmd": os.path.join(monPath, "cmd"),
        "env": os.path.join(monPath, "env"),
    }

    # monitor size
    monSize = (int(sys.argv[3]), int(sys.argv[4]))

    monDecor = not bool(int(sys.argv[5]))
    grass.verbose(_("Starting map display <%s>...") % (monName))

    # create pid file
    pidFile = os.path.join(monPath, "pid")
    fd = open(pidFile, "w")
    if not fd:
        grass.fatal(_("Unable to create file <%s>") % pidFile)
    fd.write("%s\n" % os.getpid())
    fd.close()

    RunCommand("g.gisenv", set="MONITOR_%s_PID=%d" % (monName.upper(), os.getpid()))

    start = time.time()
    gmMap = MapApp(0)
    mapDisplay = gmMap.CreateMapDisplay(monName, monDecor)
    mapDisplay.Show()
    Debug.msg(1, "WxMonitor started in %.6f sec" % (time.time() - start))

    gmMap.MainLoop()

    grass.verbose(_("Stopping map display <%s>...") % (monName))

    # clean up GRASS env variables
    try:
        shutil.rmtree(monPath)
    except OSError:
        pass

    RunCommand("g.gisenv", unset="MONITOR")

    sys.exit(0)
