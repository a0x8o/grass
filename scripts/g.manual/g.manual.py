#!/usr/bin/env python3

############################################################################
#
# MODULE:       g.manual
# AUTHOR(S):    Markus Neteler
#               Converted to Python by Glynn Clements
# PURPOSE:      Display the HTML/MAN pages
# COPYRIGHT:    (C) 2003-2015 by the GRASS Development Team
#
#               This program is free software under the GNU General Public
#               License (>=v2). Read the file COPYING that comes with GRASS
#               for details.
#
#############################################################################

# %module
# % description: Displays the manual pages of GRASS modules.
# % keyword: general
# % keyword: manual
# % keyword: help
# %end
# %flag
# % key: i
# % description: Display index
# % suppress_required: yes
# %end
# %flag
# % key: t
# % description: Display topics
# % suppress_required: yes
# %end
# %flag
# % key: m
# % description: Display as MAN text page instead of HTML page in browser
# %end
# %flag
# % key: o
# % label: Display online manuals instead of locally installed
# % description: Use online manuals available at https://grass.osgeo.org website. This flag has no effect when displaying MAN text pages.
# %end
# %option
# % key: entry
# % type: string
# % description: Manual entry to be displayed
# % required : yes
# %end

import sys
import os
from urllib.request import urlopen

import webbrowser

from grass.script.utils import basename
from grass.script import core as grass


