#include <grass/gis.h>
#include <grass/raster.h>

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
/**
 * Merges the statf[] arrays for each thread into
 * Thread 0 for use in the support computation.
 *
 * The function takes in a 2D array thread_statf[][], where
 * the rows represent each thread and each column is
 * a file that is being used to patch. The result is
 * that thread_statf[0] is an array of size [nfiles] that holds
 * the merged stats information.
 *
 * The function takes in a pointer to thread_statf[][], directly
 * modifying it
 */
void merge_threads(struct Cell_stats **thread_statf, int nprocs, int nfiles)
{
    CELL next_cell_stat;
    long merge_count;
    for (int i = 0; i < nfiles; i++) {
        for (int t = 1; t < nprocs; t++) {
            Rast_rewind_cell_stats(thread_statf[t] + i);
            while (Rast_next_cell_stat(&next_cell_stat, &merge_count,
                                       thread_statf[t] + i)) {
                if (next_cell_stat &&
                    !Rast_find_cell_stat(next_cell_stat, &merge_count,
                                         thread_statf[0] + i)) {
                    Rast_update_cell_stats(&next_cell_stat, 1,
                                           thread_statf[0] + i);
                }
            }
        }
    }
}

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
/*
 * creates new category and color structures from the patching
 * files category and color files
 *
 * the first patch file is used as the basis. Its cats and colr
 * are read into the final cats/colr structures.
 * Then the other patching layers cats/colr are added to the
 * final cats/colr only if these patching layers actually
 * contributed new categories to the final result
 */

int support(char **names, struct Cell_stats *statf, int nfiles,
            struct Categories *cats, int *cats_ok, struct Colors *colr,
            int *colr_ok, RASTER_MAP_TYPE out_type)
{
    int i;
    struct Categories pcats;
    struct Colors pcolr;
    CELL n;
    long count;
    int red, grn, blu;
    int do_cats, do_colr;

    *cats_ok = 1;
    *colr_ok = 1;
    if (Rast_read_cats(names[0], "", cats) < 0)
        *cats_ok = 0;
    G_suppress_warnings(1);
    if (Rast_read_colors(names[0], "", colr) < 0)
        *colr_ok = 0;
    G_suppress_warnings(0);

    if (*cats_ok == 0 && *colr_ok == 0)
        return 0;

    for (i = 1; i < nfiles; i++) {
        do_cats = *cats_ok && (Rast_read_cats(names[i], "", &pcats) >= 0);
        G_suppress_warnings(1);
        do_colr = *colr_ok && (Rast_read_colors(names[i], "", &pcolr) >= 0);
        G_suppress_warnings(0);
        if (!do_cats && !do_colr)
            continue;
        if (out_type == CELL_TYPE) {
            Rast_rewind_cell_stats(statf + i);
            while (Rast_next_cell_stat(&n, &count, statf + i))
                if (n && !Rast_find_cell_stat(n, &count, statf)) {
                    if (do_cats) {
                        Rast_update_cell_stats(&n, 1, statf);
                        Rast_set_c_cat(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
>>>>>>> osgeo-main
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
>>>>>>> osgeo-main
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
>>>>>>> osgeo-main
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
>>>>>>> osgeo-main
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
>>>>>>> osgeo-main
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
>>>>>>> osgeo-main
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
>>>>>>> osgeo-main
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
>>>>>>> osgeo-main
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
>>>>>>> osgeo-main
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
>>>>>>> osgeo-main
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
>>>>>>> osgeo-main
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
>>>>>>> osgeo-main
                            &n, &n, Rast_get_c_cat((CELL *) &n, &pcats), cats);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
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
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
                            &n, &n, Rast_get_c_cat((CELL *) &n, &pcats), cats);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
                            &n, &n, Rast_get_c_cat((CELL *) &n, &pcats), cats);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
=======
                            &n, &n, Rast_get_c_cat((CELL *) &n, &pcats), cats);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
=======
                            &n, &n, Rast_get_c_cat((CELL *)&n, &pcats), cats);
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
                    }
                    if (do_colr) {
                        Rast_get_c_color(&n, &red, &grn, &blu, &pcolr);
                        Rast_set_c_color(n, red, grn, blu, colr);
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        }
        else {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        }
        else {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
        }
        else {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
        }
        else {
=======
>>>>>>> osgeo-main
=======
        }
        else {
=======
>>>>>>> osgeo-main
=======
        }
        else {
=======
>>>>>>> osgeo-main
=======
        }
        else {
=======
>>>>>>> osgeo-main
=======
        }
        else {
=======
>>>>>>> osgeo-main
=======
        }
        else {
=======
>>>>>>> osgeo-main
=======
        }
        else {
=======
>>>>>>> osgeo-main
=======
        }
        else {
=======
>>>>>>> osgeo-main
=======
        }
        else {
=======
>>>>>>> osgeo-main
=======
        }
        else {
=======
>>>>>>> osgeo-main
=======
        }
        else {
=======
>>>>>>> osgeo-main
=======
        }
        else {
=======
>>>>>>> osgeo-main
        } else {
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
        }
        else {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        }
        else {
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
        }
        else {
=======
        } else {
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
        }
        else {
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
        }
        else {
=======
        } else {
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        }
        else {
=======
        } else {
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
            /* the color would be the color of the first map,
             * possibly not covering the range of the other maps */
            *colr_ok = 0;
        }

        if (do_cats)
            Rast_free_cats(&pcats);
        if (do_colr)
            /* otherwise this memory is used in colr pointer */
            Rast_free_colors(&pcolr);
    }
    return 1;
}
