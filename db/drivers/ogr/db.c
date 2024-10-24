/*!
   \file db/drivers/db.c

   \brief Low level OGR SQL driver

   (C) 2004-2009 by the GRASS Development Team
   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.

   \author Radim Blazek
   \author Some updates by Martin Landa <landa.martin gmail.com>
 */

#include <stdlib.h>
#include <string.h>

#include <grass/gis.h>
#include <grass/dbmi.h>
#include <grass/glocale.h>

#include <ogr_api.h>

#include "globals.h"
#include "proto.h"

/*!
   \brief Open database (OGR datasource)

   \param handle pointer to dbHandle (db name and schema)

   \return DB_OK on success
   \return DB_FAILED on failure
 */
int db__driver_open_database(dbHandle *handle)
{
    const char *name;
    dbConnection connection;

    db_get_connection(&connection);
    name = db_get_handle_dbname(handle);

    /* if name is empty use connection.databaseName */
    if (strlen(name) == 0)
        name = connection.databaseName;

    G_debug(3, "db_driver_open_database() name = '%s'", name);

    OGRRegisterAll();

    /* try read-write access */
    hDs = OGROpen(name, TRUE, NULL);
    if (hDs == NULL) {
        /* try read-only access */
        hDs = OGROpen(name, FALSE, NULL);
        if (hDs)
            G_important_message(_("Had to open data source read-only"));
    }

    if (hDs == NULL) {
        db_d_append_error(_("Unable to open OGR data source"));
        db_d_report_error();
        return DB_FAILED;
    }

    G_debug(3, "Datasource opened");

    return DB_OK;
}

/*!
   \brief Close open database

   \return DB_OK on success
   \return DB_FAILED on failure
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
=======
>>>>>>> main
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
int db__driver_close_database(void)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
int db__driver_close_database(void)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
int db__driver_close_database(void)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
int db__driver_close_database(void)
=======
>>>>>>> osgeo-main
=======
int db__driver_close_database(void)
=======
>>>>>>> osgeo-main
=======
int db__driver_close_database(void)
=======
>>>>>>> osgeo-main
=======
int db__driver_close_database(void)
=======
>>>>>>> osgeo-main
=======
int db__driver_close_database(void)
=======
>>>>>>> osgeo-main
=======
int db__driver_close_database(void)
=======
>>>>>>> osgeo-main
=======
int db__driver_close_database(void)
=======
>>>>>>> osgeo-main
=======
int db__driver_close_database(void)
=======
>>>>>>> osgeo-main
=======
int db__driver_close_database(void)
=======
>>>>>>> osgeo-main
=======
int db__driver_close_database(void)
=======
>>>>>>> osgeo-main
=======
int db__driver_close_database(void)
=======
>>>>>>> osgeo-main
=======
int db__driver_close_database(void)
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int db__driver_close_database()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
int db__driver_close_database(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
int db__driver_close_database()
=======
int db__driver_close_database(void)
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
int db__driver_close_database(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int db__driver_close_database()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int db__driver_close_database(void)
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
int db__driver_close_database(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int db__driver_close_database()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int db__driver_close_database(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
int db__driver_close_database(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int db__driver_close_database()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int db__driver_close_database(void)
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
{
    G_debug(3, "db_driver_close_database()");

    OGR_DS_Destroy(hDs);

    G_debug(3, "Database closed");

    return DB_OK;
}
