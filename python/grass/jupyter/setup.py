# MODULE:    grass.jupyter.setup
#
# AUTHOR(S): Caitlin Haedrich <caitlin DOT haedrich AT gmail>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 40118f6d63 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 869427c771 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 9e134ec08d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 33ca8caf20 (Add session initiations functions for Jupyter Notebooks (#1629))
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
#            Vaclav Petras <wenzeslaus gmail com>
#
# PURPOSE:   This module contains functions for launching a GRASS session
#            in Jupyter Notebooks
#
# COPYRIGHT: (C) 2021-2022 Caitlin Haedrich, and by the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.

"""Initialization GRASS GIS session and its finalization"""

import os
import weakref
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
from pathlib import Path
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

import grass.script as gs


def _set_notebook_defaults():
    """Set defaults appropriate for Jupyter Notebooks.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
#            Vaclav Petras <wenzeslaus gmail com>
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
#
# PURPOSE:   This module contains functions for launching a GRASS session
#            in Jupyter Notebooks
#
# COPYRIGHT: (C) 2021-2022 Caitlin Haedrich, and by the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.

"""Initialization GRASS GIS session and its finalization"""

import os
import weakref
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

import grass.script as gs


def _set_notebook_defaults():
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    """Set defaults appropriate for Jupyter Notebooks.

=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    """
<<<<<<< HEAD
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
    """Set defaults appropriate for Jupyter Notebooks.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
#            Vaclav Petras <wenzeslaus gmail com>
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
#
# PURPOSE:   This module contains functions for launching a GRASS session
#            in Jupyter Notebooks
#
# COPYRIGHT: (C) 2021-2022 Caitlin Haedrich, and by the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.

"""Initialization GRASS GIS session and its finalization"""

import os
import weakref

import grass.script as gs


def _set_notebook_defaults():
<<<<<<< HEAD
    """
<<<<<<< HEAD
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4625684fca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
<<<<<<< HEAD
>>>>>>> cb0f743d05 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
    """Set defaults appropriate for Jupyter Notebooks.

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
=======
<<<<<<< HEAD
>>>>>>> main
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
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
#            Vaclav Petras <wenzeslaus gmail com>
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
#
# PURPOSE:   This module contains functions for launching a GRASS session
#            in Jupyter Notebooks
#
# COPYRIGHT: (C) 2021-2022 Caitlin Haedrich, and by the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.

"""Initialization GRASS GIS session and its finalization"""

import os
import weakref

import grass.script as gs


def _set_notebook_defaults():
<<<<<<< HEAD
    """
<<<<<<< HEAD
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 40118f6d63 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
<<<<<<< HEAD
>>>>>>> 869427c771 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
=======
    """Set defaults appropriate for Jupyter Notebooks.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
#            Vaclav Petras <wenzeslaus gmail com>
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
#
# PURPOSE:   This module contains functions for launching a GRASS session
#            in Jupyter Notebooks
#
# COPYRIGHT: (C) 2021-2022 Caitlin Haedrich, and by the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.

"""Initialization GRASS GIS session and its finalization"""

import os
import weakref

import grass.script as gs


