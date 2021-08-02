# MODULE:    grass.jupyter.display
#
# AUTHOR(S): Caitlin Haedrich <caitlin DOT haedrich AT gmail>
#
# PURPOSE:   This module contains functions for non-interactive display
#            in Jupyter Notebooks
#
# COPYRIGHT: (C) 2021 Caitlin Haedrich, and by the GRASS Development Team
#
#           This program is free software under the GNU General Public
#           License (>=v2). Read the file COPYING that comes with GRASS
#           for details.

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import shutil
=======
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
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b88da686d1 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a7de541b7b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
import tempfile
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
<<<<<<< HEAD
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
>>>>>>> main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 07c04c0cb0 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
=======
=======
import shutil
>>>>>>> 686e3354a5 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
<<<<<<< HEAD
>>>>>>> b88da686d1 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
=======
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a7de541b7b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
from IPython.display import Image
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 7310acc566 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
from pathlib import Path
from IPython.display import Image
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
import tempfile
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a7de541b7b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
import grass.script as gs


class GrassRenderer:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b88da686d1 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
    """GrassRenderer creates and displays GRASS maps in
    Jupyter Notebooks.

    Elements are added to the display by calling GRASS display modules.

    Basic usage::
    >>> m = GrassRenderer()
    >>> m.run("d.rast", map="elevation")
    >>> m.run("d.legend", raster="elevation")
    >>> m.show()

    GRASS display modules can also be called by using the name of module
    as a class method and replacing "." with "_" in the name.

    Shortcut usage::
    >>> m = GrassRenderer()
    >>> m.d_rast(map="elevation")
    >>> m.d_legend(raster="elevation")
    >>> m.show()
    """
<<<<<<< HEAD
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
>>>>>>> b88da686d1 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))

    def __init__(
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self,
        height=400,
        width=600,
        filename=None,
        env=None,
        text_size=12,
        renderer="cairo",
<<<<<<< HEAD
    ):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        """Initiates an instance of the GrassRenderer class."""
=======
>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======
>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======
>>>>>>> osgeo-main

        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> osgeo-main
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> osgeo-main
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> osgeo-main

        # Copy Environment
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""

    def __init__(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self,
        height=400,
        width=600,
        filename=None,
        env=None,
        text_size=12,
        renderer="cairo",
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
<<<<<<< HEAD
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
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
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):

        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """

<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
        # Copy Environment
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 7310acc566 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""

    def __init__(
        self,
        height=400,
        width=600,
        filename=None,
        env=None,
        text_size=12,
        renderer="cairo",
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a7de541b7b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        if env:
            self._env = env.copy()
        else:
            self._env = os.environ.copy()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7310acc566 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a7de541b7b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        # Environment Settings
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

=======

=======
        # Environment Settings
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        # Environment Settings
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======

=======
        # Environment Settings
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======

=======
        # Environment Settings
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 7310acc566 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======

=======
        # Environment Settings
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
        self._filename = filename

        self.run("d.erase")

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 7310acc566 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a7de541b7b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    def run(self, module, **kwargs):
        """Run modules from "d." GRASS library"""
        # Check module is from display library then run
        if module[0] == "d":
            gs.run_command(module, env=self._env, **kwargs)
        else:
            raise ValueError("Module must begin with letter 'd'.")

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b88da686d1 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
    def __getattr__(self, name):
        """Parse attribute to GRASS display module. Attribute should be in
        the form 'd_module_name'. For example, 'd.rast' is called with 'd_rast'.
        """

        # Check to make sure format is correct
        if not name.startswith("d_"):
            raise AttributeError(_("Module must begin with 'd_'"))
        # Reformat string
        grass_module = name.replace("_", ".")
        # Assert module exists
        if not shutil.which(grass_module):
            raise AttributeError(_("Cannot find GRASS module {}").format(grass_module))

        def wrapper(**kwargs):
            # Run module
            self.run(grass_module, **kwargs)

        return wrapper

<<<<<<< HEAD
    def show(self):
        """Displays a PNG image of the map"""
        from IPython.display import Image

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
>>>>>>> b88da686d1 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
    def show(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

<<<<<<< HEAD
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
=======
<<<<<<< HEAD
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
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
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 07c04c0cb0 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
        """Displays a PNG image of the map (non-interactive)"""
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Displays a PNG image of the map"""
>>>>>>> 686e3354a5 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
<<<<<<< HEAD
>>>>>>> b88da686d1 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 2f4b0e227d (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
        """Displays a PNG image of the map (non-interactive)"""
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
        return Image(self._filename)
