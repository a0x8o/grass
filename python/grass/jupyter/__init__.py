<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
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
>>>>>>> 4625684fca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> cb0f743d05 (Add session initiations functions for Jupyter Notebooks (#1629))
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
>>>>>>> 40118f6d63 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 869427c771 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 9e134ec08d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 33ca8caf20 (Add session initiations functions for Jupyter Notebooks (#1629))
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
# MODULE:    grass.jupyter
#
# AUTHOR(S): Caitlin Haedrich <caitlin DOT haedrich AT gmail>
#            Vaclav Petras <wenzeslaus gmail com>
#            Anna Petrasova <kratochanna gmail com>
#
# PURPOSE:   Display classes and setup functions for running GRASS GIS
#            in Jupyter Notebooks
#
# COPYRIGHT: (C) 2021-2022 Caitlin Haedrich, and by the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.

"""The *grass.jupyter* is a convenient GRASS GIS interface for Jupyter notebooks.

Python is a great tool for data science and scientific computing. Jupyter_ is an
environment with computational notebooks which makes it even better tool for
analysis and workflow prototyping. Computational notebooks are documents combining
code, text, and results such as figures and tables. JupyterLab is an environment where
you interact with all these parts. You can install it locally on your machine or
use it online from some service provider.

The *grass.jupyter* subpackage improves the integration of GRASS GIS and Jupyter
notebooks compared to the standard Python API. The original version was written
as part of Google Summer of Code in 2021 and experimental version was included in
GRASS GIS 8.0. Since then, much more development happened adding better session
handling and rendering of additional data types.

Usage
=====

To start using it in a notebook, import the top level package with a convenient alias,
such as *gj*, like this::

>>> import grass.jupyter as gj

.. note::
    To import the package, you need to tell Python where the GRASS GIS Python package
    is unless you manually set this on your system or in the command line. Please, refer
    to the example notebooks linked below for an example of the full workflow.

.. note::
    On Windows, there is no system Python and GRASS GIS needs to use its own Python.
    Jupyter needs to be installed into that Python. Please, refer to the wiki_
    for Windows-specific instructions.

To use existing data, we start a GRASS session in an existing mapset::

>>> gj.init("grassdata/nc_basic_spm_grass7/user1")

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
.. note::
    Contrary to typical command line / GUI module usage, grass.jupyter
    enables output overwrite by default to align with behaviour of other
    Python packages and to allow repeated executions of the same cells and
    of the whole notebook. The default command line behaviour can be
    restored by setting GRASS_OVERWRITE environmental variable to "0" after
    `gj.init()` call: `os.environ["GRASS_OVERWRITE"] = "0"`.

=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
All classes and functions for interaction in notebooks are now available under *gj*,
for example we can display a map with a selected raster and vector::

>>> streams_map = gj.Map()
>>> streams_map.d_rast(map="elevation")
>>> streams_map.d_vect(map="streams")
>>> streams_map.show()

Other classes and functions are described below and in the example notebooks.
Static HTML versions of the example notebooks are available on GitHub_
and interactive ones with live code are available on Binder:

.. image:: https://mybinder.org/badge_logo.svg
    :target:
        https://mybinder.org/v2/gh/OSGeo/grass/main?urlpath=lab%2Ftree%2Fdoc%2Fnotebooks%2Fjupyter_example.ipynb

There are also internal classes and functions which are not guaranteed to have
as stable API, although they are available through their specific submodules.
For all standard cases, use only classes and function imported with
``import grass.jupyter as gj``. If in doubt, use ``dir(gj)`` to see available objects.
Both the objects in submodules and names of submodules may change in the future.

.. note::
    Although most of the functionality is general, the defaults, resource management,
    and other behavior assumes usage in an interactive notebook, so using the
    functionality in other contexts (e.g. a script) may result in unexpected behavior.
    Consult the documentation or mailing list if in doubt. Suggest generalized
    functionality using issues and pull requests.

.. versionadded:: 8.2

Authors
=======

Caitlin Haedrich, NC State University, Center for Geospatial Analytics

Vaclav Petras, NC State University, Center for Geospatial Analytics

Anna Petrasova, NC State University, Center for Geospatial Analytics

Initial development was done by Caitlin Haedrich during Google Summer of Code in 2021
mentored by Vaclav Petras, Stephan Blumentrath, and Helena Mitasova.

.. _Jupyter: https://jupyter.org/
.. _wiki: https://grasswiki.osgeo.org/wiki/GRASS_GIS_Jupyter_notebooks
.. _GitHub: https://github.com/OSGeo/grass/blob/main/doc/notebooks/jupyter_example.ipynb
"""

from .interactivemap import InteractiveMap, Raster, Vector
from .map import Map
from .map3d import Map3D
from .setup import init
from .timeseriesmap import TimeSeriesMap
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
from .seriesmap import SeriesMap
=======
from .setup import *
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
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
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
from .setup import *
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
from .interact_display import *
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
from .display import *
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
from .utils import *
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
>>>>>>> 4625684fca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> cb0f743d05 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
=======
=======
from .interact_display import *
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
from .display import *
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
from .utils import *
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
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
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
>>>>>>> 40118f6d63 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 869427c771 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
=======
=======
from .interact_display import *
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
from .display import *
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
from .utils import *
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
>>>>>>> 9e134ec08d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 33ca8caf20 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
=======
=======
from .interact_display import *
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
from .display import *
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
from .utils import *
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
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
