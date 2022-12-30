"""
@package startup.locdownload

@brief GRASS Location Download Management

Classes:
 - LocationDownloadPanel
 - LocationDownloadDialog
 - DownloadError

(C) 2017 by Vaclav Petras the GRASS Development Team

This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.

@author Vaclav Petras <wenzeslaus gmail com>
"""

import os
import sys
import shutil
import textwrap
import time

import wx
from wx.lib.newevent import NewEvent

from grass.script.utils import try_rmdir, legalize_vector_name
from grass.utils.download import download_and_extract, name_from_url, DownloadError
from grass.grassdb.checks import is_location_valid
from grass.script.setup import set_gui_path

set_gui_path()

from core.debug import Debug
from core.gthread import gThread
from gui_core.wrap import Button, StaticText


# TODO: labels (and descriptions) translatable?
LOCATIONS = [
    {
        "label": "Complete North Carolina dataset",
        "url": "https://grass.osgeo.org/sampledata/north_carolina/nc_spm_08_grass7.tar.gz",  # noqa: E501
    },
    {
        "label": "Basic North Carolina dataset",
        "url": "https://grass.osgeo.org/sampledata/north_carolina/nc_basic_spm_grass7.tar.gz",  # noqa: E501
    },
    {
        "label": "World dataset in LatLong/WGS84",
        "url": "https://grass.osgeo.org/sampledata/worldlocation.tar.gz",
    },
    {
        "label": "Spearfish (SD) dataset",
        "url": "https://grass.osgeo.org/sampledata/spearfish_grass70data-0.3.tar.gz",
    },
    {
        "label": "Piemonte, Italy dataset",
        "url": "https://grass.osgeo.org/sampledata/grassdata_piemonte_utm32n_wgs84_grass7.tar.gz",  # noqa: E501
    },
    {
        "label": "Slovakia 3D precipitation voxel dataset",
        "url": "https://grass.osgeo.org/sampledata/slovakia3d_grass7.tar.gz",
    },
    {
        "label": "Fire simulation sample data",
        "url": "https://grass.osgeo.org/sampledata/fire_grass6data.tar.gz",
    },
    {
        "label": "GISMentors dataset, Czech Republic",
        "url": "http://training.gismentors.eu/geodata/grass/gismentors.zip",
    },
    {
        "label": "Natural Earth Dataset in WGS84",
        "url": "https://zenodo.org/records/13370131/files/natural_earth_dataset.zip",
        "size": "121.3 MB",
        "epsg": "4326",
        "license": "ODC Public Domain Dedication and License 1.0",
        "maintainer": "Brendan Harmon (brendan.harmon@gmail.com)",
    },
]


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 490780e974 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a57bd0b80c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 7cabbb1d2e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 5f16c1cd9e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4f584ea5cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 74df1483b5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9cb19e11bd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f3ed8fdff (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 785ee36c56 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 560c477247 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd5fbf27b1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1da1fea1ab (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5f67fc32e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c6adb02431 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9eed1728a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f9445e850e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b89539ef3e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 77e6855cbe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 2d07dac9e2 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
=======
>>>>>>> 0e5ebd3da6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e6396a49fb (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0d54fc2b9b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 73992ddf8e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7f864362 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
class RedirectText:
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
class RedirectText:
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
class RedirectText:
=======
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
class RedirectText:
=======
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
class RedirectText:
=======
>>>>>>> c427da62e8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 490780e974 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 44edcd59e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a57bd0b80c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5f16c1cd9e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
class RedirectText:
=======
>>>>>>> 1797d7c620 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7cabbb1d2e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7f864362 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
class RedirectText:
=======
>>>>>>> 3f1c008cf1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4f584ea5cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 44edcd59e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> osgeo-main
=======
class RedirectText:
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 5d71474136 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
<<<<<<< HEAD
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0e5ebd3da6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
class RedirectText:
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 74df1483b5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
<<<<<<< HEAD
>>>>>>> cea31271cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 9cb19e11bd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
class RedirectText:
=======
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 4a727d4dd1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
class RedirectText:
=======
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 88bcbec39d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 7f3ed8fdff (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
>>>>>>> 186df7f9f7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 785ee36c56 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
>>>>>>> e2e8ab8598 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 560c477247 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
>>>>>>> 3e9fe02ef5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
class RedirectText:
=======
>>>>>>> ee6eb01aa7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> dd5fbf27b1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
>>>>>>> 9ab8b27ed1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 1da1fea1ab (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
>>>>>>> eb88670b58 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 5f67fc32e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
>>>>>>> de00c20d0d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> c6adb02431 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
>>>>>>> 71898be8ce (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 9eed1728a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
>>>>>>> 4fa1057fa6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> f9445e850e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
class RedirectText:
=======
>>>>>>> c427da62e8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 2d07dac9e2 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 9e4d6ad5d0 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
>>>>>>> 4f92c9c12f (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> b89539ef3e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
>>>>>>> 0d77b1a89c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 77e6855cbe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 0d54fc2b9b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 73992ddf8e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5f16c1cd9e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7f864362 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 44edcd59e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0e5ebd3da6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
class RedirectText:
=======
<<<<<<< HEAD
>>>>>>> cea31271cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> e6396a49fb (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
class RedirectText:
=======
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> a73d227631 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
class RedirectText(object):
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
    def __init__(self, window):
        self.out = window

    def write(self, string):
        try:
            if self.out:
                string = self._wrap_string(string)
                heigth = self._get_heigth(string)
                wx.CallAfter(self.out.SetLabel, string)
                self._resize(heigth)
        except:
            # window closed -> PyDeadObjectError
            pass

    def flush(self):
        pass

    def _wrap_string(self, string, width=40):
        """Wrap string

        :param str string: input string
        :param int width: maximum length allowed of the wrapped lines

        :return str: newline-separated string
        """
        wrapper = textwrap.TextWrapper(width=width)
        return wrapper.fill(text=string)

    def _get_heigth(self, string):
        """Get widget new heigth

        :param str string: input string

        :return int: widget heigth
        """
        n_lines = string.count("\n")
        attr = self.out.GetClassDefaultAttributes()
        font_size = attr.font.GetPointSize()
        return int((n_lines + 2) * font_size // 0.75)  # 1 px = 0.75 pt

    def _resize(self, heigth=-1):
        """Resize widget heigth

        :param int heigth: widget heigth
        """
        wx.CallAfter(self.out.GetParent().SetMinSize, (-1, -1))
        wx.CallAfter(self.out.SetMinSize, (-1, heigth))
        wx.CallAfter(
            self.out.GetParent().parent.sizer.Fit,
            self.out.GetParent().parent,
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
>>>>>>> c427da62e8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 490780e974 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> a57bd0b80c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 7cabbb1d2e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f584ea5cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 74df1483b5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9cb19e11bd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f3ed8fdff (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 785ee36c56 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 560c477247 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd5fbf27b1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1da1fea1ab (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5f67fc32e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c6adb02431 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9eed1728a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f9445e850e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b89539ef3e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 77e6855cbe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 2d07dac9e2 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 0e5ebd3da6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e6396a49fb (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
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
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3f1c008cf1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 4f584ea5cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 5d71474136 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
<<<<<<< HEAD
>>>>>>> 74df1483b5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 4a727d4dd1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 88bcbec39d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
<<<<<<< HEAD
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
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> c427da62e8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 2d07dac9e2 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 9e4d6ad5d0 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0d54fc2b9b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 73992ddf8e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 5f16c1cd9e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7f864362 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
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
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3f1c008cf1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> ee7f864362 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 44edcd59e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 0e5ebd3da6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> a73d227631 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
# based on
# https://blog.shichao.io/2012/10/04/
# progress_speed_indicator_for_urlretrieve_in_python.html
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a57bd0b80c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7cabbb1d2e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f584ea5cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 74df1483b5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9cb19e11bd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a727d4dd1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88bcbec39d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f3ed8fdff (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 785ee36c56 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 560c477247 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd5fbf27b1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1da1fea1ab (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5f67fc32e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c6adb02431 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9eed1728a8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f9445e850e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9e4d6ad5d0 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b89539ef3e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 77e6855cbe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0e5ebd3da6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e6396a49fb (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a73d227631 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 5d71474136 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2d07dac9e2 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 73992ddf8e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5f16c1cd9e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7f864362 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 44edcd59e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
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
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
>>>>>>> c427da62e8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 490780e974 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 44edcd59e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a57bd0b80c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 44edcd59e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 5d71474136 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
<<<<<<< HEAD
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 4a727d4dd1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 88bcbec39d (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 7f3ed8fdff (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> c427da62e8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 2d07dac9e2 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 9e4d6ad5d0 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
>>>>>>> 4f92c9c12f (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> b89539ef3e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 0d54fc2b9b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 73992ddf8e (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3f1c008cf1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> ee7f864362 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 44edcd59e3 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 0e5ebd3da6 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cea31271cd (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> e6396a49fb (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> a73d227631 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
# based on https://blog.shichao.io/2012/10/04/progress_speed_indicator_for_urlretrieve_in_python.html
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        sys.stdout.write(
            _("Download in progress, wait until it is finished 0%"),
        )
        return
    if count % 100 != 0:  # be less verbose
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write(
        _(
            "Download in progress, wait until it is finished "
            "{0}%, {1} MB, {2} KB/s, {3:.0f} seconds passed"
        ).format(
            percent,
            progress_size / (1024 * 1024),
            speed,
            duration,
        ),
    )


def download_location(url, name, database):
    """Wrapper to return DownloadError by value

    It also moves the location directory to the database.
    """
    try:
        # TODO: the unpacking could go right to the path (but less
        # robust) or replace copytree here with move
        directory = download_and_extract(source=url, reporthook=reporthook)
        destination = os.path.join(database, name)
        if not is_location_valid(directory):
            return _("Downloaded project is not valid")
        shutil.copytree(src=directory, dst=destination)
        try_rmdir(directory)
    except DownloadError as error:
        return error
    return None


def location_name_from_url(url):
    """Create location name from URL"""
    return legalize_vector_name(name_from_url(url))


DownloadDoneEvent, EVT_DOWNLOAD_DONE = NewEvent()


class LocationDownloadPanel(wx.Panel):
    """Panel to select and initiate downloads of locations.

    Has a place to report errors to user and also any potential problems
    before the user hits the button.

    In the future, it can potentially show also some details about what
    will be downloaded. The choice widget can be also replaced.

    For the future, there can be multiple panels with different methods
    or sources, e.g. direct input of URL. These can be in separate tabs
    of one panel (perhaps sharing the common background download and
    message logic).
    """

    def __init__(self, parent, database, locations=LOCATIONS):
        """

        :param database: directory with G database to download to
        :param locations: list of dictionaries with label and url
        """
        wx.Panel.__init__(self, parent=parent)

        self.parent = parent
        self._last_downloaded_location_name = None
        self._download_in_progress = False
        self.database = database
        self.locations = locations
        self._abort_btn_label = _("Abort")
        self._abort_btn_tooltip = _("Abort download")

        self.label = StaticText(
            parent=self, label=_("Select sample project to download:")
        )

        choices = []
        for item in self.locations:
            choices.append(item["label"])
        self.choice = wx.Choice(parent=self, choices=choices)

        self.choice.Bind(wx.EVT_CHOICE, self.OnChangeChoice)
        self.parent.download_button.Bind(wx.EVT_BUTTON, self.OnDownload)
        # TODO: add button for a link to an associated website?
        # TODO: add thumbnail for each location?

        # TODO: messages copied from gis_set.py, need this as API?
        self.message = StaticText(parent=self, size=(-1, 50))
        sys.stdout = RedirectText(self.message)

        # It is not clear if all wx versions supports color, so try-except.
        # The color itself may not be correct for all platforms/system settings
        # but in
        # http://xoomer.virgilio.it/infinity77/wxPython/Widgets/wx.SystemSettings.html
        # there is no 'warning' color.
        try:
            self.message.SetForegroundColour(wx.Colour(255, 0, 0))
        except AttributeError:
            pass

        self._layout()

        default = 0
        self.choice.SetSelection(default)
        self.CheckItem(self.locations[default])

        self.thread = gThread()

    def _layout(self):
        """Create and layout sizers"""
        vertical = wx.BoxSizer(wx.VERTICAL)
        self.sizer = vertical

        vertical.Add(
            self.label,
            proportion=0,
            flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT,
            border=10,
        )
        vertical.Add(
            self.choice,
            proportion=0,
            flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT,
            border=10,
        )
        vertical.AddStretchSpacer()
        vertical.Add(
            self.message,
            proportion=0,
            flag=wx.ALIGN_LEFT | wx.ALL | wx.EXPAND,
            border=10,
        )

        self.SetSizer(vertical)
        vertical.Fit(self)
        self.Layout()
        self.SetMinSize(self.GetBestSize())

    def _change_download_btn_label(
        self, label=_("Do&wnload"), tooltip=_("Download selected project")
    ):
        """Change download button label/tooltip"""
        if self.parent.download_button:
            self.parent.download_button.SetLabel(label)
            self.parent.download_button.SetToolTip(tooltip)

    def OnDownload(self, event):
        """Handle user-initiated action of download"""
        button_label = self.parent.download_button.GetLabel()
        if button_label in {_("Download"), _("Do&wnload")}:
            self._change_download_btn_label(
                label=self._abort_btn_label,
                tooltip=self._abort_btn_tooltip,
            )
            Debug.msg(1, "OnDownload")
            if self._download_in_progress:
                self._warning(_("Download in progress, wait until it is finished"))
            index = self.choice.GetSelection()
            self.DownloadItem(self.locations[index])
        else:
            self.parent.OnCancel()

    def DownloadItem(self, item):
        """Download the selected item"""
        Debug.msg(1, "DownloadItem: %s" % item)
        # similar code as in CheckItem
        url = item["url"]
        dirname = location_name_from_url(url)
        destination = os.path.join(self.database, dirname)
        if os.path.exists(destination):
            self._error(
                _(
                    "Project name {name} already exists in {path}, download canceled"
                ).format(name=dirname, path=self.database)
            )
            self._change_download_btn_label()
            return

        def download_complete_callback(event):
            self._download_in_progress = False
            errors = event.ret
            if errors:
                self._error(_("Download failed: %s") % errors)
            else:
                self._last_downloaded_location_name = dirname
                self._warning(
                    _(
                        "Download completed. The downloaded sample data is available "
                        "now in the data tree"
                    )
                )
            self._change_download_btn_label()

        def terminate_download_callback(event):
            # Clean up after urllib urlretrieve which is used internally
            # in grass.utils.
            from urllib import request  # pylint: disable=import-outside-toplevel

            self._download_in_progress = False
            request.urlcleanup()
            sys.stdout.write("Download aborted")
            self.thread = gThread()
            self._change_download_btn_label()

        self._download_in_progress = True
        self._warning(_("Download in progress, wait until it is finished"))
        self.thread.Run(
            callable=download_location,
            url=url,
            name=dirname,
            database=self.database,
            ondone=download_complete_callback,
            onterminate=terminate_download_callback,
        )

    def OnChangeChoice(self, event):
        """React to user changing the selection"""
        index = self.choice.GetSelection()
        self.CheckItem(self.locations[index])

    def CheckItem(self, item):
        """Check what user selected and report potential issues"""
        # similar code as in DownloadItem
        url = item["url"]
        dirname = location_name_from_url(url)
        destination = os.path.join(self.database, dirname)
        if os.path.exists(destination):
            self._warning(
                _("Project named {name} already exists, rename it first").format(
                    name=dirname
                )
            )
            self.parent.download_button.SetLabel(label=_("Download"))
            return
        self._clearMessage()

    def GetLocation(self):
        """Get the name of the last location downloaded by the user"""
        return self._last_downloaded_location_name

    def _warning(self, text):
        """Displays a warning, hint or info message to the user.

        This function can be used for all kinds of messages except for
        error messages.

        .. note::
            There is no cleaning procedure. You should call
            _clearMessage() when you know that there is everything
            correct.
        """
        sys.stdout.write(text)
        self.sizer.Layout()

    def _error(self, text):
        """Displays a error message to the user.

        This function should be used only when something serious and unexpected
        happens, otherwise _showWarning should be used.

        .. note::
            There is no cleaning procedure. You should call
            _clearMessage() when you know that there is everything
            correct.
        """
        sys.stdout.write(_("Error: {text}").format(text=text))
        self.sizer.Layout()

    def _clearMessage(self):
        """Clears/hides the error message."""
        # we do no hide widget
        # because we do not want the dialog to change the size
        self.message.SetLabel("")
        self.sizer.Layout()


class LocationDownloadDialog(wx.Dialog):
    """Dialog for download of locations

    Contains the panel and Cancel button.
    """

    def __init__(self, parent, database, title=_("Dataset Download")):
        """
        :param database: database to download the project (location) to
        :param title: window title if the default is not appropriate
        """
        wx.Dialog.__init__(self, parent=parent, title=title)
        cancel_button = Button(self, id=wx.ID_CANCEL)
        self.download_button = Button(parent=self, id=wx.ID_ANY, label=_("Do&wnload"))
        self.download_button.SetToolTip(_("Download selected dataset"))
        self.panel = LocationDownloadPanel(parent=self, database=database)
        cancel_button.Bind(wx.EVT_BUTTON, self.OnCancel)
        self.Bind(wx.EVT_CLOSE, self.OnCancel)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel, proportion=1, flag=wx.EXPAND)

        button_sizer = wx.StdDialogButtonSizer()
        button_sizer.Add(
            cancel_button,
            proportion=0,
            flag=wx.EXPAND | wx.LEFT | wx.RIGHT,
            border=5,
        )
        button_sizer.Add(
            self.download_button,
            proportion=0,
            flag=wx.EXPAND | wx.LEFT | wx.RIGHT,
            border=5,
        )
        button_sizer.Realize()

        self.sizer.Add(
            button_sizer,
            proportion=0,
            flag=wx.ALIGN_RIGHT | wx.TOP | wx.BOTTOM,
            border=10,
        )
        self.SetSizer(self.sizer)
        self.sizer.Fit(self)

        self.Layout()

    def GetLocation(self):
        """Get the name of the last location downloaded by the user"""
        return self.panel.GetLocation()

    def OnCancel(self, event=None):
        if self.panel._download_in_progress:
            # running thread
            dlg = wx.MessageDialog(
                parent=self,
                message=_("Do you want to cancel dataset download?"),
                caption=_("Abort download"),
                style=wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION | wx.CENTRE,
            )

            ret = dlg.ShowModal()
            dlg.Destroy()

            if ret == wx.ID_NO:
                return
            self.panel.thread.Terminate()
            self.panel._change_download_btn_label()

        if event:
            self.EndModal(wx.ID_CANCEL)


def main():
    """Tests the download dialog"""
    if len(sys.argv) < 2:
        sys.exit("Provide a test directory")
    database = sys.argv[1]

    app = wx.App()

    if len(sys.argv) == 2 or sys.argv[2] == "dialog":
        window = LocationDownloadDialog(parent=None, database=database)
        window.ShowModal()
        location = window.GetLocation()
        if location:
            print(location)
        window.Destroy()
    elif sys.argv[2] == "panel":
        window = wx.Dialog(parent=None)
        panel = LocationDownloadPanel(parent=window, database=database)
        window.ShowModal()
        location = panel.GetLocation()
        if location:
            print(location)
        window.Destroy()
    else:
        print("Unknown settings: try dialog or panel")

    app.MainLoop()


if __name__ == "__main__":
    main()
