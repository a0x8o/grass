#!/usr/bin/env python

############################################################################
#
# NAME:      interactivemap_test.py
#
# AUTHOR:    Caitlin Haedrich (caitlin dot haedrich gmail com)
#
# PURPOSE:   This is a test script for grass.jupyter's InteractiveMap
#
# COPYRIGHT: (C) 2021 by Caitlin Haedrich and the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.
#
#############################################################################


import os
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
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
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
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
import sys
import unittest
from pathlib import Path

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
import unittest
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
import sys
import unittest
from pathlib import Path
<<<<<<< HEAD
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
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
import unittest
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
import sys
import unittest
from pathlib import Path
<<<<<<< HEAD
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
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
import unittest
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
import sys
import unittest
from pathlib import Path
<<<<<<< HEAD
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
import unittest
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
import sys
import unittest
from pathlib import Path
<<<<<<< HEAD
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
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
import grass.jupyter as gj
from grass.gunittest.case import TestCase
from grass.gunittest.main import test


def can_import_folium():
    """Test folium import to see if test can be run."""
    try:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        import folium  # noqa
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        import folium  # noqa
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
        import folium  # noqa
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
        import folium  # noqa
=======
>>>>>>> osgeo-main
=======
        import folium  # noqa
=======
>>>>>>> osgeo-main
=======
        import folium  # noqa
=======
>>>>>>> osgeo-main
=======
        import folium  # noqa
=======
>>>>>>> osgeo-main
=======
        import folium  # noqa
=======
>>>>>>> osgeo-main
=======
        import folium  # noqa
=======
>>>>>>> osgeo-main
=======
        import folium  # noqa
=======
>>>>>>> osgeo-main
=======
        import folium  # noqa
=======
>>>>>>> osgeo-main
=======
        import folium  # noqa
=======
>>>>>>> osgeo-main
=======
        import folium  # noqa
=======
>>>>>>> osgeo-main
=======
        import folium  # noqa
=======
>>>>>>> osgeo-main
=======
        import folium  # noqa
=======
>>>>>>> osgeo-main
        import folium
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
=======
        import folium  # noqa
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        import folium  # noqa
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
        import folium  # noqa
=======
        import folium
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
        import folium  # noqa
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        import folium  # noqa
=======
        import folium
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
        import folium  # noqa
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        import folium  # noqa
=======
        import folium
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
        import folium  # noqa
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

        return True
    except ImportError:
        return False


def can_import_ipyleaflet():
    """Test ipyleaflet import to see if test can be run."""
    try:
        import ipyleaflet  # noqa
>>>>>>> osgeo-main

        return True
    except ImportError:
        return False


class TestDisplay(TestCase):
    # Setup variables
    files = []

    @classmethod
    def setUpClass(cls):
        """Ensures expected computational region"""
        # to not override mapset's region (which might be used by other tests)
        cls.use_temp_region()
        # cls.runModule or self.runModule is used for general module calls
        # we'll use the elevation raster as a test display
        cls.runModule("g.region", raster="elevation")

    @classmethod
    def tearDownClass(cls):
        """Remove temporary region"""
        cls.del_temp_region()

    def tearDown(self):
        """
        Remove the PNG file created after testing with "filename =" option.
        This is executed after each test run.
        """
        for f in self.files:
            f = Path(f)
            if sys.version_info < (3, 8):
                try:
                    os.remove(f)
                except FileNotFoundError:
                    pass
            else:
                f.unlink(missing_ok=True)

    @unittest.skipIf(not can_import_folium(), "Cannot import folium")
    def test_basic(self):
        # Create InteractiveMap
        interactive_map = gj.InteractiveMap()
        interactive_map.add_raster("elevation")
        interactive_map.add_vector("roadsmajor")
        interactive_map.show()

    @unittest.skipIf(not can_import_folium(), "Cannot import folium")
    def test_save_as_html(self):
        # Create InteractiveMap
        interactive_map = gj.InteractiveMap()
        interactive_map.add_vector("roadsmajor")
        filename = "InteractiveMap_test.html"
        self.files.append(filename)
        interactive_map.save(filename)
        self.assertFileExists(filename)

    @unittest.skipIf(not can_import_ipyleaflet(), "Cannot import ipyleaflet")
    def test_query_button(self):
        # Create InteractiveMap with ipyleaflet backend
        interactive_map = gj.InteractiveMap(map_backend="ipyleaflet")
        interactive_map.add_raster("elevation")
        button = interactive_map.setup_query_interface()
        self.assertIsNotNone(interactive_map._controllers[button].query_raster((0, 0)))

    @unittest.skipIf(not can_import_ipyleaflet(), "Cannot import ipyleaflet")
    def test_draw(self):
        """Test the draw_computational_region method."""
        # Create InteractiveMap
        interactive_map = gj.InteractiveMap(map_backend="ipyleaflet")
        button = interactive_map.setup_drawing_interface()
        interactive_map._controllers[button].activate()
        self.assertIsNotNone(interactive_map._controllers[button].save_button_control)

    @unittest.skipIf(not can_import_ipyleaflet(), "Cannot import ipyleaflet")
    def test_draw_computational_region(self):
        """Test the draw_computational_region method."""
        # Create InteractiveMap
        interactive_map = gj.InteractiveMap(map_backend="ipyleaflet")
        button = interactive_map.setup_computational_region_interface()
        interactive_map._controllers[button].activate()
        self.assertIsNotNone(interactive_map._controllers[button].save_button_control)


if __name__ == "__main__":
    test()
