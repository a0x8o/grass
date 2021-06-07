"""
GRASS Python testing framework module for running from command line

Copyright (C) 2014-2021 by the GRASS Development Team
This program is free software under the GNU General Public
License (>=v2). Read the file COPYING that comes with GRASS GIS
for details.

:authors: Vaclav Petras
"""

import os
import sys
import argparse
import configparser
from pathlib import Path

from unittest.main import TestProgram

import grass.script.core as gs

from .loader import GrassTestLoader
from .runner import GrassTestRunner, MultiTestResult, TextTestResult, KeyValueTestResult
from .invoker import GrassTestFilesInvoker
from .utils import silent_rmtree
from .reporters import FileAnonymizer


class GrassTestProgram(TestProgram):
    """A class to be used by individual test files (wrapped in the function)"""

    def __init__(
        self,
        exit_at_end,
        grass_location,
        clean_outputs=True,
        unittest_argv=None,
        module=None,
        verbosity=1,
        failfast=None,
        catchbreak=None,
    ):
        """Prepares the tests in GRASS way and then runs the tests.

        :param bool clean_outputs: if outputs in mapset and in ?
        """
        self.test = None
        self.grass_location = grass_location
        # it is unclear what the exact behavior is in unittest
        # buffer stdout and stderr during tests
        buffer_stdout_stderr = False

        grass_loader = GrassTestLoader(grass_location=self.grass_location)

        text_result = TextTestResult(
            stream=sys.stderr, descriptions=True, verbosity=verbosity
        )
        with open("test_keyvalue_result.txt", "w") as keyval_file:
            keyval_result = KeyValueTestResult(stream=keyval_file)
            result = MultiTestResult(results=[text_result, keyval_result])

            grass_runner = GrassTestRunner(
                verbosity=verbosity,
                failfast=failfast,
                buffer=buffer_stdout_stderr,
                result=result,
            )
            super().__init__(
                module=module,
                argv=unittest_argv,
                testLoader=grass_loader,
                testRunner=grass_runner,
                exit=exit_at_end,
                verbosity=verbosity,
                failfast=failfast,
                catchbreak=catchbreak,
                buffer=buffer_stdout_stderr,
            )


def test():
    """Run a test of a module."""
    # TODO: put the link to to the report only if available
    # TODO: how to disable Python code coverage for module and C tests?
    # TODO: we probably need to have different test  functions for C, Python modules,
    # and Python code
    # TODO: combine the results using python -m coverage --help | grep combine
    # TODO: function to anonymize/beautify file names (in content and actual filenames)
    # TODO: implement coverage but only when requested by invoker and only if
    # it makes sense for tests (need to know what is tested)
    # doing_coverage = False
    # try:
    #    import coverage
    #    doing_coverage = True
    #    cov = coverage.coverage(omit="*testsuite*")
    #    cov.start()
    # except ImportError:
    #    pass
    # TODO: add some message somewhere

    # TODO: enable passing omit to exclude also gunittest or nothing
    program = GrassTestProgram(
        module="__main__", exit_at_end=False, grass_location="all"
    )
    # TODO: check if we are in the directory where the test file is
    # this will ensure that data directory is available when it is requested

    # if doing_coverage:
    #    cov.stop()
    #    cov.html_report(directory='testcodecoverage')

    # TODO: is sys.exit the right thing here
    sys.exit(not program.result.wasSuccessful())


def discovery():
    """Recursively find all tests in testsuite directories and run them

    Everything is imported and runs in this process.

    Runs using::
        python main.py discovery [start_directory]
    """

    program = GrassTestProgram(grass_location="nc", exit_at_end=False)

    sys.exit(not program.result.wasSuccessful())


