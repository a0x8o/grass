# MODULE:    grass.benchmark
#
# AUTHOR(S): Vaclav Petras <wenzeslaus gmail com>
#
# PURPOSE:   Benchmarking for GRASS GIS modules
#
# COPYRIGHT: (C) 2021 Vaclav Petras, and by the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.


"""Handling of raw results from benchmarking"""

import copy
import json
<<<<<<< HEAD
<<<<<<< HEAD
from pathlib import Path
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
from types import SimpleNamespace


class ResultsEncoder(json.JSONEncoder):
    """Results encoder for JSON which handles SimpleNamespace objects"""

    def default(self, o):
        """Handle additional types"""
        if isinstance(o, SimpleNamespace):
            return o.__dict__
        return super().default(o)


def save_results(data):
    """Save results structure to JSON.

    If the provided object does not have results attribute,
    it is assumed that the list which should be results attribute was provided,
    so the provided object object is saved under new ``results`` key.

    Returns JSON as str.
    """
    if not hasattr(data, "results"):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        data = {"results": data}
=======
        data = dict(results=data)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
        data = dict(results=data)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        data = {"results": data}
>>>>>>> 898113134f (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
    return json.dumps(data, cls=ResultsEncoder)


def save_results_to_file(results, filename):
    """Saves results to as file as JSON.

    See :func:`save_results` for details.
    """
    text = save_results(results)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    with open(filename, "w", encoding="utf-8") as file:
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    with open(filename, "w", encoding="utf-8") as file:
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    with open(filename, "w", encoding="utf-8") as file:
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    with open(filename, "w", encoding="utf-8") as file:
=======
>>>>>>> osgeo-main
=======
    with open(filename, "w", encoding="utf-8") as file:
=======
>>>>>>> osgeo-main
=======
    with open(filename, "w", encoding="utf-8") as file:
=======
>>>>>>> osgeo-main
=======
    with open(filename, "w", encoding="utf-8") as file:
=======
>>>>>>> osgeo-main
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
    Path(filename).write_text(text, encoding="utf-8")
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
    Path(filename).write_text(text, encoding="utf-8")
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
    Path(filename).write_text(text, encoding="utf-8")
=======
<<<<<<< HEAD
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
    with open(filename, "w", encoding="utf-8") as file:
=======
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
    with open(filename, "w", encoding="utf-8") as file:
=======
>>>>>>> osgeo-main
=======
    with open(filename, "w", encoding="utf-8") as file:
=======
>>>>>>> osgeo-main
    with open(filename, "w") as file:
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
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    with open(filename, "w", encoding="utf-8") as file:
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
    with open(filename, "w", encoding="utf-8") as file:
=======
    with open(filename, "w") as file:
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    with open(filename, "w", encoding="utf-8") as file:
=======
    with open(filename, "w") as file:
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    Path(filename).write_text(text, encoding="utf-8")
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
    with open(filename, "w", encoding="utf-8") as file:
=======
    with open(filename, "w") as file:
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
    with open(filename, "w", encoding="utf-8") as file:
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
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
        file.write(text)
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
    with open(filename, "w") as file:
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        file.write(text)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
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
    with open(filename, "w", encoding="utf-8") as file:
=======
    with open(filename, "w") as file:
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
    with open(filename, "w", encoding="utf-8") as file:
=======
    with open(filename, "w") as file:
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    with open(filename, "w", encoding="utf-8") as file:
=======
    with open(filename, "w") as file:
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    with open(filename, "w", encoding="utf-8") as file:
=======
    with open(filename, "w") as file:
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
    with open(filename, "w", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        file.write(text)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
        file.write(text)
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======
        file.write(text)
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))


def load_results(data):
    """Load results structure from JSON.

    Takes str, returns nested structure with SimpleNamespace instead of the
    default dictionary object. Use attribute access to access by key
    (not dict-like syntax).
    """
    return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))


