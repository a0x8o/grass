#include <grass/dbmi.h>
#include <stdio.h>
#include <string.h>
#include <grass/gis.h>
#include "odbc.h"
#include "globals.h"
#include "proto.h"

int db__driver_open_database(dbHandle *handle)
{
    SQLCHAR msg[OD_MSG];
    const char *name;
    SQLRETURN ret;
    SQLINTEGER err;
    dbConnection connection;
    SQLCHAR dbms_name[256];

    /* Open connection */
    if (open_connection() != DB_OK)
        return DB_FAILED;

    db_get_connection(&connection);
    name = db_get_handle_dbname(handle);

    /* if name is empty use connection.databaseName */
    if (strlen(name) == 0) {
        name = connection.databaseName;
    }

    /* Connect to the datasource */
    ret =
        SQLConnect(ODconn, (SQLCHAR *)name, SQL_NTS, (SQLCHAR *)connection.user,
                   SQL_NTS, (SQLCHAR *)connection.password, SQL_NTS);
    if ((ret != SQL_SUCCESS) && (ret != SQL_SUCCESS_WITH_INFO)) {
        SQLGetDiagRec(SQL_HANDLE_DBC, ODconn, 1, NULL, &err, msg, sizeof(msg),
                      NULL);
        db_d_append_error("SQLConnect():\n%s (%d)\n", msg, (int)err);
        db_d_report_error();

        return DB_FAILED;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    }

    /* Find ODBC DB driver */
    SQLGetInfo(ODconn, SQL_DBMS_NAME, (SQLPOINTER)dbms_name, sizeof(dbms_name),
               NULL);

    if (strcmp((CHAR *)dbms_name, "MySQL") == 0 ||
        strcmp((CHAR *)dbms_name, "MariaDB") == 0) {
        dbString sql;
        cursor *c;

        c = alloc_cursor();
        if (c == NULL)
            return DB_FAILED;

        db_init_string(&sql);
        db_set_string(&sql, "SET SQL_MODE=ANSI_QUOTES;");

        /* Set SQL ANSI_QUOTES MODE which allow to use double quotes instead of
         * backticks */
        ret = SQLExecDirect(c->stmt, (SQLCHAR *)db_get_string(&sql), SQL_NTS);

        if ((ret != SQL_SUCCESS) && (ret != SQL_SUCCESS_WITH_INFO)) {
            SQLGetDiagRec(SQL_HANDLE_STMT, c->stmt, 1, NULL, &err, msg,
                          sizeof(msg), NULL);
            db_d_append_error("SQLExecDirect():\n%s\n%s (%d)\n",
                              db_get_string(&sql), msg, (int)err);
            db_d_report_error();
            free_cursor(c);
            db_free_string(&sql);
            SQLDisconnect(ODconn);
            close_connection();

            return DB_FAILED;
        }

        G_debug(3, "db__driver_open_database(): Set ODBC %s DB %s", dbms_name,
                db_get_string(&sql));

        free_cursor(c);
        db_free_string(&sql);
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
    }

    return DB_OK;
}

int db__driver_close_database()
{
    SQLDisconnect(ODconn);
    close_connection();
    return DB_OK;
}
