"""
Checking objects in a GRASS GIS Spatial Database

(C) 2020 by the GRASS Development Team
This program is free software under the GNU General Public
License (>=v2). Read the file COPYING that comes with GRASS
for details.

.. sectionauthor:: Vaclav Petras <wenzeslaus gmail com>
"""

import datetime
import glob
import os
import sys
from pathlib import Path

import grass.grassdb.config as cfg
import grass.script as gs
from grass.script import gisenv


def mapset_exists(path, location=None, mapset=None):
    """Returns True whether mapset path exists.

    Either only *path* is provided or all three parameters need to be provided.

    :param path: Path to a Mapset or to a GRASS GIS database directory
    :param location: name of a Location if not part of *path*
    :param mapset: name of a Mapset if not part of *path*
    """
    if location and mapset:
        path = os.path.join(path, location, mapset)
    elif location or mapset:
        raise ValueError(_("Provide only path or all three parameters, not two"))
    return os.path.exists(path)


def location_exists(path, location=None):
    """Returns True whether location path exists.

    :param path: Path to a Location or to a GRASS GIS database directory
    :param location: name of a Location if not part of *path*
    """
    if location:
        path = os.path.join(path, location)
    return os.path.exists(path)


# TODO: distinguish between valid for getting maps and usable as current
# https://lists.osgeo.org/pipermail/grass-dev/2016-September/082317.html
# interface created according to the current usage
def is_mapset_valid(path, location=None, mapset=None):
    """Return True if GRASS Mapset is valid

    Either only *path* is provided or all three parameters need to be provided.

    :param path: Path to a Mapset or to a GRASS GIS database directory
    :param location: name of a Location if not part of *path*
    :param mapset: name of a Mapset if not part of *path*
    """
    # WIND is created from DEFAULT_WIND by `g.region -d` and functions
    # or modules which create a new mapset. Most modules will fail if
    # WIND doesn't exist (assuming that neither GRASS_REGION nor
    # WIND_OVERRIDE environmental variables are set).
    if location and mapset:
        path = os.path.join(path, location, mapset)
    elif location or mapset:
        raise ValueError(_("Provide only path or all three parameters, not two"))
    return os.access(os.path.join(path, "WIND"), os.R_OK)


def is_location_valid(path, location=None):
    """Return True if GRASS Location is valid

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    :param path: Path to a Location or to a GRASS GIS database directory
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    :param path: Path to a Location or to a GRASS GIS database directory
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    :param path: Path to a Location or to a GRASS GIS database directory
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    :param path: Path to a Location or to a GRASS GIS database directory
=======
>>>>>>> osgeo-main
=======
    :param path: Path to a Location or to a GRASS GIS database directory
=======
>>>>>>> osgeo-main
=======
    :param path: Path to a Location or to a GRASS GIS database directory
=======
>>>>>>> osgeo-main
=======
    :param path: Path to a Location or to a GRASS GIS database directory
=======
>>>>>>> osgeo-main
=======
    :param path: Path to a Location or to a GRASS GIS database directory
=======
>>>>>>> osgeo-main
=======
    :param path: Path to a Location or to a GRASS GIS database directory
=======
>>>>>>> osgeo-main
=======
    :param path: Path to a Location or to a GRASS GIS database directory
=======
>>>>>>> osgeo-main
=======
    :param path: Path to a Location or to a GRASS GIS database directory
=======
>>>>>>> osgeo-main
=======
    :param path: Path to a Location or to a GRASS GIS database directory
=======
>>>>>>> osgeo-main
=======
    :param path: Path to a Location or to a GRASS GIS database directory
=======
>>>>>>> osgeo-main
=======
    :param path: Path to a Location or to a GRASS GIS database directory
=======
>>>>>>> osgeo-main
=======
    :param path: Path to a Location or to a GRASS GIS database directory
=======
>>>>>>> osgeo-main
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
    :param path: Path to a Location or to a GRASS GIS database directory
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
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
    :param path: Path to a Location or to a GRASS GIS database directory
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    :param path: Path to a Location or to a GRASS GIS database directory
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    :param path: Path to a Location or to a GRASS GIS database directory
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
    :param location: name of a Location if not part of *path*
    """
    # DEFAULT_WIND file should not be required until you do something
    # that actually uses them. The check is just a heuristic; a directory
    # containing a PERMANENT/DEFAULT_WIND file is probably a GRASS
    # location, while a directory lacking it probably isn't.
    if location:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        path = os.path.join(path, location)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        path = os.path.join(path, location)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
        path = os.path.join(path, location)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
        path = os.path.join(path, location)
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
>>>>>>> osgeo-main
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
        path = os.path.join(path, location)
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
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
        path = os.path.join(path, location)
