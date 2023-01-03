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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
from grass.gunittest.utils import xfail_windows
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
from grass.gunittest.utils import xfail_windows
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d0c4af5f80 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 099850264f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 3df1af6046 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 984f2e4b5f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> fa8258f7da (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f3d76d90e7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 4c14c5377c (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> b13ee245c1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f59448a530 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 115d1c2b17 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8da59835e3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 1ac37540a5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 40ae4b13c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
=======
=======
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5ce13cea96 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c745556f47 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> dfc4e9b268 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 21a39e2108 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c68c3cd4d0 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a1e3744f68 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b8d5485baf (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b0df4259cb (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> bea6abbdbb (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a40d5515e7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 91916b041f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> ae631bd878 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e93342de07 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 6a32c1731d (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 4061759949 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 824abbc8d7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c92112410b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 0ce7d7b652 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d635888aa1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 506d884519 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4c066e85bd (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 5a6c7b69e7 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2b1d4404b4 (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 30bd67812c (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7e84920a91 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
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
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2788a5026e (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 506d884519 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c68c3cd4d0 (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 5a6c7b69e7 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> a1e3744f68 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 30bd67812c (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> b8d5485baf (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 0b1431f1d8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> b0df4259cb (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
<<<<<<< HEAD
>>>>>>> b0df4259cb (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> c68c3cd4d0 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a1e3744f68 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b8d5485baf (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2ff2be4826 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8f9937d00a (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c4ee228391 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d88b10832d (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 385c333a86 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a7da23483e (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> fb8e87c2a1 (i.maxlik: fix crash when classification result is NULL (#2724))
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> bea6abbdbb (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> bea6abbdbb (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 099850264f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
=======
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2ff2be4826 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8f9937d00a (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c4ee228391 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d88b10832d (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 385c333a86 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a7da23483e (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> fb8e87c2a1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e0fc7e2fee (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> fc4d6dbb1b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 3662b58228 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> dfc4e9b268 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 480ff97f17 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 7c58471b8e (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 98158c2867 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c1fe2d6941 (i.maxlik: fix crash when classification result is NULL (#2724))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2fb156cfe5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d0c4af5f80 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 099850264f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 3df1af6046 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 984f2e4b5f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> fa8258f7da (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f3d76d90e7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 4c14c5377c (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> b13ee245c1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f59448a530 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 115d1c2b17 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8da59835e3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 1ac37540a5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 40ae4b13c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 21a39e2108 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5ce13cea96 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c745556f47 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> dfc4e9b268 (i.maxlik: fix crash when classification result is NULL (#2724))
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
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> c68c3cd4d0 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 506d884519 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4c066e85bd (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> a1e3744f68 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 5a6c7b69e7 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2b1d4404b4 (i.maxlik: fix crash when classification result is NULL (#2724))
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
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> b8d5485baf (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 30bd67812c (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7e84920a91 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
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
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 2ff2be4826 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> d0c4af5f80 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 099850264f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
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
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 3df1af6046 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 984f2e4b5f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 8f9937d00a (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> fa8258f7da (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c4ee228391 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> f3d76d90e7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> d88b10832d (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 4c14c5377c (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 385c333a86 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> b13ee245c1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> a7da23483e (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> f59448a530 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> fb8e87c2a1 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 115d1c2b17 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> e0fc7e2fee (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 8da59835e3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> fc4d6dbb1b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 1ac37540a5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 3662b58228 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 40ae4b13c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
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
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> dfc4e9b268 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 21a39e2108 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 480ff97f17 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 7c58471b8e (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 5ce13cea96 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 98158c2867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c1fe2d6941 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c745556f47 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 2788a5026e (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c68c3cd4d0 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a1e3744f68 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b8d5485baf (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 0b1431f1d8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> b0df4259cb (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> bea6abbdbb (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 2ff2be4826 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> a40d5515e7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> osgeo-main
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 91916b041f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> ae631bd878 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> e93342de07 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 8f9937d00a (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 6a32c1731d (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c4ee228391 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 4061759949 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> d88b10832d (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 824abbc8d7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 385c333a86 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> c92112410b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> a7da23483e (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 0ce7d7b652 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            expression=f"{cls.b2}=5.0+rand(-1.0,1.0)",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
            expression=f"{cls.b2}=if(row() == 3 && col() == 3, null(), 5.0+rand(-1.0,1.0))",
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> fb8e87c2a1 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> d635888aa1 (i.maxlik: fix crash when classification result is NULL (#2724))
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    @xfail_windows
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
    @xfail_windows
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
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
