#!/usr/bin/env python3

############################################################################
#
# MODULE:       r.reclass.area
# AUTHOR(S):    NRCS
#               Converted to Python by Glynn Clements
#               Added rmarea method by Luca Delucchi
# PURPOSE:      Reclasses a raster map greater or less than user specified area size (in hectares)
# COPYRIGHT:    (C) 1999,2008,2014 by the GRASS Development Team
#
#               This program is free software under the GNU General Public
#               License (>=v2). Read the file COPYING that comes with GRASS
#               for details.
#
#############################################################################
# 10/2013: added option to use a pre-clumped input map (Eric Goddard)
# 8/2012: added fp maps support, cleanup, removed tabs AK
# 3/2007: added label support MN
# 3/2004: added parser support MN
# 11/2001 added mapset support markus
# 2/2001 fixes markus
# 2000: updated to GRASS 5
# 1998 from NRCS, slightly modified for GRASS 4.2.1

# %module
# % description: Reclasses a raster map greater or less than user specified area size (in hectares).
# % keyword: raster
# % keyword: statistics
# % keyword: aggregation
# %end

# %option G_OPT_R_INPUT
# %end

# %option G_OPT_R_OUTPUT
# %end

# %option
# % key: value
# % type: double
# % description: Value option that sets the area size limit (in hectares)
# % required: yes
# % guisection: Area
# %end

# %option
# % key: mode
# % type: string
# % description: Lesser or greater than specified value
# % options: lesser,greater
# % required: yes
# % guisection: Area
# %end

# %option
# % key: method
# % type: string
# % description: Method used for reclassification
# % options: reclass,rmarea
# % answer: reclass
# % guisection: Area
# %end

# %flag
# % key: c
# % description: Input map is clumped
# %end

# %flag
# % key: d
# % description: Clumps including diagonal neighbors
# %end

import sys
import os
import atexit
import grass.script as gs
from grass.script.utils import decode, encode

TMPRAST = []