=======
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        path = os.path.join(path, location)
=======
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
    return os.access(os.path.join(path, "PERMANENT", "DEFAULT_WIND"), os.F_OK)


def is_mapset_current(database, location, mapset) -> bool:
    """Return True if the given GRASS Mapset is the current mapset"""
    genv = gisenv()
    return bool(
        database == genv["GISDBASE"]
        and location == genv["LOCATION_NAME"]
        and mapset == genv["MAPSET"]
    )


def is_location_current(database, location) -> bool:
    """Return True if the given GRASS Location is the current location"""
    genv = gisenv()
    return bool(database == genv["GISDBASE"] and location == genv["LOCATION_NAME"])


def is_current_user_mapset_owner(mapset_path):
    """Returns True if mapset owner is the current user.
    On Windows it always returns True."""
    # Note that this does account for libgis built with SKIP_MAPSET_OWN_CHK
    # which disables the ownerships check, i.e., even if it was build with the
    # skip, it still needs the env variable.
    if os.environ.get("GRASS_SKIP_MAPSET_OWNER_CHECK", None):
        # Mapset just needs to be accessible for writing.
        return os.access(mapset_path, os.W_OK)
    # Mapset needs to be owned by user.
    if sys.platform == "win32":
        return True
    stat_info = Path(mapset_path).stat()
    mapset_uid = stat_info.st_uid
    return mapset_uid == os.getuid()


def is_different_mapset_owner(mapset_path):
    """Returns True if mapset owner is different from the current user"""
    return not is_current_user_mapset_owner(mapset_path)


def get_mapset_owner(mapset_path):
    """Returns mapset owner name or None if owner name unknown.
    On Windows it always returns None."""
    if sys.platform == "win32":
        return None
    try:
        path = Path(mapset_path)
        return path.owner()
    except KeyError:
        return None


def is_fallback_session():
    """Checks if a user encounters a fallback GRASS session.

    Returns True if a user encounters a fallback session.
    It occurs when a last mapset is not usable and at the same time
    a user is in a temporary location.
    """
    if "LAST_MAPSET_PATH" in gisenv().keys():
        return is_mapset_current(
            os.environ["TMPDIR"], cfg.temporary_location, cfg.permanent_mapset
        )
    return False


def is_first_time_user():
    """Check if a user is a first-time user.

    Returns True if a user is a first-time user.
    It occurs when a gisrc file has initial settings either in last used mapset
    or in current mapset settings.
    """
    genv = gisenv()
    if "LAST_MAPSET_PATH" in genv.keys():
        return genv["LAST_MAPSET_PATH"] == os.path.join(
            Path.cwd(), cfg.unknown_location, cfg.unknown_mapset
        )
    return False


def is_mapset_locked(mapset_path):
    """Check if the mapset is locked"""
    lock_name = ".gislock"
    lockfile = os.path.join(mapset_path, lock_name)
    return os.path.exists(lockfile)


def get_lockfile_if_present(database, location, mapset):
    """Return path to lock if present, None otherwise

    Returns the path as a string or None if nothing was found, so the
    return value can be used to test if the lock is present.
    """
    lock_name = ".gislock"
    lockfile = os.path.join(database, location, mapset, lock_name)
    if os.path.isfile(lockfile):
        return lockfile
    return None


def get_mapset_lock_info(mapset_path):
    """Get information about .gislock file.
    Assumes lock file exists, use is_mapset_locked to find out.
    Returns information as a dictionary with keys
    'owner' (None if unknown), 'lockpath', and 'timestamp'.
    """
    info = {}
    lock_name = ".gislock"
    info["lockpath"] = os.path.join(mapset_path, lock_name)
    try:
        info["owner"] = Path(info["lockpath"]).owner()
    except KeyError:
        info["owner"] = None
    info["timestamp"] = (
        datetime.datetime.fromtimestamp(os.path.getmtime(info["lockpath"]))
    ).replace(microsecond=0)
    return info


