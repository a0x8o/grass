from grass.gunittest.case import TestCase
from grass.gunittest.main import test
from grass.gunittest.gmodules import call_module


class TestRSeries(TestCase):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
    average = "average"
    count = "count"
    median = "median"
    sum_ = "sum"
    sum_mapcalc = "sum_mapcalc"
    elevation = "elevation"

    @classmethod
    def setUpClass(cls):
        cls.use_temp_region()
        call_module("g.region", raster=cls.elevation)
        call_module("r.mapcalc", expression=f"{cls.sum_mapcalc} = {cls.elevation} * 4")

    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()
        call_module(
            "g.remove",
            flags="f",
            type_="raster",
            name=cls.sum_mapcalc,
        )

    def tearDown(self):
        call_module(
            "g.remove",
            flags="f",
            type_="raster",
            name=[self.average, self.count, self.median, self.sum_],
        )

    def test_basic(self):
        self.assertModule(
            "r.series",
            input=[self.elevation] * 4,
            method=["average", "count", "median", "sum"],
            output=[self.average, self.count, self.median, self.sum_],
        )
        self.assertRastersNoDifference(
            actual=self.average,
            reference=self.elevation,
            precision=0.00001,
        )
        self.assertRasterMinMax(
            map=self.count,
            refmin=4,
            refmax=4,
        )
        self.assertRastersNoDifference(
            actual=self.median,
            reference=self.elevation,
            precision=0.00001,
        )
        self.assertRastersNoDifference(
            actual=self.sum_,
            reference=self.sum_mapcalc,
            precision=0.00001,
        )

    def test_nprocs(self):
        self.assertModule(
            "r.series",
            input=[self.elevation] * 4,
            method=["average", "count", "median", "sum"],
            output=[self.average, self.count, self.median, self.sum_],
            nprocs=4,
        )
        self.assertRastersNoDifference(
            actual=self.average,
            reference=self.elevation,
            precision=0.00001,
        )
        self.assertRasterMinMax(
            map=self.count,
            refmin=4,
            refmax=4,
        )
        self.assertRastersNoDifference(
            actual=self.median,
            reference=self.elevation,
            precision=0.00001,
        )
        self.assertRastersNoDifference(
            actual=self.sum_,
            reference=self.sum_mapcalc,
            precision=0.00001,
        )

    def test_z_flag(self):
        self.assertModule(
            "r.series",
            flags="z",
            input=[self.elevation] * 4,
            method=["average", "count", "median", "sum"],
            output=[self.average, self.count, self.median, self.sum_],
            nprocs=4,
        )
        self.assertRastersNoDifference(
            actual=self.average,
            reference=self.elevation,
            precision=0.00001,
        )
        self.assertRasterMinMax(
            map=self.count,
            refmin=4,
            refmax=4,
        )
        self.assertRastersNoDifference(
            actual=self.median,
            reference=self.elevation,
            precision=0.00001,
        )
        self.assertRastersNoDifference(
            actual=self.sum_,
            reference=self.sum_mapcalc,
            precision=0.00001,
        )

    def test_file(self):
        self.assertModule(
            "r.series",
            stdin="\n".join([self.elevation] * 4),
            file="-",
            method=["average", "count", "median", "sum"],
            output=[self.average, self.count, self.median, self.sum_],
            nprocs=4,
        )
        self.assertRastersNoDifference(
            actual=self.average,
            reference=self.elevation,
            precision=0.00001,
        )
        self.assertRasterMinMax(
            map=self.count,
            refmin=4,
            refmax=4,
        )
        self.assertRastersNoDifference(
            actual=self.median,
            reference=self.elevation,
            precision=0.00001,
        )
        self.assertRastersNoDifference(
            actual=self.sum_,
            reference=self.sum_mapcalc,
            precision=0.00001,
        )


if __name__ == "__main__":
    test()
