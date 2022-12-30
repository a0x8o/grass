"""
Name:      i.maxlik general functionality
Purpose:   Test ability to perform classification

Author:    Maris Nartiss
Copyright: (C) 2022 by Maris Nartiss and the GRASS Development Team
Licence:   This program is free software under the GNU General Public
           License (>=v2). Read the file COPYING that comes with GRASS
           for details.
"""

import ctypes
import shutil

from grass.pygrass import utils
from grass.pygrass.gis import Mapset
from grass.pygrass import raster
from grass.script.core import tempname

from grass.gunittest.case import TestCase
from grass.gunittest.main import test
<<<<<<< HEAD
<<<<<<< HEAD
from grass.gunittest.utils import xfail_windows
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

from grass.lib.gis import G_mapset_path
from grass.lib.raster import Rast_write_semantic_label
from grass.lib.imagery import (
    Signature,
    Ref,
    I_init_signatures,
    I_new_signature,
    I_fopen_signature_file_new,
    I_write_signatures,
    I_init_group_ref,
    I_add_file_to_group_ref,
    I_put_group_ref,
    I_put_subgroup_ref,
)


class SuccessTest(TestCase):
    """Test successful classification"""

    @classmethod
    def setUpClass(cls):
        """Ensures expected computational region and generated data"""
        cls.use_temp_region()
        cls.runModule("g.region", n=5, s=0, e=5, w=0, res=1)
        cls.libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library("c"))
        cls.mpath = utils.decode(G_mapset_path())
        cls.mapset_name = Mapset().name
        cls.sig_name1 = tempname(10)
        cls.sig_dir1 = f"{cls.mpath}/signatures/sig/{cls.sig_name1}"
        cls.sig_name2 = tempname(10)
        cls.sig_dir2 = f"{cls.mpath}/signatures/sig/{cls.sig_name2}"
        cls.v1_class = tempname(10)
        cls.v2_class = tempname(10)

        # Imagery group to classify
        cls.b1 = tempname(10)
        cls.b2 = tempname(10)
        cls.group = tempname(10)
        cls.runModule(
            "r.mapcalc",
            expression=f"{cls.b1}=10.0+rand(-1.0,1.0)",
            flags="s",
            quiet=True,
        )
        cls.runModule(
            "r.mapcalc",
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 4255a3409f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 4c066e85bd (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2b1d4404b4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 7e84920a91 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 763393c2b3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2fb156cfe5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 506d884519 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 4c066e85bd (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 5a6c7b69e7 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 2b1d4404b4 (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 30bd67812c (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 7e84920a91 (i.maxlik: fix crash when classification result is NULL (#2724))
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
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 0b1431f1d8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 763393c2b3 (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
>>>>>>> osgeo-main
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
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
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 763393c2b3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
=======
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 2fb156cfe5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
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
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2b1d4404b4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 7e84920a91 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2fb156cfe5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 4255a3409f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 506d884519 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 4c066e85bd (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 5a6c7b69e7 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 2b1d4404b4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 30bd67812c (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 7e84920a91 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 0b1431f1d8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 763393c2b3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 2fb156cfe5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
            flags="s",
            quiet=True,
        )
        cls.semantic_label1 = "The_Doors"
        cls.semantic_label2 = "The_Who"
        Rast_write_semantic_label(cls.b1, cls.semantic_label1)
        Rast_write_semantic_label(cls.b2, cls.semantic_label2)
        Rg = Ref()
        I_init_group_ref(ctypes.byref(Rg))
        I_add_file_to_group_ref(cls.b1, cls.mapset_name, ctypes.byref(Rg))
        I_add_file_to_group_ref(cls.b2, cls.mapset_name, ctypes.byref(Rg))
        I_put_group_ref(cls.group, ctypes.byref(Rg))
        Rs = Ref()
        I_init_group_ref(ctypes.byref(Rs))
        I_add_file_to_group_ref(cls.b1, cls.mapset_name, ctypes.byref(Rs))
        I_add_file_to_group_ref(cls.b2, cls.mapset_name, ctypes.byref(Rs))
        I_put_subgroup_ref(cls.group, cls.group, ctypes.byref(Rs))

        # Old (v1) signature file
        So = Signature()
        I_init_signatures(ctypes.byref(So), 2)
        I_new_signature(ctypes.byref(So))
        I_new_signature(ctypes.byref(So))
        So.title = b"V1 signature"
        So.semantic_labels[0] = ctypes.create_string_buffer(
            cls.semantic_label1.encode()
        )
        So.semantic_labels[1] = ctypes.create_string_buffer(
            cls.semantic_label2.encode()
        )
        So.sig[0].status = 1
        So.sig[0].have_color = 0
        So.sig[0].npoints = 42
        So.sig[0].desc = b"my label"
        So.sig[0].mean[0] = 10
        So.sig[0].mean[1] = 5
        So.sig[0].var[0][0] = 1.5
        So.sig[0].var[1][0] = 2.1
        So.sig[0].var[1][1] = 5.7
        So.sig[1].status = 1
        So.sig[1].have_color = 0
        So.sig[1].npoints = 69
        So.sig[1].desc = b"not present"
        So.sig[1].mean[0] = 50
        So.sig[1].mean[1] = 75
        So.sig[1].var[0][0] = 5.5
        So.sig[1].var[1][0] = 8.1
        So.sig[1].var[1][1] = 12.7
        p_new_sigfile = I_fopen_signature_file_new(cls.sig_name1)
        I_write_signatures(p_new_sigfile, ctypes.byref(So))
        cls.libc.fclose(p_new_sigfile)

        # New (v2) signature file
        So = Signature()
        I_init_signatures(ctypes.byref(So), 2)
        I_new_signature(ctypes.byref(So))
        I_new_signature(ctypes.byref(So))
        So.title = b"V2 signature"
        So.semantic_labels[0] = ctypes.create_string_buffer(
            cls.semantic_label1.encode()
        )
        So.semantic_labels[1] = ctypes.create_string_buffer(
            cls.semantic_label2.encode()
        )
        So.have_oclass = 1
        So.sig[0].status = 1
        So.sig[0].have_color = 0
        So.sig[0].npoints = 42
        So.sig[0].oclass = 420
        So.sig[0].desc = b"my label"
        So.sig[0].mean[0] = 10
        So.sig[0].mean[1] = 5
        So.sig[0].var[0][0] = 1.5
        So.sig[0].var[1][0] = 2.1
        So.sig[0].var[1][1] = 5.7
        So.sig[1].status = 1
        So.sig[1].have_color = 0
        So.sig[1].npoints = 69
        So.sig[1].oclass = 690
        So.sig[1].desc = b"not present"
        So.sig[1].mean[0] = 50
        So.sig[1].mean[1] = 75
        So.sig[1].var[0][0] = 5.5
        So.sig[1].var[1][0] = 8.1
        So.sig[1].var[1][1] = 12.7
        p_new_sigfile = I_fopen_signature_file_new(cls.sig_name2)
        I_write_signatures(p_new_sigfile, ctypes.byref(So))
        cls.libc.fclose(p_new_sigfile)

    @classmethod
    def tearDownClass(cls):
        """Remove the temporary region and generated data"""
        cls.del_temp_region()
        shutil.rmtree(cls.sig_dir1, ignore_errors=True)
        shutil.rmtree(cls.sig_dir2, ignore_errors=True)
<<<<<<< HEAD
<<<<<<< HEAD
        cls.runModule(
            "g.remove",
            flags="f",
            type="raster",
            name=(cls.b1, cls.b2, cls.v1_class, cls.v2_class),
            quiet=True,
        )
        cls.runModule("g.remove", flags="f", type="group", name=cls.group, quiet=True)

    @xfail_windows
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        cls.runModule("g.remove", flags="f", type="raster", name=cls.b1, quiet=True)
        cls.runModule("g.remove", flags="f", type="raster", name=cls.b2, quiet=True)
        cls.runModule(
            "g.remove", flags="f", type="raster", name=cls.v1_class, quiet=True
        )
        cls.runModule(
            "g.remove", flags="f", type="raster", name=cls.v2_class, quiet=True
        )
        cls.runModule("g.remove", flags="f", type="group", name=cls.group, quiet=True)

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    def test_v1(self):
        """Test v1 signature"""
        self.assertModule(
            "i.maxlik",
            group=self.group,
            subgroup=self.group,
            signaturefile=self.sig_name1,
            output=self.v1_class,
            quiet=True,
        )
        self.assertRasterExists(self.v1_class)
        self.assertRasterMinMax(
            map=self.v1_class, refmin=1, refmax=1, msg="Wrong predicted value"
        )
        res = raster.RasterRow(self.v1_class)
        res.open()
        self.assertTrue(res.has_cats())
        self.assertEqual(res.get_cat(0)[0], "my label")
        self.assertEqual(res.get_cat(0)[1], 1)
        res.close()

<<<<<<< HEAD
<<<<<<< HEAD
    @xfail_windows
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    def test_v2(self):
        """Test v2 signature"""
        self.assertModule(
            "i.maxlik",
            group=self.group,
            subgroup=self.group,
            signaturefile=self.sig_name2,
            output=self.v2_class,
            quiet=True,
        )
        self.assertRasterExists(self.v2_class)
        self.assertRasterMinMax(
            map=self.v2_class, refmin=420, refmax=420, msg="Wrong predicted value"
        )
        res = raster.RasterRow(self.v2_class)
        res.open()
        self.assertTrue(res.has_cats())
        self.assertEqual(res.get_cat(0)[0], "my label")
        self.assertEqual(res.get_cat(0)[1], 420)
        res.close()


if __name__ == "__main__":
    test()
