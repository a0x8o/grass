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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 490780e974 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> a57bd0b80c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7cabbb1d2e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f584ea5cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5d71474136 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 74df1483b5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9cb19e11bd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a727d4dd1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88bcbec39d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f3ed8fdff (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> d1e0f3a451 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 785ee36c56 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 1b62444dcb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 560c477247 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 5b7ab488c3 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 101a8cef7f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd5fbf27b1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c621983a87 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1da1fea1ab (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 67d74ea5b0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5f67fc32e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 0ba4fb709f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c6adb02431 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 7f440f5d30 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9eed1728a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c940746c7a (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f9445e850e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> db3baef4a0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> b89539ef3e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 42e8aaeeb9 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 77e6855cbe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> f04ed1afc1 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 998dac8c79 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 273146cb7f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 2d07dac9e2 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 9e4d6ad5d0 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5f16c1cd9e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 93657d73a0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7f864362 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 9e8b5d3087 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 44edcd59e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> ff8386f9c6 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0e5ebd3da6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 8c0e82e005 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e6396a49fb (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 9375c9eaa5 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a73d227631 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> d53c2f1458 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d5b813a39d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 3864431eda (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd98bedefc (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 3fdac5af26 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4707957876 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 1a7b29659f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d2d89876a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> d636b6aa21 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0d10010492 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 5442f908c7 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 32399d4902 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 876d408376 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1797d7c620 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7cabbb1d2e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3f1c008cf1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4f584ea5cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5d71474136 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cea31271cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 186df7f9f7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 228be75788 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e2e8ab8598 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 94afdfdae9 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e9fe02ef5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> e435dd0d3f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee6eb01aa7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 0873fb5a66 (ci: Ignore paths in CodeQL (#1778))
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> ff8386f9c6 (ci: Ignore paths in CodeQL (#1778))
=======
<<<<<<< HEAD
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0e5ebd3da6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
>>>>>>> 876d408376 (ci: Ignore paths in CodeQL (#1778))
=======
<<<<<<< HEAD
>>>>>>> 32399d4902 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
>>>>>>> 5442f908c7 (ci: Ignore paths in CodeQL (#1778))
=======
<<<<<<< HEAD
>>>>>>> 0d10010492 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
>>>>>>> d636b6aa21 (ci: Ignore paths in CodeQL (#1778))
=======
<<<<<<< HEAD
>>>>>>> d2d89876a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
>>>>>>> 1a7b29659f (ci: Ignore paths in CodeQL (#1778))
=======
<<<<<<< HEAD
>>>>>>> 4707957876 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
>>>>>>> 3fdac5af26 (ci: Ignore paths in CodeQL (#1778))
=======
<<<<<<< HEAD
>>>>>>> dd98bedefc (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
>>>>>>> 9375c9eaa5 (ci: Ignore paths in CodeQL (#1778))
=======
<<<<<<< HEAD
>>>>>>> e6396a49fb (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 74df1483b5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cea31271cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 9cb19e11bd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0d54fc2b9b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> f201ec2860 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 73992ddf8e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1797d7c620 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 5f16c1cd9e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 93657d73a0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 3f1c008cf1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> ee7f864362 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
<<<<<<< HEAD
>>>>>>> 8c0e82e005 (ci: Ignore paths in CodeQL (#1778))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ee7f864362 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 93657d73a0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5f16c1cd9e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 73992ddf8e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
<<<<<<< HEAD
=======
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
>>>>>>> a676227b37 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 9e8b5d3087 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 44edcd59e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 3864431eda (ci: Ignore paths in CodeQL (#1778))
    :param path: Path to a Location or to a GRASS GIS database directory
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> a676227b37 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 9e8b5d3087 (Merge branch 'a0x8o' into stag0)
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 7f3ed8fdff (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> d1e0f3a451 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
    :param path: Path to a Location or to a GRASS GIS database directory
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
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
>>>>>>> 7f3ed8fdff (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> d1e0f3a451 (ci: Ignore paths in CodeQL (#1778))
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
<<<<<<< HEAD
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
>>>>>>> 186df7f9f7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 785ee36c56 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 228be75788 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1b62444dcb (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e2e8ab8598 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 560c477247 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 94afdfdae9 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 5b7ab488c3 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3e9fe02ef5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> e435dd0d3f (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 101a8cef7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee6eb01aa7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> dd5fbf27b1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 0873fb5a66 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c621983a87 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9ab8b27ed1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 1da1fea1ab (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> af0cda6849 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 67d74ea5b0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eb88670b58 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 5f67fc32e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> cd2a15c8d0 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 0ba4fb709f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de00c20d0d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> c6adb02431 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 12e7124573 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 7f440f5d30 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 71898be8ce (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 9eed1728a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> a74c224a9d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c940746c7a (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4fa1057fa6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> f9445e850e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 210c8f3c49 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> db3baef4a0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4f92c9c12f (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> b89539ef3e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 72d2bd2407 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 42e8aaeeb9 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0d77b1a89c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 77e6855cbe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 619ae34f9c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> f04ed1afc1 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
    :param path: Path to a Location or to a GRASS GIS database directory
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> c427da62e8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 785ee36c56 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 1b62444dcb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 560c477247 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 5b7ab488c3 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 101a8cef7f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> dd5fbf27b1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c621983a87 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 1da1fea1ab (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 67d74ea5b0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5f67fc32e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 0ba4fb709f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> c6adb02431 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 7f440f5d30 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 9eed1728a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c940746c7a (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> f9445e850e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> db3baef4a0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> b89539ef3e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 42e8aaeeb9 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 77e6855cbe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> f04ed1afc1 (ci: Ignore paths in CodeQL (#1778))
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 490780e974 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
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
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a57bd0b80c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1797d7c620 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 7cabbb1d2e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3f1c008cf1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4f584ea5cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 9e8b5d3087 (Merge branch 'a0x8o' into stag0)
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
=======
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44edcd59e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> d53c2f1458 (ci: Ignore paths in CodeQL (#1778))
    :param path: Path to a Location or to a GRASS GIS database directory
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d53c2f1458 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 3864431eda (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 5d71474136 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 74df1483b5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cea31271cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9cb19e11bd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
<<<<<<< HEAD
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
    :param path: Path to a Location or to a GRASS GIS database directory
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 4a727d4dd1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
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
    :param path: Path to a Location or to a GRASS GIS database directory
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 88bcbec39d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 7f3ed8fdff (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> d1e0f3a451 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 186df7f9f7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 785ee36c56 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 228be75788 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1b62444dcb (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e2e8ab8598 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 560c477247 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 94afdfdae9 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 5b7ab488c3 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3e9fe02ef5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
<<<<<<< HEAD
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> e435dd0d3f (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 101a8cef7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee6eb01aa7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> dd5fbf27b1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 0873fb5a66 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c621983a87 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9ab8b27ed1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 1da1fea1ab (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> af0cda6849 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 67d74ea5b0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eb88670b58 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 5f67fc32e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> cd2a15c8d0 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 0ba4fb709f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de00c20d0d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> c6adb02431 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12e7124573 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 7f440f5d30 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 71898be8ce (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 9eed1728a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> a74c224a9d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c940746c7a (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4fa1057fa6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> f9445e850e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 210c8f3c49 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> db3baef4a0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    :param path: Path to a Location or to a GRASS GIS database directory
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> c427da62e8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 2d07dac9e2 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 9e4d6ad5d0 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 998dac8c79 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 273146cb7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4f92c9c12f (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> b89539ef3e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 72d2bd2407 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 42e8aaeeb9 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0d77b1a89c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 77e6855cbe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 619ae34f9c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> f04ed1afc1 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 0d54fc2b9b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> f201ec2860 (ci: Ignore paths in CodeQL (#1778))
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 73992ddf8e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> a676227b37 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1797d7c620 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 5f16c1cd9e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 93657d73a0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3f1c008cf1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> ee7f864362 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 9e8b5d3087 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> ff8386f9c6 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 44edcd59e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ff8386f9c6 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 0e5ebd3da6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 8c0e82e005 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cea31271cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> e6396a49fb (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
<<<<<<< HEAD
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 9375c9eaa5 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    :param path: Path to a Location or to a GRASS GIS database directory
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> a73d227631 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> d53c2f1458 (ci: Ignore paths in CodeQL (#1778))
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
    :param path: Path to a Location or to a GRASS GIS database directory
=======
    :param database: Path to a Location or to a GRASS GIS database directory
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> d5b813a39d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 3864431eda (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> dd98bedefc (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 3fdac5af26 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 186df7f9f7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 4707957876 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 228be75788 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1a7b29659f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e2e8ab8598 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> d2d89876a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 94afdfdae9 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> d636b6aa21 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3e9fe02ef5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 0d10010492 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> e435dd0d3f (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 5442f908c7 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee6eb01aa7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 32399d4902 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
    :param path: Path to a Location or to a GRASS GIS database directory
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 0873fb5a66 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 876d408376 (ci: Ignore paths in CodeQL (#1778))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 490780e974 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a57bd0b80c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1797d7c620 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 7cabbb1d2e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f584ea5cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5d71474136 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 74df1483b5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9cb19e11bd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a727d4dd1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88bcbec39d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f3ed8fdff (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> d1e0f3a451 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 785ee36c56 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 1b62444dcb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 560c477247 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 5b7ab488c3 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 101a8cef7f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd5fbf27b1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c621983a87 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1da1fea1ab (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 67d74ea5b0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5f67fc32e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 0ba4fb709f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c6adb02431 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 7f440f5d30 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9eed1728a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c940746c7a (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f9445e850e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> db3baef4a0 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> b89539ef3e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 42e8aaeeb9 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 77e6855cbe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> f04ed1afc1 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 998dac8c79 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 273146cb7f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 2d07dac9e2 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 9e4d6ad5d0 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7f864362 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 9e8b5d3087 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 44edcd59e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> ff8386f9c6 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0e5ebd3da6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 8c0e82e005 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e6396a49fb (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 9375c9eaa5 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a73d227631 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> d53c2f1458 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d5b813a39d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 3864431eda (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd98bedefc (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 3fdac5af26 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4707957876 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 1a7b29659f (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d2d89876a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> d636b6aa21 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0d10010492 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 5442f908c7 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 32399d4902 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 876d408376 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 1797d7c620 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 3f1c008cf1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4f584ea5cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5d71474136 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 74df1483b5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> cea31271cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 9cb19e11bd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 7f3ed8fdff (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> d1e0f3a451 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 186df7f9f7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 785ee36c56 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 228be75788 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1b62444dcb (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> e2e8ab8598 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 560c477247 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 94afdfdae9 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 5b7ab488c3 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 3e9fe02ef5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> e435dd0d3f (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 101a8cef7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> ee6eb01aa7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> dd5fbf27b1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 0873fb5a66 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c621983a87 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 9ab8b27ed1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 1da1fea1ab (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> af0cda6849 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 67d74ea5b0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> eb88670b58 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 5f67fc32e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> cd2a15c8d0 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 0ba4fb709f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> de00c20d0d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> c6adb02431 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 12e7124573 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 7f440f5d30 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 71898be8ce (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 9eed1728a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> a74c224a9d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c940746c7a (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 4fa1057fa6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> f9445e850e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 210c8f3c49 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> db3baef4a0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4f92c9c12f (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> b89539ef3e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 72d2bd2407 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 42e8aaeeb9 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 0d77b1a89c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 77e6855cbe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 619ae34f9c (ci: Ignore paths in CodeQL (#1778))
>>>>>>> f04ed1afc1 (ci: Ignore paths in CodeQL (#1778))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
        path = os.path.join(path, location)
=======
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> c427da62e8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 490780e974 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 186df7f9f7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 785ee36c56 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 228be75788 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1b62444dcb (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> e2e8ab8598 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 560c477247 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 94afdfdae9 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 5b7ab488c3 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 3e9fe02ef5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> e435dd0d3f (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 101a8cef7f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> ee6eb01aa7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> dd5fbf27b1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 0873fb5a66 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c621983a87 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 9ab8b27ed1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 1da1fea1ab (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> af0cda6849 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 67d74ea5b0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> eb88670b58 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 5f67fc32e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> cd2a15c8d0 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 0ba4fb709f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> de00c20d0d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> c6adb02431 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12e7124573 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 7f440f5d30 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 71898be8ce (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 9eed1728a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> a74c224a9d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c940746c7a (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 4fa1057fa6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> f9445e850e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 210c8f3c49 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> db3baef4a0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 4f92c9c12f (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> b89539ef3e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 72d2bd2407 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 42e8aaeeb9 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 0d77b1a89c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 77e6855cbe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 619ae34f9c (ci: Ignore paths in CodeQL (#1778))
>>>>>>> f04ed1afc1 (ci: Ignore paths in CodeQL (#1778))
    return os.access(os.path.join(path, "PERMANENT", "DEFAULT_WIND"), os.F_OK)


def is_mapset_current(database, location, mapset) -> bool:
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0d54fc2b9b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> f201ec2860 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 73992ddf8e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> a676227b37 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1797d7c620 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 5f16c1cd9e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 1797d7c620 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 93657d73a0 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 3f1c008cf1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> ee7f864362 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 9e8b5d3087 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 44edcd59e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> ff8386f9c6 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 0e5ebd3da6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 8c0e82e005 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> cea31271cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> e6396a49fb (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 9375c9eaa5 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> dd98bedefc (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 3fdac5af26 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 186df7f9f7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 4707957876 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 228be75788 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1a7b29659f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> e2e8ab8598 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> d2d89876a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 94afdfdae9 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> d636b6aa21 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 3e9fe02ef5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 0d10010492 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> e435dd0d3f (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 5442f908c7 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> ee6eb01aa7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 32399d4902 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 0873fb5a66 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 876d408376 (ci: Ignore paths in CodeQL (#1778))
        path = os.path.join(path, location)
=======
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1797d7c620 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3f1c008cf1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
        path = os.path.join(path, location)
=======
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cea31271cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        path = os.path.join(path, location)
=======
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> c427da62e8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 2d07dac9e2 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 998dac8c79 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 0d54fc2b9b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 186df7f9f7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 4707957876 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 228be75788 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1a7b29659f (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> e2e8ab8598 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> d2d89876a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 94afdfdae9 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> d636b6aa21 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 3e9fe02ef5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 0d10010492 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> e435dd0d3f (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 5442f908c7 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> ee6eb01aa7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 32399d4902 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 0873fb5a66 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 876d408376 (ci: Ignore paths in CodeQL (#1778))
    return os.access(os.path.join(path, "PERMANENT", "DEFAULT_WIND"), os.F_OK)


<<<<<<< HEAD
def is_mapset_current(database, location, mapset):
<<<<<<< HEAD
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
def is_mapset_current(database, location, mapset) -> bool:
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
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
        path = os.path.join(path, location)
=======
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
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1797d7c620 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3f1c008cf1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cea31271cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
        path = os.path.join(path, location)
=======
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        path = os.path.join(path, location)
=======
        path = os.path.join(location)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
        path = os.path.join(path, location)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
    return os.access(os.path.join(path, "PERMANENT", "DEFAULT_WIND"), os.F_OK)


def is_mapset_current(database, location, mapset):
<<<<<<< HEAD
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> f201ec2860 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    """Return True if the given GRASS Mapset is the current mapset"""
    genv = gisenv()
    return bool(
        database == genv["GISDBASE"]
        and location == genv["LOCATION_NAME"]
        and mapset == genv["MAPSET"]
    )


<<<<<<< HEAD
def is_location_current(database, location) -> bool:
=======
def is_location_current(database, location):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> f201ec2860 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
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