def _set_notebook_defaults():
<<<<<<< HEAD
    """
<<<<<<< HEAD
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 9e134ec08d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
<<<<<<< HEAD
>>>>>>> 33ca8caf20 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
=======
    """Set defaults appropriate for Jupyter Notebooks.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
    This function sets several GRASS environment variables that are
    important for GRASS to run smoothly in Jupyter.

    It also allows GRASS to overwrite existing maps of the same name.
    """
    # We want functions to raise exceptions and see standard output of
    # the modules in the notebook.
    gs.set_raise_on_error(True)
    gs.set_capture_stderr(True)

    # Allow overwrite of existing maps
    os.environ["GRASS_OVERWRITE"] = "1"


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 40118f6d63 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 869427c771 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 9e134ec08d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 33ca8caf20 (Add session initiations functions for Jupyter Notebooks (#1629))
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
class _JupyterGlobalSession:
    """Represents a global GRASS session for Jupyter Notebooks.

    Do not create objects of this class directly. Use the standalone *init* function
    and an object will be returned to you, e.g.:

    >>> import grass.jupyter as gj
    >>> session = gj.init(...)

    An object ends the session when it is destroyed or when the *finish* method is
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
    called explicitly.

    Notably, only the mapset is closed, but the libraries and GRASS modules
    remain on path.
    """

    def __init__(self):
        self._finalizer = weakref.finalize(self, gs.setup.finish)

    def switch_mapset(self, path, location=None, mapset=None):
        """Switch to a mapset provided as a name or path.

        The mapset can be provided as a name, as a path,
        or as database, location, and mapset.
        Specifically, the *path* positional-only parameter can be either
        name of a mapset in the current location or a full path to a mapset.
        When location and mapset are provided using the additional parameters,
        the *path* parameter is path to a database.

        Raises ValueError if the mapset does not exist (e.g., when the name is
        misspelled or the mapset is invalid).
        """
        # The method could be a function, but this is more general (would work even for
        # a non-global session).
        # pylint: disable=no-self-use
        # Functions needed only here.
        # pylint: disable=import-outside-toplevel
        from grass.grassdb.checks import (
            get_mapset_invalid_reason,
            is_mapset_valid,
            mapset_exists,
        )
        from grass.grassdb.manage import resolve_mapset_path

        # For only one parameter, try if it is a mapset in the current location to
        # support switching only by its name.
        gisenv = gs.gisenv()
        if (
            not location
            and not mapset
            and len(Path(path).parts) == 1
            and mapset_exists(
                path=gisenv["GISDBASE"], location=gisenv["LOCATION_NAME"], mapset=path
            )
        ):
            gs.run_command("g.gisenv", set=f"MAPSET={path}")
            return

        mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
        if not is_mapset_valid(mapset_path):
            raise ValueError(
                _("Mapset {path} is not valid: {reason}").format(
                    path=mapset_path.path,
                    reason=get_mapset_invalid_reason(
                        mapset_path.directory, mapset_path.location, mapset_path.mapset
                    ),
                )
            )
        # This requires direct session file modification using g.gisenv because
        # g.mapset locks the mapset which is not how init and finish behave.
        # For code simplicity, we just change all even when only mapset is changed.
        gs.run_command("g.gisenv", set=f"GISDBASE={mapset_path.directory}")
        gs.run_command("g.gisenv", set=f"LOCATION_NAME={mapset_path.location}")
        gs.run_command("g.gisenv", set=f"MAPSET={mapset_path.mapset}")

    def finish(self):
        """Close the session, i.e., close the open mapset.

        Subsequent calls to GRASS GIS modules will fail because there will be
        no current (open) mapset anymore.

        The finish procedure is done automatically when process finishes or the object
        is destroyed.
        """
        self._finalizer()

    @property
    def active(self):
        """True unless the session was finalized (e.g., with the *finish* function)"""
        return self._finalizer.alive


# Pylint 2.12.2 identifies this a constant (although it is not), so it wants uppercase.
_global_session_handle = None  # pylint: disable=invalid-name


def init(path, location=None, mapset=None, grass_path=None):
    """Initiates a GRASS session and sets GRASS environment variables.

    Calling this function returns an object which represents the session.

    >>> import grass.jupyter as gj
    >>> session = gj.init(...)

    The session is ended when `session.finish` is called or when the object is
    destroyed when kernel ends or restarts. This function returns a copy of an
    internally kept reference, so the return value can be safely ignored when not
    needed.

    The returned object can be used to switch to another mapset:

    >>> session.switch_mapset("mapset_name")

    Subsequent calls to the *init* function result in switching the mapset if
    a session is active and result in creation of new session if it is not active.
    On the other hand, if you see ``GISRC - variable not set`` after calling
    a GRASS module, you know you don't have an active GRASS session.

    :param str path: path to GRASS mapset or database
    :param str location: name of GRASS location within the database
    :param str mapset: name of mapset within location
    """
    global _global_session_handle  # pylint: disable=global-statement,invalid-name
    if not _global_session_handle or not _global_session_handle.active:
        # Create a GRASS session.
        gs.setup.init(path, location=location, mapset=mapset, grass_path=grass_path)
        # Set defaults for environmental variables and library.
        _set_notebook_defaults()
        _global_session_handle = _JupyterGlobalSession()
    else:
        _global_session_handle.switch_mapset(path, location=location, mapset=mapset)
    return _global_session_handle
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
>>>>>>> 4625684fca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> cb0f743d05 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
>>>>>>> 40118f6d63 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> 869427c771 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
<<<<<<< HEAD
>>>>>>> 9e134ec08d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> 33ca8caf20 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> osgeo-main
def init(path, location, mapset):
    """
    This function initiates a GRASS session and sets GRASS
    environment variables.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