CONFIG_FILENAME = ".gunittest.cfg"


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory, config_file):
    """Read configuration if available, return empty section proxy if not

    If file is explicitly specified, it must exist.

    Raises OSError if file is not accessible, e.g., if it exists,
    but there is an issue with permissions.
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
=======
<<<<<<< HEAD
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
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
<<<<<<< HEAD
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
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> main
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
    config_parser = configparser.ConfigParser()
    if config_file:
        with open(config_file, encoding="utf-8") as file:
            config_parser.read_file(file)
    elif start_directory:
        config_file = Path(start_directory) / CONFIG_FILENAME
        # Does not check presence of the file
        config_parser.read(config_file)
<<<<<<< HEAD
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
    config_parser = configparser.ConfigParser()
    config_file = Path(start_directory) / CONFIG_FILENAME
    if config_file.is_file():
        config_parser.read(config_file)
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))


def main():
    parser = argparse.ArgumentParser(
        description="Run test files in all testsuite directories starting"
        " from the current one"
        " (runs on active GRASS session)"
    )
    parser.add_argument(
        "--location",
        dest="location",
        action="store",
        help="Name of location where to perform test",
        required=True,
    )
    parser.add_argument(
        "--location-type",
        dest="location_type",
        action="store",
        default="nc",
        help="Type of tests which should be run (tag corresponding to location)",
    )
    parser.add_argument(
        "--grassdata",
        dest="gisdbase",
        action="store",
        default=None,
        help="GRASS data(base) (GISDBASE) directory (current GISDBASE by default)",
    )
    parser.add_argument(
        "--output",
        dest="output",
        action="store",
        default="testreport",
        help="Output directory",
    )
    parser.add_argument(
        "--min-success",
        dest="min_success",
        action="store",
        default="100",
        type=int,
        help=(
            "Minimum success percentage (lower percentage"
            " than this will result in a non-zero return code; values 0-100)"
        ),
    )
    parser.add_argument(
        "--config",
        dest="config",
        action="store",
        type=str,
        help=f"Path to a configuration file (default: {CONFIG_FILENAME})",
    )
    args = parser.parse_args()
    gisdbase = args.gisdbase
    if gisdbase is None:
        # here we already rely on being in GRASS session
        gisdbase = gs.gisenv()["GISDBASE"]
    location = args.location
    location_type = args.location_type

    if not gisdbase:
        return "GISDBASE (grassdata directory) cannot be empty string\n"
    if not os.path.exists(gisdbase):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
<<<<<<< HEAD

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
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
>>>>>>> osgeo-main
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
        return f"GISDBASE (grassdata directory) <{gisdbase}> does not exist\n"
    if not os.path.exists(os.path.join(gisdbase, location)):
        return (
            f"GRASS Location <{location}>"
            f" does not exist in GRASS Database <{gisdbase}>\n"
        )
    results_dir = args.output
    silent_rmtree(results_dir)  # TODO: too brute force?

    start_dir = "."
    abs_start_dir = os.path.abspath(start_dir)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
    try:
        config = get_config(start_directory=start_dir, config_file=args.config)
    except OSError as error:
        return f"Error reading configuration: {error}"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
=======
    config = get_config(start_dir)
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
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
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
=======
    config = get_config(start_dir)
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
=======
    config = get_config(start_dir)
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
=======
    config = get_config(start_dir)
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
=======
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
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
=======
    config = get_config(start_dir)
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
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
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
=======
    config = get_config(start_dir)
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
=======
    config = get_config(start_dir)
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
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
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
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
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
=======
    config = get_config(start_dir)
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
=======
    config = get_config(start_dir)
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))

    invoker = GrassTestFilesInvoker(
        start_dir=start_dir,
        file_anonymizer=FileAnonymizer(paths_to_remove=[abs_start_dir]),
        timeout=config.getfloat("timeout", None),
    )
    # TODO: remove also results dir from files
    # as an enhancement
    # we can just iterate over all locations available in database
    # but the we don't know the right location type (category, label, shortcut)
    reporter = invoker.run_in_location(
        gisdbase=gisdbase,
        location=location,
        location_type=location_type,
        results_dir=results_dir,
        exclude=config.get("exclude", "").split(),
    )
    if not reporter.test_files:
        return "No tests found or executed"
    if reporter.file_pass_per >= args.min_success:
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
