/*
 * projection checking
 *
 * Copyright 2011-2015 by Markus Metz, and The GRASS Development Team
 * Authors:
 *  Markus Metz (v.in.lidar)
 *  Vaclav Petras (move code to standalone functions)
 *
 * This program is free software licensed under the GPL (>=v2).
 * Read the COPYING file that comes with GRASS for details.
 *
 */

#include <string.h>

#include <grass/gis.h>
#include <grass/glocale.h>
#include <grass/gprojects.h>

void projection_mismatch_report(struct Cell_head cellhd,
                                struct Cell_head loc_wind,
                                struct Key_Value *loc_proj_info,
                                struct Key_Value *loc_proj_units,
                                struct Key_Value *proj_info,
                                struct Key_Value *proj_units, int err)
{
    int i_value;
    char error_msg[8192];

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    strcpy(error_msg, _("Projection of dataset does not"
                        " appear to match current location.\n\n"));
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
    strcpy(error_msg, _("Coordinate reference system of dataset does not"
                        " appear to match current project.\n\n"));
=======
    strcpy(error_msg,
           _("Projection of dataset does not"
             " appear to match current location.\n\n"));
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
    strcpy(error_msg, _("Projection of dataset does not"
                        " appear to match current location.\n\n"));
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
    strcpy(error_msg, _("Projection of dataset does not"
                        " appear to match current location.\n\n"));
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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

