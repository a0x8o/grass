"""Test t.rast.univar

(C) 2014 by the GRASS Development Team
This program is free software under the GNU General Public
License (>=v2). Read the file COPYING that comes with GRASS
for details.

@author Soeren Gebbert
"""

from pathlib import Path
from grass.gunittest.case import TestCase
from grass.gunittest.gmodules import SimpleModule
from grass.gunittest.utils import xfail_windows


class TestRasterUnivar(TestCase):
    @classmethod
    def setUpClass(cls):
        """Initiate the temporal GIS and set the region"""
        cls.use_temp_region()
        cls.runModule("g.region", s=0, n=80, w=0, e=120, b=0, t=50, res=1, res3=1)

        cls.runModule(
            "r3.mapcalc",
            expression="zones = int(if(row() <= 5, 1, if(row() >= 20, 3, 2)))",
            overwrite=True,
        )

        cls.runModule("r3.mapcalc", expression="a_1 = 100", overwrite=True)
        cls.runModule("r3.mapcalc", expression="a_2 = 200", overwrite=True)
        cls.runModule("r3.mapcalc", expression="a_3 = 300", overwrite=True)
        cls.runModule("r3.mapcalc", expression="a_4 = 400", overwrite=True)

        cls.runModule(
            "t.create",
            type="str3ds",
            temporaltype="absolute",
            output="A",
            title="A test",
            description="A test",
            overwrite=True,
        )
        cls.runModule(
            "t.register",
            flags="i",
            type="raster_3d",
            input="A",
            maps="a_1,a_2,a_3,a_4",
            start="2001-01-01",
            increment="3 months",
            overwrite=True,
        )

    @classmethod
    def tearDownClass(cls):
        """Remove the temporary region"""
        cls.runModule("t.remove", flags="df", type="str3ds", inputs="A")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        cls.runModule("g.remove", flags="f", type="raster_3d", name="zones")
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
        cls.del_temp_region()

    def test_with_all_maps(self):
=======
        cls.runModule("g.remove", flags="f", type="raster_3d", name="zones")
        cls.del_temp_region()
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
        cls.runModule("g.remove", flags="f", type="raster_3d", name="zones")
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
        cls.del_temp_region()

    def test_with_all_maps(self):
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
        cls.runModule("g.remove", flags="f", type="raster_3d", name="zones")
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
        cls.del_temp_region()

<<<<<<< HEAD
=======
    @xfail_windows
>>>>>>> osgeo-main
    def test_with_all_maps(self):
=======
        cls.runModule("g.remove", flags="f", type="raster_3d", name="zones")
        cls.del_temp_region()
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
        cls.runModule("g.remove", flags="f", type="raster_3d", name="zones")
        cls.del_temp_region()
