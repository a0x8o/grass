/****************************************************************************
 *
 * MODULE:       r3.out.vtk
 *
 * AUTHOR(S):    Original author
 *               Soeren Gebbert soerengebbert at gmx de
 *                 27 Feb 2006 Berlin
 * PURPOSE:      Converts 3D raster maps (RASTER3D) into the VTK-Ascii format
 *
 * COPYRIGHT:    (C) 2005 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 *****************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <grass/gis.h>
#include <grass/raster3d.h>
#include <grass/glocale.h>
#include "globalDefs.h"
#include "writeVTKHead.h"
#include "parameters.h"
#include "errorHandling.h"

/* ************************************************************************* */
/* Writes the structured points Header ************************************* */

/* ************************************************************************* */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
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
void write_vtk_structured_point_header(FILE *fp, char *vtkFile UNUSED,
=======
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
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
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
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
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_point_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
                                       RASTER3D_Region region, int dp,
                                       double scale)
{
    G_debug(
        3,
        "write_vtk_structured_point_header: Writing VTKStructuredPoint-Header");

    /*Simple vtk ASCII header */

    fprintf(fp, "# vtk DataFile Version 3.0\n");
    /* The header line describes the data. */
    fprintf(fp, "GRASS GIS %i Export\n", GRASS_VERSION_MAJOR);
    fprintf(fp, "ASCII\n");
    fprintf(fp, "DATASET STRUCTURED_POINTS\n"); /*We are using the structured
                                                   point dataset. */

    if (param.point->answer)
        fprintf(fp, "DIMENSIONS %i %i %i\n", region.cols, region.rows,
                region.depths);
    else
        fprintf(fp, "DIMENSIONS %i %i %i\n", region.cols + 1, region.rows + 1,
                region.depths + 1);

    fprintf(fp, "SPACING %.*f %.*f %.*f\n", dp, region.ew_res, dp,
            region.ns_res, dp, (region.tb_res * scale));

    if (param.point->answer) {
        if (param.origin->answer)
            fprintf(fp, "ORIGIN %.*f %.*f %.*f\n", dp,
                    (region.west + region.ew_res / 2) - x_extent, dp,
                    (region.south + region.ns_res / 2) - y_extent, dp,
                    region.bottom * scale + (region.tb_res * scale) / 2);
        else
            fprintf(fp, "ORIGIN %.*f %.*f %.*f\n", dp,
                    (region.west + region.ew_res / 2) - x_extent, dp,
                    (region.south + region.ns_res / 2) - y_extent, dp,
                    region.bottom + (region.tb_res * scale) / 2);
    }
    else {
        if (param.origin->answer)
            fprintf(fp, "ORIGIN %.*f %.*f %.*f\n", dp, region.west - x_extent,
                    dp, region.south - y_extent, dp, region.bottom * scale);
        else
            fprintf(fp, "ORIGIN %.*f %.*f %.*f\n", dp, region.west - x_extent,
                    dp, region.south - y_extent, dp, region.bottom);
    }

    if (param.point->answer)
        fprintf(fp, "POINT_DATA %i\n",
                region.cols * region.rows *
                    region.depths); /*We have pointdata */
    else
        fprintf(fp, "CELL_DATA %i\n",
                region.cols * region.rows *
                    region.depths); /*We have celldata */

    return;
}

/* ************************************************************************* */
/* Writes the strcutured grid header **************************************** */

/* ************************************************************************* */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
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
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile UNUSED,
=======
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
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
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
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
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_structured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
                                      RASTER3D_Region region)
{
    G_debug(
        3,
        "write_vtk_structured_grid_header: Writing VTKStructuredGrid-Header");
    fprintf(fp, "# vtk DataFile Version 3.0\n");
    fprintf(fp, "GRASS GIS %i Export\n", GRASS_VERSION_MAJOR);
    fprintf(fp, "ASCII\n");
    fprintf(fp, "DATASET STRUCTURED_GRID\n"); /*We are using the structured grid
                                                 dataset. */
    fprintf(fp, "DIMENSIONS %i %i %i\n", region.cols, region.rows,
            region.depths);
    /*Only point data is available */
    fprintf(fp, "POINTS %i float\n", region.cols * region.rows * region.depths);

    return;
}

/* ************************************************************************* */
/* Writes the unstrcutured grid header ************************************* */

/* ************************************************************************* */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
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
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile UNUSED,
=======
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
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
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
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
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void write_vtk_unstructured_grid_header(FILE *fp, char *vtkFile,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
                                        RASTER3D_Region region)
{
    G_debug(3, "write_vtk_unstructured_grid_header: Writing "
               "VTKUnstructuredGrid-Header");
    fprintf(fp, "# vtk DataFile Version 3.0\n");
    fprintf(fp, "GRASS GIS %i Export\n", GRASS_VERSION_MAJOR);
    fprintf(fp, "ASCII\n");
    fprintf(fp, "DATASET UNSTRUCTURED_GRID\n"); /*We are using the unstructured
                                                   grid dataset. */
    /*Only cell data is available, because we creating a hexaeder/vtk-voxel for
     * every voxel */
    fprintf(fp, "POINTS %i float\n",
            region.cols * region.rows * region.depths *
                8); /*a Voxel has 8 points */

    return;
}
