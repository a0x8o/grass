/*!
   \file lib/vector/Vlib/write.c

   \brief Vector library - write vector features

   Higher level functions for reading/writing/manipulating vectors.

   Supported operations:
   - Write a new feature
   - Rewrite existing feature
   - Delete existing feature
   - Restore deleted feature

   (C) 2001-2010, 2012-2013 by the GRASS Development Team

   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.

   \author Radim Blazek
   \author Updated by Martin Landa <landa.martin gmail.com> (restore lines, OGR
   & PostGIS support)
 */

#include <inttypes.h>
#include <sys/types.h>
#include <grass/glocale.h>
#include <grass/vector.h>

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
static off_t write_dummy(struct Map_info *Map, int type,
                         const struct line_pnts *points,
                         const struct line_cats *cats)
{
    G_warning("Vect_write_line() %s", _("for this format/level not supported"));
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
static off_t write_dummy(struct Map_info *Map UNUSED, int type UNUSED,
                         const struct line_pnts *points UNUSED,
                         const struct line_cats *cats UNUSED)
=======
static off_t write_dummy(struct Map_info *Map, int type,
                         const struct line_pnts *points,
                         const struct line_cats *cats)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
{
    G_warning("Vect_write_line() %s", _("for this format/level not supported"));
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
static off_t write_dummy(struct Map_info *Map, int type,
                         const struct line_pnts *points,
                         const struct line_cats *cats)
{
    G_warning("Vect_write_line() %s", _("for this format/level not supported"));
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    return -1;
}

static off_t rewrite_dummy(struct Map_info *Map, off_t line, int type,
                           const struct line_pnts *points,
                           const struct line_cats *cats)
{
    G_warning("Vect_rewrite_line() %s",
              _("for this format/level not supported"));
    return -1;
}

static int delete_dummy(struct Map_info *Map, off_t line)
{
    G_warning("Vect_delete_line() %s",
              _("for this format/level not supported"));
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    return -1;
}

static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    return -1;
}

<<<<<<< HEAD
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
static off_t write_dummy(struct Map_info *Map, int type,
                         const struct line_pnts *points,
                         const struct line_cats *cats)
{
    G_warning("Vect_write_line() %s", _("for this format/level not supported"));
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    return -1;
}

static off_t rewrite_dummy(struct Map_info *Map, off_t line, int type,
                           const struct line_pnts *points,
                           const struct line_cats *cats)
{
    G_warning("Vect_rewrite_line() %s",
              _("for this format/level not supported"));
    return -1;
}

static int delete_dummy(struct Map_info *Map, off_t line)
{
    G_warning("Vect_delete_line() %s",
              _("for this format/level not supported"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    return -1;
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
static off_t write_dummy(struct Map_info *Map, int type,
                         const struct line_pnts *points,
                         const struct line_cats *cats)
{
    G_warning("Vect_write_line() %s", _("for this format/level not supported"));
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    return -1;
}

static off_t rewrite_dummy(struct Map_info *Map, off_t line, int type,
                           const struct line_pnts *points,
                           const struct line_cats *cats)
{
    G_warning("Vect_rewrite_line() %s",
              _("for this format/level not supported"));
    return -1;
}

static int delete_dummy(struct Map_info *Map, off_t line)
{
    G_warning("Vect_delete_line() %s",
              _("for this format/level not supported"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    return -1;
}

<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
static off_t write_dummy(struct Map_info *Map, int type,
                         const struct line_pnts *points,
                         const struct line_cats *cats)
{
    G_warning("Vect_write_line() %s", _("for this format/level not supported"));
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    return -1;
}

static off_t rewrite_dummy(struct Map_info *Map, off_t line, int type,
                           const struct line_pnts *points,
                           const struct line_cats *cats)
{
    G_warning("Vect_rewrite_line() %s",
              _("for this format/level not supported"));
    return -1;
}

static int delete_dummy(struct Map_info *Map, off_t line)
{
    G_warning("Vect_delete_line() %s",
              _("for this format/level not supported"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    return -1;
}

<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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
static off_t rewrite_dummy()
{
    G_warning("Vect_rewrite_line() %s",
              _("for this format/level not supported"));
    return -1;
}

static int delete_dummy()
{
    G_warning("Vect_delete_line() %s",
              _("for this format/level not supported"));
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    return -1;
}

static off_t rewrite_dummy(struct Map_info *Map UNUSED, off_t line UNUSED,
                           int type UNUSED,
                           const struct line_pnts *points UNUSED,
                           const struct line_cats *cats UNUSED)
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
    return -1;
}

static off_t rewrite_dummy(struct Map_info *Map, off_t line, int type,
                           const struct line_pnts *points,
                           const struct line_cats *cats)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
{
    G_warning("Vect_rewrite_line() %s",
              _("for this format/level not supported"));
    return -1;
}

<<<<<<< HEAD
static int delete_dummy(struct Map_info *Map UNUSED, off_t line UNUSED)
=======
static int delete_dummy(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
{
    G_warning("Vect_delete_line() %s",
              _("for this format/level not supported"));
    return -1;
}

<<<<<<< HEAD
static int restore_dummy(struct Map_info *Map UNUSED, off_t offset UNUSED,
                         off_t line UNUSED)
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int restore_dummy(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
{
    G_warning("Vect_restore_line() %s",
              _("for this format/level not supported"));
    return -1;
}

#if !defined HAVE_OGR || !defined HAVE_POSTGRES
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
static int format(struct Map_info *Map, off_t line)
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
static int format(struct Map_info *Map UNUSED, off_t line UNUSED)
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format(struct Map_info *Map, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
{
    G_fatal_error(_("Requested format is not compiled in this version"));
    return 0;
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
static int format2(struct Map_info *Map, off_t offset, off_t line)
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
static int format2(struct Map_info *Map UNUSED, off_t offset UNUSED,
                   off_t line UNUSED)
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
static int format2(struct Map_info *Map, off_t offset, off_t line)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
{
    G_fatal_error(_("Requested format is not compiled in this version"));
    return 0;
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
static off_t format_l(struct Map_info *Map, int type,
                      const struct line_pnts *points,
                      const struct line_cats *cats)
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
static off_t format_l(struct Map_info *Map UNUSED, int type UNUSED,
                      const struct line_pnts *points UNUSED,
                      const struct line_cats *cats UNUSED)
=======
static off_t format_l(struct Map_info *Map, int type,
                      const struct line_pnts *points,
                      const struct line_cats *cats)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
static off_t format_l(struct Map_info *Map, int type,
                      const struct line_pnts *points,
                      const struct line_cats *cats)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
{
    G_fatal_error(_("Requested format is not compiled in this version"));
    return 0;
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
static off_t format_l2(struct Map_info *Map, off_t line, int type,
                       const struct line_pnts *points,
                       const struct line_cats *cats)
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
static off_t format_l2(struct Map_info *Map UNUSED, off_t line UNUSED,
                       int type UNUSED, const struct line_pnts *points UNUSED,
                       const struct line_cats *cats UNUSED)
=======
static off_t format_l2(struct Map_info *Map, off_t line, int type,
                       const struct line_pnts *points,
                       const struct line_cats *cats)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
static off_t format_l2(struct Map_info *Map, off_t line, int type,
                       const struct line_pnts *points,
                       const struct line_cats *cats)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
{
    G_fatal_error(_("Requested format is not compiled in this version"));
    return 0;
}
#endif

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
static off_t (*Vect_write_line_array[][3])(struct Map_info *, int,
                                           const struct line_pnts *,
                                           const struct line_cats *) = {
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
=======
<<<<<<< HEAD
>>>>>>> main
static off_t (*Vect_write_line_array[][3])(struct Map_info *, int,
                                           const struct line_pnts *,
                                           const struct line_cats *) = {
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
static off_t (*Vect_write_line_array[][3])() = {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
static off_t (*Vect_write_line_array[][3])() = {
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
static off_t (*Vect_write_line_array[][3])() = {
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
static off_t (*Vect_write_line_array[][3])() = {
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
static off_t (*Vect_write_line_array[][3])() = {
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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
static off_t (*Vect_write_line_array[][3])() = {
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
static off_t (*Vect_write_line_array[][3])(struct Map_info *, int,
                                           const struct line_pnts *,
                                           const struct line_cats *) = {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
static off_t (*Vect_write_line_array[][3])() = {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
static off_t (*Vect_write_line_array[][3])() = {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
static off_t (*Vect_write_line_array[][3])() = {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
    {write_dummy, V1_write_line_nat, V2_write_line_nat}
#ifdef HAVE_OGR
    ,
    {write_dummy, V1_write_line_ogr, V2_write_line_sfa},
    {write_dummy, V1_write_line_ogr, V2_write_line_sfa}
#else
    ,
    {write_dummy, format_l, format_l},
    {write_dummy, format_l, format_l}
#endif
#ifdef HAVE_POSTGRES
    ,
    {write_dummy, V1_write_line_pg, V2_write_line_pg}
#else
    ,
    {write_dummy, format_l, format_l}
#endif
};

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
static off_t (*Vect_rewrite_line_array[][3])(struct Map_info *, off_t, int,
                                             const struct line_pnts *,
                                             const struct line_cats *) = {
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
=======
<<<<<<< HEAD
>>>>>>> main
static off_t (*Vect_rewrite_line_array[][3])(struct Map_info *, off_t, int,
                                             const struct line_pnts *,
                                             const struct line_cats *) = {
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
static off_t (*Vect_rewrite_line_array[][3])() = {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
static off_t (*Vect_rewrite_line_array[][3])() = {
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
static off_t (*Vect_rewrite_line_array[][3])() = {
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
static off_t (*Vect_rewrite_line_array[][3])() = {
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
static off_t (*Vect_rewrite_line_array[][3])() = {
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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
static off_t (*Vect_rewrite_line_array[][3])() = {
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
static off_t (*Vect_rewrite_line_array[][3])(struct Map_info *, off_t, int,
                                             const struct line_pnts *,
                                             const struct line_cats *) = {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
static off_t (*Vect_rewrite_line_array[][3])() = {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
static off_t (*Vect_rewrite_line_array[][3])() = {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
static off_t (*Vect_rewrite_line_array[][3])() = {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
    {rewrite_dummy, V1_rewrite_line_nat, V2_rewrite_line_nat}
#ifdef HAVE_OGR
    ,
    {rewrite_dummy, V1_rewrite_line_ogr, V2_rewrite_line_sfa},
    {rewrite_dummy, V1_rewrite_line_ogr, V2_rewrite_line_sfa}
#else
    ,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
>>>>>>> osgeo-main
=======
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
>>>>>>> osgeo-main
=======
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
>>>>>>> osgeo-main
=======
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
>>>>>>> osgeo-main
=======
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
>>>>>>> osgeo-main
=======
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
>>>>>>> osgeo-main
=======
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
>>>>>>> osgeo-main
=======
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
>>>>>>> osgeo-main
=======
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
>>>>>>> osgeo-main
=======
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
>>>>>>> osgeo-main
=======
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
>>>>>>> osgeo-main
=======
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
>>>>>>> osgeo-main
    {rewrite_dummy, format_l, format_l},
    {rewrite_dummy, format_l, format_l}
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    {rewrite_dummy, format_l, format_l},
    {rewrite_dummy, format_l, format_l}
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
    {rewrite_dummy, format_l, format_l},
    {rewrite_dummy, format_l, format_l}
=======
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
    {rewrite_dummy, format_l, format_l},
    {rewrite_dummy, format_l, format_l}
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
    {rewrite_dummy, format_l, format_l},
    {rewrite_dummy, format_l, format_l}
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
    {rewrite_dummy, format_l, format_l},
    {rewrite_dummy, format_l, format_l}
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    {rewrite_dummy, format_l2, format_l2},
    {rewrite_dummy, format_l2, format_l2}
=======
    {rewrite_dummy, format_l, format_l},
    {rewrite_dummy, format_l, format_l}
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
#endif
#ifdef HAVE_POSTGRES
    ,
    {rewrite_dummy, V1_rewrite_line_pg, V2_rewrite_line_pg}
#else
    ,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
    {rewrite_dummy, format_l2, format_l2}
#endif
};

static int (*Vect_delete_line_array[][3])(struct Map_info *, off_t) = {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
    {rewrite_dummy, format_l, format_l}
#endif
};

static int (*Vect_delete_line_array[][3])() = {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    {delete_dummy, V1_delete_line_nat, V2_delete_line_nat}
#ifdef HAVE_OGR
    ,
    {delete_dummy, V1_delete_line_ogr, V2_delete_line_sfa},
    {delete_dummy, V1_delete_line_ogr, V2_delete_line_sfa}
#else
    ,
    {delete_dummy, format, format},
    {delete_dummy, format, format}
#endif
#ifdef HAVE_POSTGRES
    ,
    {delete_dummy, V1_delete_line_pg, V2_delete_line_pg}
#else
    ,
    {delete_dummy, format, format}
=======
    {rewrite_dummy, format_l, format_l}
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    {rewrite_dummy, format_l2, format_l2}
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
=======
    {rewrite_dummy, format_l2, format_l2}
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
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
    {rewrite_dummy, format_l2, format_l2}
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
    {rewrite_dummy, format_l2, format_l2}
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
=======
    {rewrite_dummy, format_l2, format_l2}
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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
#endif
};

static int (*Vect_delete_line_array[][3])(struct Map_info *, off_t) = {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
    {delete_dummy, V1_delete_line_nat, V2_delete_line_nat}
#ifdef HAVE_OGR
    ,
    {delete_dummy, V1_delete_line_ogr, V2_delete_line_sfa},
    {delete_dummy, V1_delete_line_ogr, V2_delete_line_sfa}
#else
    ,
    {delete_dummy, format, format},
    {delete_dummy, format, format}
#endif
#ifdef HAVE_POSTGRES
    ,
    {delete_dummy, V1_delete_line_pg, V2_delete_line_pg}
#else
    ,
    {delete_dummy, format, format}
#endif
};

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
static int (*Vect_restore_line_array[][3])() = {
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
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
static int (*Vect_restore_line_array[][3])() = {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
static int (*Vect_restore_line_array[][3])() = {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
static int (*Vect_restore_line_array[][3])() = {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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
    {restore_dummy, V1_restore_line_nat, V2_restore_line_nat}
#ifdef HAVE_OGR
    ,
    {restore_dummy, restore_dummy, restore_dummy},
    {restore_dummy, restore_dummy, restore_dummy}
#else
    ,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    {restore_dummy, format2, format2},
    {restore_dummy, format2, format2}
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
    {restore_dummy, format, format},
    {restore_dummy, format, format}
=======
    {restore_dummy, format2, format2},
    {restore_dummy, format2, format2}
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
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
    {restore_dummy, format, format},
    {restore_dummy, format, format}
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
    {restore_dummy, format2, format2},
    {restore_dummy, format2, format2}
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    {restore_dummy, format2, format2},
    {restore_dummy, format2, format2}
=======
    {restore_dummy, format, format},
    {restore_dummy, format, format}
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
    {restore_dummy, format2, format2},
    {restore_dummy, format2, format2}
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
    {restore_dummy, format2, format2},
    {restore_dummy, format2, format2}
=======
    {restore_dummy, format, format},
    {restore_dummy, format, format}
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
    {restore_dummy, format2, format2},
    {restore_dummy, format2, format2}
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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
#endif
#ifdef HAVE_POSTGRES
    ,
    {restore_dummy, restore_dummy, restore_dummy}
#else
    ,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    {restore_dummy, format, format}
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    {restore_dummy, format2, format2}
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    {rewrite_dummy, format_l, format_l}
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
#endif
};

static int (*Vect_delete_line_array[][3])() = {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    {delete_dummy, V1_delete_line_nat, V2_delete_line_nat}
#ifdef HAVE_OGR
    ,
    {delete_dummy, V1_delete_line_ogr, V2_delete_line_sfa},
    {delete_dummy, V1_delete_line_ogr, V2_delete_line_sfa}
#else
    ,
    {delete_dummy, format, format},
    {delete_dummy, format, format}
#endif
#ifdef HAVE_POSTGRES
    ,
    {delete_dummy, V1_delete_line_pg, V2_delete_line_pg}
#else
    ,
    {delete_dummy, format, format}
=======
    {rewrite_dummy, format_l, format_l}
=======
    {rewrite_dummy, format_l2, format_l2}
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
=======
    {rewrite_dummy, format_l2, format_l2}
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
#endif
};

static int (*Vect_delete_line_array[][3])(struct Map_info *, off_t) = {
<<<<<<< HEAD
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
    {delete_dummy, V1_delete_line_nat, V2_delete_line_nat}
#ifdef HAVE_OGR
    ,
    {delete_dummy, V1_delete_line_ogr, V2_delete_line_sfa},
    {delete_dummy, V1_delete_line_ogr, V2_delete_line_sfa}
#else
    ,
    {delete_dummy, format, format},
    {delete_dummy, format, format}
#endif
#ifdef HAVE_POSTGRES
    ,
    {delete_dummy, V1_delete_line_pg, V2_delete_line_pg}
#else
    ,
    {delete_dummy, format, format}
#endif
};

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
<<<<<<< HEAD
static int (*Vect_restore_line_array[][3])() = {
=======
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
static int (*Vect_restore_line_array[][3])() = {
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
static int (*Vect_restore_line_array[][3])() = {
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
static int (*Vect_restore_line_array[][3])() = {
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
    {restore_dummy, V1_restore_line_nat, V2_restore_line_nat}
#ifdef HAVE_OGR
    ,
    {restore_dummy, restore_dummy, restore_dummy},
    {restore_dummy, restore_dummy, restore_dummy}
#else
    ,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
    {restore_dummy, format2, format2},
    {restore_dummy, format2, format2}
=======
<<<<<<< HEAD
    {restore_dummy, format, format},
    {restore_dummy, format, format}
=======
    {restore_dummy, format2, format2},
    {restore_dummy, format2, format2}
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    {restore_dummy, format, format},
    {restore_dummy, format, format}
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
    {restore_dummy, format, format},
    {restore_dummy, format, format}
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
    {restore_dummy, format, format},
    {restore_dummy, format, format}
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
#endif
#ifdef HAVE_POSTGRES
    ,
    {restore_dummy, restore_dummy, restore_dummy}
#else
    ,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    {restore_dummy, format, format}
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    {restore_dummy, format2, format2}
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
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
=======
    {restore_dummy, format2, format2}
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
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
    {restore_dummy, format, format}
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
    {restore_dummy, format, format}
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    {restore_dummy, format2, format2}
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
=======
    {restore_dummy, format2, format2}
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    {restore_dummy, format, format}
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
    {restore_dummy, format, format}
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    {restore_dummy, format2, format2}
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
=======
    {restore_dummy, format2, format2}
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    {restore_dummy, format, format}
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
    {restore_dummy, format, format}
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    {restore_dummy, format2, format2}
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
=======
    {restore_dummy, format2, format2}
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
#endif
};

<<<<<<< HEAD
static int (*Vect_restore_line_array[][3])(struct Map_info *, off_t, off_t) = {
=======
static int (*Vect_restore_line_array[][3])() = {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    {restore_dummy, V1_restore_line_nat, V2_restore_line_nat}
#ifdef HAVE_OGR
    ,
    {restore_dummy, restore_dummy, restore_dummy},
    {restore_dummy, restore_dummy, restore_dummy}
#else
    ,
<<<<<<< HEAD
    {restore_dummy, format2, format2},
    {restore_dummy, format2, format2}
=======
    {restore_dummy, format, format},
    {restore_dummy, format, format}
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
#endif
#ifdef HAVE_POSTGRES
    ,
    {restore_dummy, restore_dummy, restore_dummy}
#else
    ,
<<<<<<< HEAD
    {restore_dummy, format2, format2}
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
    {restore_dummy, format2, format2}
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    {restore_dummy, format2, format2}
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    {restore_dummy, format2, format2}
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
    {restore_dummy, format, format}
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
#endif
};

static int check_map(struct Map_info *);

/*!
   \brief Writes a new feature

   New feature is written to the end of file (in the case of native
   format). Topological level is not required.

   A warning is printed on error.

   \param Map pointer to Map_info structure
   \param type feature type (see dig_defines.h for supported types)
   \param points pointer to line_pnts structure (feature geometry)
   \param cats pointer to line_cats structure (feature categories)

   \return new feature id (on level 2) (or 0 when build level < GV_BUILD_BASE)
   \return offset into file where the feature starts (on level 1)
   \return -1 on error
 */
off_t Vect_write_line(struct Map_info *Map, int type,
                      const struct line_pnts *points,
                      const struct line_cats *cats)
{
    off_t offset;

    G_debug(3, "Vect_write_line(): name = %s, format = %d, level = %d",
            Map->name, Map->format, Map->level);

    if (!check_map(Map))
        return -1;

    offset = (*Vect_write_line_array[Map->format][Map->level])(Map, type,
                                                               points, cats);

    if (offset < 0)
        G_warning(_("Unable to write feature in vector map <%s>"),
                  Vect_get_name(Map));

    return offset;
}

/*!
   \brief Rewrites existing feature (topological level required)

   Note: Topology must be built at level >= GV_BUILD_BASE

   A warning is printed on error.

   The number of points or cats or type may change. If necessary, the
   old feature is deleted and new is written.

   \param Map pointer to Map_info structure
   \param line feature id (level 2) or feature offset (level 1)
   \param type feature type (GV_POINT, GV_LINE, ...)
   \param points feature geometry
   \param cats feature categories

   \return new feature id (on level 2) (or 0 when build level < GV_BUILD_BASE)
   \return offset into file where the feature starts (on level 1)
   \return -1 on error
 */
off_t Vect_rewrite_line(struct Map_info *Map, off_t line, int type,
                        const struct line_pnts *points,
                        const struct line_cats *cats)
{
    off_t ret;

    G_debug(3,
            "Vect_rewrite_line(): name = %s, format = %d, level = %d, "
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            "line/offset = %" PRI_OFF_T,
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
            "line/offset = %" PRId64,
=======
            "line/offset = %" PRI_OFF_T,
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
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            "line/offset = %" PRI_OFF_T,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
            Map->name, Map->format, Map->level, line);

    if (!check_map(Map))
        return -1;

    ret = (*Vect_rewrite_line_array[Map->format][Map->level])(Map, line, type,
                                                              points, cats);
    if (ret == -1)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
        G_warning(_("Unable to rewrite feature/offset %" PRId64
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
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
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to rewrite feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
                    " in vector map <%s>"),
                  line, Vect_get_name(Map));

    return ret;
}

/*!
   \brief Delete existing feature (topological level required)

   Note: Topology must be built at level >= GV_BUILD_BASE

   A warning is printed on error.

   \param Map pointer to Map_info structure
   \param line feature id (level 2) or feature offset (level 1)

   \return 0 on success
   \return -1 on error
 */
int Vect_delete_line(struct Map_info *Map, off_t line)
{
    int ret;

    G_debug(3, "Vect_delete_line(): name = %s, line/offset = %" PRId64,
            Map->name, line);

    if (!check_map(Map))
        return -1;

    ret = (*Vect_delete_line_array[Map->format][Map->level])(Map, line);

    if (ret == -1)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
        G_warning(_("Unable to delete feature/offset %" PRId64
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
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
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to delete feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
                    " from vector map <%s>"),
                  line, Vect_get_name(Map));

    return ret;
}

/*!
   \brief Restore previously deleted feature (topological level required)

   Note: Topology must be built at level >= GV_BUILD_BASE

   A warning is printed on error.

   \param Map pointer to Map_info structure
   \param offset feature offset to be restored
   \param line feature id to be restored (used only on level 2)

   \return 0 on success
   \return -1 on error
 */
int Vect_restore_line(struct Map_info *Map, off_t offset, off_t line)
{
    int ret;

    G_debug(3,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            "Vect_restore_line(): name = %s, level = %d, offset = %" PRI_OFF_T
            ", line = %" PRI_OFF_T,
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
            "Vect_restore_line(): name = %s, level = %d, offset = %" PRId64
            ", line = %" PRId64,
=======
            "Vect_restore_line(): name = %s, level = %d, offset = %" PRI_OFF_T
            ", line = %" PRI_OFF_T,
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
            "Vect_restore_line(): name = %s, level = %d, offset = %" PRI_OFF_T
            ", line = %" PRI_OFF_T,
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
            Map->name, Map->level, offset, line);

    if (!check_map(Map))
        return -1;

    ret =
        (*Vect_restore_line_array[Map->format][Map->level])(Map, offset, line);

    if (ret == -1)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
        G_warning(_("Unable to restore feature/offset %" PRId64
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
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
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_warning(_("Unable to restore feature/offset %" PRI_OFF_T
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
                    " in vector map <%s>"),
                  offset, Vect_get_name(Map));

    return ret;
}

int check_map(struct Map_info *Map)
{
    if (!VECT_OPEN(Map)) {
        G_warning(_("Vector map <%s> is not opened"), Vect_get_name(Map));
        return 0;
    }

    if (Map->mode != GV_MODE_RW && Map->mode != GV_MODE_WRITE) {
        G_warning(_("Vector map <%s> is not opened in write mode"),
                  Vect_get_name(Map));
        return 0;
    }

    return 1;
}
