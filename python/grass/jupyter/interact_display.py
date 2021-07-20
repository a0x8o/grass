#
# AUTHOR(S): Caitlin Haedrich <caitlin DOT haedrich AT gmail>
#
# PURPOSE:   This module contains functions for interactive display
#            in Jupyter Notebooks.
#
# COPYRIGHT: (C) 2021 Caitlin Haedrich, and by the GRASS Development Team
#
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
=======
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.

import os
import sys
import tempfile
import weakref
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 2f4b0e227d (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 4a4e8d0c8b (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 5e764f6bfd (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> f3a0d5f10c (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> 40f77bd087 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 91ac389e42 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
>>>>>>> 3774f705e0 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 6b7b02b03b (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 6711551a1e (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 160d954222 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 4c2a8e0e3c (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> ebd8d6c4e0 (libraster: fix Rast_legal_bandref() (#1796))
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """

        import folium

        self._folium = folium
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
#            This program is free software under the GNU Gernal Public
#            License (>=v2). Read teh file COPYING that comes with GRASS
=======
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
#            for details.

import os
import sys
import tempfile
import weakref
from pathlib import Path
import folium
=======
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

<<<<<<< HEAD
        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        import folium

        self._folium = folium
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
#            This program is free software under the GNU Gernal Public
#            License (>=v2). Read teh file COPYING that comes with GRASS
=======
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
#            for details.

import os
import sys
import tempfile
import weakref
from pathlib import Path
import folium
=======
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

<<<<<<< HEAD
        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        import folium

        self._folium = folium
=======
<<<<<<< HEAD
#            This program is free software under the GNU Gernal Public
#            License (>=v2). Read teh file COPYING that comes with GRASS
=======
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
#            for details.

import os
import sys
import tempfile
import weakref
from pathlib import Path
import folium
=======
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

<<<<<<< HEAD
        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        import folium

        self._folium = folium
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
#            This program is free software under the GNU Gernal Public
#            License (>=v2). Read teh file COPYING that comes with GRASS
=======
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
>>>>>>> ee253be79a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
#            for details.

import os
import sys
import tempfile
import weakref
from pathlib import Path
import folium
=======
>>>>>>> 07c04c0cb0 (libraster: fix Rast_legal_bandref() (#1796))
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

<<<<<<< HEAD
        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """
>>>>>>> ee253be79a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        import folium

        self._folium = folium
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
#            This program is free software under the GNU Gernal Public
#            License (>=v2). Read teh file COPYING that comes with GRASS
<<<<<<< HEAD
<<<<<<< HEAD
=======
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
#            for details.

import os
import sys
import tempfile
import weakref
from pathlib import Path
import folium
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

<<<<<<< HEAD
        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        import folium

        self._folium = folium
=======
#            This program is free software under the GNU Gernal Public
#            License (>=v2). Read teh file COPYING that comes with GRASS
=======
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
#            for details.

import os
import sys
import tempfile
import weakref
from pathlib import Path
import folium
=======
>>>>>>> 29f5805aab (libraster: fix Rast_legal_bandref() (#1796))
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

<<<<<<< HEAD
        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        import folium

        self._folium = folium
=======
#            This program is free software under the GNU Gernal Public
#            License (>=v2). Read teh file COPYING that comes with GRASS
=======
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
#            for details.

import os
import sys
import tempfile
import weakref
from pathlib import Path
import folium
=======
>>>>>>> ab87aab656 (libraster: fix Rast_legal_bandref() (#1796))
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

<<<<<<< HEAD
        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        import folium

        self._folium = folium
=======
#            This program is free software under the GNU Gernal Public
#            License (>=v2). Read teh file COPYING that comes with GRASS
=======
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
#            for details.

import os
import sys
import tempfile
import weakref
from pathlib import Path
import folium
=======
>>>>>>> d039fa87a3 (libraster: fix Rast_legal_bandref() (#1796))
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

<<<<<<< HEAD
        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        import folium

        self._folium = folium
=======
=======
=======
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
#            for details.

import os
import sys
import tempfile
import weakref
from pathlib import Path
import folium
=======
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

<<<<<<< HEAD
        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        import folium

        self._folium = folium
=======
#            This program is free software under the GNU Gernal Public
#            License (>=v2). Read teh file COPYING that comes with GRASS
=======
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
#            for details.

import os
import sys
import tempfile
import weakref
from pathlib import Path
import folium
=======
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

<<<<<<< HEAD
        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        import folium

        self._folium = folium
=======
#            This program is free software under the GNU Gernal Public
#            License (>=v2). Read teh file COPYING that comes with GRASS
=======
<<<<<<< HEAD
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
#            for details.

import os
import sys
import tempfile
import weakref
from pathlib import Path
import folium
=======
>>>>>>> fb5abcdf0c (libraster: fix Rast_legal_bandref() (#1796))
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

<<<<<<< HEAD
        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        import folium

        self._folium = folium
=======
>>>>>>> osgeo-main
=======
#            This program is free software under the GNU Gernal Public
#            License (>=v2). Read teh file COPYING that comes with GRASS
=======
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
#            for details.

import os
import sys
import tempfile
import weakref
from pathlib import Path
import folium
=======
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

<<<<<<< HEAD
        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        import folium

        self._folium = folium
=======
#            This program is free software under the GNU Gernal Public
#            License (>=v2). Read teh file COPYING that comes with GRASS
=======
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
#            for details.

import os
import sys
import tempfile
import weakref
from pathlib import Path
import folium
=======
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

<<<<<<< HEAD
        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        import folium

        self._folium = folium
=======
#            This program is free software under the GNU Gernal Public
#            License (>=v2). Read teh file COPYING that comes with GRASS
#            for details.

import os
from pathlib import Path

import folium

import grass.script as gs


class InteractiveMap:
    """This class creates interative GRASS maps with folium"""

    def __init__(self, width=400, height=400):
        """This initiates a folium map centered on g.region.

        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))

        # Store height and width
        self.width = width
        self.height = height
        # Make temporary folder for all our files
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
<<<<<<< HEAD
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
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
>>>>>>> ee253be79a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        self._tmp_dir = tempfile.TemporaryDirectory()

        # Remember original environment; all environments used
        # in this class are derived from this one
        self._src_env = os.environ.copy()

        # Set up temporary locations  in WGS84 and Pseudo-Mercator
        # We need two because folium uses WGS84 for vectors and coordinates
        # and Pseudo-Mercator for raster overlays
        self.rcfile_psmerc, self._psmerc_env = setup_location(
            "psmerc", self._tmp_dir.name, "3857", self._src_env
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
        self.map = self._folium.Map(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
        self.tmp_dir = Path("./tmp/")
        try:
            os.mkdir(self.tmp_dir)
        except FileExistsError:
            pass
        # Create new environment for tmp WGS84 location
        rcfile, self._vector_env = gs.create_environment(
            self.tmp_dir, "temp_folium_WGS84", "PERMANENT"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
<<<<<<< HEAD
        self.map = folium.Map(
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        self.map = self._folium.Map(
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
<<<<<<< HEAD
        self.map = folium.Map(
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        self.map = self._folium.Map(
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
=======
<<<<<<< HEAD
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
<<<<<<< HEAD
        self.map = folium.Map(
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        self.map = self._folium.Map(
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
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
>>>>>>> ee253be79a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
<<<<<<< HEAD
        self.map = folium.Map(
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        self.map = self._folium.Map(
>>>>>>> 07c04c0cb0 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
<<<<<<< HEAD
        self.map = folium.Map(
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        self.map = self._folium.Map(
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 2f4b0e227d (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
<<<<<<< HEAD
        self.map = folium.Map(
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        self.map = self._folium.Map(
>>>>>>> 29f5805aab (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 4a4e8d0c8b (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
<<<<<<< HEAD
        self.map = folium.Map(
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        self.map = self._folium.Map(
>>>>>>> ab87aab656 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 5e764f6bfd (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
<<<<<<< HEAD
        self.map = folium.Map(
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
        self.map = self._folium.Map(
>>>>>>> d039fa87a3 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> f3a0d5f10c (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
<<<<<<< HEAD
        self.map = folium.Map(
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
        self.map = self._folium.Map(
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 4c2a8e0e3c (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> ebd8d6c4e0 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
<<<<<<< HEAD
        self.map = folium.Map(
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        self.map = self._folium.Map(
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 40f77bd087 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
<<<<<<< HEAD
        self.map = folium.Map(
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        self.map = self._folium.Map(
>>>>>>> fb5abcdf0c (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 91ac389e42 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
<<<<<<< HEAD
        self.map = folium.Map(
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
        self.map = self._folium.Map(
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 6711551a1e (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 160d954222 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
<<<<<<< HEAD
        self.map = folium.Map(
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
        self.map = self._folium.Map(
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 3774f705e0 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 6b7b02b03b (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
        )
        # Location and mapset and region
        gs.create_location(
            self.tmp_dir, "temp_folium_WGS84", epsg="4326", overwrite=True
        )
        self._extent = self._convert_extent(
            env=os.environ
        )  # Get the extent of the original area in WGS84
        # Set region to match original region extent
        gs.run_command(
            "g.region",
            n=self._extent["north"],
            s=self._extent["south"],
            e=self._extent["east"],
            w=self._extent["west"],
            env=self._vector_env,
        )
        # Get Center of tmp GRASS region
        center = gs.parse_command("g.region", flags="cg", env=self._vector_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))
        # Create Folium Map
        self.map = folium.Map(
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
            width=self.width,
            height=self.height,
            location=center,
            tiles="cartodbpositron",
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
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
=======
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        # Set LayerControl default
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
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
=======
        # Create LayerControl default
=======
        # Set LayerControl default
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
        )
<<<<<<< HEAD
=======
        # Create LayerControl default
=======
        # Set LayerControl default
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
        )
<<<<<<< HEAD
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        # Create LayerControl default
=======
        # Set LayerControl default
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
        )
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        # Create LayerControl default
=======
        # Set LayerControl default
>>>>>>> ee253be79a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
        )
<<<<<<< HEAD
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        # Create LayerControl default
<<<<<<< HEAD
<<<<<<< HEAD
=======
        # Set LayerControl default
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
        )
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
        # Create LayerControl default
=======
        # Set LayerControl default
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
        )
<<<<<<< HEAD
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        # Create LayerControl default
=======
        # Set LayerControl default
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
        )
<<<<<<< HEAD
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        # Create LayerControl default
=======
        # Set LayerControl default
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
        )
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
        # Set LayerControl default
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
        )
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
        # Create LayerControl default
=======
        # Set LayerControl default
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
        )
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        # Create LayerControl default
=======
        # Set LayerControl default
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
        )
<<<<<<< HEAD
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
        # Create LayerControl default
=======
        # Set LayerControl default
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
        )
<<<<<<< HEAD
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
        # Create LayerControl default
=======
        # Set LayerControl default
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
        )
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        # Create LayerControl default
        self.layer_control = False

    def _convert_coordinates(self, x, y, proj_in):
        """This function reprojects coordinates to WGS84, the required
        projection for vectors in folium.

        Arguments:
            x -- x coordinate (string)
            y -- y coordinate (string)
            proj_in -- proj4 string of location (for example, the output
            of g.region run with the `g` flag."""

        # Reformat input
        coordinates = f"{x}, {y}"
        # Reproject coordinates
        coords_folium = gs.read_command(
            "m.proj",
            coordinates=coordinates,
            proj_in=proj_in,
            separator="comma",
            flags="do",
        )
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
        # Reformat from string to array
        coords_folium = coords_folium.strip()  # Remove '\n' at end of string
        coords_folium = coords_folium.split(",")  # Split on comma
        coords_folium = [float(value) for value in coords_folium]  # Convert to floats
        return coords_folium[1], coords_folium[0]  # Return Lat and Lon

    def _convert_extent(self, env=None):
        """This function returns the bounding box of the current region
        in WGS84, the required projection for folium"""

        # Get proj of current GRASS region
        proj = gs.read_command("g.proj", flags="jf", env=env)
        # Get extent
        extent = gs.parse_command("g.region", flags="g", env=env)
        # Convert extent to EPSG:3857, required projection for Folium
        north, east = self._convert_coordinates(extent["e"], extent["n"], proj)
        south, west = self._convert_coordinates(extent["w"], extent["s"], proj)
        extent = {"north": north, "south": south, "east": east, "west": west}
        return extent

    def _folium_bounding_box(self, extent):
        """Reformats extent into bounding box to pass to folium"""
        return [[extent["north"], extent["west"]], [extent["south"], extent["east"]]]
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
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
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ee253be79a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))

    def add_vector(self, name):
        """Imports vector into temporary WGS84 location,
        re-formats to a GeoJSON and adds to folium map.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
=======
        Arguments:
            name -- a positional-only parameter; name of vector to be added
            to map as a string"""
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> osgeo-main
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> osgeo-main
=======
        Arguments:
            name -- a positional-only parameter; name of vector to be added
            to map as a string"""
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
<<<<<<< HEAD
        Arguments:
            name -- a positional-only parameter; name of vector to be added
            to map as a string"""
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> osgeo-main
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> osgeo-main
>>>>>>> main
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> osgeo-main
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> osgeo-main
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> osgeo-main
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> osgeo-main
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> osgeo-main
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> osgeo-main
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> osgeo-main
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> osgeo-main
=======
        Arguments:
            name -- a positional-only parameter; name of vector to be added
            to map as a string"""
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> ee253be79a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> osgeo-main
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> osgeo-main
=======
=======
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
        Arguments:
            name -- a positional-only parameter; name of vector to be added
            to map as a string"""
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
        Arguments:
            name -- a positional-only parameter; name of vector to be added
            to map as a string"""
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
        Arguments:
            name -- a positional-only parameter; name of vector to be added
            to map as a string"""
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
        Arguments:
            name -- a positional-only parameter; name of vector to be added
            to map as a string"""
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
        Arguments:
            name -- a positional-only parameter; name of vector to be added
            to map as a string"""
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
<<<<<<< HEAD
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> osgeo-main
=======
        Arguments:
            name -- a positional-only parameter; name of vector to be added
            to map as a string"""
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
        Arguments:
            name -- a positional-only parameter; name of vector to be added
            to map as a string"""
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
        Arguments:
            name -- a positional-only parameter; name of vector to be added
            to map as a string"""
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))

        # Find full name of vector
        file_info = gs.find_file(name, element="vector")
        full_name = file_info["fullname"]
        name = file_info["name"]
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2f4b0e227d (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4a4e8d0c8b (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5e764f6bfd (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> f3a0d5f10c (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 40f77bd087 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 91ac389e42 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
=======
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 3774f705e0 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 6b7b02b03b (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6711551a1e (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 160d954222 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4c2a8e0e3c (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> ebd8d6c4e0 (libraster: fix Rast_legal_bandref() (#1796))
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
        """This function returns a folium figure object with a GRASS raster
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
<<<<<<< HEAD
        """This function creates a folium map with a GRASS raster
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        """This function returns a folium figure object with a GRASS raster
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
<<<<<<< HEAD
        """This function creates a folium map with a GRASS raster
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        """This function returns a folium figure object with a GRASS raster
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
=======
<<<<<<< HEAD
=======
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
<<<<<<< HEAD
        """This function creates a folium map with a GRASS raster
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        """This function returns a folium figure object with a GRASS raster
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
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
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
>>>>>>> 07c04c0cb0 (libraster: fix Rast_legal_bandref() (#1796))
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
<<<<<<< HEAD
        """This function creates a folium map with a GRASS raster
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        """This function returns a folium figure object with a GRASS raster
>>>>>>> 07c04c0cb0 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
<<<<<<< HEAD
        """This function creates a folium map with a GRASS raster
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        """This function returns a folium figure object with a GRASS raster
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 2f4b0e227d (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
>>>>>>> 29f5805aab (libraster: fix Rast_legal_bandref() (#1796))
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
<<<<<<< HEAD
        """This function creates a folium map with a GRASS raster
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        """This function returns a folium figure object with a GRASS raster
>>>>>>> 29f5805aab (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 4a4e8d0c8b (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
>>>>>>> ab87aab656 (libraster: fix Rast_legal_bandref() (#1796))
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
<<<<<<< HEAD
        """This function creates a folium map with a GRASS raster
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        """This function returns a folium figure object with a GRASS raster
>>>>>>> ab87aab656 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 5e764f6bfd (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
>>>>>>> d039fa87a3 (libraster: fix Rast_legal_bandref() (#1796))
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
<<<<<<< HEAD
        """This function creates a folium map with a GRASS raster
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
        """This function returns a folium figure object with a GRASS raster
>>>>>>> d039fa87a3 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> f3a0d5f10c (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
=======
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 4c2a8e0e3c (libraster: fix Rast_legal_bandref() (#1796))
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
<<<<<<< HEAD
        """This function creates a folium map with a GRASS raster
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
        """This function returns a folium figure object with a GRASS raster
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 4c2a8e0e3c (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> ebd8d6c4e0 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
<<<<<<< HEAD
        """This function creates a folium map with a GRASS raster
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        """This function returns a folium figure object with a GRASS raster
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 40f77bd087 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
<<<<<<< HEAD
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
>>>>>>> fb5abcdf0c (libraster: fix Rast_legal_bandref() (#1796))
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
<<<<<<< HEAD
        """This function creates a folium map with a GRASS raster
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        """This function returns a folium figure object with a GRASS raster
>>>>>>> fb5abcdf0c (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 91ac389e42 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> osgeo-main
=======
=======
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
<<<<<<< HEAD
        """This function creates a folium map with a GRASS raster
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
        """This function returns a folium figure object with a GRASS raster
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 6711551a1e (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 160d954222 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
=======
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
<<<<<<< HEAD
        """This function creates a folium map with a GRASS raster
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
        """This function returns a folium figure object with a GRASS raster
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 3774f705e0 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 6b7b02b03b (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=os.environ)
        gs.run_command(
            "v.proj",
            input=full_name,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._vector_env,
        )
        # Convert to GeoJSON
        json_file = self.tmp_dir / f"tmp_{name}.json"
        gs.run_command(
            "v.out.ogr",
            input=name,
            output=json_file,
            format="GeoJSON",
            env=self._vector_env,
        )
        # Import GeoJSON to folium and add to map
        folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_layer_control(self, **kwargs):
        self.layer_control = True
        self.layer_control_object = folium.LayerControl(**kwargs)

    def show(self):
        """This function creates a folium map with a GRASS raster
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
        overlayed on a basemap.

        If map has layer control enabled, additional layers cannot be
        added after calling show()."""

        if self.layer_control:
            self.map.add_child(self.layer_control_object)
        # Create Figure
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        fig = self._folium.Figure(width=self.width, height=self.height)
=======
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> osgeo-main
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> osgeo-main
=======
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
=======
<<<<<<< HEAD
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> osgeo-main
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> osgeo-main
>>>>>>> main
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> osgeo-main
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> osgeo-main
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> osgeo-main
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> osgeo-main
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> osgeo-main
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> osgeo-main
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> osgeo-main
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> osgeo-main
=======
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> 07c04c0cb0 (libraster: fix Rast_legal_bandref() (#1796))
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> osgeo-main
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> osgeo-main
=======
=======
>>>>>>> 2f4b0e227d (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4a4e8d0c8b (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 5e764f6bfd (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> f3a0d5f10c (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ebd8d6c4e0 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 40f77bd087 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 91ac389e42 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6b7b02b03b (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6711551a1e (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 160d954222 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 3774f705e0 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 6b7b02b03b (libraster: fix Rast_legal_bandref() (#1796))
        fig = self._folium.Figure(width=self.width, height=self.height)
=======
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 2f4b0e227d (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> 29f5805aab (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 4a4e8d0c8b (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> ab87aab656 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 5e764f6bfd (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> d039fa87a3 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> f3a0d5f10c (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
>>>>>>> 4c2a8e0e3c (libraster: fix Rast_legal_bandref() (#1796))
        fig = self._folium.Figure(width=self.width, height=self.height)
=======
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 4c2a8e0e3c (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> ebd8d6c4e0 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 40f77bd087 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
<<<<<<< HEAD
>>>>>>> fb5abcdf0c (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 91ac389e42 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> osgeo-main
=======
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 6711551a1e (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 160d954222 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
        fig = self._folium.Figure(width=self.width, height=self.height)
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 3774f705e0 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 6b7b02b03b (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
        # Add map to figure
        fig.add_child(self.map)

        return fig
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
<<<<<<< HEAD
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
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
>>>>>>> ee253be79a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

    def save(self, filename):
        """Save map as an html map.

        :param str filename: name of html file
        """
        self.map.save(filename)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
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
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> ee253be79a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
<<<<<<< HEAD
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