def reclass(inf, outf, lim, clump, diag, les):
    infile = inf
    outfile = outf
    lesser = les
    limit = lim
    clumped = clump
    diagonal = diag

    s = gs.read_command("g.region", flags="p")
    s = decode(s)
    kv = gs.parse_key_val(s, sep=":")
    s = kv["projection"].strip().split()
    if s == "0":
        gs.fatal(_("xy-locations are not supported"))
        gs.fatal(_("Need projected data with grids in meters"))

    if not gs.find_file(infile)["name"]:
        gs.fatal(_("Raster map <%s> not found") % infile)

    if clumped and diagonal:
        gs.fatal(_("flags c and d are mutually exclusive"))

    if clumped:
        clumpfile = infile
    else:
        clumpfile = "%s.clump.%s" % (infile.split("@")[0], outfile)
        TMPRAST.append(clumpfile)

        if not gs.overwrite():
            if gs.find_file(clumpfile)["name"]:
                gs.fatal(_("Temporary raster map <%s> exists") % clumpfile)
        if diagonal:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            gs.message(
=======
<<<<<<< HEAD
<<<<<<< HEAD
            grass.message(
=======
            gs.message(
>>>>>>> osgeo-main
>>>>>>> main
=======
            grass.message(
>>>>>>> fb2b1e4ce2 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
<<<<<<< HEAD
>>>>>>> c866535f04 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
            gs.message(
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
>>>>>>> cc1bb01ea7 (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
=======
=======
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
            gs.message(
=======
            grass.message(
>>>>>>> fb2b1e4ce2 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
<<<<<<< HEAD
>>>>>>> d10220bba4 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
            gs.message(
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
                _("Generating a clumped raster file including diagonal neighbors...")
            )
            gs.run_command("r.clump", flags="d", input=infile, output=clumpfile)
        else:
            gs.message(_("Generating a clumped raster file ..."))
            gs.run_command("r.clump", input=infile, output=clumpfile)

    if lesser:
        gs.message(
            _(
                "Generating a reclass map with area size less than "
                "or equal to %f hectares..."
            )
            % limit
        )
    else:
        gs.message(
            _(
                "Generating a reclass map with area size greater "
                "than or equal to %f hectares..."
            )
            % limit
        )

    recfile = outfile + ".recl"
    TMPRAST.append(recfile)

    sflags = "aln"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if gs.raster_info(infile)["datatype"] in {"FCELL", "DCELL"}:
=======
<<<<<<< HEAD
<<<<<<< HEAD
    if grass.raster_info(infile)["datatype"] in {"FCELL", "DCELL"}:
=======
    if gs.raster_info(infile)["datatype"] in {"FCELL", "DCELL"}:
>>>>>>> osgeo-main
>>>>>>> main
=======
    if grass.raster_info(infile)["datatype"] in {"FCELL", "DCELL"}:
>>>>>>> 75456afff2 (style: Fixes literal-membership (PLR6201) for other code (#3954))
<<<<<<< HEAD
>>>>>>> d2a8cd08c4 (style: Fixes literal-membership (PLR6201) for other code (#3954))
=======
=======
    if gs.raster_info(infile)["datatype"] in {"FCELL", "DCELL"}:
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
>>>>>>> cc1bb01ea7 (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
=======
=======
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
    if gs.raster_info(infile)["datatype"] in {"FCELL", "DCELL"}:
=======
    if grass.raster_info(infile)["datatype"] in {"FCELL", "DCELL"}:
>>>>>>> 75456afff2 (style: Fixes literal-membership (PLR6201) for other code (#3954))
<<<<<<< HEAD
>>>>>>> 001cfcbd00 (style: Fixes literal-membership (PLR6201) for other code (#3954))
=======
=======
    if gs.raster_info(infile)["datatype"] in {"FCELL", "DCELL"}:
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
        sflags += "i"
    p1 = gs.pipe_command("r.stats", flags=sflags, input=(clumpfile, infile), sep=";")
    p2 = gs.feed_command("r.reclass", input=clumpfile, output=recfile, rules="-")
    rules = ""
    for line in p1.stdout:
        f = decode(line).rstrip(os.linesep).split(";")
        if len(f) < 5:
            continue
        hectares = float(f[4]) * 0.0001
        test = hectares <= limit if lesser else hectares >= limit
        if test:
            rules += "%s = %s %s\n" % (f[0], f[2], f[3])
    if rules:
        p2.stdin.write(encode(rules))
    p1.wait()
    p2.stdin.close()
    p2.wait()
    if p2.returncode != 0:
        if lesser:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d10220bba4 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
            gs.fatal(
                _("No areas of size less than or equal to %f hectares found.") % limit
            )
        else:
            gs.fatal(
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c866535f04 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
>>>>>>> d10220bba4 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
            grass.fatal(
                _("No areas of size less than or equal to %f hectares found.") % limit
            )
        else:
            grass.fatal(
<<<<<<< HEAD
<<<<<<< HEAD
=======
            gs.fatal(
                _("No areas of size less than or equal to %f hectares found.") % limit
            )
        else:
            gs.fatal(
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> fb2b1e4ce2 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c866535f04 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
=======
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
=======
            gs.fatal(
                _("No areas of size less than or equal to %f hectares found.") % limit
            )
        else:
            gs.fatal(
>>>>>>> e089dc6c2c (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
<<<<<<< HEAD
>>>>>>> cc1bb01ea7 (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
=======
>>>>>>> fb2b1e4ce2 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
>>>>>>> d10220bba4 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
=======
>>>>>>> a08f2382ac (style: Fix unconventional-import-alias (ICN001) (consolidate `import grass.script as gs`) (#3981))
                _("No areas of size greater than or equal to %f hectares found.")
                % limit
            )
    gs.mapcalc("$outfile = $recfile", outfile=outfile, recfile=recfile)


def rmarea(infile, outfile, thresh, coef):
    # transform user input from hectares to map units (kept this for future)
    # thresh = thresh * 10000.0 / (float(coef)**2)
    # grass.debug("Threshold: %d, coeff linear: %s, coef squared: %d" %
    # (thresh, coef, (float(coef)**2)), 0)

    # transform user input from hectares to meters because currently v.clean
    # rmarea accept only meters as threshold
    thresh *= 10000.0
    vectfile = "%s_vect_%s" % (infile.split("@")[0], outfile)
    TMPRAST.append(vectfile)
    gs.run_command("r.to.vect", input=infile, output=vectfile, type="area")
    cleanfile = "%s_clean_%s" % (infile.split("@")[0], outfile)
    TMPRAST.append(cleanfile)
    gs.run_command(
        "v.clean", input=vectfile, output=cleanfile, tool="rmarea", threshold=thresh
    )

    gs.run_command(
        "v.to.rast", input=cleanfile, output=outfile, use="attr", attrcolumn="value"
    )


def main():
    infile = options["input"]
    value = options["value"]
    mode = options["mode"]
    outfile = options["output"]
    global method
    method = options["method"]
    clumped = flags["c"]
    diagonal = flags["d"]

    # check for unsupported locations
    in_proj = gs.parse_command("g.proj", flags="g")
    if in_proj["unit"].lower() == "degree":
        gs.fatal(_("Latitude-longitude locations are not supported"))
    if in_proj["name"].lower() == "xy_location_unprojected":
        gs.fatal(_("xy-locations are not supported"))

    # check lesser and greater parameters
    limit = float(value)
    if mode == "greater" and method == "rmarea":
        gs.fatal(_("You have to specify mode='lesser' with method='rmarea'"))

    if not gs.find_file(infile)["name"]:
        gs.fatal(_("Raster map <%s> not found") % infile)

    if method == "reclass":
        reclass(infile, outfile, limit, clumped, diagonal, mode == "lesser")
    elif method == "rmarea":
        rmarea(infile, outfile, limit, in_proj["meters"])

    gs.message(_("Generating output raster map <%s>...") % outfile)


def cleanup():
    """!Delete temporary maps"""
    TMPRAST.reverse()  # reclassed map first
    for mapp in TMPRAST:
        if method == "rmarea":
            gs.run_command("g.remove", flags="f", type="vector", name=mapp, quiet=True)
        else:
            gs.run_command("g.remove", flags="f", type="raster", name=mapp, quiet=True)


if __name__ == "__main__":
    options, flags = gs.parser()
    atexit.register(cleanup)
    sys.exit(main())
