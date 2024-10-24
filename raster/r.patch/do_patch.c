#include <grass/gis.h>
#include <grass/raster.h>

/*
 * patch in non-zero data over zero data
 * keep track of the categories which are patched in
 * for later use in constructing the new category and color files
 *
 * returns: 1 the result still contains nulls
 *          0 the result contains no zero nulls
 */

int is_zero_value(void *rast, RASTER_MAP_TYPE data_type)
{

    /* insert 0 check here */

    return Rast_is_null_value(rast, data_type) ||
                   Rast_get_d_value(rast, data_type) != 0.0
               ? 0
               : 1;
}

int do_patch(void *result, void *patch, struct Cell_stats *statf, int ncols,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
>>>>>>> osgeo-main
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
>>>>>>> osgeo-main
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
>>>>>>> osgeo-main
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
>>>>>>> osgeo-main
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
>>>>>>> osgeo-main
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
>>>>>>> osgeo-main
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
>>>>>>> osgeo-main
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
>>>>>>> osgeo-main
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
>>>>>>> osgeo-main
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
>>>>>>> osgeo-main
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
>>>>>>> osgeo-main
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
>>>>>>> osgeo-main
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
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
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
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
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero,
             int no_support)
=======
             RASTER_MAP_TYPE out_type, size_t out_cell_size, int use_zero)
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
{
    int more;

    more = 0;
    while (ncols-- > 0) {
        if (use_zero) { /* use 0 for transparency instead of NULL */
            if (is_zero_value(result, out_type) ||
                Rast_is_null_value(result, out_type)) {
                /* Don't patch hole with a null, just mark as more */
                if (Rast_is_null_value(patch, out_type))
                    more = 1;
                else {
                    /* Mark that there is more to be done if we patch with 0 */
                    if (is_zero_value(patch, out_type))
                        more = 1;
                    Rast_raster_cpy(result, patch, 1, out_type);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
                }
            } /* ZERO support */
        }
        else { /* use NULL for transparency instead of 0 */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
                    if (out_type == CELL_TYPE)
                        Rast_update_cell_stats((CELL *) result, 1, statf);
                }
            }    /* ZERO support */
        } else { /* use NULL for transparency instead of 0 */
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
                }
            } /* ZERO support */
        }
        else { /* use NULL for transparency instead of 0 */
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
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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

            if (Rast_is_null_value(result, out_type)) {
                if (Rast_is_null_value(patch, out_type))
                    more = 1;
                else {
                    Rast_raster_cpy(result, patch, 1, out_type);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
>>>>>>> osgeo-main
=======
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
>>>>>>> osgeo-main
=======
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
>>>>>>> osgeo-main
=======
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
>>>>>>> osgeo-main
=======
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
>>>>>>> osgeo-main
=======
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
>>>>>>> osgeo-main
=======
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
>>>>>>> osgeo-main
=======
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
>>>>>>> osgeo-main
=======
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
>>>>>>> osgeo-main
=======
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
>>>>>>> osgeo-main
=======
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
>>>>>>> osgeo-main
=======
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
>>>>>>> osgeo-main
                    if (out_type == CELL_TYPE)
                        Rast_update_cell_stats((CELL *) result, 1, statf);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
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
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
                    if (out_type == CELL_TYPE)
                        Rast_update_cell_stats((CELL *) result, 1, statf);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
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
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
                    if (out_type == CELL_TYPE)
                        Rast_update_cell_stats((CELL *) result, 1, statf);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
                    if (out_type == CELL_TYPE && !no_support)
                        Rast_update_cell_stats((CELL *)result, 1, statf);
=======
                    if (out_type == CELL_TYPE)
                        Rast_update_cell_stats((CELL *) result, 1, statf);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
                }
            } /* NULL support */
        }
        result = G_incr_void_ptr(result, out_cell_size);
        patch = G_incr_void_ptr(patch, out_cell_size);
    }
    return more;
}
