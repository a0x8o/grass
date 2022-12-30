"""
Name:      r.in.pdal binning method test
Purpose:   Validates output of various binning methods

Author:    Maris Nartiss
Copyright: (C) 2021 by Maris Nartiss and the GRASS Development Team
Licence:   This program is free software under the GNU General Public
           License (>=v2). Read the file COPYING that comes with GRASS
           for details.
"""

import os
import pathlib
import unittest
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
import shutil
from tempfile import TemporaryDirectory

from grass.script import core as grass
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
from tempfile import TemporaryDirectory

from grass.script import core as grass
from grass.script import shutil_which
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
import shutil
from tempfile import TemporaryDirectory

from grass.script import core as grass
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
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
import shutil
from tempfile import TemporaryDirectory

from grass.script import core as grass
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
from grass.gunittest.case import TestCase
from grass.gunittest.main import test


class BinningTest(TestCase):
    """Test binning methods

    This test requires pdal CLI util to be available.
    This tests expects r.in.ascii to work properly.
    """

    @classmethod
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("pdal") is None, "Cannot find pdal utility")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
    @unittest.skipIf(shutil_which("pdal") is None, "Cannot find pdal utility")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
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
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
    @unittest.skipIf(shutil_which("pdal") is None, "Cannot find pdal utility")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
    @unittest.skipIf(shutil_which("pdal") is None, "Cannot find pdal utility")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
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
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
=======
    @unittest.skipIf(shutil_which("pdal") is None, "Cannot find pdal utility")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
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
    @unittest.skipIf(shutil_which("pdal") is None, "Cannot find pdal utility")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("pdal") is None, "Cannot find pdal utility")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def setUpClass(cls):
        """Ensures expected computational region and generated data"""
        cls.use_temp_region()
        cls.runModule("g.region", n=18, s=0, e=18, w=0, res=6)

        cls.data_dir = os.path.join(pathlib.Path(__file__).parent.absolute(), "data")
        cls.point_file = os.path.join(cls.data_dir, "points.csv")
        cls.tmp_dir = TemporaryDirectory()
        cls.las_file = os.path.join(cls.tmp_dir.name, "points.las")
        grass.call(
            [
                "pdal",
                "translate",
                "-i",
                cls.point_file,
                "-o",
                cls.las_file,
                "-r",
                "text",
                "-w",
                "las",
                "--writers.las.format=0",
                "--writers.las.extra_dims=all",
                "--writers.las.minor_version=4",
            ]
        )

    @classmethod
    def tearDownClass(cls):
        """Remove the temporary region and generated data"""
        cls.tmp_dir.cleanup()
        cls.del_temp_region()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def tearDown(self):
        """Remove the outputs created by the import

        This is executed after each test run.
        """
