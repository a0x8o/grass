#!/usr/bin/env python3

############################################################################
#
# MODULE:   t.remove
# AUTHOR(S):    Soeren Gebbert
#
# PURPOSE:  Remove space time datasets from the temporal database
# COPYRIGHT:    (C) 2011-2017 by the GRASS Development Team
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#############################################################################

# %module
# % description: Removes space time datasets from temporal database.
# % keyword: temporal
# % keyword: map management
# % keyword: remove
# % keyword: time
# %end

# %option G_OPT_STDS_INPUTS
# % guisection: Input
# % required: no
# %end

# %option
# % key: type
# % type: string
# % description: Type of the space time dataset, default is strds
# % guidependency: inputs
# % guisection: Input
# % required: no
# % options: strds, str3ds, stvds
# % answer: strds
# %end

# %option G_OPT_F_INPUT
# % key: file
# % description: Input file with dataset names, one per line
# % guisection: Input
# % required: no
# %end

# %flag
# % key: r
# % description: Remove stds and unregister maps from temporal database
# %end

# %flag
# % key: f
# % description: Force removal (required for actual deletion of files)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
# %end

# %flag
# % key: d
# % description: Remove stds, unregister maps from temporal database and delete them from mapset
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
# %end

# %flag
# % key: d
# % description: Remove stds, unregister maps from temporal database and delete them from mapset
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
# %end

# %flag
# % key: d
# % description: Remove stds, unregister maps from temporal database and delete them from mapset
# %end

<<<<<<< HEAD
<<<<<<< HEAD
import grass.script as gs
=======
<<<<<<< HEAD
<<<<<<< HEAD
import grass.script as grass
=======
import grass.script as gs
>>>>>>> osgeo-main
>>>>>>> main
=======
import grass.script as grass
>>>>>>> 0c13ccda1f (style(temporal): Sort and group imports (#3959))
<<<<<<< HEAD
>>>>>>> c8cd2d055b (style(temporal): Sort and group imports (#3959))
=======
=======
import grass.script as gs
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
>>>>>>> cc1bb01ea7 (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))

# lazy imports at the end of the file

############################################################################


def main():
    # Get the options
    datasets = options["inputs"]
    file = options["file"]
    type = options["type"]
    recursive = flags["r"]
    force = flags["f"]
    clean = flags["d"]

    if datasets and file:
        gs.fatal(_("%s= and %s= are mutually exclusive") % ("input", "file"))

    # Make sure the temporal database exists
    tgis.init()

    dbif = tgis.SQLDatabaseInterfaceConnection()
    dbif.connect()

    dataset_list = []

    # Dataset names as comma separated string
    if datasets:
        if datasets.find(",") == -1:
            dataset_list = (datasets,)
        else:
            dataset_list = tuple(datasets.split(","))

    # Read the dataset list from file
    if file:
        fd = open(file)

        line = True
        while True:
            line = fd.readline()
            if not line:
                break

            line_list = line.split("\n")
            dataset_name = line_list[0]
            dataset_list.append(dataset_name)

    statement = ""

    # Create the pygrass Module object for g.remove
    remove = pyg.Module("g.remove", quiet=True, flags="f", run_=False)

    if not force:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        gs.message(_("The following data base element files will be deleted:"))
=======
        grass.message(_("The following data base element files will be deleted:"))
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
        grass.message(_("The following data base element files will be deleted:"))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        gs.message(_("The following data base element files will be deleted:"))
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))

    for name in dataset_list:
        name = name.strip()
        sp = tgis.open_old_stds(name, type, dbif)
        if not force:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            gs.message(
                _("{stds}: {gid}").format(stds=sp.get_type().upper(), gid=sp.get_id())
=======
            grass.message(
=======
            gs.message(
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
                _("{stds}: {gid}".format(stds=sp.get_type().upper(), gid=sp.get_id()))
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
            grass.message(
                _("{stds}: {gid}".format(stds=sp.get_type().upper(), gid=sp.get_id()))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            )
        if recursive or clean:
            if not force:
                if recursive:
<<<<<<< HEAD
<<<<<<< HEAD
                    msg = _(
=======
                    msg = (
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
                    msg = (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                        "The following maps of {stds} {gid} will be "
                        "unregistered from temporal database:"
                    )
                elif clean:
<<<<<<< HEAD
<<<<<<< HEAD
                    msg = _(
=======
                    msg = (
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
                    msg = (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                        "The following maps of {stds} {gid} will be "
                        "unregistered from temporal database and removed "
                        "from spatial database:"
                    )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

                if recursive or clean:
                    gs.message(msg.format(stds=sp.get_type(), gid=sp.get_id()))

=======
                grass.message(_(msg.format(stds=sp.get_type(), gid=sp.get_id())))
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
                grass.message(_(msg.format(stds=sp.get_type(), gid=sp.get_id())))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                gs.message(_(msg.format(stds=sp.get_type(), gid=sp.get_id())))
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
            maps = sp.get_registered_maps_as_objects(dbif=dbif)
            map_statement = ""
            count = 1
            name_list = []
            for map in maps:
                map.select(dbif)
                # We may have multiple layer for a single map, hence we need
                # to avoid multiple deletions of the same map,
                # but the database entries are still present and must be removed
                if not force:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    gs.message(_("- %s") % map.get_name())
=======
                    grass.message(_("- %s" % map.get_name()))
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
                    grass.message(_("- %s" % map.get_name()))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                    gs.message(_("- %s" % map.get_name()))
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
                    continue
                if clean and force:
                    if map.get_name() not in name_list:
                        name_list.append(str(map.get_name()))
                map_statement += map.delete(dbif=dbif, execute=False)

                count += 1
                # Delete every 100 maps
                if count % 100 == 0:
                    dbif.execute_transaction(map_statement)
                    if clean:
                        if type == "strds":
                            remove(type="raster", name=name_list, run_=True)
                        if type == "stvds":
                            remove(type="vector", name=name_list, run_=True)
                        if type == "str3ds":
                            remove(type="raster_3d", name=name_list, run_=True)
                    map_statement = ""
                    name_list = []

            if map_statement:
                dbif.execute_transaction(map_statement)
            if clean and name_list:
                if type == "strds":
                    remove(type="raster", name=name_list, run_=True)
                if type == "stvds":
                    remove(type="vector", name=name_list, run_=True)
                if type == "str3ds":
                    remove(type="raster_3d", name=name_list, run_=True)
        if force:
            statement += sp.delete(dbif=dbif, execute=False)

    if not force:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        gs.message(
            _(
                "Nothing removed. You must use the force flag (-{flag}) to actually "
                "remove them."
            ).format(flag="f")
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        grass.message(
=======
        gs.message(
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
            _(
                "Nothing removed. You must use the force flag (-{flag}) to actually "
                "remove them.".format(flag="f")
            )
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        )
    else:
        # Execute the collected SQL statenents
        dbif.execute_transaction(statement)
        dbif.close()


if __name__ == "__main__":
    options, flags = gs.parser()

    # lazy imports
    import grass.pygrass.modules as pyg
    import grass.temporal as tgis

    tgis.profile_function(main)