def can_start_in_mapset(mapset_path, ignore_lock: bool = False) -> bool:
    """Check if a mapset from a gisrc file is usable for new session"""
    return not (
        (not is_mapset_valid(mapset_path))
        or (not is_current_user_mapset_owner(mapset_path))
        or (not ignore_lock and is_mapset_locked(mapset_path))
    )


def get_reason_id_mapset_not_usable(mapset_path):
    """It finds a reason why mapset is not usable.

    Returns a reason id as a string.
    If mapset path is None or no reason found, returns None.
    """
    # Check whether mapset exists
    if not os.path.exists(mapset_path):
        return "non-existent"
    # Check whether mapset is valid
    if not is_mapset_valid(mapset_path):
        return "invalid"
    # Check whether mapset is owned by current user
    if not is_current_user_mapset_owner(mapset_path):
        return "different-owner"
    # Check whether mapset is locked
    if is_mapset_locked(mapset_path):
        return "locked"
    return None


def dir_contains_location(path):
    """Return True if directory *path* contains a valid location"""
    if not os.path.isdir(path):
        return False
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            if is_location_valid(path, name):
                return True
    return False


# basically checking location, possibly split into two functions
# (mapset one can call location one)
def get_mapset_invalid_reason(database, location, mapset, none_for_no_reason=False):
    """Returns a message describing what is wrong with the Mapset

    The goal is to provide the most suitable error message
    (rather than to do a quick check).

    :param database: Path to GRASS GIS database directory
    :param location: name of a Location
    :param mapset: name of a Mapset
    :returns: translated message
    """
    # Since we are trying to get the one most likely message, we need all
    # those return statements here.
    # pylint: disable=too-many-return-statements
    location_path = os.path.join(database, location)
    mapset_path = os.path.join(location_path, mapset)
    # first checking the location validity
    # perhaps a special set of checks with different messages mentioning mapset
    # will be needed instead of the same set of messages used for location
    location_msg = get_location_invalid_reason(
        database, location, none_for_no_reason=True
    )
    if location_msg:
        return location_msg
    # if location is valid, check mapset
    if mapset not in os.listdir(location_path):
        # TODO: remove the grass.py specific wording
        return _(
            "Mapset <{mapset}> doesn't exist in GRASS Location <{location}>"
        ).format(mapset=mapset, location=location)
    if not os.path.isdir(mapset_path):
        return _("<%s> is not a GRASS Mapset because it is not a directory") % mapset
    if not os.path.isfile(os.path.join(mapset_path, "WIND")):
        return (
            _(
                "<%s> is not a valid GRASS Mapset"
                " because it does not have a WIND file"
            )
            % mapset
        )
    # based on the is_mapset_valid() function
    if not os.access(os.path.join(mapset_path, "WIND"), os.R_OK):
        return (
            _(
                "<%s> is not a valid GRASS Mapset"
                " because its WIND file is not readable"
            )
            % mapset
        )
    # no reason for invalidity found (might be valid)
    if none_for_no_reason:
        return None
    return _(
        "Mapset <{mapset}> or Location <{location}> is invalid for an unknown reason"
    ).format(mapset=mapset, location=location)


