"""Test of imagery library file searching functionality

@author Maris Nartiss

@copyright 2021 by Maris Nartiss and the GRASS Development Team

@license This program is free software under the GNU General Public License (>=v2).
Read the file COPYING that comes with GRASS
for details
"""
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import os
import shutil
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

import os
import shutil
<<<<<<< HEAD
=======
import os
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
import os
import shutil
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======

import os
import shutil
<<<<<<< HEAD
=======
import os
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======

import os
import shutil
<<<<<<< HEAD
=======
import os
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD

import os
import shutil
<<<<<<< HEAD
=======
import os
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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

from grass.gunittest.case import TestCase
from grass.gunittest.main import test

from grass.script.core import tempname
from grass.pygrass import utils
from grass.pygrass.gis import Mapset

from grass.lib.gis import G_mapset_path
from grass.lib.imagery import (
    I_SIGFILE_TYPE_SIG,
    I_SIGFILE_TYPE_SIGSET,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    I_SIGFILE_TYPE_LIBSVM,
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    I_SIGFILE_TYPE_LIBSVM,
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    I_SIGFILE_TYPE_LIBSVM,
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    I_SIGFILE_TYPE_LIBSVM,
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
    I_find_signature,
    I_find_signature2,
)


class FindSignatureTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mpath = utils.decode(G_mapset_path())
        cls.mapset_name = Mapset().name
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        cls.sigdirs = []
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        cls.sigdirs = []
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
        cls.sigdirs = []
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
        cls.sigdirs = []
=======
>>>>>>> osgeo-main
=======
        cls.sigdirs = []
=======
>>>>>>> osgeo-main
=======
        cls.sigdirs = []
=======
>>>>>>> osgeo-main
=======
        cls.sigdirs = []
=======
>>>>>>> osgeo-main
=======
        cls.sigdirs = []
=======
>>>>>>> osgeo-main
=======
        cls.sigdirs = []
=======
>>>>>>> osgeo-main
=======
        cls.sigdirs = []
=======
>>>>>>> osgeo-main
=======
        cls.sigdirs = []
=======
>>>>>>> osgeo-main
=======
        cls.sigdirs = []
=======
>>>>>>> osgeo-main
=======
        cls.sigdirs = []
=======
>>>>>>> osgeo-main
=======
        cls.sigdirs = []
=======
>>>>>>> osgeo-main
=======
        cls.sigdirs = []
=======
>>>>>>> osgeo-main
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
        cls.sigdirs = []
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        cls.sigdirs = []
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        cls.sigdirs = []
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        cls.sigdirs = []
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
        cls.sigdirs = []
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        cls.sigdirs = []
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        cls.sigdirs = []
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
        cls.sigdirs = []
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
        cls.sigdirs = []
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        cls.sigdirs = []
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        cls.sigdirs = []
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
        cls.sigdirs = []
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
        cls.sigdirs = []
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        cls.sigdirs = []
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
        # As signatures are created directly not via signature creation
        # tools, we must ensure signature directories exist
        os.makedirs(f"{cls.mpath}/signatures/sig/", exist_ok=True)
        os.makedirs(f"{cls.mpath}/signatures/sigset/", exist_ok=True)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
        os.makedirs(f"{cls.mpath}/signatures/libsvm/", exist_ok=True)
        cls.sig_name1 = tempname(10)
        cls.sig_dir1 = f"{cls.mpath}/signatures/sigset/{cls.sig_name1}"
        os.makedirs(cls.sig_dir1)
        cls.sigdirs.append(cls.sig_dir1)
        open(f"{cls.sig_dir1}/sig", "a").close()
        cls.sig_name2 = tempname(10)
        cls.sig_dir2 = f"{cls.mpath}/signatures/sig/{cls.sig_name2}"
        os.makedirs(cls.sig_dir2)
        cls.sigdirs.append(cls.sig_dir2)
        open(f"{cls.sig_dir2}/sig", "a").close()
        cls.sig_name3 = tempname(10)
        cls.sig_dir3 = f"{cls.mpath}/signatures/libsvm/{cls.sig_name3}"
        os.makedirs(cls.sig_dir3)
        cls.sigdirs.append(cls.sig_dir3)
        open(f"{cls.sig_dir3}/sig", "a").close()

    @classmethod
    def tearDownClass(cls):
        for d in cls.sigdirs:
            shutil.rmtree(d, ignore_errors=True)
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
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
        cls.sig_name1 = tempname(10)
        cls.sig_dir1 = f"{cls.mpath}/signatures/sigset/{cls.sig_name1}"
        os.makedirs(cls.sig_dir1)
        cls.sigdirs.append(cls.sig_dir1)
        open(f"{cls.sig_dir1}/sig", "a").close()
        cls.sig_name2 = tempname(10)
        cls.sig_dir2 = f"{cls.mpath}/signatures/sig/{cls.sig_name2}"
        os.makedirs(cls.sig_dir2)
        cls.sigdirs.append(cls.sig_dir2)
        open(f"{cls.sig_dir2}/sig", "a").close()

    @classmethod
    def tearDownClass(cls):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        for d in cls.sigdirs:
            shutil.rmtree(d, ignore_errors=True)
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
        cls.sig_name1 = tempname(10)
        cls.sig_dir1 = f"{cls.mpath}/signatures/sigset/{cls.sig_name1}"
        os.makedirs(cls.sig_dir1)
        cls.sigdirs.append(cls.sig_dir1)
        open(f"{cls.sig_dir1}/sig", "a").close()
        cls.sig_name2 = tempname(10)
        cls.sig_dir2 = f"{cls.mpath}/signatures/sig/{cls.sig_name2}"
        os.makedirs(cls.sig_dir2)
        cls.sigdirs.append(cls.sig_dir2)
        open(f"{cls.sig_dir2}/sig", "a").close()

    @classmethod
    def tearDownClass(cls):
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        cls.sig_name1 = tempname(10)
        cls.sig_dir1 = f"{cls.mpath}/signatures/sigset/{cls.sig_name1}"
        os.makedirs(cls.sig_dir1)
        cls.sigdirs.append(cls.sig_dir1)
        open(f"{cls.sig_dir1}/sig", "a").close()
        cls.sig_name2 = tempname(10)
        cls.sig_dir2 = f"{cls.mpath}/signatures/sig/{cls.sig_name2}"
        os.makedirs(cls.sig_dir2)
        cls.sigdirs.append(cls.sig_dir2)
        open(f"{cls.sig_dir2}/sig", "a").close()

    @classmethod
    def tearDownClass(cls):
