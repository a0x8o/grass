#include "vizual.h"
#include <grass/raster3d.h>

#define NO_RESAMPLE

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
int r3read_level(void *g3map, RASTER3D_Region *g3reg, file_info *Headfax,
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
int r3read_level(void *g3map, RASTER3D_Region *g3reg UNUSED, file_info *Headfax,
=======
int r3read_level(void *g3map, RASTER3D_Region *g3reg, file_info *Headfax,
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
=======
int r3read_level(void *g3map, RASTER3D_Region *g3reg, file_info *Headfax,
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
int r3read_level(void *g3map, RASTER3D_Region *g3reg, file_info *Headfax,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int r3read_level(void *g3map, RASTER3D_Region *g3reg, file_info *Headfax,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
int r3read_level(void *g3map, RASTER3D_Region *g3reg, file_info *Headfax,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int r3read_level(void *g3map, RASTER3D_Region *g3reg, file_info *Headfax,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int r3read_level(void *g3map, RASTER3D_Region *g3reg, file_info *Headfax,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int r3read_level(void *g3map, RASTER3D_Region *g3reg, file_info *Headfax,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
int r3read_level(void *g3map, RASTER3D_Region *g3reg, file_info *Headfax,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
int r3read_level(void *g3map, RASTER3D_Region *g3reg, file_info *Headfax,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
                 float *data, int n_lev)
{
#ifdef NO_RESAMPLE
    Rast3d_get_block(g3map, 0, 0, n_lev, Headfax->xdim, Headfax->ydim, 1,
                     (char *)data, FCELL_TYPE);
#else
    /* Rast3d_getBlockRegion might be handy */
    /*
       Rast3d_getAllignedVolume (map, originNorth, originWest, originBottom,
       lengthNorth, lengthWest, lengthBottom,
       nx, ny, nz, volumeBuf, type);
     */
    Rast3d_getAllignedVolume(
        g3map, g3reg->north, g3reg->west, g3reg->top - n_lev * g3reg->tb_res,
        g3reg->north - g3reg->south, g3reg->east - g3reg->west, g3reg->tb_res,
        Headfax->xdim, Headfax->ydim, 1, (char *)data, FCELL_TYPE);
#endif

    return 0;
}
