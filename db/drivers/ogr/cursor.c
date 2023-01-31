/*!
   \file db/drivers/cursor.c

   \brief Low level OGR SQL driver

   (C) 2004-2009 by the GRASS Development Team
   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.

   \author Radim Blazek
   \author Some updates by Martin Landa <landa.martin gmail.com>
 */

#include <stdio.h>

#include <grass/gis.h>
#include <grass/dbmi.h>
#include <grass/glocale.h>

#include <ogr_api.h>

#include "globals.h"
#include "proto.h"

/*!
   \brief Close cursor

   \param dbc pointer to dbCursor to be closed

   \return DB_OK on success
   \return DB_FAILED on failure
 */
int db__driver_close_cursor(dbCursor *dbc)
{
    cursor *c;

    G_debug(3, "db_driver_close_cursor()");

    /* get my cursor via the dbc token */
    c = (cursor *)db_find_token(db_get_cursor_token(dbc));
    if (c == NULL)
        return DB_FAILED;

    /* free_cursor(cursor) */
    free_cursor(c);

    G_debug(3, "Cursor closed");

    return DB_OK;
}

/*!
   \brief Allocate cursor

   \return pointer to cursor structure
   \return NULL on error
 */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
cursor *alloc_cursor(void)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
cursor *alloc_cursor(void)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
cursor *alloc_cursor(void)
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
cursor *alloc_cursor()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
cursor *alloc_cursor(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
cursor *alloc_cursor()
=======
cursor *alloc_cursor(void)
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
cursor *alloc_cursor(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
cursor *alloc_cursor()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
cursor *alloc_cursor(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
cursor *alloc_cursor(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
cursor *alloc_cursor()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
cursor *alloc_cursor(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
cursor *alloc_cursor(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
cursor *alloc_cursor()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
cursor *alloc_cursor(void)
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
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
cursor *alloc_cursor(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
cursor *alloc_cursor()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
cursor *alloc_cursor(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
cursor *alloc_cursor(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
cursor *alloc_cursor()
=======
cursor *alloc_cursor(void)
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
cursor *alloc_cursor(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
cursor *alloc_cursor()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
cursor *alloc_cursor(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
{
    cursor *c;

    /* allocate the cursor */
    c = (cursor *)db_malloc(sizeof(cursor));
    if (c == NULL) {
        db_d_append_error(_("Unable to allocate cursor"));
        return NULL;
    }

    G_zero(c, sizeof(cursor));

    /* tokenize it */
    c->token = db_new_token(c);
    if (c->token < 0) {
        db_d_append_error(_("Unable to add new token"));
        return NULL;
    }
    return c;
}

/*!
   \brief Free cursor structure (destroy OGR feature and release OGR layer)

   \param c pointer to cursor
 */
void free_cursor(cursor *c)
{
    if (c->hFeature)
        OGR_F_Destroy(c->hFeature);

    if (c->hLayer)
        OGR_DS_ReleaseResultSet(hDs, c->hLayer);

    G_free(c->cols);
    G_free(c);

    db_drop_token(c->token);
}
