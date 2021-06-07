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
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
=======
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
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
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
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    else:
        raise ValueError("Either start_directory or config_file must be set")
    if "gunittest" not in config_parser:
        # Create an empty section if file is not available or section is not present.
        config_parser.read_dict({"gunittest": {}})
    return config_parser["gunittest"]
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
def get_config(start_directory):
    """Read configuration if available, return empty dict if not"""
    config_parser = configparser.ConfigParser()
    config_file = Path(start_directory) / CONFIG_FILENAME
    if config_file.is_file():
        config_parser.read(config_file)
    if "gunittest" in config_parser:
        return config_parser["gunittest"]
    return {}
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)


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
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))

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

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
=======
=======
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
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
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
=======
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
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
=======
=======
    config = get_config(start_dir)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)

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