    /* TODO: output this info sorted by key: */
    if (loc_wind.proj != cellhd.proj || err != -2) {
        if (loc_proj_info != NULL) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
            strcat(error_msg, _("GRASS project PROJ_INFO is:\n"));
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, _("GRASS LOCATION PROJ_INFO is:\n"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
            for (i_value = 0; i_value < loc_proj_info->nitems; i_value++)
                sprintf(error_msg + strlen(error_msg), "%s: %s\n",
                        loc_proj_info->key[i_value],
                        loc_proj_info->value[i_value]);
            strcat(error_msg, "\n");
        }

        if (proj_info != NULL) {
            strcat(error_msg, _("Import dataset PROJ_INFO is:\n"));
            for (i_value = 0; i_value < proj_info->nitems; i_value++)
                sprintf(error_msg + strlen(error_msg), "%s: %s\n",
                        proj_info->key[i_value], proj_info->value[i_value]);
        }
        else {
            strcat(error_msg, _("Import dataset PROJ_INFO is:\n"));
            if (cellhd.proj == PROJECTION_XY)
                sprintf(error_msg + strlen(error_msg),
                        "Dataset proj = %d (unreferenced/unknown)\n",
                        cellhd.proj);
            else if (cellhd.proj == PROJECTION_LL)
                sprintf(error_msg + strlen(error_msg),
                        "Dataset proj = %d (lat/long)\n", cellhd.proj);
            else if (cellhd.proj == PROJECTION_UTM)
                sprintf(error_msg + strlen(error_msg),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
                        "Dataset proj = %d (UTM), zone = %d\n", cellhd.proj,
                        cellhd.zone);
            else
                sprintf(error_msg + strlen(error_msg),
                        "Dataset proj = %d (unknown), zone = %d\n", cellhd.proj,
                        cellhd.zone);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
                        "Dataset proj = %d (UTM), zone = %d\n",
                        cellhd.proj, cellhd.zone);
            else
                sprintf(error_msg + strlen(error_msg),
                        "Dataset proj = %d (unknown), zone = %d\n",
                        cellhd.proj, cellhd.zone);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
                        "Dataset proj = %d (UTM), zone = %d\n", cellhd.proj,
                        cellhd.zone);
            else
                sprintf(error_msg + strlen(error_msg),
                        "Dataset proj = %d (unknown), zone = %d\n", cellhd.proj,
                        cellhd.zone);
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
    }
    else {
        if (loc_proj_units != NULL) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
            strcat(error_msg, "GRASS project PROJ_UNITS is:\n");
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
            strcat(error_msg, "GRASS LOCATION PROJ_UNITS is:\n");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
            for (i_value = 0; i_value < loc_proj_units->nitems; i_value++)
                sprintf(error_msg + strlen(error_msg), "%s: %s\n",
                        loc_proj_units->key[i_value],
                        loc_proj_units->value[i_value]);
            strcat(error_msg, "\n");
        }

        if (proj_units != NULL) {
            strcat(error_msg, "Import dataset PROJ_UNITS is:\n");
            for (i_value = 0; i_value < proj_units->nitems; i_value++)
                sprintf(error_msg + strlen(error_msg), "%s: %s\n",
                        proj_units->key[i_value], proj_units->value[i_value]);
        }
    }
    sprintf(error_msg + strlen(error_msg),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
            _("\nIn case of no significant differences"
              " in the coordinate reference system definitions,"
              " use the -o flag to ignore them and use"
              " current project definition.\n"));
    strcat(error_msg,
           _("Consider generating a new project with 'project' parameter"
=======
            _("\nIn case of no significant differences in the projection definitions,"
             " use the -o flag to ignore them and use"
             " current location definition.\n"));
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
            _("\nIn case of no significant differences in the projection "
              "definitions,"
              " use the -o flag to ignore them and use"
              " current location definition.\n"));
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    strcat(error_msg,
           _("Consider generating a new location with 'location' parameter"
=======
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    strcat(error_msg,
           _("Consider generating a new location with 'location' parameter"
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
    strcat(error_msg,
           _("Consider generating a new location with 'location' parameter"
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
    strcat(error_msg,
           _("Consider generating a new location with 'location' parameter"
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    strcat(error_msg,
           _("Consider generating a new location with 'location' parameter"
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    strcat(error_msg,
           _("Consider generating a new location with 'location' parameter"
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
             " from input data set.\n"));
    G_fatal_error("%s", error_msg);
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
>>>>>>> osgeo-main
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
>>>>>>> osgeo-main
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
>>>>>>> osgeo-main
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
>>>>>>> osgeo-main
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
>>>>>>> osgeo-main
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
>>>>>>> osgeo-main
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
>>>>>>> osgeo-main
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
>>>>>>> osgeo-main
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
>>>>>>> osgeo-main
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
>>>>>>> osgeo-main
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
>>>>>>> osgeo-main
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
>>>>>>> osgeo-main
void projection_check_wkt(struct Cell_head cellhd,
                          struct Cell_head loc_wind,
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
void projection_check_wkt(struct Cell_head cellhd,
                          struct Cell_head loc_wind,
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
void projection_check_wkt(struct Cell_head cellhd,
                          struct Cell_head loc_wind,
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
=======
void projection_check_wkt(struct Cell_head cellhd,
                          struct Cell_head loc_wind,
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
void projection_check_wkt(struct Cell_head cellhd, struct Cell_head loc_wind,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
                          const char *projstr, int override, int verbose)
{
    struct Key_Value *loc_proj_info = NULL, *loc_proj_units = NULL;
    struct Key_Value *proj_info, *proj_units;
    int err = 0;

    proj_info = NULL;
    proj_units = NULL;

    /* Projection only required for checking so convert non-interactively */
    if (GPJ_wkt_to_grass(&cellhd, &proj_info, &proj_units, projstr, 0) < 0)
        G_warning(_("Unable to convert input map projection information to "
                    "GRASS format for checking"));

    /* Does the projection of the current location match the dataset? */

    /* fetch LOCATION PROJ info */
    if (loc_wind.proj != PROJECTION_XY) {
        loc_proj_info = G_get_projinfo();
        loc_proj_units = G_get_projunits();
    }

    if (override) {
        cellhd.proj = loc_wind.proj;
        cellhd.zone = loc_wind.zone;
        if (verbose)
            G_message(_("Overriding projection check"));
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
    else if (loc_wind.proj != cellhd.proj ||
             (err = G_compare_projections(loc_proj_info, loc_proj_units,
                                          proj_info, proj_units)) != TRUE) {
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
    }
    else {
        if (verbose) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
            G_message(_("Projection of input dataset and current location "
                        "appear to match"));
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
            G_message(_("Coordinate reference system of input dataset and "
                        "current project appear to match"));
=======
    else if (loc_wind.proj != cellhd.proj
             || (err =
                 G_compare_projections(loc_proj_info, loc_proj_units,
                                       proj_info, proj_units)) != TRUE) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
    else if (loc_wind.proj != cellhd.proj ||
             (err = G_compare_projections(loc_proj_info, loc_proj_units,
                                          proj_info, proj_units)) != TRUE) {
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
=======
<<<<<<< HEAD
>>>>>>> main
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units,
                                   proj_info, proj_units, err);
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
>>>>>>> osgeo-main
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
>>>>>>> osgeo-main
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units,
                                   proj_info, proj_units, err);
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
<<<<<<< HEAD
                                   loc_proj_units,
                                   proj_info, proj_units, err);
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
                                   loc_proj_units, proj_info, proj_units, err);
>>>>>>> osgeo-main
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
>>>>>>> osgeo-main
>>>>>>> main
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
>>>>>>> osgeo-main
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
>>>>>>> osgeo-main
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
>>>>>>> osgeo-main
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
>>>>>>> osgeo-main
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
>>>>>>> osgeo-main
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
>>>>>>> osgeo-main
=======
        projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                                   loc_proj_units, proj_info, proj_units, err);
>>>>>>> osgeo-main
    }
    else {
        if (verbose) {
            G_message(_("Projection of input dataset and current location "
                        "appear to match"));
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
            G_message(_("Projection of input dataset and current location "
                        "appear to match"));
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
    }
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
/* Does the projection of the current location match the dataset? */
int is_wkt_projection_same_as_loc(const char *wkt)
{
    struct Key_Value *loc_proj_info = NULL, *loc_proj_units = NULL;
    struct Key_Value *proj_info = NULL, *proj_units = NULL;
    struct Cell_head cellhd;
    struct Cell_head loc_wind;

    G_get_default_window(&loc_wind);

    /* Projection only required for checking so convert non-interactively */
    if (GPJ_wkt_to_grass(&cellhd, &proj_info, &proj_units, wkt, 0) < 0)
        G_warning(_("Unable to convert input map projection information to "
                    "GRASS format for checking"));

    /* fetch LOCATION PROJ info */
    if (loc_wind.proj != PROJECTION_XY) {
        loc_proj_info = G_get_projinfo();
        loc_proj_units = G_get_projunits();
    }

    if (loc_wind.proj != cellhd.proj) {
        return FALSE;
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
>>>>>>> osgeo-main
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
>>>>>>> osgeo-main
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
>>>>>>> osgeo-main
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
>>>>>>> osgeo-main
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
>>>>>>> osgeo-main
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
>>>>>>> osgeo-main
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
>>>>>>> osgeo-main
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
>>>>>>> osgeo-main
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
>>>>>>> osgeo-main
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
>>>>>>> osgeo-main
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
>>>>>>> osgeo-main
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
>>>>>>> osgeo-main
    else if (G_compare_projections(loc_proj_info, loc_proj_units,
                                   proj_info, proj_units) != 1) {
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units,
                                   proj_info, proj_units) != 1) {
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units,
                                   proj_info, proj_units) != 1) {
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    else if (G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                   proj_units) != 1) {
=======
    else if (G_compare_projections(loc_proj_info, loc_proj_units,
                                   proj_info, proj_units) != 1) {
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
        return FALSE;
    }
    else {
        return TRUE;
    }
}

/* Does the projection of the current location match the dataset? */
void wkt_projection_mismatch_report(const char *wkt)
{
    struct Key_Value *loc_proj_info = NULL, *loc_proj_units = NULL;
    struct Key_Value *proj_info = NULL, *proj_units = NULL;
    struct Cell_head cellhd;
    struct Cell_head loc_wind;

    G_get_default_window(&loc_wind);

    /* Projection only required for checking so convert non-interactively */
    if (GPJ_wkt_to_grass(&cellhd, &proj_info, &proj_units, wkt, 0) < 0)
        G_warning(_("Unable to convert input map projection information to "
                    "GRASS format for checking"));

    /* fetch LOCATION PROJ info */
    if (loc_wind.proj != PROJECTION_XY) {
        loc_proj_info = G_get_projinfo();
        loc_proj_units = G_get_projunits();
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
    int err = G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                    proj_units);

    projection_mismatch_report(cellhd, loc_wind, loc_proj_info, loc_proj_units,
                               proj_info, proj_units, err);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
    int err = G_compare_projections(loc_proj_info, loc_proj_units,
                                    proj_info, proj_units);

    projection_mismatch_report(cellhd, loc_wind, loc_proj_info,
                               loc_proj_units, proj_info, proj_units, err);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
    int err = G_compare_projections(loc_proj_info, loc_proj_units, proj_info,
                                    proj_units);

    projection_mismatch_report(cellhd, loc_wind, loc_proj_info, loc_proj_units,
                               proj_info, proj_units, err);
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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

/* caller should free the returned string */
char *location_projection_as_wkt(int prettify)
{
    struct Key_Value *proj_info = G_get_projinfo();
    struct Key_Value *proj_units = G_get_projunits();
    char *proj_wkt = GPJ_grass_to_wkt(proj_info, proj_units, FALSE, prettify);

    G_free_key_value(proj_info);
    G_free_key_value(proj_units);
    return proj_wkt;
}
