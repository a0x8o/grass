"""
GRASS Python testing framework test files invoker (runner)

Copyright (C) 2014 by the GRASS Development Team
This program is free software under the GNU General Public
License (>=v2). Read the file COPYING that comes with GRASS GIS
for details.

:authors: Vaclav Petras
"""

import collections
import os
from pathlib import Path
import shutil
import subprocess
import sys

from .checkers import text_to_keyvalue

from .loader import GrassTestLoader, discover_modules
from .reporters import (
    GrassTestFilesMultiReporter,
    GrassTestFilesTextReporter,
    GrassTestFilesHtmlReporter,
    TestsuiteDirReporter,
    GrassTestFilesKeyValueReporter,
    get_svn_path_authors,
    NoopFileAnonymizer,
    keyvalue_to_text,
)
from .utils import silent_rmtree, ensure_dir

import grass.script as gs
from grass.script.utils import decode, _get_encoding

<<<<<<< HEAD
maketrans = str.maketrans
=======
try:
    from string import maketrans
except ImportError:
    maketrans = str.maketrans

import collections
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))


# TODO: this might be more extend then update
def update_keyval_file(filename, module, returncode):
    if os.path.exists(filename):
        keyval = text_to_keyvalue(Path(filename).read_text(), sep="=")
    else:
        keyval = {}

    # this is for one file
    test_file_authors = get_svn_path_authors(module.abs_file_path)
    # in case that SVN is not available use empty authors
    if test_file_authors is None:
        test_file_authors = ""

    # always overwrite name and status
    keyval["name"] = module.name
    keyval["tested_dir"] = module.tested_dir
    if "status" not in keyval.keys():
<<<<<<< HEAD
<<<<<<< HEAD
        status = "failed" if returncode is None or returncode else "passed"
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        if returncode is None or returncode:
            status = "failed"
        else:
            status = "passed"
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        keyval["status"] = status
    keyval["returncode"] = returncode
    keyval["test_file_authors"] = test_file_authors

    Path(filename).write_text(keyvalue_to_text(keyval))
    return keyval


class GrassTestFilesInvoker:
    """A class used to invoke test files and create the main report"""

    # TODO: it is not clear what clean_outputs mean, if should be split
    # std stream, random outputs, saved results, profiling
    # not stdout and stderr if they contain test results
    # we can also save only failed tests, or generate only if assert fails
    def __init__(
        self,
        start_dir,
        clean_mapsets=True,
        clean_outputs=True,
        clean_before=True,
        testsuite_dir="testsuite",
        file_anonymizer=None,
        timeout=None,
    ):
        """

        :param bool clean_mapsets: if the mapsets should be removed
        :param bool clean_outputs: meaning is unclear: random tests outputs,
            saved images from maps, profiling?
        :param bool clean_before: if mapsets, outputs, and results
            should be removed before the tests start
            (advantageous when the previous run left everything behind)
        :param float timeout: maximum duration of one test in seconds
        """
        self.start_dir = start_dir
        self.clean_mapsets = clean_mapsets
        self.clean_outputs = clean_outputs
        self.clean_before = clean_before
        self.testsuite_dir = testsuite_dir  # TODO: solve distribution of this constant
        # reporter is created for each call of run_in_location()
        self.reporter = None

        self.testsuite_dirs = None
        if file_anonymizer is None:
            self._file_anonymizer = NoopFileAnonymizer()
        else:
            self._file_anonymizer = file_anonymizer

        self.timeout = timeout

    def _create_mapset(self, gisdbase, location, module):
        """Create mapset according to information in module.

        :param loader.GrassTestPythonModule module:
        """
        # TODO: use g.mapset -c, no need to duplicate functionality
        # All path characters such as slash, backslash and dot are replaced.
        dir_as_name = gs.legalize_vector_name(module.tested_dir, fallback_prefix=None)
        # Multiple processes can run the same test in the same location.
        mapset = gs.append_node_pid(f"{dir_as_name}_{module.name}")
        # TODO: use grass module to do this? but we are not in the right gisdbase
        mapset_dir = os.path.join(gisdbase, location, mapset)
        if self.clean_before:
            silent_rmtree(mapset_dir)
        os.mkdir(mapset_dir)
        # TODO: default region in mapset will be what?
        # copy DEFAULT_WIND file from PERMANENT to WIND