class _JupyterGlobalSession:
    """Represents a global GRASS session for Jupyter Notebooks.
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
=======
<<<<<<< HEAD
>>>>>>> main

    Do not create objects of this class directly. Use the standalone *init* function
    and an object will be returned to you, e.g.:
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    called explicitely.

    Notably, only the mapset is closed, but the libraries and GRASS modules
    remain on path.
    """

    def __init__(self):
        self._finalizer = weakref.finalize(self, gs.setup.finish)

    def switch_mapset(self, path, location=None, mapset=None):
        """Switch to a mapset provided as a name or path.

        The mapset can be provided as a name, as a path,
        or as database, location, and mapset.
        Specifically, the *path* positional-only parameter can be either
        name of a mapset in the current location or a full path to a mapset.
        When location and mapset are provided using the additional parameters,
        the *path* parameter is path to a database.

        Raises ValueError if the mapset does not exist (e.g., when the name is
        misspelled or the mapset is invalid).
        """
        # The method could be a function, but this is more general (would work even for
        # a non-global session).
        # pylint: disable=no-self-use
        # Functions needed only here.
        # pylint: disable=import-outside-toplevel
        from grass.grassdb.checks import (
            get_mapset_invalid_reason,
            is_mapset_valid,
            mapset_exists,
        )
        from grass.grassdb.manage import resolve_mapset_path

        # For only one parameter, try if it is a mapset in the current location to
        # support switching only by its name.
        gisenv = gs.gisenv()
        if (
            not location
            and not mapset
            and mapset_exists(
                path=gisenv["GISDBASE"], location=gisenv["LOCATION_NAME"], mapset=path
            )
        ):
            gs.run_command("g.gisenv", set=f"MAPSET={path}")
            return

        mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
        if not is_mapset_valid(mapset_path):
            raise ValueError(
                _("Mapset {path} is not valid: {reason}").format(
                    path=mapset_path.path,
                    reason=get_mapset_invalid_reason(
                        mapset_path.directory, mapset_path.location, mapset_path.mapset
                    ),
                )
            )
        # This requires direct session file modification using g.gisenv because
        # g.mapset locks the mapset which is not how init and finish behave.
        # For code simplicity, we just change all even when only mapset is changed.
        gs.run_command("g.gisenv", set=f"GISDBASE={mapset_path.directory}")
        gs.run_command("g.gisenv", set=f"LOCATION_NAME={mapset_path.location}")
        gs.run_command("g.gisenv", set=f"MAPSET={mapset_path.mapset}")

    def finish(self):
        """Close the session, i.e., close the open mapset.

        Subsequent calls to GRASS GIS modules will fail because there will be
        no current (open) mapset anymore.

        The finish procedure is done automatically when process finishes or the object
        is destroyed.
        """
        self._finalizer()

    @property
    def active(self):
        """True unless the session was finalized (e.g., with the *finish* function)"""
        return self._finalizer.alive


# Pylint 2.12.2 identifies this a constant (although it is not), so it wants uppercase.
_global_session_handle = None  # pylint: disable=invalid-name


def init(path, location=None, mapset=None, grass_path=None):
    """Initiates a GRASS session and sets GRASS environment variables.

    Calling this function returns an object which represents the session.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    >>> import grass.jupyter as gj
    >>> session = gj.init(...)

<<<<<<< HEAD
    An object ends the session when it is destroyed or when the *finish* method is
    called explicitely.

    Notably, only the mapset is closed, but the libraries and GRASS modules
    remain on path.
    """
