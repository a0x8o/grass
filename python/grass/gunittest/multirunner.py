"""
Testing framework module for running tests in Python unittest fashion

Copyright (C) 2014-2021 by the GRASS Development Team
This program is free software under the GNU General Public
License (>=v2). Read the file COPYING that comes with GRASS GIS
for details.

:authors: Vaclav Petras
"""

import sys
import os
import argparse
import subprocess
import locale


def _get_encoding():
    try:
        # Python >= 3.11
        encoding = locale.getencoding()
    except AttributeError:
        encoding = locale.getdefaultlocale()[1]
    if not encoding:
        encoding = "UTF-8"
    return encoding


def decode(bytes_, encoding=None):
    if isinstance(bytes_, bytes):
        return bytes_.decode(_get_encoding())
    return bytes_


def encode(string, encoding=None):
    if isinstance(string, str):
        return string.encode(_get_encoding())
    return string


def text_to_string(text):
    """Convert text to str. Useful when passing text into environments,
    in Python 2 it needs to be bytes on Windows, in Python 3 in needs unicode.
    """
    return decode(text)


def main():
    parser = argparse.ArgumentParser(description="Run tests with new")
    parser.add_argument(
        "--location",
        "-l",
        required=True,
        action="append",
        dest="locations",
        metavar="LOCATION",
        help="Directories with reports",
    )
    parser.add_argument(
        "--location-type",
        "-t",
        action="append",
        dest="location_types",
        default=[],
        metavar="TYPE",
        help="Add repeated values to a list",
    )
    parser.add_argument(
        "--grassbin",
        required=True,
        help="Use file timestamp instead of date in test summary",
    )
    # TODO: rename since every src can be used?
    parser.add_argument(
        "--grasssrc", required=True, help="GRASS GIS source code (to take tests from)"
    )
    parser.add_argument(
        "--grassdata", required=True, help="GRASS GIS data base (GISDBASE)"
    )
    parser.add_argument(
        "--create-main-report",
        help="Create also main report for all tests",
        action="store_true",
        default=False,
        dest="main_report",
    )

    args = parser.parse_args()
    gisdb = args.grassdata
    locations = args.locations
    locations_types = args.location_types

    # TODO: if locations empty or just one we can suppose the same all the time
    if len(locations) != len(locations_types):
        print(
            "ERROR: Number of locations and their tags must be the same",
            file=sys.stderr,
        )
        return 1

    main_report = args.main_report
    grasssrc = args.grasssrc  # TODO: can be guessed from dist
    # TODO: create directory according to date and revision and create reports there

    # some predefined variables, name of the GRASS launch script + location/mapset
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
    grass_executable = args.grassbin

    # Software
    # query GRASS GIS itself for its GISBASE
    # we assume that the start script is available and in the PATH
<<<<<<< HEAD
    # the shell=True is here because of MS Windows? (code taken from wiki)
    startcmd = grass_executable + " --config path"
=======
    # the shell=True is here because of MS Windows? (code taken from wiki)
    startcmd = grass_executable + " --config path"
=======
    # grass8bin = 'C:\Program Files (x86)\GRASS GIS 8.0.git\grass.bat'
    grass8bin = args.grassbin  # TODO: can be used if pressent

    # Software
=======
    # grass8bin = 'C:\Program Files (x86)\GRASS GIS 8.0.git\grass.bat'
    grass8bin = args.grassbin  # TODO: can be used if pressent

    # Software
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    # query GRASS GIS 8 itself for its GISBASE
    # we assume that GRASS GIS' start script is available and in the PATH
    # the shell=True is here because of MS Windows? (code taken from wiki)
    startcmd = grass8bin + " --config path"