def load_results_from_file(filename):
    """Loads results from a JSON file.

    See :func:`load_results` for details.
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
>>>>>>> osgeo-main
>>>>>>> main
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
>>>>>>> main
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
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
>>>>>>> osgeo-main
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
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
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
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
<<<<<<< HEAD
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    return load_results(Path(filename).read_text(encoding="utf-8"))
=======
<<<<<<< HEAD
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
    with open(filename, "r", encoding="utf-8") as file:
        return load_results(file.read())
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))


def join_results(results, prefixes=None, select=None, prefixes_as_labels=False):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
    with open(filename, "r") as file:
=======
    with open(filename, "r", encoding="utf-8") as file:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        return load_results(file.read())


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
def join_results(results, prefixes=None, select=None, prefixes_as_labels=False):
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
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
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
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
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
def join_results(results, prefixes=None, select=None, prefixes_as_labels=False):
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
    with open(filename, "r", encoding="utf-8") as file:
        return load_results(file.read())


def join_results(results, prefixes=None, select=None, prefixes_as_labels=False):
<<<<<<< HEAD
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
    with open(filename, "r") as file:
        return load_results(file.read())


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
def join_results(results, prefixes=None, select=None, prefixes_as_labels=False):
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
def join_results(results, prefixes=None, select=None, prefixes_as_labels=False):
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
def join_results(results, prefixes=None, select=None, prefixes_as_labels=False):
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
def join_results(results, prefixes=None, select=None, prefixes_as_labels=False):
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
def join_results(results, prefixes=None, select=None, prefixes_as_labels=False):
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
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
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
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
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
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
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
def join_results(results, prefixes=None, select=None, prefixes_as_labels=False):
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
def join_results(results, prefixes=None, select=None, prefixes_as_labels=False):
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
def join_results(results, prefixes=None):
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
    """Join multiple lists of results together

    The *results* argument either needs to be a list of result objects
    or an object with attribute *results* which is the list of result objects.
    This allows for results loaded from a file to be combined with a simple list.

    The function always returns just a simple list of result objects.
    """
    if not prefixes:
        prefixes = [None] * len(results)
    joined = []
    for result_list, prefix in zip(results, prefixes):
        if hasattr(result_list, "results"):
            # This is the actual list in the full results structure.
            result_list = result_list.results
        for result in result_list:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
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
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
            if select and not select(result):
                continue
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
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
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> d3014fcc0b (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 65fcf97c3a (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 0a00d6f9df (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 24f1b856fa (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> aae21b95f4 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c2d961e4a1 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> b74f907088 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 51791d82db (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 170fde8596 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 166e88ec39 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> c001cb7fb4 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 8219efca34 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> f6b704e2b3 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 4ff0c573d6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> eda3ed4fd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 962d13bfd3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> b4b5db6d74 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 5e89836168 (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> c1e96d556f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> a4c9b5af1d (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 12630fd17f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> d23d575d0e (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 3bcef5e53e (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 947f9098cd (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 010f50c2fc (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 4d38e4070b (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 21cac8ec4f (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 8c89098fcc (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ea1d751118 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fa5174ed4f (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 97b8f7a849 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> b8b0054745 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> ee77e9ab5c (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 267c735c0f (wxGUI: fix layout flag assert in wms dialog (#1764))
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
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 057765b894 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 19eb1e1772 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> fc6bee21bf (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
            if select and not select(result):
                continue
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
            result = copy.deepcopy(result)
            if prefix:
                if prefixes_as_labels:
                    result.label = prefix
                else:
                    result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
=======


def join_results_from_files(
    source_filenames, prefixes=None, select=None, prefixes_as_labels=False
):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
<<<<<<< HEAD
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 1691c94d89 (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> 949d58a435 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
=======
    return join_results(
        to_merge,
        prefixes=prefixes,
        select=select,
        prefixes_as_labels=prefixes_as_labels,
    )
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
>>>>>>> 1efa7f7b91 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 71106e29f6 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            result = copy.deepcopy(result)
            if prefix:
                result.label = f"{prefix}: {result.label}"
            joined.append(result)
    return joined
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
=======


def join_results_from_files(source_filenames, prefixes):
    """Join multiple files into one results object."""
    to_merge = []
    for result_file in source_filenames:
        to_merge.append(load_results_from_file(result_file))
    return join_results(to_merge, prefixes=prefixes)
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 94090db73c (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 81ee4cdfd6 (libpython: Support benchmarks of non-parallel runs better (#1733))
