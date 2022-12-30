/*!
   \file lib/db/dbmi_driver/d_error.c

   \brief DBMI Library (driver) - error reporting

   Taken from DB drivers.

   (C) 1999-2008, 2012 by the GRASS Development Team

   This program is free software under the GNU General Public
   License (>=v2). Read the file COPYING that comes with GRASS
   for details.

   \author Joel Jones (CERL/UIUC)
   \author Radim Blazek
   \author Adopted for DBMI by Martin Landa <landa.martin@gmail.com>
 */

#include <string.h>
#include <errno.h>
#include <grass/dbmi.h>
#include <grass/glocale.h>

/* initialize the global struct */
struct error_state {
    char *driver_name;
    dbString *errMsg;
};

static struct error_state state;
static struct error_state *st = &state;

static void init(void)
{
    db_set_string(st->errMsg, "");
    db_d_append_error(_("DBMI-%s driver error:"), st->driver_name);
    db_append_string(st->errMsg, "\n");
}

/*!
   \brief Init error message for DB driver

   Initialize prefix

   \param name driver name (eg. "SQLite"))
 */
void db_d_init_error(const char *name)
{
    if (!st->errMsg) {
        st->errMsg = (dbString *)G_malloc(sizeof(dbString));
        db_init_string(st->errMsg);
    }

    G_debug(1, "db_d_init_error(): %s", name);

    st->driver_name = G_malloc(strlen(name) + 1);
    strcpy(st->driver_name, name);
    init();
}

/*!
   \brief Append error message for DB driver

   \param fmt formatted message
 */
void db_d_append_error(const char *fmt, ...)
{
    FILE *fp = NULL;
    char *work = NULL;
    int count = 0;
    va_list ap;

    va_start(ap, fmt);
    if ((fp = tmpfile())) {
        count = vfprintf(fp, fmt, ap);
        if (count >= 0 && (work = G_calloc(count + 1, 1))) {
            rewind(fp);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
>>>>>>> osgeo-main
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
>>>>>>> osgeo-main
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
>>>>>>> osgeo-main
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
>>>>>>> osgeo-main
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
>>>>>>> osgeo-main
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
>>>>>>> osgeo-main
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
>>>>>>> osgeo-main
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
>>>>>>> osgeo-main
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
>>>>>>> osgeo-main
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
>>>>>>> osgeo-main
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
>>>>>>> osgeo-main
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
>>>>>>> osgeo-main
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
>>>>>>> osgeo-main
            if (fread(work, 1, count, fp) != count) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            if (fread(work, 1, count, fp) != count) {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
            if (fread(work, 1, count, fp) != count) {
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
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
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
            if (fread(work, 1, count, fp) != count) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if (fread(work, 1, count, fp) != count) {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
            if (fread(work, 1, count, fp) != count) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if (fread(work, 1, count, fp) != count) {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
            if (fread(work, 1, count, fp) != count) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if (fread(work, 1, count, fp) != count) {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
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
            if (fread(work, 1, count, fp) != (size_t)count) {
=======
            if (fread(work, 1, count, fp) != count) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if (fread(work, 1, count, fp) != count) {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
                if (ferror(fp))
                    G_fatal_error(_("DBMI-%s driver file reading error: %s"),
                                  st->driver_name, strerror(errno));
            }
            db_append_string(st->errMsg, work);
            G_free(work);
        }
        fclose(fp);
    }
    va_end(ap);
}

/*!
   \brief Report error message for DB driver
 */
void db_d_report_error(void)
{
    db_append_string(st->errMsg, "\n");
    db_error(db_get_string(st->errMsg));

    init();
}