<<<<<<< HEAD
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        cls.sig_name1 = tempname(10)
        cls.sig_dir1 = f"{cls.mpath}/signatures/sigset/{cls.sig_name1}"
        os.makedirs(cls.sig_dir1)
        cls.sigdirs.append(cls.sig_dir1)
        open(f"{cls.sig_dir1}/sig", "a").close()
        cls.sig_name2 = tempname(10)
        cls.sig_dir2 = f"{cls.mpath}/signatures/sig/{cls.sig_name2}"
        os.makedirs(cls.sig_dir2)
        cls.sigdirs.append(cls.sig_dir2)
        open(f"{cls.sig_dir2}/sig", "a").close()

    @classmethod
    def tearDownClass(cls):
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
        try:
            os.remove(cls.sigfile_name1)
            os.remove(cls.sigfile_name2)
        except OSError:
            pass
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
        for d in cls.sigdirs:
            shutil.rmtree(d, ignore_errors=True)
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
        for d in cls.sigdirs:
            shutil.rmtree(d, ignore_errors=True)
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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

    def test_find_sig(self):
        # Non existing without a mapset
        ret = I_find_signature(I_SIGFILE_TYPE_SIG, tempname(10), None)
        self.assertFalse(ret)
        # Non existing with a mapset
        ret = I_find_signature(I_SIGFILE_TYPE_SIG, tempname(10), self.mapset_name)
        self.assertFalse(ret)
        # Sigset with sig type should equal non existing
        ret = I_find_signature(I_SIGFILE_TYPE_SIG, self.sig_name1, self.mapset_name)
        self.assertFalse(ret)
        # Existing without a mapset
        ret = I_find_signature(I_SIGFILE_TYPE_SIG, self.sig_name2, None)
        self.assertTrue(ret)
        ms = utils.decode(ret)
        self.assertEqual(ms, self.mapset_name)
        # Existing with a mapset
        ret = I_find_signature(I_SIGFILE_TYPE_SIG, self.sig_name2, self.mapset_name)
        self.assertTrue(ret)
        ms = utils.decode(ret)
        self.assertEqual(ms, self.mapset_name)
        # Existing in a different mapset should fail
        ret = I_find_signature(I_SIGFILE_TYPE_SIG, self.sig_name2, "PERMANENT")
        self.assertFalse(ret)

    def test_find_sigset(self):
        # Non existing without a mapset
        ret = I_find_signature(I_SIGFILE_TYPE_SIGSET, tempname(10), None)
        self.assertFalse(ret)
        # Non existing with a mapset
        ret = I_find_signature(I_SIGFILE_TYPE_SIGSET, tempname(10), self.mapset_name)
        self.assertFalse(ret)
        # Sig with sigset type should equal non existing
        ret = I_find_signature(I_SIGFILE_TYPE_SIGSET, self.sig_name2, self.mapset_name)
        self.assertFalse(ret)
        # Existing without a mapset
        ret = I_find_signature(I_SIGFILE_TYPE_SIGSET, self.sig_name1, None)
        self.assertTrue(ret)
        ms = utils.decode(ret)
        self.assertEqual(ms, self.mapset_name)
        # Existing with a mapset
        ret = I_find_signature(I_SIGFILE_TYPE_SIGSET, self.sig_name1, self.mapset_name)
        self.assertTrue(ret)
        ms = utils.decode(ret)
        self.assertEqual(ms, self.mapset_name)
        # Existing in a different mapset should fail
        ret = I_find_signature(I_SIGFILE_TYPE_SIGSET, self.sig_name1, "PERMANENT")
        self.assertFalse(ret)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
    def test_find_libsvm(self):
        # Non existing without a mapset
        ret = I_find_signature(I_SIGFILE_TYPE_LIBSVM, tempname(10), None)
        self.assertFalse(ret)
        # Non existing with a mapset
        ret = I_find_signature(I_SIGFILE_TYPE_LIBSVM, tempname(10), self.mapset_name)
        self.assertFalse(ret)
        # Libsvm with sig type should equal non existing
        ret = I_find_signature(I_SIGFILE_TYPE_SIG, self.sig_name3, self.mapset_name)
        self.assertFalse(ret)
        # Existing without a mapset
        ret = I_find_signature(I_SIGFILE_TYPE_LIBSVM, self.sig_name3, None)
        self.assertTrue(ret)
        ms = utils.decode(ret)
        self.assertEqual(ms, self.mapset_name)
        # Existing with a mapset
        ret = I_find_signature(I_SIGFILE_TYPE_LIBSVM, self.sig_name3, self.mapset_name)
        self.assertTrue(ret)
        ms = utils.decode(ret)
        self.assertEqual(ms, self.mapset_name)
        # Existing in a different mapset should fail
        ret = I_find_signature(I_SIGFILE_TYPE_LIBSVM, self.sig_name3, "PERMANENT")
        self.assertFalse(ret)

