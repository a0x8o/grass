# MODULE:    grass.utils
#
# AUTHOR(S): Vaclav Petras <wenzeslaus gmail com>
#
# PURPOSE:   Collection of various helper general (non-GRASS) utilities
#
# COPYRIGHT: (C) 2021 Vaclav Petras, and by the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.

"""Download and extract various archives"""

import os
<<<<<<< HEAD
<<<<<<< HEAD
import re
=======
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
import shutil
import tarfile
import tempfile
import zipfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import urlretrieve


<<<<<<< HEAD
<<<<<<< HEAD
reponse_content_type_header_pattern = re.compile(r"application/(zip|octet-stream)")
reponse_content_disposition_header_pattern = re.compile(r"attachment; filename=.*.zip$")


=======
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
def debug(*args, **kwargs):
    """Print a debug message (to be used in this module only)

    Using the stanard grass.script debug function is nice, but it may create a circular
    dependency if this is used from grass.script, so this is a wrapper which lazy
    imports the standard function.
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    # Lazy import to avoding potential circular dependency.
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
    # Lazy import to avoding potential circular dependency.
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
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 74df1483b5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
    # Lazy import to avoiding potential circular dependency.
=======
    # Lazy import to avoding potential circular dependency.
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
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5d71474136 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
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
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd181bd378 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3c5e1e78e7 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> c427da62e8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 490780e974 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 8179f73812 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> a57bd0b80c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
<<<<<<< HEAD
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
    # Lazy import to avoding potential circular dependency.
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
    # Lazy import to avoding potential circular dependency.
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
    # Lazy import to avoding potential circular dependency.
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
    # Lazy import to avoding potential circular dependency.
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
    # Lazy import to avoding potential circular dependency.
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
    # Lazy import to avoding potential circular dependency.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3e9fe02ef5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
    import grass.script as gs  # pylint: disable=import-outside-toplevel

    gs.debug(*args, **kwargs)


class DownloadError(Exception):
    """Error happened during download or when processing the file"""


# modified copy from g.extension
# TODO: Possibly migrate to shutil.unpack_archive.
def extract_tar(name, directory, tmpdir):
    """Extract a TAR or a similar file into a directory"""
    debug(
        f"extract_tar(name={name}, directory={directory}, tmpdir={tmpdir})",
        3,
    )
    try:
        tar = tarfile.open(name)
        extract_dir = os.path.join(tmpdir, "extract_dir")
        os.mkdir(extract_dir)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        tar.extractall(path=extract_dir)
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
        tar.extractall(path=extract_dir)
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
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 74df1483b5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))

        # Extraction filters were added in Python 3.12,
        # and backported to 3.8.17, 3.9.17, 3.10.12, and 3.11.4
        # See
        # https://docs.python.org/3.12/library/tarfile.html#tarfile-extraction-filter
        # and https://peps.python.org/pep-0706/
        # In Python 3.12, using `filter=None` triggers a DepreciationWarning,
        # and in Python 3.14, `filter='data'` will be the default
        if hasattr(tarfile, "data_filter"):
            tar.extractall(path=extract_dir, filter="data")
        else:
            # Remove this when no longer needed
            debug(_("Extracting may be unsafe; consider updating Python"))
            tar.extractall(path=extract_dir)

=======
        tar.extractall(path=extract_dir)
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
<<<<<<< HEAD
<<<<<<< HEAD
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
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> ef2ef53f44 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5ff187f7d5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> c427da62e8 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> 490780e974 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
<<<<<<< HEAD
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e3f946d7fe (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
>>>>>>> a57bd0b80c (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
        tar.extractall(path=extract_dir)
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
        tar.extractall(path=extract_dir)
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
        tar.extractall(path=extract_dir)
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
        tar.extractall(path=extract_dir)
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
        tar.extractall(path=extract_dir)
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
        tar.extractall(path=extract_dir)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3e9fe02ef5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> c3b0cfd10b (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
        files = os.listdir(extract_dir)
        _move_extracted_files(
            extract_dir=extract_dir, target_dir=directory, files=files
        )
    except tarfile.TarError as error:
        raise DownloadError(
            _("Archive file is unreadable: {0}").format(error)
        ) from error
    except EOFError as error:
        raise DownloadError(
            _("Archive file is incomplete: {0}").format(error)
        ) from error


extract_tar.supported_formats = ["tar.gz", "gz", "bz2", "tar", "gzip", "targz", "xz"]


# modified copy from g.extension
# TODO: Possibly migrate to shutil.unpack_archive.
def extract_zip(name, directory, tmpdir):
    """Extract a ZIP file into a directory"""
    debug(
        f"extract_zip(name={name}, directory={directory}, tmpdir={tmpdir})",
        3,
    )
    try:
        zip_file = zipfile.ZipFile(name, mode="r")
        file_list = zip_file.namelist()
        # we suppose we can write to parent of the given dir
        # (supposing a tmp dir)
        extract_dir = os.path.join(tmpdir, "extract_dir")
        os.mkdir(extract_dir)
        for subfile in file_list:
            # this should be safe in Python 2.7.4
            zip_file.extract(subfile, extract_dir)
        files = os.listdir(extract_dir)
        _move_extracted_files(
            extract_dir=extract_dir, target_dir=directory, files=files
        )
    except zipfile.BadZipfile as error:
        raise DownloadError(_("ZIP file is unreadable: {0}").format(error))


# modified copy from g.extension
def _move_extracted_files(extract_dir, target_dir, files):
    """Fix state of extracted file by moving them to different directory

    When extracting, it is not clear what will be the root directory
    or if there will be one at all. So this function moves the files to
    a different directory in the way that if there was one directory extracted,
    the contained files are moved.
    """
    debug("_move_extracted_files({})".format(locals()))
    if len(files) == 1:
        actual_path = os.path.join(extract_dir, files[0])
        if os.path.isdir(actual_path):
            shutil.copytree(actual_path, target_dir)
        else:
            shutil.copy(actual_path, target_dir)
    else:
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        for file_name in files:
            actual_file = os.path.join(extract_dir, file_name)
            if os.path.isdir(actual_file):
                # Choice of copy tree function:
                # shutil.copytree() fails when subdirectory exists.
                # However, distutils.copy_tree() may fail to create directories before
                # copying files into them when copying to a recently deleted directory.
                shutil.copytree(actual_file, os.path.join(target_dir, file_name))
            else:
                shutil.copy(actual_file, os.path.join(target_dir, file_name))


# modified copy from g.extension
# TODO: remove the hardcoded location/extension, use general name
def download_and_extract(source, reporthook=None):
    """Download a file (archive) from URL and extract it

    Call urllib.request.urlcleanup() to clean up after urlretrieve if you terminate
    this function from another thread.
    """
    source_path = Path(urlparse(source).path)
    tmpdir = tempfile.mkdtemp()
    debug("Tmpdir: {}".format(tmpdir))
    directory = Path(tmpdir) / "extracted"
    http_error_message = _("Download file from <{url}>, return status code {code}, ")
    url_error_message = _(
        "Download file from <{url}>, failed. Check internet connection."
    )
    if source_path.suffix and source_path.suffix == ".zip":
        archive_name = os.path.join(tmpdir, "archive.zip")
        try:
            filename, headers = urlretrieve(source, archive_name, reporthook)
        except HTTPError as err:
            raise DownloadError(
                http_error_message.format(
                    url=source,
                    code=err,
                ),
            )
        except URLError:
            raise DownloadError(url_error_message.format(url=source))
<<<<<<< HEAD
<<<<<<< HEAD

        if not re.search(
            reponse_content_type_header_pattern, headers.get("content-type", "")
        ) and not re.search(
            reponse_content_disposition_header_pattern,
            headers.get("content-disposition", ""),
        ):
=======
        if headers.get("content-type", "") != "application/zip":
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
        if headers.get("content-type", "") != "application/zip":
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            raise DownloadError(
                _(
                    "Download of <{url}> failed or file <{name}> is not a ZIP file"
                ).format(url=source, name=filename)
            )
        extract_zip(name=archive_name, directory=directory, tmpdir=tmpdir)
    elif source_path.suffix and source_path.suffix[1:] in extract_tar.supported_formats:
        ext = "".join(source_path.suffixes)
        archive_name = os.path.join(tmpdir, "archive" + ext)
        try:
            urlretrieve(source, archive_name, reporthook)
        except HTTPError as err:
            raise DownloadError(
                http_error_message.format(
                    url=source,
                    code=err,
                ),
            )
        except URLError:
            raise DownloadError(url_error_message.format(url=source))
        extract_tar(name=archive_name, directory=directory, tmpdir=tmpdir)
    else:
        # probably programmer error
        raise DownloadError(_("Unknown format '{}'.").format(source))
    return directory


def name_from_url(url):
    """Extract name from URL"""
    name = os.path.basename(urlparse(url).path)
    name = os.path.splitext(name)[0]
    if name.endswith(".tar"):
        # Special treatment of .tar.gz extension.
        return os.path.splitext(name)[0]
    return name