<<<<<<< HEAD
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
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

    Do not create objects of this class directly. Use the standalone *init* function
    and an object will be returned to you, e.g.:
=======
    called explicitely.

    Notably, only the mapset is closed, but the libraries and GRASS modules
    remain on path.
    """

    def __init__(self):
        self._finalizer = weakref.finalize(self, gs.setup.finish)

    def switch_mapset(self, path, location=None, mapset=None):
        """Switch to a mapset provided as a name or path.

        The mapset can be provided as a name, as a path,
        or as database, location, and mapset.
        Specifically, the *path* positional-only parameter can be either
        name of a mapset in the current location or a full path to a mapset.
        When location and mapset are provided using the additional parameters,
        the *path* parameter is path to a database.

        Raises ValueError if the mapset does not exist (e.g., when the name is
        misspelled or the mapset is invalid).
        """
        # The method could be a function, but this is more general (would work even for
        # a non-global session).
        # pylint: disable=no-self-use
        # Functions needed only here.
        # pylint: disable=import-outside-toplevel
        from grass.grassdb.checks import (
            get_mapset_invalid_reason,
            is_mapset_valid,
            mapset_exists,
        )
        from grass.grassdb.manage import resolve_mapset_path

        # For only one parameter, try if it is a mapset in the current location to
        # support switching only by its name.
        gisenv = gs.gisenv()
        if (
            not location
            and not mapset
            and mapset_exists(
                path=gisenv["GISDBASE"], location=gisenv["LOCATION_NAME"], mapset=path
            )
        ):
            gs.run_command("g.gisenv", set=f"MAPSET={path}")
            return

        mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
        if not is_mapset_valid(mapset_path):
            raise ValueError(
                _("Mapset {path} is not valid: {reason}").format(
                    path=mapset_path.path,
                    reason=get_mapset_invalid_reason(
                        mapset_path.directory, mapset_path.location, mapset_path.mapset
                    ),
                )
            )
        # This requires direct session file modification using g.gisenv because
        # g.mapset locks the mapset which is not how init and finish behave.
        # For code simplicity, we just change all even when only mapset is changed.
        gs.run_command("g.gisenv", set=f"GISDBASE={mapset_path.directory}")
        gs.run_command("g.gisenv", set=f"LOCATION_NAME={mapset_path.location}")
        gs.run_command("g.gisenv", set=f"MAPSET={mapset_path.mapset}")

    def finish(self):
        """Close the session, i.e., close the open mapset.

        Subsequent calls to GRASS GIS modules will fail because there will be
        no current (open) mapset anymore.

        The finish procedure is done automatically when process finishes or the object
        is destroyed.
        """
        self._finalizer()

    @property
    def active(self):
        """True unless the session was finalized (e.g., with the *finish* function)"""
        return self._finalizer.alive


# Pylint 2.12.2 identifies this a constant (although it is not), so it wants uppercase.
_global_session_handle = None  # pylint: disable=invalid-name


def init(path, location=None, mapset=None, grass_path=None):
    """Initiates a GRASS session and sets GRASS environment variables.

    Calling this function returns an object which represents the session.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    >>> import grass.jupyter as gj
    >>> session = gj.init(...)

<<<<<<< HEAD
    An object ends the session when it is destroyed or when the *finish* method is
    called explicitely.

    Notably, only the mapset is closed, but the libraries and GRASS modules
    remain on path.
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
>>>>>>> 4625684fca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))

    Do not create objects of this class directly. Use the standalone *init* function
    and an object will be returned to you, e.g.:
=======
    called explicitely.

    Notably, only the mapset is closed, but the libraries and GRASS modules
    remain on path.
    """

    def __init__(self):
        self._finalizer = weakref.finalize(self, gs.setup.finish)

    def switch_mapset(self, path, location=None, mapset=None):
        """Switch to a mapset provided as a name or path.

        The mapset can be provided as a name, as a path,
        or as database, location, and mapset.
        Specifically, the *path* positional-only parameter can be either
        name of a mapset in the current location or a full path to a mapset.
        When location and mapset are provided using the additional parameters,
        the *path* parameter is path to a database.

        Raises ValueError if the mapset does not exist (e.g., when the name is
        misspelled or the mapset is invalid).
        """
        # The method could be a function, but this is more general (would work even for
        # a non-global session).
        # pylint: disable=no-self-use
        # Functions needed only here.
        # pylint: disable=import-outside-toplevel
        from grass.grassdb.checks import (
            get_mapset_invalid_reason,
            is_mapset_valid,
            mapset_exists,
        )
        from grass.grassdb.manage import resolve_mapset_path

        # For only one parameter, try if it is a mapset in the current location to
        # support switching only by its name.
        gisenv = gs.gisenv()
        if (
            not location
            and not mapset
            and mapset_exists(
                path=gisenv["GISDBASE"], location=gisenv["LOCATION_NAME"], mapset=path
            )
        ):
            gs.run_command("g.gisenv", set=f"MAPSET={path}")
            return

        mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
        if not is_mapset_valid(mapset_path):
            raise ValueError(
                _("Mapset {path} is not valid: {reason}").format(
                    path=mapset_path.path,
                    reason=get_mapset_invalid_reason(
                        mapset_path.directory, mapset_path.location, mapset_path.mapset
                    ),
                )
            )
        # This requires direct session file modification using g.gisenv because
        # g.mapset locks the mapset which is not how init and finish behave.
        # For code simplicity, we just change all even when only mapset is changed.
        gs.run_command("g.gisenv", set=f"GISDBASE={mapset_path.directory}")
        gs.run_command("g.gisenv", set=f"LOCATION_NAME={mapset_path.location}")
        gs.run_command("g.gisenv", set=f"MAPSET={mapset_path.mapset}")

    def finish(self):
        """Close the session, i.e., close the open mapset.

        Subsequent calls to GRASS GIS modules will fail because there will be
        no current (open) mapset anymore.

        The finish procedure is done automatically when process finishes or the object
        is destroyed.
        """
        self._finalizer()

    @property
    def active(self):
        """True unless the session was finalized (e.g., with the *finish* function)"""
        return self._finalizer.alive


# Pylint 2.12.2 identifies this a constant (although it is not), so it wants uppercase.
_global_session_handle = None  # pylint: disable=invalid-name


def init(path, location=None, mapset=None, grass_path=None):
    """Initiates a GRASS session and sets GRASS environment variables.

    Calling this function returns an object which represents the session.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    >>> import grass.jupyter as gj
    >>> session = gj.init(...)

<<<<<<< HEAD
    An object ends the session when it is destroyed or when the *finish* method is
    called explicitely.

    Notably, only the mapset is closed, but the libraries and GRASS modules
    remain on path.
    """
<<<<<<< HEAD
>>>>>>> 40118f6d63 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))

    Do not create objects of this class directly. Use the standalone *init* function
    and an object will be returned to you, e.g.:
=======
    called explicitely.

    Notably, only the mapset is closed, but the libraries and GRASS modules
    remain on path.
    """

    def __init__(self):
        self._finalizer = weakref.finalize(self, gs.setup.finish)

    def switch_mapset(self, path, location=None, mapset=None):
        """Switch to a mapset provided as a name or path.

        The mapset can be provided as a name, as a path,
        or as database, location, and mapset.
        Specifically, the *path* positional-only parameter can be either
        name of a mapset in the current location or a full path to a mapset.
        When location and mapset are provided using the additional parameters,
        the *path* parameter is path to a database.

        Raises ValueError if the mapset does not exist (e.g., when the name is
        misspelled or the mapset is invalid).
        """
        # The method could be a function, but this is more general (would work even for
        # a non-global session).
        # pylint: disable=no-self-use
        # Functions needed only here.
        # pylint: disable=import-outside-toplevel
        from grass.grassdb.checks import (
            get_mapset_invalid_reason,
            is_mapset_valid,
            mapset_exists,
        )
        from grass.grassdb.manage import resolve_mapset_path

        # For only one parameter, try if it is a mapset in the current location to
        # support switching only by its name.
        gisenv = gs.gisenv()
        if (
            not location
            and not mapset
            and mapset_exists(
                path=gisenv["GISDBASE"], location=gisenv["LOCATION_NAME"], mapset=path
            )
        ):
            gs.run_command("g.gisenv", set=f"MAPSET={path}")
            return

        mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
        if not is_mapset_valid(mapset_path):
            raise ValueError(
                _("Mapset {path} is not valid: {reason}").format(
                    path=mapset_path.path,
                    reason=get_mapset_invalid_reason(
                        mapset_path.directory, mapset_path.location, mapset_path.mapset
                    ),
                )
            )
        # This requires direct session file modification using g.gisenv because
        # g.mapset locks the mapset which is not how init and finish behave.
        # For code simplicity, we just change all even when only mapset is changed.
        gs.run_command("g.gisenv", set=f"GISDBASE={mapset_path.directory}")
        gs.run_command("g.gisenv", set=f"LOCATION_NAME={mapset_path.location}")
        gs.run_command("g.gisenv", set=f"MAPSET={mapset_path.mapset}")

    def finish(self):
        """Close the session, i.e., close the open mapset.

        Subsequent calls to GRASS GIS modules will fail because there will be
        no current (open) mapset anymore.

        The finish procedure is done automatically when process finishes or the object
        is destroyed.
        """
        self._finalizer()

    @property
    def active(self):
        """True unless the session was finalized (e.g., with the *finish* function)"""
        return self._finalizer.alive


