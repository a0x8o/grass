#!/usr/bin/env python3
#
############################################################################
#
# MODULE:       v.db.addcolumnumn
# AUTHOR(S):    Moritz Lennert
#               Converted to Python by Glynn Clements
# PURPOSE:      interface to db.execute to add a column to the attribute table
#               connected to a given vector map
# COPYRIGHT:    (C) 2005 by the GRASS Development Team
#
#               This program is free software under the GNU General Public
#               License (>=v2). Read the file COPYING that comes with GRASS
#               for details.
#
#############################################################################


# %module
# % description: Adds one or more columns to the attribute table connected to a given vector map.
# % keyword: vector
# % keyword: attribute table
# % keyword: database
# %end

# %option G_OPT_V_MAP
# %end

# %option G_OPT_V_FIELD
# % label: Layer number where to add column(s)
# %end

# %option
# % key: columns
# % type: string
# % label: Name and type of the new column(s) ('name type [,name type, ...]')
# % description: Types depend on database backend, but all support VARCHAR(), INT, DOUBLE PRECISION and DATE. Example: 'label varchar(250), value integer'
# % required: yes
# % multiple: yes
# % key_desc: name type
# %end

import atexit
import os
from pathlib import Path
import re

from grass.exceptions import CalledModuleError
import grass.script as gs

rm_files = []


def cleanup():
    for file in rm_files:
        if os.path.isfile(file):
            try:
                os.remove(file)
            except Exception as e:
                gs.warning(
                    _("Unable to remove file {file}: {message}").format(
                        file=file, message=e
                    )
                )


def main():
    global rm_files
    map = options["map"]
    layer = options["layer"]
    columns = options["columns"]
    columns = [col.strip() for col in columns.split(",")]

    # does map exist in CURRENT mapset?
    mapset = gs.gisenv()["MAPSET"]
    exists = bool(gs.find_file(map, element="vector", mapset=mapset)["file"])

    if not exists:
        gs.fatal(_("Vector map <{}> not found in current mapset").format(map))

    try:
        f = gs.vector_db(map)[int(layer)]
    except KeyError:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
        if gs.vector_db(map):
            gs.fatal(
=======
        if grass.vector_db(map):
            grass.fatal(
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
        if grass.vector_db(map):
            grass.fatal(
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
=======
        if gs.vector_db(map):
            gs.fatal(
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
                _(
                    "There is no table connected to layer <{layer}> of <{name}>. "
                    "Run v.db.connect or v.db.addtable first."
                ).format(name=map, layer=layer)
            )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
        gs.fatal(
=======
        grass.fatal(
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
        grass.fatal(
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        gs.fatal(
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
        grass.fatal(
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
            _(
                "There is no table connected to <{name}>. "
                "Run v.db.connect or v.db.addtable first."
            ).format(name=map)
        )

    table = f["table"]
    database = f["database"]
    driver = f["driver"]
    column_existing = gs.vector_columns(map, int(layer)).keys()

    add_str = "BEGIN TRANSACTION\n"
    pattern = re.compile(r"\s+")
    for col in columns:
        if not col:
            gs.fatal(_("There is an empty column. Did you leave a trailing comma?"))
        whitespace = re.search(pattern, col)
        if not whitespace:
            gs.fatal(
                _(
                    "Incorrect new column(s) format, use"
                    " <'name type [,name type, ...]'> format, please."
                )
            )
        col_name, col_type = col.split(whitespace.group(0), 1)
        if col_name in column_existing:
            gs.error(
                _("Column <{}> is already in the table. Skipping.").format(col_name)
            )
            continue
        gs.verbose(_("Adding column <{}> to the table").format(col_name))
        add_str += f'ALTER TABLE {table} ADD COLUMN "{col_name}" {col_type};\n'
    add_str += "END TRANSACTION"
    sql_file = gs.tempfile()
    rm_files.append(sql_file)
    cols_add_str = ",".join([col[0] for col in columns])
    Path(sql_file).write_text(add_str)
    try:
        gs.run_command(
            "db.execute",
            input=sql_file,
            database=database,
            driver=driver,
        )
    except CalledModuleError:
        gs.fatal(_("Error adding columns {}").format(cols_add_str))
    # write cmd history:
    gs.vector_history(map)


if __name__ == "__main__":
    options, flags = gs.parser()
    atexit.register(cleanup)
    main()
