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
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> c248909064 (pythonlib: Remove star imports (#1546))
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 7e83b17a18 (pythonlib: Remove star imports (#1546))
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
<<<<<<< HEAD
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
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
=======
>>>>>>> main
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 29302c9ef8 (pythonlib: Remove star imports (#1546))
=======
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
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
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
                    return decode(data, encoding=encoding)
=======
                    return decode(stdout, encoding=encoding)
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
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
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
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