# Pylint 2.12.2 identifies this a constant (although it is not), so it wants uppercase.
_global_session_handle = None  # pylint: disable=invalid-name


def init(path, location=None, mapset=None, grass_path=None):
    """Initiates a GRASS session and sets GRASS environment variables.

    Calling this function returns an object which represents the session.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    >>> import grass.jupyter as gj
    >>> session = gj.init(...)

<<<<<<< HEAD
    An object ends the session when it is destroyed or when the *finish* method is
    called explicitely.

    Notably, only the mapset is closed, but the libraries and GRASS modules
    remain on path.
    """
<<<<<<< HEAD
>>>>>>> 9e134ec08d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
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
    # Create a GRASS GIS session.
    gsetup.init(os.environ["GISBASE"], path, location, mapset)
    # Set GRASS env. variables
    _set_notebook_defaults()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 4625684fca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 40118f6d63 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 9e134ec08d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
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


def display_settings(font="sans", driver="cairo"):
    """
    This function sets the display settings for a GRASS session
    in Jupyter Notebooks.

    Example Usage: display_settings(font="sans", driver="cairo")

    Inputs:
        font - specifies the font as either the name of a font from
        $GISBASE/etc/fontcap (or alternative fontcap file specified by
        GRASS_FONT_CAP), or alternatively the full path to a FreeType
        font file.

        driver - tell teh display library which driver to use
            Possible values: "cairo", "png", "ps", "html"
    """
    # Set display font
    os.environ["GRASS_FONT"] = font

    # Set display modeules to render to a file (named map.png by
    # default).
    os.environ["GRASS_RENDER_IMMEDIATE"] = driver
    os.environ["GRASS_RENDER_FILE_READ"] = "TRUE"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
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

    def __init__(self):
        self._finalizer = weakref.finalize(self, gs.setup.finish)

    def switch_mapset(self, path, location=None, mapset=None):
        """Switch to a mapset provided as a name or path.

        The mapset can be provided as a name, as a path,
        or as database, location, and mapset.
        Specifically, the *path* positional-only parameter can be either
        name of a mapset in the current location or a full path to a mapset.
        When location and mapset are provided using the additional parameters,
        the *path* parameter is path to a database.

        Raises ValueError if the mapset does not exist (e.g., when the name is
        misspelled or the mapset is invalid).
        """
        # The method could be a function, but this is more general (would work even for
        # a non-global session).
        # pylint: disable=no-self-use
        # Functions needed only here.
        # pylint: disable=import-outside-toplevel
        from grass.grassdb.checks import (
            get_mapset_invalid_reason,
            is_mapset_valid,
            mapset_exists,
        )
        from grass.grassdb.manage import resolve_mapset_path

        # For only one parameter, try if it is a mapset in the current location to
        # support switching only by its name.
        gisenv = gs.gisenv()
        if (
            not location
            and not mapset
            and mapset_exists(
                path=gisenv["GISDBASE"], location=gisenv["LOCATION_NAME"], mapset=path
            )
        ):
            gs.run_command("g.gisenv", set=f"MAPSET={path}")
            return

        mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
        if not is_mapset_valid(mapset_path):
            raise ValueError(
                _("Mapset {path} is not valid: {reason}").format(
                    path=mapset_path.path,
                    reason=get_mapset_invalid_reason(
                        mapset_path.directory, mapset_path.location, mapset_path.mapset
                    ),
                )
            )
        # This requires direct session file modification using g.gisenv because
        # g.mapset locks the mapset which is not how init and finish behave.
        # For code simplicity, we just change all even when only mapset is changed.
        gs.run_command("g.gisenv", set=f"GISDBASE={mapset_path.directory}")
        gs.run_command("g.gisenv", set=f"LOCATION_NAME={mapset_path.location}")
        gs.run_command("g.gisenv", set=f"MAPSET={mapset_path.mapset}")

    def finish(self):
        """Close the session, i.e., close the open mapset.

        Subsequent calls to GRASS GIS modules will fail because there will be
        no current (open) mapset anymore.

        The finish procedure is done automatically when process finishes or the object
        is destroyed.
        """
        self._finalizer()

    @property
    def active(self):
        """True unless the session was finalized (e.g., with the *finish* function)"""
        return self._finalizer.alive