def start_browser(entry):
    if (
        browser
        and browser not in {"xdg-open", "start"}
        and not grass.find_program(browser)
    ):
        grass.fatal(_("Browser '%s' not found") % browser)

    if flags["o"]:
        major, minor, patch = grass.version()["version"].split(".")
        url_path = "https://grass.osgeo.org/grass%s%s/manuals/%s.html" % (
            major,
            minor,
            entry,
        )
        if urlopen(url_path).getcode() != 200:
            url_path = "https://grass.osgeo.org/grass%s%s/manuals/addons/%s.html" % (
                major,
                minor,
                entry,
            )
    else:
        path = os.path.join(gisbase, "docs", "html", entry + ".html")
        if not os.path.exists(path) and os.getenv("GRASS_ADDON_BASE"):
            path = os.path.join(
                os.getenv("GRASS_ADDON_BASE"), "docs", "html", entry + ".html"
            )

        if not os.path.exists(path):
            grass.fatal(_("No HTML manual page entry for '%s'") % entry)

        url_path = "file://" + path

    if browser and browser not in {"xdg-open", "start"}:
        webbrowser.register(browser_name, None)

    grass.verbose(
<<<<<<< HEAD
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
        _("Starting browser '%(browser)s' for manual entry '%(entry)s'...")
=======
        _("Starting browser '%(browser)s' for manual" " entry '%(entry)s'...")
>>>>>>> 898113134f (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
=======
        _("Starting browser '%(browser)s' for manual entry '%(entry)s'...")
>>>>>>> fb2b1e4ce2 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
>>>>>>> 873c50e991 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
>>>>>>> c1f9bb45a5 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
        _("Starting browser '%(browser)s' for manual entry '%(entry)s'...")
=======
        _("Starting browser '%(browser)s' for manual" " entry '%(entry)s'...")
>>>>>>> 386d478441 (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
<<<<<<< HEAD
=======
        _("Starting browser '%(browser)s' for manual entry '%(entry)s'...")
>>>>>>> 28bbce8dd7 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
>>>>>>> c866535f04 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
>>>>>>> a0dfa20fef (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
=======
>>>>>>> e0ba42ca3d (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
>>>>>>> d10220bba4 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
>>>>>>> 6a40d37cf9 (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
        _("Starting browser '%(browser)s' for manual entry '%(entry)s'...")
=======
        _("Starting browser '%(browser)s' for manual" " entry '%(entry)s'...")
>>>>>>> 898113134f (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 26db9acf7d (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
=======
=======
        _("Starting browser '%(browser)s' for manual entry '%(entry)s'...")
>>>>>>> fb2b1e4ce2 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c866535f04 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
=======
>>>>>>> 873c50e991 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
>>>>>>> 6a40d37cf9 (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
        _("Starting browser '%(browser)s' for manual entry '%(entry)s'...")
=======
        _("Starting browser '%(browser)s' for manual" " entry '%(entry)s'...")
>>>>>>> 386d478441 (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 95fa5f2f6a (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
<<<<<<< HEAD
>>>>>>> a0dfa20fef (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
=======
=======
<<<<<<< HEAD
>>>>>>> 95fa5f2f6a (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
>>>>>>> c1f9bb45a5 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
        _("Starting browser '%(browser)s' for manual entry '%(entry)s'...")
>>>>>>> 28bbce8dd7 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
>>>>>>> 873c50e991 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
<<<<<<< HEAD
>>>>>>> e0ba42ca3d (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
        _("Starting browser '%(browser)s' for manual entry '%(entry)s'...")
=======
        _("Starting browser '%(browser)s' for manual" " entry '%(entry)s'...")
>>>>>>> 898113134f (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
>>>>>>> d449c4afcc (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
=======
=======
        _("Starting browser '%(browser)s' for manual entry '%(entry)s'...")
>>>>>>> fb2b1e4ce2 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
>>>>>>> d10220bba4 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
>>>>>>> 95fa5f2f6a (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
>>>>>>> 6a40d37cf9 (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
=======
>>>>>>> c1f9bb45a5 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
        % {"browser": browser_name, "entry": entry}
    )

    try:
        webbrowser.open(url_path)
    except Exception:
        grass.fatal(
<<<<<<< HEAD
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
            _("Error starting browser '%(browser)s' for HTML file '%(path)s'")
=======
            _("Error starting browser '%(browser)s' for HTML file" " '%(path)s'")
>>>>>>> 898113134f (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
=======
            _("Error starting browser '%(browser)s' for HTML file '%(path)s'")
>>>>>>> fb2b1e4ce2 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
>>>>>>> 873c50e991 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
>>>>>>> c1f9bb45a5 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
            _("Error starting browser '%(browser)s' for HTML file '%(path)s'")
=======
            _("Error starting browser '%(browser)s' for HTML file" " '%(path)s'")
>>>>>>> 386d478441 (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
<<<<<<< HEAD
=======
            _("Error starting browser '%(browser)s' for HTML file '%(path)s'")
>>>>>>> 28bbce8dd7 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
>>>>>>> c866535f04 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
>>>>>>> a0dfa20fef (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
=======
>>>>>>> e0ba42ca3d (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
>>>>>>> d10220bba4 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
>>>>>>> 6a40d37cf9 (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
            _("Error starting browser '%(browser)s' for HTML file '%(path)s'")
=======
            _("Error starting browser '%(browser)s' for HTML file" " '%(path)s'")
>>>>>>> 898113134f (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 26db9acf7d (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
=======
=======
            _("Error starting browser '%(browser)s' for HTML file '%(path)s'")
>>>>>>> fb2b1e4ce2 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c866535f04 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
=======
>>>>>>> 873c50e991 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
>>>>>>> 6a40d37cf9 (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
            _("Error starting browser '%(browser)s' for HTML file '%(path)s'")
=======
            _("Error starting browser '%(browser)s' for HTML file" " '%(path)s'")
>>>>>>> 386d478441 (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 95fa5f2f6a (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
<<<<<<< HEAD
>>>>>>> a0dfa20fef (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
=======
=======
<<<<<<< HEAD
>>>>>>> 95fa5f2f6a (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
>>>>>>> c1f9bb45a5 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
            _("Error starting browser '%(browser)s' for HTML file '%(path)s'")
>>>>>>> 28bbce8dd7 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
>>>>>>> 873c50e991 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
<<<<<<< HEAD
>>>>>>> e0ba42ca3d (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
            _("Error starting browser '%(browser)s' for HTML file '%(path)s'")
=======
            _("Error starting browser '%(browser)s' for HTML file" " '%(path)s'")
>>>>>>> 898113134f (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
>>>>>>> d449c4afcc (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
=======
=======
            _("Error starting browser '%(browser)s' for HTML file '%(path)s'")
>>>>>>> fb2b1e4ce2 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
>>>>>>> d10220bba4 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
>>>>>>> 95fa5f2f6a (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
>>>>>>> 6a40d37cf9 (style: Fixes unnecessary-collection-call (C408) for remaining code (#3948))
=======
>>>>>>> c1f9bb45a5 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
            % {"browser": browser, "path": path}
        )


def start_man(entry):
    path = os.path.join(gisbase, "docs", "man", "man1", entry + ".1")
    if not os.path.exists(path) and os.getenv("GRASS_ADDON_BASE"):
        path = os.path.join(
            os.getenv("GRASS_ADDON_BASE"), "docs", "man", "man1", entry + ".1"
        )

    for ext in ["", ".gz", ".bz2"]:
        if os.path.exists(path + ext):
            os.execlp("man", "man", path + ext)
            grass.fatal(_("Error starting 'man' for '%s'") % path)
    grass.fatal(_("No manual page entry for '%s'") % entry)


def main():
    global gisbase, browser, browser_name

    if flags["i"] and flags["t"]:
        grass.fatal(_("Flags -%c and -%c are mutually exclusive") % ("i", "t"))

    special = None
    if flags["i"]:
        special = "index"
    elif flags["t"]:
        special = "topics"

    start = start_man if flags["m"] else start_browser

    entry = options["entry"]
    gisbase = os.environ["GISBASE"]
    browser = os.getenv("GRASS_HTML_BROWSER", "")

    if sys.platform == "darwin":
        # hack for MacOSX
        browser_name = os.getenv("GRASS_HTML_BROWSER_MACOSX", "..").split(".")[2]
    elif sys.platform == "cygwin":
        # hack for Cygwin
        browser_name = basename(browser, "exe")
    else:
        browser_name = basename(browser)

    # keep order!
    # first test for index...
    if special:
        start(special)
    else:
        start(entry)

    return 0


if __name__ == "__main__":
    options, flags = grass.parser()
    sys.exit(main())