<<<<<<< HEAD
        # TODO: this should be a function in grass.script (used also in gis_set.py,
        # PyGRASS also has its way with Mapset)
=======
        # TODO: this should be a function in grass.script (used also in gis_set.py, PyGRASS also has its way with Mapset)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
        shutil.copy(
            os.path.join(gisdbase, location, "PERMANENT", "DEFAULT_WIND"),
            os.path.join(mapset_dir, "WIND"),
        )
        return mapset, mapset_dir

    def _run_test_module(self, module, results_dir, gisdbase, location, timeout):
        """Run one test file."""
        self.testsuite_dirs[module.tested_dir].append(module.name)
        cwd = os.path.join(results_dir, module.tested_dir, module.name)
        data_dir = os.path.join(module.file_dir, "data")
        if os.path.exists(data_dir):
            # TODO: link dir instead of copy tree and remove link afterwads
            # (removing is good because of testsuite dir in samplecode)
            # TODO: use different dir name in samplecode and test if it works
            shutil.copytree(
                data_dir,
                os.path.join(cwd, "data"),
                ignore=shutil.ignore_patterns("*.svn*"),
            )
        ensure_dir(os.path.abspath(cwd))
        # TODO: put this to constructor and copy here again
        env = os.environ.copy()
        mapset, mapset_dir = self._create_mapset(gisdbase, location, module)
        gisrc = gs.setup.write_gisrc(gisdbase, location, mapset)

        # here is special setting of environmental variables for running tests
        # some of them might be set from outside in the future and if the list
        # will be long they should be stored somewhere separately

        # use custom gisrc, not current session gisrc
        env["GISRC"] = gisrc
        # percentage in plain format is 0...10...20... ...100
        env["GRASS_MESSAGE_FORMAT"] = "plain"

        stdout_path = os.path.join(cwd, "stdout.txt")
        stderr_path = os.path.join(cwd, "stderr.txt")

        self.reporter.start_file_test(module)
        # TODO: we might clean the directory here before test if non-empty

        if module.file_type == "py":
            # ignoring shebang line to use current Python
            # and also pass parameters to it
            # add also '-Qwarn'?
            args = [sys.executable, "-tt", module.abs_file_path]
        elif module.file_type == "sh":
            # ignoring shebang line to pass parameters to shell
            # expecting system to have sh or something compatible
            # TODO: add some special checks for MS Windows
            # using -x to see commands in stderr
            # using -e to terminate fast
            # from dash manual:
            # -e errexit     If not interactive, exit immediately if any
            #                untested command fails.  The exit status of a com‐
            #                mand is considered to be explicitly tested if the
            #                command is used to control an if, elif, while, or
            #                until; or if the command is the left hand operand
            #                of an '&&' or '||' operator.
            args = ["sh", "-e", "-x", module.abs_file_path]
        else:
            args = [module.abs_file_path]
        try:
            p = subprocess.run(
                args,
                cwd=cwd,
                env=env,
<<<<<<< HEAD
<<<<<<< HEAD
                capture_output=True,
                timeout=timeout,
                check=False,
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
>>>>>>> 29302c9ef8 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e2f520cfc3 (pythonlib: Remove star imports (#1546))
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c97872ced (pythonlib: Remove star imports (#1546))
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
>>>>>>> 2b9c47dad2 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7879fb0d48 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2e4a058ca6 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9bd3ee5790 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 958298688f (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cda7754789 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> edbe88c194 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> abaa36c727 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> fd6b673316 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4d9f88c17a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 9407a0d6c1 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d7915bf932 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 38eafe025f (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12c7bdbe15 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> c5e22f8b98 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d4718ecdfb (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 813bf89b9d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 16b8b4fdeb (pythonlib: Remove star imports (#1546))
=======
>>>>>>> a55384b51b (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a2835ab3d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2e22515ef0 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c72ebf83a6 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> bca36f399f (pythonlib: Remove star imports (#1546))
>>>>>>> 585ba722f9 (pythonlib: Remove star imports (#1546))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
>>>>>>> c6554e4c24 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 29302c9ef8 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c97872ced (pythonlib: Remove star imports (#1546))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d7d1827cf8 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f523f7cda (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 694dd243d2 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 655dd6fc15 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5d3b09cb4 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a78d3eda (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8e0602d79 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b0bb5f8b62 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c9ede9fa1e (pythonlib: Remove star imports (#1546))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7879fb0d48 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9bd3ee5790 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cda7754789 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> abaa36c727 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4d9f88c17a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d7915bf932 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12c7bdbe15 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d4718ecdfb (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 16b8b4fdeb (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a2835ab3d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c72ebf83a6 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 29302c9ef8 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 240dcc86f4 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> e2f520cfc3 (pythonlib: Remove star imports (#1546))
=======
<<<<<<< HEAD
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 5c97872ced (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 628e5dfc04 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 2b9c47dad2 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
=======
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
=======
                capture_output=True,
>>>>>>> b90fc735fa (style: Fix replace-stdout-stderr (UP022) (#4000))
                timeout=timeout,
                check=False,
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
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> 65eebf45c4 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> ac5ea6fbe2 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 2f785ecbac (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> f008e4ec0d (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1de92a2db2 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 30e75ea311 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e83b17a18 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 29302c9ef8 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 95adae2f53 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e2f520cfc3 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c97872ced (pythonlib: Remove star imports (#1546))
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
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3c9b290870 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 06688e02ca (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 1de92a2db2 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 2911772b25 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> ba719f126c (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 8fcf52b064 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 30e75ea311 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> aa4e8b6611 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> ba3eb01af9 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 1acc93c650 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e83b17a18 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> c248909064 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> c6554e4c24 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 8ac6037718 (pythonlib: Remove star imports (#1546))
=======
=======
=======
=======
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
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 29302c9ef8 (pythonlib: Remove star imports (#1546))
>>>>>>> 9ddc609ecd (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 7879fb0d48 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 8630c1908e (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 29302c9ef8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 88c8bac31a (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> bdc1a9eff8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> e54d3f3e40 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 95adae2f53 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 60747a09b3 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 240dcc86f4 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 65eebf45c4 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 705f9aa694 (pythonlib: Remove star imports (#1546))
=======
=======
=======
=======
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
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> e2f520cfc3 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 3c9b290870 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 1493fa586e (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> bd15a01a37 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 858dcd2c02 (pythonlib: Remove star imports (#1546))
=======
=======
=======
=======
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
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 5c97872ced (pythonlib: Remove star imports (#1546))
>>>>>>> 06688e02ca (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> af682d8734 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 2e4a058ca6 (pythonlib: Remove star imports (#1546))
=======
=======
=======
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
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 5c97872ced (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 9bd3ee5790 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 0b441b6432 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 958298688f (pythonlib: Remove star imports (#1546))
=======
=======
=======
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
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> d7d1827cf8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> cda7754789 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 474e98d46c (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> edbe88c194 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 2f523f7cda (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> abaa36c727 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 4bd0126b6c (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> fd6b673316 (pythonlib: Remove star imports (#1546))
=======
=======
=======
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
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 694dd243d2 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 4d9f88c17a (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 9e2a78d963 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 9407a0d6c1 (pythonlib: Remove star imports (#1546))
=======
=======
=======
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
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 655dd6fc15 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> d7915bf932 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> f4b9197871 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 38eafe025f (pythonlib: Remove star imports (#1546))
=======
=======
=======
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
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> c5d3b09cb4 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 12c7bdbe15 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 6d81b53481 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> c5e22f8b98 (pythonlib: Remove star imports (#1546))
=======
=======
=======
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
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 71a78d3eda (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> d4718ecdfb (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> e1e8127d65 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 813bf89b9d (pythonlib: Remove star imports (#1546))
=======
=======
=======
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
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> e8e0602d79 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 16b8b4fdeb (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> ce79f96bcb (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> a55384b51b (pythonlib: Remove star imports (#1546))
=======
=======
=======
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
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> b0bb5f8b62 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 8a2835ab3d (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 81fdb5da80 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 2e22515ef0 (pythonlib: Remove star imports (#1546))
=======
=======
=======
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
=======
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> c9ede9fa1e (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> c72ebf83a6 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 628e5dfc04 (pythonlib: Remove star imports (#1546))
>>>>>>> bca36f399f (pythonlib: Remove star imports (#1546))
>>>>>>> 585ba722f9 (pythonlib: Remove star imports (#1546))
            stdout = p.stdout
            stderr = p.stderr
            returncode = p.returncode
            # No timeout to report. Non-none time out values are used to indicate
            # the timeout case.
            timed_out = None
        except subprocess.TimeoutExpired as error:
            stdout = error.stdout
            stderr = error.stderr
            if stdout is None:
                stdout = ""
            if stderr is None:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
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
=======
>>>>>>> osgeo-main
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
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
                stderr = (
                    f"Process has timed out in {timeout}s and produced no error "
                    "output.\n"
                )
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
<<<<<<< HEAD
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
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
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                stderr = f"Process has timed out in {timeout}s and produced no error output.\n"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
            # Return code is None if the process times out.
            # Rest of the code expects success to evaluate as False.
            # So, we assign a failing return code.
            # In any case, we treat the timeout case as a failure.
            returncode = 1
            timed_out = timeout
<<<<<<< HEAD

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
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
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 65eebf45c4 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c6554e4c24 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

=======
>>>>>>> osgeo-main
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 1de92a2db2 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 30e75ea311 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e83b17a18 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 2f785ecbac (pythonlib: Remove star imports (#1546))
=======
=======
=======

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 1de92a2db2 (pythonlib: Remove star imports (#1546))
=======

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e83b17a18 (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 9441e85caa (pythonlib: Remove star imports (#1546))
        def try_decode(data, encodings):
            """Try to decode data (bytes) using one of encodings
=======
=======
<<<<<<< HEAD
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> ba719f126c (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> e2d3096606 (pythonlib: Remove star imports (#1546))
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> ba3eb01af9 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> e1a7453c89 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> osgeo-main
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> c6554e4c24 (pythonlib: Remove star imports (#1546))
=======
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
>>>>>>> 3960f36bc5 (pythonlib: Remove star imports (#1546))
=======
=======
<<<<<<< HEAD
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
=======
=======
<<<<<<< HEAD
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
=======
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> bdc1a9eff8 (pythonlib: Remove star imports (#1546))
=======
=======
<<<<<<< HEAD
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 56010eb999 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> osgeo-main
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 240dcc86f4 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 65eebf45c4 (pythonlib: Remove star imports (#1546))
=======
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 3ab33fc0b6 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ec038aafa (pythonlib: Remove star imports (#1546))
=======
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
>>>>>>> 06688e02ca (pythonlib: Remove star imports (#1546))
=======
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
=======
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 0b441b6432 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 0915ba12ad (pythonlib: Remove star imports (#1546))
=======
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 474e98d46c (pythonlib: Remove star imports (#1546))
=======
<<<<<<< HEAD
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fbbce42f6 (pythonlib: Remove star imports (#1546))
=======
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 4bd0126b6c (pythonlib: Remove star imports (#1546))
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> dd23d5dc15 (pythonlib: Remove star imports (#1546))
=======
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 9e2a78d963 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> e397082cd0 (pythonlib: Remove star imports (#1546))
=======
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> f4b9197871 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 3ced907ea6 (pythonlib: Remove star imports (#1546))
=======
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 6d81b53481 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 53344b046a (pythonlib: Remove star imports (#1546))
=======
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> e1e8127d65 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 0fa369e964 (pythonlib: Remove star imports (#1546))
=======
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> ce79f96bcb (pythonlib: Remove star imports (#1546))
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> da0563df3d (pythonlib: Remove star imports (#1546))
=======
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 81fdb5da80 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> ffb921b231 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> osgeo-main
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 628e5dfc04 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> bca36f399f (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> c190252548 (pythonlib: Remove star imports (#1546))
>>>>>>> 4d810f7f30 (pythonlib: Remove star imports (#1546))
        def try_decode(data, encodings):
            """Try to decode data (bytes) using one of encodings

            Falls back to decoding as UTF-8 with replacement for bytes.
            Strings are returned unmodified.
            """
            for encoding in encodings:
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 4d810f7f30 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> bca36f399f (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e83b17a18 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> c6554e4c24 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3960f36bc5 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
<<<<<<< HEAD
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
=======
                    return decode(data, encoding=encoding)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
                except UnicodeError:
                    pass
            if isinstance(data, bytes):
                return data.decode(encoding="utf-8", errors="replace")
            return data

        stdout = try_decode(stdout, encodings=encodings)
        stderr = try_decode(stderr, encodings=encodings)
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))

            Falls back to decoding as UTF-8 with replacement for bytes.
            Strings are returned unmodified.
            """
            for encoding in encodings:
                try:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e1a7453c89 (pythonlib: Remove star imports (#1546))
                    return decode(data, encoding=encoding)
=======
<<<<<<< HEAD
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
=======
                    return decode(data, encoding=encoding)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
                except UnicodeError:
                    pass
            if isinstance(data, bytes):
                return data.decode(encoding="utf-8", errors="replace")
            return data

        stdout = try_decode(stdout, encodings=encodings)
        stderr = try_decode(stderr, encodings=encodings)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 30e75ea311 (pythonlib: Remove star imports (#1546))
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]
>>>>>>> 29302c9ef8 (pythonlib: Remove star imports (#1546))
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]
>>>>>>> 95adae2f53 (pythonlib: Remove star imports (#1546))

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 240dcc86f4 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 3ab33fc0b6 (pythonlib: Remove star imports (#1546))
=======
<<<<<<< HEAD
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
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
        stdout, stderr = p.communicate()
        returncode = p.returncode
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 628e5dfc04 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> c190252548 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
        stdout, stderr = p.communicate()
        returncode = p.returncode
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        encodings = [_get_encoding(), "utf8", "latin-1", "ascii"]

<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> bd15a01a37 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 858dcd2c02 (pythonlib: Remove star imports (#1546))
=======
=======
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
>>>>>>> 1df4f6c1a9 (pythonlib: Remove star imports (#1546))
>>>>>>> b62c64d69c (pythonlib: Remove star imports (#1546))
        def try_decode(data, encodings):
            """Try to decode data (bytes) using one of encodings

            Falls back to decoding as UTF-8 with replacement for bytes.
            Strings are returned unmodified.
            """
            for encoding in encodings:
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
=======
<<<<<<< HEAD
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 65eebf45c4 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2ec038aafa (pythonlib: Remove star imports (#1546))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 29302c9ef8 (pythonlib: Remove star imports (#1546))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e2f520cfc3 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c97872ced (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b9c47dad2 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 7879fb0d48 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88c8bac31a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 29302c9ef8 (pythonlib: Remove star imports (#1546))
>>>>>>> 9ddc609ecd (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 7879fb0d48 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 6fdaa03757 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 29302c9ef8 (pythonlib: Remove star imports (#1546))
>>>>>>> 88c8bac31a (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
>>>>>>> 56010eb999 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 692afe97f6 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 95adae2f53 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 60747a09b3 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> e2f520cfc3 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 3c9b290870 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 1493fa586e (pythonlib: Remove star imports (#1546))
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5c97872ced (pythonlib: Remove star imports (#1546))
>>>>>>> 06688e02ca (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> af682d8734 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> fcbc6eaf1c (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c97872ced (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 9bd3ee5790 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 0915ba12ad (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> db4f0c5e9e (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d7d1827cf8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> cda7754789 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 4fbbce42f6 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 7c9ebb33c7 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2f523f7cda (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> abaa36c727 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> dd23d5dc15 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> bf337dfc4c (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 694dd243d2 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 4d9f88c17a (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> e397082cd0 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> f8a1d36c40 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 655dd6fc15 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> d7915bf932 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3ced907ea6 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 9cb1837c15 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c5d3b09cb4 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 12c7bdbe15 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 53344b046a (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 16628047b7 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 71a78d3eda (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> d4718ecdfb (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 0fa369e964 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 7ee999faa1 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e8e0602d79 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 16b8b4fdeb (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> da0563df3d (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> da2395c9c7 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b0bb5f8b62 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 8a2835ab3d (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> ffb921b231 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 43413f8004 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c9ede9fa1e (pythonlib: Remove star imports (#1546))
>>>>>>> c72ebf83a6 (pythonlib: Remove star imports (#1546))
                    return decode(data, encoding=encoding)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    return decode(data, encoding=encoding)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
>>>>>>> osgeo-main
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
                    return decode(data, encoding=encoding)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
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
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 57aff3a06a (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3ab33fc0b6 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
=======
>>>>>>> c190252548 (pythonlib: Remove star imports (#1546))
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 29302c9ef8 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 240dcc86f4 (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 3ab33fc0b6 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e2f520cfc3 (pythonlib: Remove star imports (#1546))
=======
<<<<<<< HEAD
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c97872ced (pythonlib: Remove star imports (#1546))
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
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 628e5dfc04 (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> c190252548 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b9c47dad2 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> aa4e8b6611 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7879fb0d48 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 88c8bac31a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 60747a09b3 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 9bd3ee5790 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> cda7754789 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> abaa36c727 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 4d9f88c17a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> d7915bf932 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 12c7bdbe15 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> d4718ecdfb (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 16b8b4fdeb (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 8a2835ab3d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> c72ebf83a6 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> ba719f126c (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 8fcf52b064 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> e2d3096606 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 2bb9b85a2d (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 30e75ea311 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> aa4e8b6611 (pythonlib: Remove star imports (#1546))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 9ddc609ecd (pythonlib: Remove star imports (#1546))
=======
>>>>>>> osgeo-main
>>>>>>> c6554e4c24 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3ab33fc0b6 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
=======
>>>>>>> c190252548 (pythonlib: Remove star imports (#1546))
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ba3eb01af9 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 1acc93c650 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> e1a7453c89 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 158dbc71ea (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
>>>>>>> c6554e4c24 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 8ac6037718 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 2ec038aafa (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 1df4f6c1a9 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 4d810f7f30 (pythonlib: Remove star imports (#1546))
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 3960f36bc5 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> d08c50382a (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 29302c9ef8 (pythonlib: Remove star imports (#1546))
>>>>>>> 9ddc609ecd (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 7879fb0d48 (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 8630c1908e (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 6fdaa03757 (pythonlib: Remove star imports (#1546))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 29302c9ef8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 88c8bac31a (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(data, encoding=encoding)
=======
<<<<<<< HEAD
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> bdc1a9eff8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> e54d3f3e40 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 56010eb999 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 692afe97f6 (pythonlib: Remove star imports (#1546))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 95adae2f53 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 60747a09b3 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> osgeo-main
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 240dcc86f4 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 65eebf45c4 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 705f9aa694 (pythonlib: Remove star imports (#1546))
=======
=======
=======
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 3ab33fc0b6 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 2ec038aafa (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 78a24c3407 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> e2f520cfc3 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 3c9b290870 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 1493fa586e (pythonlib: Remove star imports (#1546))
=======
=======
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> bd15a01a37 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 858dcd2c02 (pythonlib: Remove star imports (#1546))
=======
=======
=======
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 1df4f6c1a9 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> b62c64d69c (pythonlib: Remove star imports (#1546))
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
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5c97872ced (pythonlib: Remove star imports (#1546))
>>>>>>> 06688e02ca (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> af682d8734 (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 2e4a058ca6 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> fcbc6eaf1c (pythonlib: Remove star imports (#1546))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c97872ced (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 9bd3ee5790 (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 0b441b6432 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 958298688f (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 0915ba12ad (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> db4f0c5e9e (pythonlib: Remove star imports (#1546))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d7d1827cf8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> cda7754789 (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(data, encoding=encoding)
=======
<<<<<<< HEAD
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 474e98d46c (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> edbe88c194 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 4fbbce42f6 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 7c9ebb33c7 (pythonlib: Remove star imports (#1546))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2f523f7cda (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> abaa36c727 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> osgeo-main
>>>>>>> bca36f399f (pythonlib: Remove star imports (#1546))
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 4bd0126b6c (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> fd6b673316 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> dd23d5dc15 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> bf337dfc4c (pythonlib: Remove star imports (#1546))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 694dd243d2 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 4d9f88c17a (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 9e2a78d963 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 9407a0d6c1 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> e397082cd0 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> f8a1d36c40 (pythonlib: Remove star imports (#1546))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 655dd6fc15 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> d7915bf932 (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> f4b9197871 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 38eafe025f (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3ced907ea6 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 9cb1837c15 (pythonlib: Remove star imports (#1546))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c5d3b09cb4 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 12c7bdbe15 (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 6d81b53481 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> c5e22f8b98 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 53344b046a (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 16628047b7 (pythonlib: Remove star imports (#1546))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 71a78d3eda (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> d4718ecdfb (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> e1e8127d65 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 813bf89b9d (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 0fa369e964 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 7ee999faa1 (pythonlib: Remove star imports (#1546))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e8e0602d79 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 16b8b4fdeb (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> ce79f96bcb (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> a55384b51b (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> da0563df3d (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> da2395c9c7 (pythonlib: Remove star imports (#1546))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b0bb5f8b62 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 8a2835ab3d (pythonlib: Remove star imports (#1546))
=======
=======
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 81fdb5da80 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 2e22515ef0 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> ffb921b231 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 43413f8004 (pythonlib: Remove star imports (#1546))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
=======
                    return decode(data, encoding=encoding)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c9ede9fa1e (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> c72ebf83a6 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 628e5dfc04 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> bca36f399f (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 585ba722f9 (pythonlib: Remove star imports (#1546))
=======
=======
=======
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> c190252548 (pythonlib: Remove star imports (#1546))
>>>>>>> 4d810f7f30 (pythonlib: Remove star imports (#1546))
>>>>>>> aaf70da5d9 (pythonlib: Remove star imports (#1546))
                except UnicodeError:
                    pass
            if isinstance(data, bytes):
                return data.decode(encoding="utf-8", errors="replace")
            return data

        stdout = try_decode(stdout, encodings=encodings)
        stderr = try_decode(stderr, encodings=encodings)

        Path(stdout_path).write_text(stdout)
        with open(stderr_path, "w") as stderr_file:
            if isinstance(stderr, bytes):
                stderr_file.write(decode(stderr))
            elif isinstance(stderr, str):
                stderr_file.write(stderr)
            else:
                stderr_file.write(stderr.encode("utf8"))
        self._file_anonymizer.anonymize([stdout_path, stderr_path])

        test_summary = update_keyval_file(
            os.path.join(os.path.abspath(cwd), "test_keyvalue_result.txt"),
            module=module,
            returncode=returncode,
        )
        self.reporter.end_file_test(
            module=module,
            cwd=cwd,
            returncode=returncode,
            stdout=stdout_path,
            stderr=stderr_path,
            test_summary=test_summary,
            timed_out=timed_out,
        )
        # TODO: add some try-except or with for better error handling
        os.remove(gisrc)
        # TODO: only if clean up
        if self.clean_mapsets:
            try:
                shutil.rmtree(mapset_dir)
            except OSError:
                # If there are still running processes (e.g., in timeout case),
                # the cleaning may fail on non-empty directory. Although this does
                # not guarantee removal of the directory, try it again, but this
                # time ignore errors if something happens. (More file can appear
                # later on if the processes are still running.)
                shutil.rmtree(mapset_dir, ignore_errors=True)

    def run_in_location(self, gisdbase, location, location_type, results_dir, exclude):
        """Run tests in a given location

        Returns an object with counting attributes of GrassTestFilesCountingReporter,
        i.e., a file-oriented reporter as opposed to testsuite-oriented one.
        Use only the attributes related to the summary, such as file_pass_per,
        not to one file as these will simply contain the last executed file.
        """
        if os.path.abspath(results_dir) == os.path.abspath(self.start_dir):
            raise RuntimeError(
                "Results root directory should not be the same"
                " as discovery start directory"
            )
        self.reporter = GrassTestFilesMultiReporter(
            reporters=[
                GrassTestFilesTextReporter(stream=sys.stderr),
                GrassTestFilesHtmlReporter(
                    file_anonymizer=self._file_anonymizer,
                    main_page_name="testfiles.html",
                ),
                GrassTestFilesKeyValueReporter(
                    info={"location": location, "location_type": location_type}
                ),
            ]
        )
        self.testsuite_dirs = collections.defaultdict(
            list
        )  # reset list of dirs each time
        # TODO: move constants out of loader class or even module
        modules = discover_modules(
            start_dir=self.start_dir,
            grass_location=location_type,
            file_regexp=r".*\.(py|sh)$",
            skip_dirs=GrassTestLoader.skip_dirs,
            testsuite_dir=GrassTestLoader.testsuite_dir,
            all_locations_value=GrassTestLoader.all_tests_value,
            universal_location_value=GrassTestLoader.universal_tests_value,
            import_modules=False,
            exclude=exclude,
        )

        self.reporter.start(results_dir)
        for module in modules:
            self._run_test_module(
                module=module,
                results_dir=results_dir,
                gisdbase=gisdbase,
                location=location,
                timeout=self.timeout,
            )
        self.reporter.finish()

        # TODO: move this to some (new?) reporter
        # TODO: add basic summary of linked files so that the page is not empty
        Path(os.path.join(results_dir, "index.html")).write_text(
            "<html><body>"
            "<h1>Tests for &lt;{location}&gt;"
            " using &lt;{type}&gt; type tests</h1>"
            "<ul>"
            '<li><a href="testsuites.html">Results by testsuites</a>'
            " (testsuite directories)</li>"
            '<li><a href="testfiles.html">Results by test files</a></li>'
            "<ul>"
            "</body></html>".format(location=location, type=location_type)
        )

        testsuite_dir_reporter = TestsuiteDirReporter(
            main_page_name="testsuites.html",
            testsuite_page_name="index.html",
            top_level_testsuite_page_name="testsuite_index.html",
        )
        testsuite_dir_reporter.report_for_dirs(
            root=results_dir, directories=self.testsuite_dirs
        )
        return self.reporter
