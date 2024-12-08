/*
 * Copyright (C) 2000 by the GRASS Development Team
 * Author: Bob Covill <bcovill@tekmap.ns.ca>
 *
 * This Program is free software under the GPL (>=v2)
 * Read the file COPYING coming with GRASS for details
 *
 */

#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/glocale.h>
#include <grass/parson.h>
#include "local_proto.h"

int read_rast(double east, double north, double dist, int fd, int coords,
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
>>>>>>> af93827ea1 (r.profile: add JSON support (#3872))
              RASTER_MAP_TYPE data_type, FILE *fp, char *null_string,
              enum OutputFormat format, char *name, JSON_Array *array)
=======
              RASTER_MAP_TYPE data_type, FILE *fp, char *null_string)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
              RASTER_MAP_TYPE data_type, FILE *fp, char *null_string)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
              RASTER_MAP_TYPE data_type, FILE *fp, char *null_string,
              enum OutputFormat format, char *name, JSON_Array *array)
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
              RASTER_MAP_TYPE data_type, FILE *fp, char *null_string)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af93827ea1 (r.profile: add JSON support (#3872))
{
    static DCELL *dcell;
    static int cur_row = -1;
    static CELL nullcell;
    static int nrows, ncols;
    static struct Cell_head window;
    int row, col;
    int outofbounds = FALSE;
    JSON_Object *object;
    JSON_Value *value;

    if (format == JSON) {
        value = json_value_init_object();
        object = json_object(value);
    }

    if (!dcell) {
        Rast_set_c_null_value(&nullcell, 1);
        dcell = Rast_allocate_d_buf();
        G_get_window(&window);
        nrows = window.rows;
        ncols = window.cols;
    }

    row = (window.north - north) / window.ns_res;
    col = (east - window.west) / window.ew_res;
    G_debug(4, "row=%d:%d  col=%d:%d", row, nrows, col, ncols);

    if ((row < 0) || (row >= nrows) || (col < 0) || (col >= ncols))
        outofbounds = TRUE;

    if (!outofbounds) {
        if (row != cur_row)
            Rast_get_d_row(fd, dcell, row);
        cur_row = row;
    }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
>>>>>>> af93827ea1 (r.profile: add JSON support (#3872))
    switch (format) {
    case JSON:
        if (coords) {
            json_object_set_number(object, "easting", east);
            json_object_set_number(object, "northing", north);
        }
        json_object_set_number(object, "distance", dist);
        break;
    case PLAIN:
        if (coords)
            fprintf(fp, "%f %f", east, north);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> af93827ea1 (r.profile: add JSON support (#3872))
=======
    if (coords)
        fprintf(fp, "%f %f", east, north);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
<<<<<<< HEAD
=======
=======
    if (coords)
        fprintf(fp, "%f %f", east, north);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af93827ea1 (r.profile: add JSON support (#3872))

        fprintf(fp, " %f", dist);
        break;
    }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
>>>>>>> af93827ea1 (r.profile: add JSON support (#3872))
    if (outofbounds || Rast_is_d_null_value(&dcell[col])) {
        switch (format) {
        case JSON:
            json_object_set_null(object, name);
            break;
        case PLAIN:
            fprintf(fp, " %s", null_string);
            break;
        }
    }
<<<<<<< HEAD
    else {
        if (data_type == CELL_TYPE) {
            int dvalue = (int)dcell[col];
            switch (format) {
            case JSON:
                json_object_set_number(object, name, dvalue);
                break;
            case PLAIN:
                fprintf(fp, " %d", dvalue);
                break;
            }
        }
        else {
            switch (format) {
            case JSON:
                json_object_set_number(object, name, dcell[col]);
                break;
            case PLAIN:
                fprintf(fp, " %f", dcell[col]);
                break;
            }
        }
=======
    if (outofbounds || Rast_is_d_null_value(&dcell[col]))
        fprintf(fp, " %s", null_string);
    else {
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
    if (outofbounds || Rast_is_d_null_value(&dcell[col]))
        fprintf(fp, " %s", null_string);
    else {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
        if (data_type == CELL_TYPE)
            fprintf(fp, " %d", (int)dcell[col]);
        else
            fprintf(fp, " %f", dcell[col]);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    else {
        if (data_type == CELL_TYPE) {
            int dvalue = (int)dcell[col];
            switch (format) {
            case JSON:
                json_object_set_number(object, name, dvalue);
                break;
            case PLAIN:
                fprintf(fp, " %d", dvalue);
                break;
            }
        }
        else {
            switch (format) {
            case JSON:
                json_object_set_number(object, name, dcell[col]);
                break;
            case PLAIN:
                fprintf(fp, " %f", dcell[col]);
                break;
            }
        }
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af93827ea1 (r.profile: add JSON support (#3872))
    }

    if (clr) {
        int red, green, blue;

        if (outofbounds)
            Rast_get_c_color(&nullcell, &red, &green, &blue, &colors);
        else
            Rast_get_d_color(&dcell[col], &red, &green, &blue, &colors);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
>>>>>>> af93827ea1 (r.profile: add JSON support (#3872))
        switch (format) {
        case JSON:
            json_object_set_number(object, "red", red);
            json_object_set_number(object, "green", green);
            json_object_set_number(object, "blue", blue);
            break;
        case PLAIN:
            fprintf(fp, " %03d:%03d:%03d", red, green, blue);
            break;
        }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> af93827ea1 (r.profile: add JSON support (#3872))
=======

        fprintf(fp, " %03d:%03d:%03d", red, green, blue);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======

        fprintf(fp, " %03d:%03d:%03d", red, green, blue);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
>>>>>>> af93827ea1 (r.profile: add JSON support (#3872))
    }

    switch (format) {
    case JSON:
        json_array_append_value(array, value);
        break;
    case PLAIN:
        fprintf(fp, "\n");
        break;
    }

    return 0;
}