def get_location_invalid_reason(database, location, none_for_no_reason=False):
    """Returns a message describing what is wrong with the Location

    The goal is to provide the most suitable error message
    (rather than to do a quick check).

    By default, when no reason is found, a message about unknown reason is
    returned. This applies also to the case when this function is called on
    a valid location (e.g. as a part of larger investigation).
    ``none_for_no_reason=True`` allows the function to be used as part of other
    diagnostic. When this function fails to find reason for invalidity, other
    the caller can continue the investigation in their context.

    :param database: Path to GRASS GIS database directory
    :param location: name of a Location
    :param none_for_no_reason: When True, return None when reason is unknown
    :returns: translated message or None
    """
    location_path = os.path.join(database, location)
    permanent_path = os.path.join(location_path, "PERMANENT")

    # directory
    if not os.path.exists(location_path):
        return _("Location <%s> doesn't exist") % location_path
    # permanent mapset
    if "PERMANENT" not in os.listdir(location_path):
        return (
            _(
                "<%s> is not a valid GRASS Location"
                " because PERMANENT Mapset is missing"
            )
            % location_path
        )
    if not os.path.isdir(permanent_path):
        return (
            _(
                "<%s> is not a valid GRASS Location"
                " because PERMANENT is not a directory"
            )
            % location_path
        )
    # partially based on the is_location_valid() function
    if not os.path.isfile(os.path.join(permanent_path, "DEFAULT_WIND")):
        return (
            _(
                "<%s> is not a valid GRASS Location"
                " because PERMANENT Mapset does not have a DEFAULT_WIND file"
                " (default computational region)"
            )
            % location_path
        )
    # no reason for invalidity found (might be valid)
    if none_for_no_reason:
        return None
    return _("Location <{location_path}> is invalid for an unknown reason").format(
        location_path=location_path
    )


def get_location_invalid_suggestion(database, location):
    """Return suggestion what to do when specified location is not valid

    It gives suggestion when:
     * A mapset was specified instead of a location.
     * A GRASS database was specified instead of a location.
    """
    location_path = os.path.join(database, location)
    # a common error is to use mapset instead of location,
    # if that's the case, include that info into the message
    if is_mapset_valid(location_path):
        return _(
            "<{location}> looks like a mapset, not a location."
            " Did you mean just <{one_dir_up}>?"
        ).format(location=location, one_dir_up=database)
    # confusion about what is database and what is location
    if dir_contains_location(location_path):
        return _(
            "It looks like <{location}> contains locations."
            " Did you mean to specify one of them?"
        ).format(location=location)
    return None


def get_mapset_name_invalid_reason(database, location, mapset_name):
    """Get reasons why mapset name is not valid.

    It gets reasons when:
     * Name is not valid.
     * Name is reserved for OGR layers.
     * Mapset in the same path already exists.

    Returns message as string if there was a reason, otherwise None.
    """
    message = None
    mapset_path = os.path.join(database, location, mapset_name)

    # Check if mapset name is valid
    if not gs.legal_name(mapset_name):
        message = _(
            "Name '{}' is not a valid name for location or mapset. "
            "Please use only ASCII characters excluding characters {} "
            "and space."
        ).format(mapset_name, "/\"'@,=*~")
    # Check reserved mapset name
    elif mapset_name.lower() == "ogr":
        message = _(
            "Name '{}' is reserved for direct "
            "read access to OGR layers. Please use "
            "another name for your mapset."
        ).format(mapset_name)
    # Check whether mapset exists
    elif mapset_exists(database, location, mapset_name):
        message = _(
            "Mapset  <{mapset}> already exists. Please consider using "
            "another name for your mapset."
        ).format(mapset=mapset_path)

    return message


def get_location_name_invalid_reason(grassdb, location_name):
    """Get reasons why location name is not valid.

    It gets reasons when:
     * Name is not valid.
     * Location in the same path already exists.

    Returns message as string if there was a reason, otherwise None.
    """
    message = None
    location_path = os.path.join(grassdb, location_name)

    # Check if mapset name is valid
    if not gs.legal_name(location_name):
        message = _(
            "Name '{}' is not a valid name for location or mapset. "
            "Please use only ASCII characters excluding characters {} "
            "and space."
        ).format(location_name, "/\"'@,=*~")
    # Check whether location exists
    elif location_exists(grassdb, location_name):
        message = _(
            "Location  <{location}> already exists. Please consider using "
            "another name for your location."
        ).format(location=location_path)

    return message


def is_mapset_name_valid(database, location, mapset_name):
    """Check if mapset name is valid.

    Returns True if mapset name is valid, otherwise False.
    """
    return (
        gs.legal_name(mapset_name)
        and mapset_name.lower() != "ogr"
        and not mapset_exists(database, location, mapset_name)
    )


def is_location_name_valid(database, location_name):
    """Check if location name is valid.

    Returns True if location name is valid, otherwise False.
    """
    return gs.legal_name(location_name) and not location_exists(database, location_name)