<<<<<<< HEAD
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
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
    grass_executable = args.grassbin

    # Software
    # query GRASS GIS itself for its GISBASE
    # we assume that the start script is available and in the PATH
    # the shell=True is here because of MS Windows? (code taken from wiki)
    startcmd = grass_executable + " --config path"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
    # grass8bin = 'C:\Program Files (x86)\GRASS GIS 8.0.git\grass.bat'
    grass8bin = args.grassbin  # TODO: can be used if pressent

    # Software
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    # grass8bin = 'C:\Program Files (x86)\GRASS GIS 8.0.git\grass.bat'
    grass8bin = args.grassbin  # TODO: can be used if pressent

    # Software
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
    # query GRASS GIS 8 itself for its GISBASE
    # we assume that GRASS GIS' start script is available and in the PATH
    # the shell=True is here because of MS Windows? (code taken from wiki)
    startcmd = grass8bin + " --config path"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
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
    grass_executable = args.grassbin

    # Software
    # query GRASS GIS itself for its GISBASE
    # we assume that the start script is available and in the PATH
    # the shell=True is here because of MS Windows? (code taken from wiki)
    startcmd = grass_executable + " --config path"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    grass_executable = args.grassbin

    # Software
    # query GRASS GIS itself for its GISBASE
    # we assume that the start script is available and in the PATH
    # the shell=True is here because of MS Windows? (code taken from wiki)
    startcmd = grass_executable + " --config path"
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
    grass_executable = args.grassbin

    # Software
    # query GRASS GIS itself for its GISBASE
    # we assume that the start script is available and in the PATH
    # the shell=True is here because of MS Windows? (code taken from wiki)
    startcmd = grass_executable + " --config path"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
    p = subprocess.Popen(
        startcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, err = p.communicate()
    if p.returncode != 0:
        print(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
>>>>>>> osgeo-main
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
>>>>>>> osgeo-main
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
>>>>>>> osgeo-main
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
>>>>>>> osgeo-main
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
>>>>>>> osgeo-main
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
>>>>>>> osgeo-main
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
>>>>>>> osgeo-main
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
>>>>>>> osgeo-main
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
>>>>>>> osgeo-main
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
>>>>>>> osgeo-main
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
>>>>>>> osgeo-main
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
>>>>>>> osgeo-main
            "ERROR: Cannot find GRASS GIS 8 start script (%s):\n%s" % (startcmd, err),
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
            "ERROR: Cannot find GRASS GIS 8 start script (%s):\n%s" % (startcmd, err),
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
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
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
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
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
            "ERROR: Cannot find GRASS GIS 8 start script (%s):\n%s" % (startcmd, err),
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
            "ERROR: Cannot find GRASS GIS 8 start script (%s):\n%s" % (startcmd, err),
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
            "ERROR: Cannot find GRASS GIS 8 start script (%s):\n%s" % (startcmd, err),
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
            "ERROR: Cannot find GRASS GIS 8 start script (%s):\n%s" % (startcmd, err),
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
=======
            "ERROR: Cannot find GRASS GIS 8 start script (%s):\n%s" % (startcmd, err),
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
            "ERROR: Cannot find GRASS GIS 8 start script (%s):\n%s" % (startcmd, err),
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "ERROR: Cannot find GRASS GIS start script (%s):\n%s" % (startcmd, err),
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
            file=sys.stderr,
        )
        return 1
    gisbase = decode(out.strip())

    # set GISBASE environment variable
    os.environ["GISBASE"] = text_to_string(gisbase)
    # define GRASS Python environment
    grass_python_dir = os.path.join(gisbase, "etc", "python")
    sys.path.append(grass_python_dir)

    # Data
    # define GRASS DATABASE

    # Set GISDBASE environment variable
    os.environ["GISDBASE"] = text_to_string(gisdb)

    # import GRASS Python package for initialization
    import grass.script as gs

    # launch session
    # we need some location and mapset here
    # TODO: can init work without it or is there some demo location in dist?
    location = locations[0].split(":")[0]
    mapset = "PERMANENT"
    gs.setup.init(gisbase, gisdb, location, mapset)

    reports = []
    for location, location_type in zip(locations, locations_types):
        # here it is quite a good place to parallelize
        # including also type to make it unique and preserve it for sure
        report = "report_for_" + location + "_" + location_type
        absreport = os.path.abspath(report)
        p = subprocess.Popen(
            [
                sys.executable,
                "-tt",
                "-m",
                "grass.gunittest.main",
                "--grassdata",
                gisdb,
                "--location",
                location,
                "--location-type",
                location_type,
                "--output",
                absreport,
            ],
            cwd=grasssrc,
        )
        returncode = p.wait()
        reports.append(report)

    if main_report:
        # TODO: solve the path to source code (work now only for grass source code)
        arguments = [
            sys.executable,
            grasssrc + "/python/grass/gunittest/" + "multireport.py",
            "--timestapms",
        ]
        arguments.extend(reports)
        p = subprocess.Popen(arguments)
        returncode = p.wait()
        if returncode != 0:
            print("ERROR: Creation of main report failed.", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
