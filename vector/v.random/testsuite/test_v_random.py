#!/usr/bin/env python3
"""
Name:      v.random test
Purpose:   Tests v.random and its flags/options.
Authors:   Josef Pudil (original draft)
           Sunveer Singh (finished test)
Copyright: (C) 2020-2021 by Sunveer Singh and the GRASS Development Team
Licence:   This program is free software under the GNU General Public
           License (>=v2). Read the file COPYING that comes with GRASS
           for details.
"""
from grass.gunittest.case import TestCase
from grass.gunittest.main import test


class TestVRandom(TestCase):
    output = "test01"
    output2 = "test02"
    npoints = 100
    state = "nc_state"
    zmin = 10
    zmax = 120

    @classmethod
    def setUpClass(cls):
        cls.use_temp_region()
        cls.runModule("g.region", vector=cls.state)

    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()

<<<<<<< HEAD
<<<<<<< HEAD
    def tearDown(self):
        self.runModule(
            "g.remove", type="vector", flags="f", name=(self.output, self.output2)
        )
=======
    def tearDown(cls):
        cls.runModule("g.remove", type="vector", flags="f", name=cls.output)
        cls.runModule("g.remove", type="vector", flags="f", name=cls.output2)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    def tearDown(cls):
        cls.runModule("g.remove", type="vector", flags="f", name=cls.output)
        cls.runModule("g.remove", type="vector", flags="f", name=cls.output2)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    def test_num_points(self):
        """Checking if number of points equals 100"""
        self.assertModule("v.random", output=self.output, npoints=self.npoints)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        topology = {"points": self.npoints}
=======
        topology = dict(points=self.npoints)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        topology = dict(points=self.npoints)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        topology = {"points": self.npoints}
>>>>>>> b120cf7523 (style: Fixes unnecessary-collection-call (C408) for testsuite (#3947))
        self.assertVectorFitsTopoInfo(vector=self.output, reference=topology)

    def test_num_points_3D(self):
        """Checking if the map is 3D and number of points is 100"""
        self.assertModule(
            "v.random",
            output=self.output,
            npoints=self.npoints,
            zmin=self.zmin,
            zmax=self.zmax,
            flags="z",
        )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        topology = {"points": self.npoints, "map3d": 1}
=======
        topology = dict(points=self.npoints, map3d=1)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        topology = dict(points=self.npoints, map3d=1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        topology = {"points": self.npoints, "map3d": 1}
>>>>>>> b120cf7523 (style: Fixes unnecessary-collection-call (C408) for testsuite (#3947))
        self.assertVectorFitsTopoInfo(vector=self.output, reference=topology)

    def test_restrict(self):
        """Checking if all points are in the polygon boundary state"""
        self.assertModule(
            "v.random", output=self.output, npoints=self.npoints, restrict=self.state
        )
        self.assertModule(
            "v.clip", input=self.output, clip=self.state, output=self.output2
        )
        self.assertVectorInfoEqualsVectorInfo(self.output, self.output2, precision=0.01)


if __name__ == "__main__":
    test()