# Pylint 2.12.2 identifies this a constant (although it is not), so it wants uppercase.
_global_session_handle = None  # pylint: disable=invalid-name


def init(path, location=None, mapset=None, grass_path=None):
    """Initiates a GRASS session and sets GRASS environment variables.

    Calling this function returns an object which represents the session.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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

    >>> import grass.jupyter as gj
    >>> session = gj.init(...)

    The session is ended when `session.finish` is called or when the object is
    destroyed when kernel ends or restarts. This function returns a copy of an
    internally kept reference, so the return value can be safely ignored when not
    needed.

    The returned object can be used to switch to another mapset:

    >>> session.switch_mapset("mapset_name")

    Subsequent calls to the *init* function result in switching the mapset if
    a session is active and result in creation of new session if it is not active.
    On the other hand, if you see ``GISRC - variable not set`` after calling
    a GRASS module, you know you don't have an active GRASS session.

    :param str path: path to GRASS mapset or database
    :param str location: name of GRASS location within the database
    :param str mapset: name of mapset within location
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
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
    The session is ended when `session.finish` is called or when the object is
    destroyed when kernel ends or restarts. This function returns a copy of an
    internally kept reference, so the return value can be safely ignored when not
    needed.

    The returned object can be used to switch to another mapset:

    >>> session.switch_mapset("mapset_name")

    Subsequent calls to the *init* function result in switching the mapset if
    a session is active and result in creation of new session if it is not active.
    On the other hand, if you see ``GISRC - variable not set`` after calling
    a GRASS module, you know you don't have an active GRASS session.

    :param str path: path to GRASS mapset or database
    :param str location: name of GRASS location within the database
    :param str mapset: name of mapset within location
    """
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
    global _global_session_handle  # pylint: disable=global-statement,invalid-name
    if not _global_session_handle or not _global_session_handle.active:
        # Create a GRASS session.
        gs.setup.init(path, location=location, mapset=mapset, grass_path=grass_path)
        # Set defaults for environmental variables and library.
        _set_notebook_defaults()
        _global_session_handle = _JupyterGlobalSession()
    else:
        _global_session_handle.switch_mapset(path, location=location, mapset=mapset)
    return _global_session_handle
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
>>>>>>> 4625684fca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> cb0f743d05 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
>>>>>>> 40118f6d63 (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> 869427c771 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
>>>>>>> 9e134ec08d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
>>>>>>> 33ca8caf20 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