=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
    def test_find2_sig(self):
        # Non existing without a mapset
        ret = I_find_signature2(I_SIGFILE_TYPE_SIG, tempname(10), None)
        self.assertFalse(ret)
        # Non existing with a mapset
        ret = I_find_signature2(I_SIGFILE_TYPE_SIG, tempname(10), self.mapset_name)
        self.assertFalse(ret)
        # Sigset with sig type should equal non existing
        ret = I_find_signature2(I_SIGFILE_TYPE_SIG, self.sig_name1, self.mapset_name)
        self.assertFalse(ret)
        # Existing without a mapset
        ret = I_find_signature2(I_SIGFILE_TYPE_SIG, self.sig_name2, None)
        self.assertTrue(ret)
        ms = utils.decode(ret)
        self.assertEqual(ms, self.mapset_name)
        # Existing with a mapset
        ret = I_find_signature2(I_SIGFILE_TYPE_SIG, self.sig_name2, self.mapset_name)
        self.assertTrue(ret)
        ms = utils.decode(ret)
        self.assertEqual(ms, self.mapset_name)
        # Existing in a different mapset should fail
        ret = I_find_signature2(I_SIGFILE_TYPE_SIG, self.sig_name2, "PERMANENT")
        self.assertFalse(ret)

    def test_find2_sigset(self):
        # Non existing without a mapset
        ret = I_find_signature2(I_SIGFILE_TYPE_SIGSET, tempname(10), None)
        self.assertFalse(ret)
        # Non existing with a mapset
        ret = I_find_signature2(I_SIGFILE_TYPE_SIGSET, tempname(10), self.mapset_name)
        self.assertFalse(ret)
        # Sig with sigset type should equal non existing
        ret = I_find_signature2(I_SIGFILE_TYPE_SIGSET, self.sig_name2, self.mapset_name)
        self.assertFalse(ret)
        # Existing without a mapset
        ret = I_find_signature2(I_SIGFILE_TYPE_SIGSET, self.sig_name1, None)
        self.assertTrue(ret)
        ms = utils.decode(ret)
        self.assertEqual(ms, self.mapset_name)
        # Existing with a mapset
        ret = I_find_signature2(I_SIGFILE_TYPE_SIGSET, self.sig_name1, self.mapset_name)
        self.assertTrue(ret)
        ms = utils.decode(ret)
        self.assertEqual(ms, self.mapset_name)
        # Existing in a different mapset should fail
        ret = I_find_signature2(I_SIGFILE_TYPE_SIGSET, self.sig_name1, "PERMANENT")
        self.assertFalse(ret)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
    def test_find2_libsvm(self):
        # Non existing without a mapset
        ret = I_find_signature2(I_SIGFILE_TYPE_LIBSVM, tempname(10), None)
        self.assertFalse(ret)
        # Non existing with a mapset
        ret = I_find_signature2(I_SIGFILE_TYPE_LIBSVM, tempname(10), self.mapset_name)
        self.assertFalse(ret)
        # Libsvm with sig type should equal non existing
        ret = I_find_signature2(I_SIGFILE_TYPE_SIG, self.sig_name3, self.mapset_name)
        self.assertFalse(ret)
        # Existing without a mapset
        ret = I_find_signature2(I_SIGFILE_TYPE_LIBSVM, self.sig_name3, None)
        self.assertTrue(ret)
        ms = utils.decode(ret)
        self.assertEqual(ms, self.mapset_name)
        # Existing with a mapset
        ret = I_find_signature2(I_SIGFILE_TYPE_LIBSVM, self.sig_name3, self.mapset_name)
        self.assertTrue(ret)
        ms = utils.decode(ret)
        self.assertEqual(ms, self.mapset_name)
        # Existing in a different mapset should fail
        ret = I_find_signature2(I_SIGFILE_TYPE_LIBSVM, self.sig_name3, "PERMANENT")
        self.assertFalse(ret)

=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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

if __name__ == "__main__":
    test()
