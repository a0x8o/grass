"""
(C) 2013 by the GRASS Development Team
This program is free software under the GNU General Public
License (>=v2). Read the file COPYING that comes with GRASS
for details.

:authors: Soeren Gebbert
"""

import datetime
import os
import grass.temporal as tgis
from grass.gunittest.case import TestCase
from grass.gunittest.main import test


class TestTRastAlgebra(TestCase):
    @classmethod
    def setUpClass(cls):
        """Initiate the temporal GIS and set the region"""
        os.putenv("GRASS_OVERWRITE", "1")
        tgis.init(True)  # Raise on error instead of exit(1)
        cls.use_temp_region()
        cls.runModule("g.region", n=80.0, s=0.0, e=120.0, w=0.0, t=1.0, b=0.0, res=10.0)

        cls.runModule("r.mapcalc", quiet=True, expression="a1 = 1")
        cls.runModule("r.mapcalc", quiet=True, expression="a2 = 2")
        cls.runModule("r.mapcalc", quiet=True, expression="a3 = 3")
        cls.runModule("r.mapcalc", quiet=True, expression="a4 = 4")
        cls.runModule("r.mapcalc", quiet=True, expression="b1 = 5")
        cls.runModule("r.mapcalc", quiet=True, expression="b2 = 6")
        cls.runModule("r.mapcalc", quiet=True, expression="c1 = 7")
        cls.runModule("r.mapcalc", quiet=True, expression="d1 = 8")
        cls.runModule("r.mapcalc", quiet=True, expression="d2 = 9")
        cls.runModule("r.mapcalc", quiet=True, expression="d3 = 10")
        cls.runModule("r.mapcalc", quiet=True, expression="singletmap = 99")
        cls.runModule("r.mapcalc", quiet=True, expression="singlemap = 100")

        tgis.open_new_stds(
            name="A",
            type="strds",
            temporaltype="absolute",
            title="A",
            descr="A",
            semantic="field",
        )
        tgis.open_new_stds(
            name="B",
            type="strds",
            temporaltype="absolute",
            title="B",
            descr="B",
            semantic="field",
        )
        tgis.open_new_stds(
            name="C",
            type="strds",
            temporaltype="absolute",
            title="B",
            descr="C",
            semantic="field",
        )
        tgis.open_new_stds(
            name="D",
            type="strds",
            temporaltype="absolute",
            title="D",
            descr="D",
            semantic="field",
        )

        tgis.register_maps_in_space_time_dataset(
            type="raster",
            name="A",
            maps="a1,a2,a3,a4",
            start="2001-01-01",
            increment="1 day",
            interval=True,
        )
        tgis.register_maps_in_space_time_dataset(
            type="raster",
            name="B",
            maps="b1,b2",
            start="2001-01-01",
            increment="2 day",
            interval=True,
        )
        tgis.register_maps_in_space_time_dataset(
            type="raster",
            name="C",
            maps="c1",
            start="2001-01-02",
            increment="2 day",
            interval=True,
        )
        tgis.register_maps_in_space_time_dataset(
            type="raster",
            name="D",
            maps="d1,d2,d3",
            start="2001-01-03",
            increment="1 day",
            interval=True,
        )
        tgis.register_maps_in_space_time_dataset(
            type="raster",
            name=None,
            maps="singletmap",
            start="2001-01-03",
            end="2001-01-04",
        )

    def tearDown(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> e494d37988 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 56f3d5a1bd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1d6ad40ebe (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7b80a7eedd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3454fc4883 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 52e6c1ff9f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5faab49e7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> osgeo-main
>>>>>>> main
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
>>>>>>> e494d37988 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 56f3d5a1bd (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1d6ad40ebe (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7b80a7eedd (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
>>>>>>> 3454fc4883 (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
=======
        self.runModule("t.remove", flags="rf", inputs="R", quiet=True)
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
>>>>>>> 52e6c1ff9f (Dockerfile: fix broken lib link (#1625))
=======
=======
        self.runModule("t.remove", flags="df", inputs="R", quiet=True)
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
>>>>>>> 5faab49e7e (libpython: Save and load benchmark results (#1711))

    @classmethod
    def tearDownClass(cls):
        """Remove the temporary region"""
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> e494d37988 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 56f3d5a1bd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1d6ad40ebe (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7b80a7eedd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3454fc4883 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 52e6c1ff9f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5faab49e7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> osgeo-main
>>>>>>> main
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
>>>>>>> e494d37988 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 56f3d5a1bd (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1d6ad40ebe (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7b80a7eedd (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
>>>>>>> 3454fc4883 (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
=======
        cls.runModule("t.remove", flags="rf", inputs="A,B,C,D", quiet=True)
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
>>>>>>> 52e6c1ff9f (Dockerfile: fix broken lib link (#1625))
=======
=======
        cls.runModule("t.remove", flags="df", inputs="A,B,C,D", quiet=True)
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
>>>>>>> 5faab49e7e (libpython: Save and load benchmark results (#1711))
        cls.runModule("t.unregister", maps="singletmap", quiet=True)
        cls.del_temp_region()

    def test_temporal_conditional_time_dimension_bug(self):
        """Testing the conditional time dimension bug, that uses the time
        dimension of the conditional statement instead the time dimension
        of the then/else statement."""
        self.assertModule(
            "t.rast.algebra",
            expression="R = if({contains}, B == 5, " "A - 1,  A + 1)",
            basename="r",
            flags="d",
        )
        self.assertModule(
            "t.rast.algebra",
            expression="R = if({contains}, B == 5, " "A - 1,  A + 1)",
            basename="r",
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 0)  # 1 - 1
        self.assertEqual(D.metadata.get_max_max(), 5)  # 4 + 1
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "1 day")

    def test_simple_arith_hash_1(self):
        """Simple arithmetic test including the hash operator"""

        self.assertModule(
            "t.rast.algebra",
            expression="R = A + (A {#, equal,l} A)",
            basename="r",
            flags="d",
        )
        self.assertModule(
            "t.rast.algebra", expression="R = A + (A {#, equal,l} A)", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 2)
        self.assertEqual(D.metadata.get_max_max(), 5)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))

    def test_simple_arith_td_1(self):
        """Simple arithmetic test"""

        self.assertModule(
            "t.rast.algebra",
            expression="R = A + td(A)",
            basename="r",
            flags="d",
            suffix="time",
        )
        self.assertModule(
            "t.rast.algebra", expression="R = A + td(A)", basename="r", suffix="time"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 2)
        self.assertEqual(D.metadata.get_max_max(), 5)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))

    def test_simple_arith_td_2(self):
        """Simple arithmetic test"""

        self.assertModule(
            "t.rast.algebra",
            expression="R = A / td(A)",
            basename="r",
            flags="d",
            suffix="gran",
        )
        self.assertModule(
            "t.rast.algebra", expression="R = A / td(A)", basename="r", suffix="gran"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 1)
        self.assertEqual(D.metadata.get_max_max(), 4)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))

    def test_simple_arith_td_3(self):
        """Simple arithmetic test"""

        self.assertModule(
            "t.rast.algebra",
            expression="R = A {+,equal} td(A)",
            basename="r",
            flags="d",
        )
        self.assertModule(
            "t.rast.algebra", expression="R = A {+,equal} td(A)", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 2)
        self.assertEqual(D.metadata.get_max_max(), 5)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))

    def test_simple_arith_td_4(self):
        """Simple arithmetic test"""

        self.assertModule(
            "t.rast.algebra",
            expression="R = A {/, equal} td(A)",
            basename="r",
            flags="d",
        )
        self.assertModule(
            "t.rast.algebra", expression="R = A {/, equal} td(A)", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 1)
        self.assertEqual(D.metadata.get_max_max(), 4)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))

    def test_simple_arith_if_1(self):
        """Simple arithmetic test with if condition"""

        self.assertModule(
            "t.rast.algebra",
            expression="R = if({equal}, start_date(A)" ' >= "2001-01-02", A + A)',
            basename="r",
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 3)
        self.assertEqual(D.metadata.get_min_min(), 4)
        self.assertEqual(D.metadata.get_max_max(), 8)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 2))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))

    def test_simple_arith_if_2(self):
        """Simple arithmetic test with if condition"""

        self.assertModule(
            "t.rast.algebra",
            expression="R = if({equal}, A#A == 1, A - A)",
            basename="r",
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 0)
        self.assertEqual(D.metadata.get_max_max(), 0)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))

    def test_complex_arith_if_1(self):
        """Complex arithmetic test with if condition"""

        self.assertModule(
            "t.rast.algebra",
            expression='R = if(start_date(A) < "2001-01-03" && A#A == 1,'
            " A{+, starts,l}C, A{+, finishes,l}C)",
            basename="r",
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 2)
        self.assertEqual(D.metadata.get_min_min(), 9)  # 2 + 7 a2 + c1
        self.assertEqual(D.metadata.get_max_max(), 10)  # 3 + 7 a3 + c1
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 2))
        self.assertEqual(end, datetime.datetime(2001, 1, 4))

    def test_simple_arith_1(self):
        """Simple arithmetic test"""

        self.assertModule(
            "t.rast.algebra", expression="R = A {*, equal} A {+, equal} A", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 2)  # 1*1 + 1
        self.assertEqual(D.metadata.get_max_max(), 20)  # 4*4 + 4
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))

    def test_simple_arith_2(self):
        """Simple arithmetic test that creates an empty strds"""

        self.assertModule(
            "t.rast.algebra",
            expression="R = A {*, during} A {+, during} A",
            basename="r",
        )
        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 0)

    def test_simple_arith_3(self):
        """Simple arithmetic test"""

        self.assertModule(
            "t.rast.algebra", expression="R = A / A + A*A/A", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 2)  # 1/1 + 1*1/1
        self.assertEqual(D.metadata.get_max_max(), 5)  # 4/4 + 4*4/4
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))

    def test_temporal_intersection_1(self):
        """Simple temporal intersection test"""

        self.assertModule(
            "t.rast.algebra", expression="R = A {+,equal,i} B", basename="r"
        )
        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 0)

    def test_temporal_intersection_2(self):
        """Simple temporal intersection test"""

        self.assertModule(
            "t.rast.algebra", expression="R = A {+,during,i} B", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 6)  # 1 + 5
        self.assertEqual(D.metadata.get_max_max(), 10)  # 4 + 6
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))

    def test_temporal_intersection_3(self):
        """Simple temporal intersection test"""

        self.assertModule(
            "t.rast.algebra", expression="R = A {+,starts,i} B", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 2)
        self.assertEqual(D.metadata.get_min_min(), 6)  # 1 + 5
        self.assertEqual(D.metadata.get_max_max(), 9)  # 3 + 6
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 4))

    def test_temporal_intersection_4(self):
        """Simple temporal intersection test"""

        self.assertModule(
            "t.rast.algebra", expression="R = A {+,finishes,intersect} B", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 2)
        self.assertEqual(D.metadata.get_min_min(), 7)  # 2 + 5
        self.assertEqual(D.metadata.get_max_max(), 10)  # 4 + 6
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 2))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))

    def test_temporal_intersection_5(self):
        """Simple temporal intersection test"""

        self.assertModule(
            "t.rast.algebra", expression="R = A {+,starts|finishes,i} B", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 6)  # 1 + 5
        self.assertEqual(D.metadata.get_max_max(), 10)  # 4 + 6
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))

    def test_temporal_intersection_6(self):
        """Simple temporal intersection test"""

        self.assertModule(
            "t.rast.algebra", expression="R = B {+,overlaps,u} C", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 1)
        self.assertEqual(D.metadata.get_min_min(), 12)  # 5 + 7
        self.assertEqual(D.metadata.get_max_max(), 12)  # 5 + 7
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 4))

    def test_temporal_intersection_7(self):
        """Simple temporal intersection test"""

        self.assertModule(
            "t.rast.algebra", expression="R = B {+,overlapped,u} C", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 1)
        self.assertEqual(D.metadata.get_min_min(), 13)  # 6 + 7
        self.assertEqual(D.metadata.get_max_max(), 13)  # 6 + 7
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 2))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))

    def test_temporal_intersection_8(self):
        """Simple temporal intersection test"""

        self.assertModule(
            "t.rast.algebra",
            expression='R = A {+,during,l} buff_t(C, "1 day") ',
            basename="r",
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 8)  # 1 + 7  a1 + c1
        self.assertEqual(D.metadata.get_max_max(), 11)  # 4 + 7  a4 + c1
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))

    def test_temporal_neighbors_1(self):
        """Simple temporal neighborhood computation test"""

        self.assertModule("t.rast.algebra", expression="R = A[-1] + A[1]", basename="r")

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 2)
        self.assertEqual(D.metadata.get_min_min(), 4)  # 1 + 3
        self.assertEqual(D.metadata.get_max_max(), 6)  # 2 + 4
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 2))
        self.assertEqual(end, datetime.datetime(2001, 1, 4))

    def test_temporal_neighbors_2(self):
        """Simple temporal neighborhood computation test"""

        self.assertModule(
            "t.rast.algebra", expression="R = A[0,0,-1] + A[0,0,1]", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 2)
        self.assertEqual(D.metadata.get_min_min(), 4)  # 1 + 3
        self.assertEqual(D.metadata.get_max_max(), 6)  # 2 + 4
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 2))
        self.assertEqual(end, datetime.datetime(2001, 1, 4))

    def test_tmap_function1(self):
        """Testing the tmap function."""

        self.assertModule(
            "t.rast.algebra", expression="R = tmap(singletmap)", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        maplist = D.get_registered_maps_as_objects()
        self.assertEqual(D.metadata.get_number_of_maps(), 1)
        self.assertEqual(D.metadata.get_min_min(), 99)
        self.assertEqual(D.metadata.get_max_max(), 99)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 3))
        self.assertEqual(end, datetime.datetime(2001, 1, 4))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "1 day")

    def test_tmap_function2(self):
        """Testing the tmap function."""

        self.assertModule(
            "t.rast.algebra", expression="R = tmap(singletmap) + 1", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        maplist = D.get_registered_maps_as_objects()
        self.assertEqual(D.metadata.get_number_of_maps(), 1)
        self.assertEqual(D.metadata.get_min_min(), 100)
        self.assertEqual(D.metadata.get_max_max(), 100)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 3))
        self.assertEqual(end, datetime.datetime(2001, 1, 4))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "1 day")

    def test_map_function1(self):
        """Testing the map function."""

        self.assertModule(
            "t.rast.algebra", expression="R = map(singlemap) + A", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        maplist = D.get_registered_maps_as_objects()
        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 101)
        self.assertEqual(D.metadata.get_max_max(), 104)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "1 day")

    def test_map_function2(self):
        """Testing the map function."""

        self.assertModule(
            "t.rast.algebra", expression="R =  A * map(singlemap)", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        maplist = D.get_registered_maps_as_objects()
        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 100)
        self.assertEqual(D.metadata.get_max_max(), 400)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "1 day")

    def test_temporal_select(self):
        """Testing the temporal select operator."""

        self.assertModule("t.rast.algebra", expression="R = A : A", basename="r")

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 1)
        self.assertEqual(D.metadata.get_max_max(), 4)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "1 day")

    def test_temporal_select(self):
        """Testing the temporal select operator."""

        self.assertModule("t.rast.algebra", expression="R = A : D", basename="r")

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 2)
        self.assertEqual(D.metadata.get_min_min(), 3)
        self.assertEqual(D.metadata.get_max_max(), 4)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 3))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "1 day")

    def test_temporal_select_operators1(self):
        """Testing the temporal select operator. Including temporal relations."""

        self.assertModule("t.rast.algebra", expression="R = A : D", basename="r")

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 2)
        self.assertEqual(D.metadata.get_min_min(), 3)
        self.assertEqual(D.metadata.get_max_max(), 4)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 3))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "1 day")

    def test_temporal_select_operators2(self):
        """Testing the temporal select operator. Including temporal relations."""

        self.assertModule(
            "t.rast.algebra", expression="R = A {!:,during} C", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 2)
        self.assertEqual(D.metadata.get_min_min(), 1)
        self.assertEqual(D.metadata.get_max_max(), 4)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "1 day")

    def test_temporal_select_operators3(self):
        """Testing the temporal select operator. Including temporal relations and
        different temporal operators (lr|+&)"""

        self.assertModule(
            "t.rast.algebra", expression="R = A {:,during,d} B", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 1)
        self.assertEqual(D.metadata.get_max_max(), 4)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))
        self.assertEqual(D.check_temporal_topology(), False)
        self.assertEqual(D.get_granularity(), "2 days")

    def test_temporal_select_operators4(self):
        """Testing the temporal select operator. Including temporal relations and
        different temporal operators (lr|+&)"""

        self.assertModule(
            "t.rast.algebra", expression="R = A {:,equal|during,r} C", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        maplist = D.get_registered_maps_as_objects()
        for map_i in maplist:
            start_map, end_map = map_i.get_absolute_time()
            self.assertEqual(start_map, datetime.datetime(2001, 1, 2))
            self.assertEqual(end_map, datetime.datetime(2001, 1, 4))
        self.assertEqual(D.metadata.get_number_of_maps(), 2)
        self.assertEqual(D.metadata.get_min_min(), 2)
        self.assertEqual(D.metadata.get_max_max(), 3)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 2))
        self.assertEqual(end, datetime.datetime(2001, 1, 4))
        self.assertEqual(D.check_temporal_topology(), False)
        self.assertEqual(D.get_granularity(), "2 days")

    def test_temporal_hash_operator1(self):
        """Testing the temporal hash operator in the raster algebra."""

        self.assertModule(
            "t.rast.algebra", expression="R = if(A # D == 1, A)", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 2)
        self.assertEqual(D.metadata.get_min_min(), 3)
        self.assertEqual(D.metadata.get_max_max(), 4)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 3))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "1 day")

    def test_temporal_hash_operator2(self):
        """Testing the temporal hash operator in the raster algebra."""

        self.assertModule("t.rast.algebra", expression="R = A # D", basename="r")

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 2)
        self.assertEqual(D.metadata.get_min_min(), 1)
        self.assertEqual(D.metadata.get_max_max(), 1)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 3))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "1 day")

    def test_temporal_hash_operator3(self):
        """Testing the temporal hash operator in the raster algebra."""

        self.assertModule(
            "t.rast.algebra", expression="R = C {#,contains} A", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 1)
        self.assertEqual(D.metadata.get_min_min(), 2)
        self.assertEqual(D.metadata.get_max_max(), 2)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 2))
        self.assertEqual(end, datetime.datetime(2001, 1, 4))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "2 days")

    def test_temporal_hash_operator4(self):
        """Testing the temporal hash operator in the raster algebra."""

        self.assertModule(
            "t.rast.algebra",
            expression="R = if({contains},A # D == 1, C {#,contains} A)",
            basename="r",
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 1)
        self.assertEqual(D.metadata.get_min_min(), 2)
        self.assertEqual(D.metadata.get_max_max(), 2)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 2))
        self.assertEqual(end, datetime.datetime(2001, 1, 4))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "2 days")

    def test_raster_arithmetic_relation_1(self):
        """Arithmetic test with temporal intersection"""

        self.assertModule(
            "t.rast.algebra", expression="R = B {+,contains,l} A ", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 2)
        self.assertEqual(D.metadata.get_min_min(), 8)
        self.assertEqual(D.metadata.get_max_max(), 13)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "2 days")

    def test_raster_arithmetic_relation_2(self):
        """Arithmetic test with temporal intersection"""

        self.assertModule(
            "t.rast.algebra", expression="R = B {*,contains,l} A ", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 2)
        self.assertEqual(D.metadata.get_min_min(), 10)
        self.assertEqual(D.metadata.get_max_max(), 72)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "2 days")

    def test_raster_arithmetic_relation_3(self):
        """Arithmetic test with temporal intersection"""

        self.assertModule(
            "t.rast.algebra", expression="R = B {+,contains,l} A ", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 2)
        self.assertEqual(D.metadata.get_min_min(), 8)
        self.assertEqual(D.metadata.get_max_max(), 13)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "2 days")

    def test_raster_arithmetic_relation_4(self):
        """Arithmetic test with temporal intersection"""

        self.assertModule(
            "t.rast.algebra", expression="R = B {+,contains,r} A ", basename="r"
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 4)
        self.assertEqual(D.metadata.get_min_min(), 8)
        self.assertEqual(D.metadata.get_max_max(), 13)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 1))
        self.assertEqual(end, datetime.datetime(2001, 1, 5))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "1 day")

    def test_raster_arithmetic_relation_5(self):
        """Complex arithmetic test with temporal intersection"""

        self.assertModule(
            "t.rast.algebra",
            expression="R = tmap(singletmap) "
            "{+,equal| precedes| follows,l} "
            "A + map(singlemap)",
            basename="r",
        )

        D = tgis.open_old_stds("R", type="strds")

        self.assertEqual(D.metadata.get_number_of_maps(), 1)
        self.assertEqual(D.metadata.get_min_min(), 208)
        self.assertEqual(D.metadata.get_max_max(), 208)
        start, end = D.get_absolute_time()
        self.assertEqual(start, datetime.datetime(2001, 1, 3))
        self.assertEqual(end, datetime.datetime(2001, 1, 4))
        self.assertEqual(D.check_temporal_topology(), True)
        self.assertEqual(D.get_granularity(), "1 day")


if __name__ == "__main__":
    test()
