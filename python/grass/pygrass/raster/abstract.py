"""
Created on Fri Aug 17 16:05:25 2012

@author: pietro
"""

import ctypes

#
# import GRASS modules
#
from grass.script import fatal, gisenv
import grass.lib.gis as libgis
import grass.lib.raster as libraster

#
# import pygrass modules
#
from grass.pygrass import utils
from grass.pygrass.gis.region import Region
from grass.pygrass.errors import must_be_open, must_be_in_current_mapset
from grass.pygrass.shell.conversion import dict2html
from grass.pygrass.shell.show import raw_figure

#
# import raster classes
#
from grass.pygrass.raster.raster_type import TYPE as RTYPE, RTYPE_STR
from grass.pygrass.raster.category import Category
from grass.pygrass.raster.history import History

test_raster_name = "abstract_test_map"

# Define global variables to not exceed the 80 columns
INDXOUTRANGE = "The index (%d) is out of range, have you open the map?."
INFO = """{name}@{mapset}
rows: {rows}
cols: {cols}
north: {north} south: {south} nsres:{nsres}
east:  {east} west: {west} ewres:{ewres}
range: {min}, {max}
proj: {proj}
"""


class Info:
    def __init__(self, name, mapset=""):
        """Read the information for a raster map. ::

        >>> info = Info(test_raster_name)
        >>> info.read()
        >>> info  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
        abstract_test_map@
        rows: 4
        cols: 4
        north: 40.0 south: 0.0 nsres:10.0
        east:  40.0 west: 0.0 ewres:10.0
        range: 11, 44
        ...
        <BLANKLINE>

        """
        self.name = name
        self.mapset = mapset
        self.c_region = ctypes.pointer(libraster.struct_Cell_head())
        self.c_range = None

    def _get_range(self):
        if self.mtype == "CELL":
            self.c_range = ctypes.pointer(libraster.Range())
            libraster.Rast_read_range(self.name, self.mapset, self.c_range)
        else:
            self.c_range = ctypes.pointer(libraster.FPRange())
            libraster.Rast_read_fp_range(self.name, self.mapset, self.c_range)

    def _get_raster_region(self):
        libraster.Rast_get_cellhd(self.name, self.mapset, self.c_region)

    def read(self):
        self._get_range()
        self._get_raster_region()

    @property
    def north(self):
        return self.c_region.contents.north

    @property
    def south(self):
        return self.c_region.contents.south

    @property
    def east(self):
        return self.c_region.contents.east

    @property
    def west(self):
        return self.c_region.contents.west

    @property
    def top(self):
        return self.c_region.contents.top

    @property
    def bottom(self):
        return self.c_region.contents.bottom

    @property
    def rows(self):
        return self.c_region.contents.rows

    @property
    def cols(self):
        return self.c_region.contents.cols

    @property
    def nsres(self):
        return self.c_region.contents.ns_res

    @property
    def ewres(self):
        return self.c_region.contents.ew_res

    @property
    def tbres(self):
        return self.c_region.contents.tb_res

    @property
    def zone(self):
        return self.c_region.contents.zone

    @property
    def proj(self):
        return self.c_region.contents.proj

    @property
    def min(self):
        if self.c_range is None:
            return None
        return self.c_range.contents.min

    @property
    def max(self):
        if self.c_range is None:
            return None
        return self.c_range.contents.max

    @property
    def range(self):
        if self.c_range is None:
            return None, None
        return self.c_range.contents.min, self.c_range.contents.max

    @property
    def mtype(self):
        return RTYPE_STR[libraster.Rast_map_type(self.name, self.mapset)]

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
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
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
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
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
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
    def _get_semantic_label(self):
        """Get semantic label identifier.
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
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
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
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
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
=======
    def _get_bandref(self):
        """Get band reference identifier.
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_bandref(self):
        """Get band reference identifier.
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
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
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
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
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
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
<<<<<<< HEAD
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
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
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
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
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
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
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
<<<<<<< HEAD
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
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
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
    def _get_semantic_label(self):
        """Get semantic label identifier.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
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
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
=======
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
    def _get_semantic_label(self):
        """Get semantic label identifier.
=======
    def _get_bandref(self):
        """Get band reference identifier.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))

        :return str: semantic label (eg. S2_1) or None
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
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
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
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
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
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
        semantic_label = libraster.Rast_read_semantic_label(self.name, self.mapset)
        if semantic_label:
            return utils.decode(semantic_label)
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
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
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
        semantic_label = libraster.Rast_read_semantic_label(self.name, self.mapset)
        if semantic_label:
            return utils.decode(semantic_label)
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

    semantic_label = property(_get_semantic_label, _set_semantic_label)
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
        bandref = libraster.Rast_read_bandref(self.name, self.mapset)
        if bandref:
            return utils.decode(bandref)
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
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
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
        semantic_label = libraster.Rast_read_semantic_label(self.name, self.mapset)
        if semantic_label:
            return utils.decode(semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
        bandref = libraster.Rast_read_bandref(self.name, self.mapset)
        if bandref:
            return utils.decode(bandref)
=======
        semantic_label = libraster.Rast_read_semantic_label(self.name, self.mapset)
        if semantic_label:
            return utils.decode(semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
        bandref = libraster.Rast_read_bandref(self.name, self.mapset)
        if bandref:
            return utils.decode(bandref)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
        semantic_label = libraster.Rast_read_semantic_label(self.name, self.mapset)
        if semantic_label:
            return utils.decode(semantic_label)
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
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
        bandref = libraster.Rast_read_bandref(self.name, self.mapset)
        if bandref:
            return utils.decode(bandref)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
        semantic_label = libraster.Rast_read_semantic_label(self.name, self.mapset)
        if semantic_label:
            return utils.decode(semantic_label)
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
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
        bandref = libraster.Rast_read_bandref(self.name, self.mapset)
        if bandref:
            return utils.decode(bandref)
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
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
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
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
=======
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
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
        bandref = libraster.Rast_read_bandref(self.name, self.mapset)
        if bandref:
            return utils.decode(bandref)
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
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
        semantic_label = libraster.Rast_read_semantic_label(self.name, self.mapset)
        if semantic_label:
            return utils.decode(semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
>>>>>>> osgeo-main
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
        bandref = libraster.Rast_read_bandref(self.name, self.mapset)
        if bandref:
            return utils.decode(bandref)
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
        semantic_label = libraster.Rast_read_semantic_label(self.name, self.mapset)
        if semantic_label:
            return utils.decode(semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
        return None

    @must_be_in_current_mapset
    def _set_semantic_label(self, semantic_label):
        """Set/Unset semantic label identifier.

        :param str semantic_label: semantic label to assign or None to remove (unset)
        """
        if semantic_label:
            if libraster.Rast_legal_semantic_label(semantic_label) is False:
                raise ValueError(_("Invalid semantic label"))
            libraster.Rast_write_semantic_label(self.name, semantic_label)
        else:
            libgis.G_remove_misc("cell_misc", "semantic_label", self.name)

<<<<<<< HEAD
    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
    semantic_label = property(_get_semantic_label, _set_semantic_label)
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
        return None

    @must_be_in_current_mapset
    def _set_bandref(self, bandref):
        """Set/Unset band reference identifier.

        :param str bandref: band reference to assign or None to remove (unset)
        """
        if bandref:
            if libraster.Rast_legal_bandref(bandref) < 0:
                raise ValueError(_("Invalid band reference"))
            libraster.Rast_write_bandref(self.name, bandref)
        else:
            libgis.G_remove_misc("cell_misc", "bandref", self.name)

    bandref = property(_get_bandref, _set_bandref)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))

    def _get_units(self):
        units = libraster.Rast_read_units(self.name, self.mapset)
        if units:
            return utils.decode(units)
        return None

    @must_be_in_current_mapset
    def _set_units(self, units):
        libraster.Rast_write_units(self.name, units)

    units = property(_get_units, _set_units)

    def _get_vdatum(self):
        vdatum = libraster.Rast_read_vdatum(self.name, self.mapset)
        if vdatum:
            return utils.decode(vdatum)
        return None

    @must_be_in_current_mapset
    def _set_vdatum(self, vdatum):
        libraster.Rast_write_vdatum(self.name, vdatum)

    vdatum = property(_get_vdatum, _set_vdatum)

    def __repr__(self):
        return INFO.format(
            name=self.name,
            mapset=self.mapset,
            rows=self.rows,
            cols=self.cols,
            north=self.north,
            south=self.south,
            east=self.east,
            west=self.west,
            top=self.top,
            bottom=self.bottom,
            nsres=self.nsres,
            ewres=self.ewres,
            tbres=self.tbres,
            zone=self.zone,
            proj=self.proj,
            min=self.min,
            max=self.max,
        )

    def keys(self):
        return [
            "name",
            "mapset",
            "rows",
            "cols",
            "north",
            "south",
            "east",
            "west",
            "top",
            "bottom",
            "nsres",
            "ewres",
            "tbres",
            "zone",
            "proj",
            "min",
            "max",
        ]

    def items(self):
        return [(k, getattr(self, k)) for k in self.keys()]

    def __iter__(self):
        return ((k, getattr(self, k)) for k in self.keys())

    def _repr_html_(self):
        return dict2html(dict(self.items()), keys=self.keys(), border="1", kdec="b")


class RasterAbstractBase:
    """Raster_abstract_base: The base class from which all sub-classes
    inherit. It does not implement any row or map access methods:

    * Implements raster metadata information access (Type, ...)
    * Implements an open method that will be overwritten by the sub-classes
    * Implements the close method that might be overwritten by sub-classes
      (should work for simple row access)
    * Implements get and set region methods
    * Implements color, history and category handling
    * Renaming, deletion, ...

    """

    def __init__(self, name, mapset="", *aopen, **kwopen):
        """The constructor need at least the name of the map
        *optional* field is the `mapset`.

        >>> ele = RasterAbstractBase(test_raster_name)
        >>> ele.name
        'abstract_test_map'
        >>> ele.exist()
        True

        ..
        """
        self.mapset = mapset
        if not mapset:
            # note that @must_be_in_current_mapset requires mapset to be set
            mapset = libgis.G_find_raster(name, mapset)
            if mapset is not None:
                self.mapset = utils.decode(mapset)

        self._name = name
        # Private attribute `_fd` that return the file descriptor of the map
        self._fd = None
        # Private attribute `_rows` that return the number of rows
        # in active window, When the class is instanced is empty and it is set
        # when you open the file, using Rast_window_rows()
        self._rows = None
        # Private attribute `_cols` that return the number of rows
        # in active window, When the class is instanced is empty and it is set
        # when you open the file, using Rast_window_cols()
        self._cols = None
        # self.region = Region()
        self.hist = History(self.name, self.mapset)
        self.cats = Category(self.name, self.mapset)
        self.info = Info(self.name, self.mapset)
        self._aopen = aopen
        self._kwopen = kwopen
        self._mtype = "CELL"
        self._mode = "r"
        self._overwrite = False

    def __enter__(self):
        self.open(*self._aopen, **self._kwopen)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def _get_mtype(self):
        """Private method to get the Raster type"""
        return self._mtype

    def _set_mtype(self, mtype):
        """Private method to change the Raster type"""
        if mtype.upper() not in {"CELL", "FCELL", "DCELL"}:
            str_err = "Raster type: {0} not supported ('CELL','FCELL','DCELL')"
            raise ValueError(_(str_err).format(mtype))
        self._mtype = mtype
        self._gtype = RTYPE[self.mtype]["grass type"]

    mtype = property(fget=_get_mtype, fset=_set_mtype)

    def _get_mode(self):
        return self._mode

    def _set_mode(self, mode):
        if mode.upper() not in {"R", "W"}:
            str_err = _("Mode type: {0} not supported ('r', 'w')")
            raise ValueError(str_err.format(mode))
        self._mode = mode

    mode = property(fget=_get_mode, fset=_set_mode)

    def _get_overwrite(self):
        return self._overwrite

    def _set_overwrite(self, overwrite):
        if overwrite not in {True, False}:
            str_err = _("Overwrite type: {0} not supported (True/False)")
            raise ValueError(str_err.format(overwrite))
        self._overwrite = overwrite

    overwrite = property(fget=_get_overwrite, fset=_set_overwrite)

    def _get_name(self):
        """Private method to return the Raster name"""
        return self._name

    def _set_name(self, newname):
        """Private method to change the Raster name"""
        if not utils.is_clean_name(newname):
            str_err = _("Map name {0} not valid")
            raise ValueError(str_err.format(newname))
        if self.exist():
            self.rename(newname)
        self._name = newname

    name = property(fget=_get_name, fset=_set_name)

    @must_be_open
    def _get_cats_title(self):
        return self.cats.title

    @must_be_open
    def _set_cats_title(self, newtitle):
        self.cats.title = newtitle

    cats_title = property(fget=_get_cats_title, fset=_set_cats_title)

    def __unicode__(self):
        return self.name_mapset()

    def __str__(self):
        """Return the string of the object"""
        return self.__unicode__()

    def __len__(self):
        return self._rows

    def __getitem__(self, key):
        """Return the row of Raster object, slice allowed."""
        if isinstance(key, slice):
            # Get the start, stop, and step from the slice
            return (self.get_row(ii) for ii in range(*key.indices(len(self))))
        if isinstance(key, tuple):
            x, y = key
            return self.get(x, y)
        if isinstance(key, int):
            if not self.is_open():
                raise IndexError("Can not operate on a closed map. Call open() first.")
            if key < 0:  # Handle negative indices
                key += self._rows
            if key >= self._rows:
                raise IndexError(
                    "The row index {0} is out of range [0, {1}).".format(
                        key, self._rows
                    )
                )
            return self.get_row(key)
        fatal("Invalid argument type.")

    def __iter__(self):
        """Return a constructor of the class"""
        return (self.__getitem__(irow) for irow in range(self._rows))

    def _repr_png_(self):
        return raw_figure(utils.r_export(self))

    def exist(self):
        """Return True if the map already exist, and
        set the mapset if were not set.

        call the C function `G_find_raster`.

        >>> ele = RasterAbstractBase(test_raster_name)
        >>> ele.exist()
        True
        """
        if self.name:
            if self.mapset == "":
                mapset = utils.get_mapset_raster(self.name, self.mapset)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                self.mapset = mapset if mapset else ""
=======
                self.mapset = mapset or ""
>>>>>>> main
=======
                self.mapset = mapset or ""
=======
                self.mapset = mapset if mapset else ""
>>>>>>> 9a2b1d234a (style: Fix if-expr-with-true-false (SIM210) and if-expr-with-false-true (SIM211) (#3999))
>>>>>>> a2f268d57b (style: Fix if-expr-with-true-false (SIM210) and if-expr-with-false-true (SIM211) (#3999))
=======
                self.mapset = mapset or ""
=======
                self.mapset = mapset if mapset else ""
>>>>>>> 9a2b1d234a (style: Fix if-expr-with-true-false (SIM210) and if-expr-with-false-true (SIM211) (#3999))
>>>>>>> 15e8e3a5c5 (style: Fix if-expr-with-true-false (SIM210) and if-expr-with-false-true (SIM211) (#3999))
                return bool(mapset)
            return bool(utils.get_mapset_raster(self.name, self.mapset))
        return False

    def is_open(self):
        """Return True if the map is open False otherwise.

        >>> ele = RasterAbstractBase(test_raster_name)
        >>> ele.is_open()
        False

        """
        return bool(self._fd is not None and self._fd >= 0)

    @must_be_open
    def close(self):
        """Close the map"""
        libraster.Rast_close(self._fd)
        # update rows and cols attributes
        self._rows = None
        self._cols = None
        self._fd = None

    def remove(self):
        """Remove the map"""
        if self.is_open():
            self.close()
        utils.remove(self.name, "rast")

    def fullname(self):
        """Return the full name of a raster map: name@mapset"""
        return "{name}@{mapset}".format(name=self.name, mapset=self.mapset)

    def name_mapset(self, name=None, mapset=None):
        """Return the full name of the Raster.

        >>> ele = RasterAbstractBase(test_raster_name)
        >>> name = ele.name_mapset().split("@")
        >>> name
        ['abstract_test_map']

        """
        if name is None:
            name = self.name
        if mapset is None:
            self.exist()
            mapset = self.mapset

        gis_env = gisenv()

        if mapset and mapset != gis_env["MAPSET"]:
            return "{name}@{mapset}".format(name=name, mapset=mapset)
        return name

    def rename(self, newname):
        """Rename the map"""
        if self.exist():
            utils.rename(self.name, newname, "rast")
        self._name = newname

    def set_region_from_rast(self, rastname="", mapset=""):
        """Set the computational region from a map,
        if rastername and mapset is not specify, use itself.
        This region will be used by all
        raster map layers that are opened in the same process.

        The GRASS region settings will not be modified.

        call C function `Rast_get_cellhd`, `Rast_set_window`

        """
        if self.is_open():
            fatal("You cannot change the region if map is open")
            raise
        region = Region()
        if rastname == "":
            rastname = self.name
        if mapset == "":
            mapset = self.mapset

        libraster.Rast_get_cellhd(rastname, mapset, region.byref())
        self._set_raster_window(region)

    def set_region(self, region):
        """Set the computational region that can be different from the
        current region settings. This region will be used by all
        raster map layers that are opened in the same process.

        The GRASS region settings will not be modified.
        """
        if self.is_open():
            fatal("You cannot change the region if map is open")
            raise
        self._set_raster_window(region)

    def _set_raster_window(self, region):
        libraster.Rast_set_window(region.byref())
        # update rows and cols attributes
        self._rows = libraster.Rast_window_rows()
        self._cols = libraster.Rast_window_cols()

    @must_be_open
    def get_value(self, point, region=None):
        """This method returns the pixel value of a given pair of coordinates:

        :param point: pair of coordinates in tuple object or class object with coords()
            method
        """
        # Check for tuple
        if not isinstance(point, list) and not isinstance(point, tuple):
            point = point.coords()

        if not region:
            region = Region()
        row, col = utils.coor2pixel(point, region)
        if col < 0 or col > region.cols or row < 0 or row > region.rows:
            return None
        line = self.get_row(int(row))
        return line[int(col)]

    @must_be_open
    def has_cats(self):
        """Return True if the raster map has categories"""
        if self.exist():
            self.cats.read()
            if len(self.cats) != 0:
                return True
        return False

    @must_be_open
    def num_cats(self):
        """Return the number of categories"""
        return len(self.cats)

    @must_be_open
    def copy_cats(self, raster):
        """Copy categories from another raster map object"""
        self.cats.copy(raster.cats)

    @must_be_open
    def sort_cats(self):
        """Sort categories order by range"""
        self.cats.sort()

    @must_be_open
    def read_cats(self):
        """Read category from the raster map file"""
        self.cats.read(self)

    @must_be_open
    def write_cats(self):
        """Write category to the raster map file"""
        self.cats.write(self)

    @must_be_open
    def read_cats_rules(self, filename, sep=":"):
        """Read category from the raster map file"""
        self.cats.read_rules(filename, sep)

    @must_be_open
    def write_cats_rules(self, filename, sep=":"):
        """Write category to the raster map file"""
        self.cats.write_rules(filename, sep)

    @must_be_open
    def get_cats(self):
        """Return a category object"""
        cat = Category(name=self.name, mapset=self.mapset)
        cat.read()
        return cat

    @must_be_open
    def set_cats(self, category):
        """The internal categories are copied from this object."""
        self.cats.copy(category)

    @must_be_open
    def get_cat(self, label):
        """Return a category given an index or a label"""
        return self.cats[label]

    @must_be_open
    def set_cat(self, label, min_cat, max_cat=None, index=None):
        """Set or update a category"""
        self.cats.set_cat(index, (label, min_cat, max_cat))


if __name__ == "__main__":
    import doctest
    from grass.pygrass.modules import Module

    Module("g.region", n=40, s=0, e=40, w=0, res=10)
    Module(
        "r.mapcalc",
        expression="%s = row() + (10 * col())" % (test_raster_name),
        overwrite=True,
    )

    doctest.testmod()

    """Remove the generated vector map, if exist"""
    mset = utils.get_mapset_raster(test_raster_name, mapset="")
    if mset:
        Module("g.remove", flags="f", type="raster", name=test_raster_name)
