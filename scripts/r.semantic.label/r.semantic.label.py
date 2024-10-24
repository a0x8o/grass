#!/usr/bin/env python3

############################################################################
#
# MODULE:       r.semantic.label
# AUTHOR(S):    Martin Landa <landa.martin gmail com>
#
# PURPOSE:      Manages semantic label information assigned to a single
#               raster map or to a list of raster maps.
#
# COPYRIGHT:    (C) 2019 by mundialis GmbH & Co.KG, and the GRASS Development Team
#
#               This program is free software under the GNU General
#               Public License (>=v2). Read the file COPYING that
#               comes with GRASS for details.
#
#############################################################################

# %module
# % description: Manages semantic label information assigned to a single raster map or to a list of raster maps.
# % keyword: general
# % keyword: imagery
# % keyword: semantic label
# % keyword: image collections
# %end
# %option G_OPT_R_MAPS
# %end
# %option
# % key: semantic_label
# % type: string
# % key_desc: name
# % description: Name of semantic label identifier (example: S2_1)
# % required: no
# % multiple: yes
# %end
# %option
# % key: operation
# % type: string
# % required: yes
# % multiple: no
# % options: add,remove,print
# % description: Operation to be performed
# % answer: add

import sys

import grass.script as gs
from grass.exceptions import GrassError, OpenError


def print_map_semantic_label(name, label_reader):
    """Print semantic label information assigned to a single raster map

    :param str name: raster map name
    """
    from grass.pygrass.raster import RasterRow

    try:
        with RasterRow(name) as rast:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
            semantic_label = rast.info.semantic_label
            if semantic_label:
                label_reader.print_info(semantic_label)
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
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
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
            semantic_label = rast.info.semantic_label
            if semantic_label:
                label_reader.print_info(semantic_label=semantic_label)
=======
            band_ref = rast.info.bandref
            if band_ref:
                shortcut, band = band_ref.split("_")
                band_reader.print_info(shortcut, band)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711)):scripts/i.band/i.band.py
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
            semantic_label = rast.info.semantic_label
            if semantic_label:
                label_reader.print_info(semantic_label)
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
            semantic_label = rast.info.semantic_label
            if semantic_label:
                label_reader.print_info(semantic_label)
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
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
            else:
                gs.info(_("No semantic label assigned to <{}>").format(name))
    except OpenError:
        gs.error(_("Map <{}> not found").format(name))


def manage_map_semantic_label(name, semantic_label):
    """Manage semantic label assigned to a single raster map

    :param str name: raster map name
    :param str semantic_label: semantic label (None for dissociating semantic label)

    :return int: return code
    """
    from grass.pygrass.raster import RasterRow

    try:
        with RasterRow(name) as rast:
            if semantic_label:
                gs.debug(
                    _("Semantic label <{}> assigned to raster map <{}>").format(
                        semantic_label, name
                    ),
                    1,
                )
            else:
                gs.debug(
                    _("Semantic label dissociated from raster map <{}>").format(name), 1
                )
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
=======
>>>>>>> main
                rast.info.semantic_label = semantic_label
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
>>>>>>> osgeo-main
                rast.info.bandref = band_ref
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711)):scripts/i.band/i.band.py
=======
                rast.info.semantic_label = semantic_label
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                rast.info.semantic_label = semantic_label
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
                rast.info.bandref = band_ref
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711)):scripts/i.band/i.band.py
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
                rast.info.semantic_label = semantic_label
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
                rast.info.bandref = band_ref
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711)):scripts/i.band/i.band.py
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
                rast.info.semantic_label = semantic_label
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD:scripts/r.semantic.label/r.semantic.label.py
                rast.info.semantic_label = semantic_label
=======
                rast.info.bandref = band_ref
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711)):scripts/i.band/i.band.py
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
                rast.info.semantic_label = semantic_label
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
            except GrassError as e:
                gs.error(_("Unable to assign/dissociate semantic label. {}").format(e))
                return 1
    except OpenError:
        gs.error(_("Map <{}> not found in current mapset").format(name))
        return 1

    return 0


def main():
    maps = options["map"].split(",")
    if options["operation"] == "add":
        if not options["semantic_label"]:
            gs.fatal(
                _("Operation {}: required parameter <{}> not set").format(
                    options["operation"], "semantic_label"
                )
            )
        semantic_labels = options["semantic_label"].split(",")
        if len(semantic_labels) > 1 and len(semantic_labels) != len(maps):
            gs.fatal(_("Number of maps differs from number of semantic labels"))
    else:
        semantic_labels = [None]

    if options["operation"] == "print":
        from grass.semantic_label import SemanticLabelReader

        label_reader = SemanticLabelReader()
    else:
        label_reader = None
    multi_labels = len(semantic_labels) > 1
    ret = 0
    for i in range(len(maps)):
        semantic_label = semantic_labels[i] if multi_labels else semantic_labels[0]
        if options["operation"] == "print":
            print_map_semantic_label(maps[i], label_reader)
        elif manage_map_semantic_label(maps[i], semantic_label) != 0:
            ret = 1

    return ret


if __name__ == "__main__":
    options, flags = gs.parser()

    sys.exit(main())
