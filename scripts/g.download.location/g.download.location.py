#!/usr/bin/env python3
############################################################################
#
# MODULE:    g.download.location
# AUTHOR(S): Vaclav Petras <wenzeslaus gmail com>
# PURPOSE:   Download and extract project (location) from web
# COPYRIGHT: (C) 2017-2024 by the GRASS Development Team
#
#    This program is free software under the GNU General
#    Public License (>=v2). Read the file COPYING that
#    comes with GRASS for details.
#
#############################################################################

"""Download GRASS projects"""

# %module
# % label: Download GRASS project (location) from the web
# % description: Get GRASS project from an URL or file path
# % keyword: general
# % keyword: data
# % keyword: download
# % keyword: import
# %end
# %option
# % key: url
# % multiple: no
# % type: string
# % label: URL of the archive with a project to be downloaded
# % description: URL of ZIP, TAR.GZ, or other similar archive
# % required: yes
# %end
# %option G_OPT_M_LOCATION
# % key: name
# % required: no
# % multiple: no
# % key_desc: name
# %end
# %option G_OPT_M_DBASE
# % key: path
# % required: no
# % multiple: no
# %end

import grass.script as gs


def main(options, unused_flags):
<<<<<<< HEAD
    """Download and copy project to destination"""
    gs.run_command("g.download.project", **options)
=======
    """Download and copy location to destination"""
    url = options["url"]
    name = options["name"]
    database = options["path"]

    if not database:
        # Use the current database path.
        database = gs.gisenv()["GISDBASE"]
    if not name:
        name = location_name_from_url(url)
    destination = Path(database) / name

    if destination.exists():
        gs.fatal(
            _("Location named <{}> already exists, download canceled").format(name)
        )

    gs.message(_("Downloading and extracting..."))
    try:
        directory = download_and_extract(url)
        if not directory.is_dir():
            gs.fatal(_("Archive contains only one file and no mapset directories"))
        atexit.register(lambda: try_rmdir(directory))
    except DownloadError as error:
        gs.fatal(_("Unable to get the location: {error}").format(error=error))
    if not is_location_valid(directory):
        gs.verbose(_("Searching for valid location..."))
        # This in fact deal with location being on the third level of directories
        # thanks to how the extraction functions work (leaving out one level).
        result = find_location_in_directory(directory, recurse=1)
        if result:
            # We just want to show relative path in the message.
            # The relative path misses the root directory (name), because we
            # loose it on the way. (We should use parent directory to get the
<<<<<<< HEAD
            # full relative path, but the directory name is different now.
=======
            # full relative path, but the directory name is diffrent now.
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
            # This is the consequence of how the extract functions work.)
            relative = os.path.relpath(result, start=directory)
            gs.verbose(
                _("Location found in a nested directory '{directory}'").format(
                    directory=relative
                )
            )
            directory = result
        else:
            # The list is similarly misleading as the relative path above
            # as it misses the root directory, but it still should be useful.
            files_and_dirs = os.listdir(directory)
            gs.fatal(
                _(
<<<<<<< HEAD
                    "The downloaded file is not a valid GRASS Location."
=======
                    "The dowloaded file is not a valid GRASS Location."
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
                    " The extracted file contains these files and directories:"
                    "\n{files_and_dirs}"
                ).format(files_and_dirs=" ".join(files_and_dirs))
            )
    gs.verbose(_("Copying to final destination..."))
    shutil.copytree(src=directory, dst=destination)
    gs.message(_("Path to the location now <{path}>").format(path=destination))
>>>>>>> 3e9fe02ef5 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))


if __name__ == "__main__":
    main(*gs.parser())
