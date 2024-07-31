#include <stdio.h>
#include <grass/dbmi.h>
#include <grass/gis.h>
#include <grass/glocale.h>
#include "odbc.h"
#include "globals.h"
#include "proto.h"

int db__driver_close_cursor(dbCursor *dbc)
{
    cursor *c;

    /* get my cursor via the dbc token */
    c = (cursor *)db_find_token(db_get_cursor_token(dbc));
    if (c == NULL)
        return DB_FAILED;

    /* free_cursor(cursor) */
    free_cursor(c);

    return DB_OK;
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
<<<<<<< HEAD
=======
>>>>>>> main
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
cursor *alloc_cursor(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
cursor *alloc_cursor()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
cursor *alloc_cursor(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
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
{
    cursor *c;
    SQLRETURN ret;
    SQLCHAR msg[OD_MSG];
    SQLINTEGER err;

    /* allocate the cursor */
    c = (cursor *)db_malloc(sizeof(cursor));
    if (c == NULL) {
        db_d_append_error(_("Unable to allocate cursor"));
        db_d_report_error();
        return c;
    }

    ret = SQLAllocHandle(SQL_HANDLE_STMT, ODconn, &c->stmt);
    if ((ret != SQL_SUCCESS) && (ret != SQL_SUCCESS_WITH_INFO)) {
        SQLGetDiagRec(SQL_HANDLE_DBC, ODconn, 1, NULL, &err, msg, sizeof(msg),
                      NULL);
        db_d_append_error("AllocStatement()\n%s (%d)\n", msg, (int)err);
        db_d_report_error();
        return c;
    }

    /* tokenize it */
    c->token = db_new_token(c);
    if (c->token < 0) {
        free_cursor(c);
        c = NULL;
        db_d_append_error(_("Unable to add new token."));
        db_d_report_error();
    }

    return c;
}

void free_cursor(cursor *c)
{
    db_drop_token(c->token);
    SQLFreeHandle(SQL_HANDLE_STMT, c->stmt);
    G_free(c);
}