def get_reasons_mapsets_not_removable(mapsets, check_permanent):
    """Get reasons why mapsets cannot be removed.

    Parameter *mapsets* is a list of tuples (database, location, mapset).
    Parameter *check_permanent* is True of False. It depends on whether
    we want to check for permanent mapset or not.

    Returns messages as list if there were any failed checks, otherwise empty list.
    """
    messages = []
    for grassdb, location, mapset in mapsets:
        message = get_reason_mapset_not_removable(
            grassdb, location, mapset, check_permanent
        )
        if message:
            messages.append(message)
    return messages


def get_reason_mapset_not_removable(grassdb, location, mapset, check_permanent):
    """Get reason why one mapset cannot be removed.

    Parameter *check_permanent* is True of False. It depends on whether
    we want to check for permanent mapset or not.

    Returns message as string if there was failed check, otherwise None.
    """
    message = None
    mapset_path = os.path.join(grassdb, location, mapset)

    # Check if mapset is permanent
    if check_permanent and mapset == "PERMANENT":
        message = _("Mapset <{mapset}> is required for a valid location.").format(
            mapset=mapset_path
        )
    # Check if mapset is current
    elif is_mapset_current(grassdb, location, mapset):
        message = _("Mapset <{mapset}> is the current mapset.").format(
            mapset=mapset_path
        )
    # Check whether mapset is in use
    elif is_mapset_locked(mapset_path):
        message = _("Mapset <{mapset}> is in use.").format(mapset=mapset_path)
    # Check whether mapset is owned by different user
    elif is_different_mapset_owner(mapset_path):
        message = _("Mapset <{mapset}> is owned by a different user.").format(
            mapset=mapset_path
        )

    return message


def get_reasons_locations_not_removable(locations):
    """Get reasons why locations cannot be removed.

    Parameter *locations* is a list of tuples (database, location).

    Returns messages as list if there were any failed checks, otherwise empty list.
    """
    messages = []
    for grassdb, location in locations:
        messages += get_reasons_location_not_removable(grassdb, location)
    return messages


def get_reasons_location_not_removable(grassdb, location):
    """Get reasons why one location cannot be removed.

    Returns messages as list if there were any failed checks, otherwise empty list.
    """
    messages = []
    location_path = os.path.join(grassdb, location)

    # Check if location is current
    if is_location_current(grassdb, location):
        messages.append(
            _("Location <{location}> is the current location.").format(
                location=location_path
            )
        )
        return messages

    # Find mapsets in particular location
    tmp_gisrc_file, env = gs.create_environment(grassdb, location, "PERMANENT")
    env["GRASS_SKIP_MAPSET_OWNER_CHECK"] = "1"

    g_mapsets = (
        gs.read_command("g.mapsets", flags="l", separator="comma", quiet=True, env=env)
        .strip()
        .split(",")
    )

    # Append to the list of tuples
    mapsets = []
    for g_mapset in g_mapsets:
        mapsets.append((grassdb, location, g_mapset))

    # Concentenate both checks
    messages += get_reasons_mapsets_not_removable(mapsets, check_permanent=False)

    gs.try_remove(tmp_gisrc_file)
    return messages


def get_reasons_grassdb_not_removable(grassdb):
    """Get reasons why one grassdb cannot be removed.

    Returns messages as list if there were any failed checks, otherwise empty list.
    """
    messages = []
    genv = gisenv()

    # Check if grassdb is current
    if grassdb == genv["GISDBASE"]:
        messages.append(
            _("GRASS database <{grassdb}> is the current database.").format(
                grassdb=grassdb
            )
        )
        return messages

    g_locations = get_list_of_locations(grassdb)

    # Append to the list of tuples
    locations = []
    for g_location in g_locations:
        locations.append((grassdb, g_location))
    return get_reasons_locations_not_removable(locations)


def get_list_of_locations(dbase):
    """Get list of GRASS locations in given dbase

    :param dbase: GRASS database path

    :return: list of locations (sorted)
    """
    locations = []
    for location in glob.glob(os.path.join(dbase, "*")):
        if os.path.join(location, "PERMANENT") in glob.glob(
            os.path.join(location, "*")
        ):
            locations.append(os.path.basename(location))

    locations.sort(key=lambda x: x.lower())

    return locations