>>>>>>> osgeo-main

    def test_with_all_maps(self):
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
        cls.runModule("g.remove", flags="f", type="raster_3d", name="zones")
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
        cls.del_temp_region()

    def test_with_all_maps(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main
        cls.runModule("g.remove", flags="f", type="raster_3d", name="zones")
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
        cls.del_temp_region()

    def test_with_all_maps(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
        cls.runModule("g.remove", flags="f", type="raster_3d", name="zones")
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
        cls.del_temp_region()

    def test_with_all_maps(self):
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
        cls.runModule("g.remove", flags="f", type="raster_3d", name="zones")
        cls.del_temp_region()
=======
=======
>>>>>>> osgeo-main
        cls.runModule("g.remove", flags="f", type="raster_3d", name="zones")
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
        cls.del_temp_region()

    def test_with_all_maps(self):
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        cls.runModule("g.remove", flags="f", type="raster_3d", name="zones")
        cls.del_temp_region()
=======
        cls.runModule("g.remove", flags="f", type="raster_3d", name="zones")
        cls.del_temp_region()

    def test_with_all_maps(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main

    def test_with_all_maps(self):

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        t_rast3d_univar = SimpleModule(
            "t.rast3d.univar",
            input="A",
            where="start_time >= '2001-01-01'",
            overwrite=True,
            verbose=True,
        )
        self.assertModule(t_rast3d_univar)

        univar_text = """id|start|end|mean|min|max|mean_of_abs|stddev|variance|coeff_var|sum|null_cells|cells|non_null_cells
a_1@testing|2001-01-01 00:00:00|2001-04-01 00:00:00|100|100|100|100|0|0|0|48000000|0|480000|480000
a_2@testing|2001-04-01 00:00:00|2001-07-01 00:00:00|200|200|200|200|0|0|0|96000000|0|480000|480000
a_3@testing|2001-07-01 00:00:00|2001-10-01 00:00:00|300|300|300|300|0|0|0|144000000|0|480000|480000
a_4@testing|2001-10-01 00:00:00|2002-01-01 00:00:00|400|400|400|400|0|0|0|192000000|0|480000|480000
"""
        for ref, res in zip(
            univar_text.split("\n"), t_rast3d_univar.outputs.stdout.split("\n")
        ):
            if ref and res:
                ref_line = ref.split("|", 1)[1]
                res_line = res.split("|", 1)[1]
                self.assertLooksLike(ref_line, res_line)

    @xfail_windows
    def test_with_subset_of_maps(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        t_rast3d_univar = SimpleModule(
            "t.rast3d.univar",
            input="A",
            where="start_time >= '2001-03-01'",
            overwrite=True,
            verbose=True,
        )
        self.assertModule(t_rast3d_univar)

        univar_text = """id|start|end|mean|min|max|mean_of_abs|stddev|variance|coeff_var|sum|null_cells|cells|non_null_cells
a_2@testing|2001-04-01 00:00:00|2001-07-01 00:00:00|200|200|200|200|0|0|0|96000000|0|480000|480000
a_3@testing|2001-07-01 00:00:00|2001-10-01 00:00:00|300|300|300|300|0|0|0|144000000|0|480000|480000
a_4@testing|2001-10-01 00:00:00|2002-01-01 00:00:00|400|400|400|400|0|0|0|192000000|0|480000|480000
"""
        for ref, res in zip(
            univar_text.split("\n"), t_rast3d_univar.outputs.stdout.split("\n")
        ):
            if ref and res:
                ref_line = ref.split("|", 1)[1]
                res_line = res.split("|", 1)[1]
                self.assertLooksLike(ref_line, res_line)

    def test_subset_with_output(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        self.assertModule(
            "t.rast3d.univar",
            input="A",
            output="univar_output.txt",
            where="start_time >= '2001-03-01'",
            overwrite=True,
            verbose=True,
        )

        univar_text = """id|start|end|mean|min|max|mean_of_abs|stddev|variance|coeff_var|sum|null_cells|cells|non_null_cells
a_2@testing|2001-04-01 00:00:00|2001-07-01 00:00:00|200|200|200|200|0|0|0|96000000|0|480000|480000
a_3@testing|2001-07-01 00:00:00|2001-10-01 00:00:00|300|300|300|300|0|0|0|144000000|0|480000|480000
a_4@testing|2001-10-01 00:00:00|2002-01-01 00:00:00|400|400|400|400|0|0|0|192000000|0|480000|480000
"""
        univar_output = Path("univar_output.txt").read_text()

        for ref, res in zip(univar_text.split("\n"), univar_output.split("\n")):
            if ref and res:
                ref_line = ref.split("|", 1)[1]
                res_line = res.split("|", 1)[1]
                self.assertLooksLike(ref_line, res_line)

    def test_subset_with_output_no_header(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        self.assertModule(
            "t.rast3d.univar",
            input="A",
            output="univar_output.txt",
            flags="s",
            where="start_time >= '2001-03-01'",
            overwrite=True,
            verbose=True,
        )

        univar_text = """a_2@testing|2001-04-01 00:00:00|2001-07-01 00:00:00|200|200|200|200|0|0|0|96000000|0|480000|480000
a_3@testing|2001-07-01 00:00:00|2001-10-01 00:00:00|300|300|300|300|0|0|0|144000000|0|480000|480000
a_4@testing|2001-10-01 00:00:00|2002-01-01 00:00:00|400|400|400|400|0|0|0|192000000|0|480000|480000
"""
        univar_output = Path("univar_output.txt").read_text()

        for ref, res in zip(univar_text.split("\n"), univar_output.split("\n")):
            if ref and res:
                ref_line = ref.split("|", 1)[1]
                res_line = res.split("|", 1)[1]
                self.assertLooksLike(ref_line, res_line)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    def test_error_handling_empty_strds(self):
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
    def test_handling_empty_strds(self):
=======
    def test_error_handling_empty_strds(self):
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
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    def test_error_handling_empty_strds(self):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
        # Empty str3ds
        self.assertModule(
            "t.rast3d.univar",
            input="A",
            output="univar_output.txt",
            where="start_time >= '2015-03-01'",
            overwrite=True,
            verbose=True,
        )

    def test_error_handling_no_input(self):
        # No input
        self.assertModuleFail("t.rast3d.univar", output="out.txt")

    @xfail_windows
    def test_with_zones(self):
        """Test use of zones"""

        t_rast_univar_zones = SimpleModule(
            "t.rast3d.univar",
            input="A",
            where="start_time >= '2001-01-01'",
            zones="zones",
            overwrite=True,
            verbose=True,
        )
        self.runModule("g.region", res=1)
        self.assertModule(t_rast_univar_zones)

        univar_text = """id|start|end|zone|mean|min|max|mean_of_abs|stddev|variance|coeff_var|sum|null_cells|cells|non_null_cells
a_1@PERMANENT|2001-01-01 00:00:00|2001-04-01 00:00:00|1|100|100|100|100|0|0|0|3000000|0|30000|30000
a_1@PERMANENT|2001-01-01 00:00:00|2001-04-01 00:00:00|2|100|100|100|100|0|0|0|8400000|0|84000|84000
a_1@PERMANENT|2001-01-01 00:00:00|2001-04-01 00:00:00|3|100|100|100|100|0|0|0|36600000|0|366000|366000
a_2@PERMANENT|2001-04-01 00:00:00|2001-07-01 00:00:00|1|200|200|200|200|0|0|0|6000000|0|30000|30000
a_2@PERMANENT|2001-04-01 00:00:00|2001-07-01 00:00:00|2|200|200|200|200|0|0|0|16800000|0|84000|84000
a_2@PERMANENT|2001-04-01 00:00:00|2001-07-01 00:00:00|3|200|200|200|200|0|0|0|73200000|0|366000|366000
a_3@PERMANENT|2001-07-01 00:00:00|2001-10-01 00:00:00|1|300|300|300|300|0|0|0|9000000|0|30000|30000
a_3@PERMANENT|2001-07-01 00:00:00|2001-10-01 00:00:00|2|300|300|300|300|0|0|0|25200000|0|84000|84000
a_3@PERMANENT|2001-07-01 00:00:00|2001-10-01 00:00:00|3|300|300|300|300|0|0|0|109800000|0|366000|366000
a_4@PERMANENT|2001-10-01 00:00:00|2002-01-01 00:00:00|1|400|400|400|400|0|0|0|12000000|0|30000|30000
a_4@PERMANENT|2001-10-01 00:00:00|2002-01-01 00:00:00|2|400|400|400|400|0|0|0|33600000|0|84000|84000
a_4@PERMANENT|2001-10-01 00:00:00|2002-01-01 00:00:00|3|400|400|400|400|0|0|0|146400000|0|366000|366000
"""

        for ref, res in zip(
            univar_text.split("\n"), t_rast_univar_zones.outputs.stdout.split("\n")
        ):
            if ref and res:
                ref_line = ref.split("|", 1)[1]
                res_line = res.split("|", 1)[1]
                self.assertLooksLike(ref_line, res_line)

    @xfail_windows
    def test_with_zones_parallel(self):
        """Test use of zones"""

        t_rast_univar_zones = SimpleModule(
            "t.rast3d.univar",
            input="A",
            where="start_time >= '2001-01-01'",
            zones="zones",
            nprocs=2,
            overwrite=True,
            verbose=True,
        )
        self.runModule("g.region", res=1)
        self.assertModule(t_rast_univar_zones)

        univar_text = """id|start|end|zone|mean|min|max|mean_of_abs|stddev|variance|coeff_var|sum|null_cells|cells|non_null_cells
a_1@PERMANENT|2001-01-01 00:00:00|2001-04-01 00:00:00|1|100|100|100|100|0|0|0|3000000|0|30000|30000
a_1@PERMANENT|2001-01-01 00:00:00|2001-04-01 00:00:00|2|100|100|100|100|0|0|0|8400000|0|84000|84000
a_1@PERMANENT|2001-01-01 00:00:00|2001-04-01 00:00:00|3|100|100|100|100|0|0|0|36600000|0|366000|366000
a_2@PERMANENT|2001-04-01 00:00:00|2001-07-01 00:00:00|1|200|200|200|200|0|0|0|6000000|0|30000|30000
a_2@PERMANENT|2001-04-01 00:00:00|2001-07-01 00:00:00|2|200|200|200|200|0|0|0|16800000|0|84000|84000
a_2@PERMANENT|2001-04-01 00:00:00|2001-07-01 00:00:00|3|200|200|200|200|0|0|0|73200000|0|366000|366000
a_3@PERMANENT|2001-07-01 00:00:00|2001-10-01 00:00:00|1|300|300|300|300|0|0|0|9000000|0|30000|30000
a_3@PERMANENT|2001-07-01 00:00:00|2001-10-01 00:00:00|2|300|300|300|300|0|0|0|25200000|0|84000|84000
a_3@PERMANENT|2001-07-01 00:00:00|2001-10-01 00:00:00|3|300|300|300|300|0|0|0|109800000|0|366000|366000
a_4@PERMANENT|2001-10-01 00:00:00|2002-01-01 00:00:00|1|400|400|400|400|0|0|0|12000000|0|30000|30000
a_4@PERMANENT|2001-10-01 00:00:00|2002-01-01 00:00:00|2|400|400|400|400|0|0|0|33600000|0|84000|84000
a_4@PERMANENT|2001-10-01 00:00:00|2002-01-01 00:00:00|3|400|400|400|400|0|0|0|146400000|0|366000|366000
"""

        for ref, res in zip(
            univar_text.split("\n"), t_rast_univar_zones.outputs.stdout.split("\n")
        ):
            if ref and res:
                ref_line = ref.split("|", 1)[1]
                res_line = res.split("|", 1)[1]
                self.assertLooksLike(ref_line, res_line)


if __name__ == "__main__":
    from grass.gunittest.main import test

    test()