<<<<<<< HEAD
<<<<<<< HEAD
        self.runModule(
            "g.remove",
            flags="f",
            type="raster",
            name=(self.bin_raster, self.ref_raster),
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
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
        self.runModule("g.remove", flags="f", type="raster", name=self.bin_raster)
        self.runModule("g.remove", flags="f", type="raster", name=self.ref_raster)

<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
        self.runModule("g.remove", flags="f", type="raster", name=self.bin_raster)
        self.runModule("g.remove", flags="f", type="raster", name=self.ref_raster)

<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def test_method_n(self):
        """Test binning with n method"""
        self.bin_raster = "bin_n"
        self.ref_raster = "ref_n"

        self.assertModule(
            "r.in.pdal",
            input=self.las_file,
            output=self.bin_raster,
            flags="o",
            quiet=True,
            method="n",
        )
        self.assertRasterExists(self.bin_raster)

        self.runModule(
            "r.in.ascii",
            input=os.path.join(self.data_dir, "res_n_all.ascii"),
            output=self.ref_raster,
        )
        self.assertRastersEqual(self.bin_raster, self.ref_raster, 0)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def test_method_min(self):
        self.bin_raster = "bin_min"
        self.ref_raster = "ref_min"

        self.assertModule(
            "r.in.pdal",
            input=self.las_file,
            output=self.bin_raster,
            flags="o",
            quiet=True,
            method="min",
        )
        self.assertRasterExists(self.bin_raster)

        self.runModule(
            "r.in.ascii",
            input=os.path.join(self.data_dir, "res_min_z.ascii"),
            output=self.ref_raster,
        )
        self.assertRastersEqual(self.bin_raster, self.ref_raster, 0)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def test_method_max(self):
        self.bin_raster = "bin_max"
        self.ref_raster = "ref_max"

        self.assertModule(
            "r.in.pdal",
            input=self.las_file,
            output=self.bin_raster,
            flags="o",
            quiet=True,
            method="max",
        )
        self.assertRasterExists(self.bin_raster)

        self.runModule(
            "r.in.ascii",
            input=os.path.join(self.data_dir, "res_max_z.ascii"),
            output=self.ref_raster,
        )
        self.assertRastersEqual(self.bin_raster, self.ref_raster, 0)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def test_method_range(self):
        self.bin_raster = "bin_range"
        self.ref_raster = "ref_range"

        self.assertModule(
            "r.in.pdal",
            input=self.las_file,
            output=self.bin_raster,
            flags="o",
            quiet=True,
            method="range",
        )
        self.assertRasterExists(self.bin_raster)

        self.runModule(
            "r.in.ascii",
            input=os.path.join(self.data_dir, "res_range_z.ascii"),
            output=self.ref_raster,
        )
        self.assertRastersEqual(self.bin_raster, self.ref_raster, 0)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def test_method_sum(self):
        self.bin_raster = "bin_sum"
        self.ref_raster = "ref_sum"

        self.assertModule(
            "r.in.pdal",
            input=self.las_file,
            output=self.bin_raster,
            flags="o",
            quiet=True,
            method="sum",
        )
        self.assertRasterExists(self.bin_raster)

        self.runModule(
            "r.in.ascii",
            input=os.path.join(self.data_dir, "res_sum_z.ascii"),
            output=self.ref_raster,
        )
        self.assertRastersEqual(self.bin_raster, self.ref_raster, 0)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def test_method_mean(self):
        self.bin_raster = "bin_mean"
        self.ref_raster = "ref_mean"

        self.assertModule(
            "r.in.pdal",
            input=self.las_file,
            output=self.bin_raster,
            flags="o",
            quiet=True,
            method="mean",
        )
        self.assertRasterExists(self.bin_raster)

        self.runModule(
            "r.in.ascii",
            input=os.path.join(self.data_dir, "res_mean_z.ascii"),
            output=self.ref_raster,
        )
        self.assertRastersEqual(self.bin_raster, self.ref_raster, 0.0001)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def test_method_stddev(self):
        self.bin_raster = "bin_stddev"
        self.ref_raster = "ref_stddev"

        self.assertModule(
            "r.in.pdal",
            input=self.las_file,
            output=self.bin_raster,
            flags="o",
            quiet=True,
            method="stddev",
        )
        self.assertRasterExists(self.bin_raster)

        self.runModule(
            "r.in.ascii",
            input=os.path.join(self.data_dir, "res_stddev_z.ascii"),
            output=self.ref_raster,
        )
        self.assertRastersEqual(self.bin_raster, self.ref_raster, 0.0001)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def test_method_variance(self):
        self.bin_raster = "bin_variance"
        self.ref_raster = "ref_variance"

        self.assertModule(
            "r.in.pdal",
            input=self.las_file,
            output=self.bin_raster,
            flags="o",
            quiet=True,
            method="variance",
        )
        self.assertRasterExists(self.bin_raster)

        self.runModule(
            "r.in.ascii",
            input=os.path.join(self.data_dir, "res_variance_z.ascii"),
            output=self.ref_raster,
        )
        self.assertRastersEqual(self.bin_raster, self.ref_raster, 0.0001)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def test_method_coeff_var(self):
        self.bin_raster = "bin_coeff_var"
        self.ref_raster = "ref_coeff_var"

        self.assertModule(
            "r.in.pdal",
            input=self.las_file,
            output=self.bin_raster,
            flags="o",
            quiet=True,
            method="coeff_var",
        )
        self.assertRasterExists(self.bin_raster)

        self.runModule(
            "r.in.ascii",
            input=os.path.join(self.data_dir, "res_coeff_var_z.ascii"),
            output=self.ref_raster,
        )
        self.assertRastersEqual(self.bin_raster, self.ref_raster, 0.0001)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def test_method_median(self):
        self.bin_raster = "bin_median"
        self.ref_raster = "ref_median"

        self.assertModule(
            "r.in.pdal",
            input=self.las_file,
            output=self.bin_raster,
            flags="o",
            quiet=True,
            method="median",
        )
        self.assertRasterExists(self.bin_raster)

        self.runModule(
            "r.in.ascii",
            input=os.path.join(self.data_dir, "res_median_z.ascii"),
            output=self.ref_raster,
        )
        self.assertRastersEqual(self.bin_raster, self.ref_raster, 0.0001)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def test_method_mode(self):
        self.bin_raster = "bin_mode"
        self.ref_raster = "ref_mode"

        self.assertModule(
            "r.in.pdal",
            input=self.las_file,
            output=self.bin_raster,
            flags="o",
            quiet=True,
            method="mode",
        )
        self.assertRasterExists(self.bin_raster)

        self.runModule(
            "r.in.ascii",
            input=os.path.join(self.data_dir, "res_mode_z.ascii"),
            output=self.ref_raster,
        )
        self.assertRastersEqual(self.bin_raster, self.ref_raster, 0)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def test_method_sidnmax(self):
        self.bin_raster = "bin_sidnmax"
        self.ref_raster = "ref_sidnmax"

        self.assertModule(
            "r.in.pdal",
            input=self.las_file,
            output=self.bin_raster,
            flags="o",
            quiet=True,
            method="sidnmax",
        )
        self.assertRasterExists(self.bin_raster)

        self.runModule(
            "r.in.ascii",
            input=os.path.join(self.data_dir, "res_sidnmax_all.ascii"),
            output=self.ref_raster,
        )
        self.assertRastersEqual(self.bin_raster, self.ref_raster, 0)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
>>>>>>> osgeo-main
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
=======
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
    @unittest.skipIf(shutil_which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    @unittest.skipIf(shutil.which("r.in.pdal") is None, "Cannot find r.in.pdal")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    def test_method_sidnmin(self):
        self.bin_raster = "bin_sidnmin"
        self.ref_raster = "ref_sidnmin"

        self.assertModule(
            "r.in.pdal",
            input=self.las_file,
            output=self.bin_raster,
            flags="o",
            quiet=True,
            method="sidnmin",
        )
        self.assertRasterExists(self.bin_raster)

        self.runModule(
            "r.in.ascii",
            input=os.path.join(self.data_dir, "res_sidnmin_all.ascii"),
            output=self.ref_raster,
        )
        self.assertRastersEqual(self.bin_raster, self.ref_raster, 0)


if __name__ == "__main__":
    test()
