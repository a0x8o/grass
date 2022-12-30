#include <grass/config.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <grass/lidar.h>

/*----------------------------------------------------------------------------------------*/
void P_zero_dim(struct Reg_dimens *dim)
{
    dim->edge_h = 0.0;
    dim->edge_v = 0.0;
    dim->overlap = 0.0;
    dim->sn_size = 0.0;
    dim->ew_size = 0.0;
    return;
}

/*----------------------------------------------------------------------------------------*/
/*
   --------------------------------------------
   |            Elaboration region            |
   |   ------------------------------------   |
   |   |          General region          |   |
   |   |   ----------------------------   |   |
   |   |   |                          |   |   |
   |   |   |                          |   |   |
   |   |   |                          |   |   |
   |   |   |      Overlap region      |   |   |
   |   |   |                          |   |   |
   |   |   |                          |   |   |
   |   |   |                          |   |   |
   |   |   ----------------------------   |   |
   |   |                                  |   |
   |   ------------------------------------   |
   |                                          |
   --------------------------------------------

   The terminology is misleading:
   The Overlap region does NOT overlap with neighbouring segments,
   but the Elaboration and General region do overlap

   Elaboration is used for interpolation
   Interpolated points in Elaboration but outside General are discarded
   Interpolated points in General but outside Overlap are weighed by
   their distance to Overlap and summed up
   Interpolated points in Overlap are taken as they are

   The buffer zones Elaboration - General and General - Overlap must be
   large enough to avoid artifacts
 */

int P_set_regions(struct Cell_head *Elaboration, struct bound_box *General,
                  struct bound_box *Overlap, struct Reg_dimens dim, int type)
{
    /* Set the Elaboration, General, and Overlap region limits
     * Returns 0 on success; -1 on failure*/
    struct Cell_head orig;

    G_get_window(&orig);

    switch (type) {
    case GENERAL_ROW: /* General case N-S direction */
        Elaboration->north =
            Elaboration->south + dim.overlap + (2 * dim.edge_h);
        Elaboration->south = Elaboration->north - dim.sn_size;
        General->N = Elaboration->north - dim.edge_h;
        General->S = Elaboration->south + dim.edge_h;
        Overlap->N = General->N - dim.overlap;
        Overlap->S = General->S + dim.overlap;
        return 0;

    case GENERAL_COLUMN: /* General case E-W direction */
        Elaboration->west = Elaboration->east - dim.overlap - (2 * dim.edge_v);
        Elaboration->east = Elaboration->west + dim.ew_size;
        General->W = Elaboration->west + dim.edge_v;
        General->E = Elaboration->east - dim.edge_v;
        Overlap->W = General->W + dim.overlap;
        Overlap->E = General->E - dim.overlap;
        return 0;

    case FIRST_ROW: /* Just started with first row */
        Elaboration->north = orig.north + 2 * dim.edge_h;
        Elaboration->south = Elaboration->north - dim.sn_size;
        General->N = orig.north;
        General->S = Elaboration->south + dim.edge_h;
        Overlap->N = General->N;
        Overlap->S = General->S + dim.overlap;
        return 0;

    case LAST_ROW: /* Reached last row */
        Elaboration->south = orig.south - 2 * dim.edge_h;
        General->S = orig.south;
        Overlap->S = General->S;
        return 0;

    case FIRST_COLUMN: /* Just started with first column */
        Elaboration->west = orig.west - 2 * dim.edge_v;
        Elaboration->east = Elaboration->west + dim.ew_size;
        General->W = orig.west;
        General->E = Elaboration->east - dim.edge_v;
        Overlap->W = General->W;
        Overlap->E = General->E - dim.overlap;
        return 0;

    case LAST_COLUMN: /* Reached last column */
        Elaboration->east = orig.east + 2 * dim.edge_v;
        General->E = orig.east;
        Overlap->E = General->E;
        return 0;
    }

    return -1;
}

/*----------------------------------------------------------------------------------------*/
int P_set_dim(struct Reg_dimens *dim, double pe, double pn, int *nsplx,
              int *nsply)
{
    int total_splines, edge_splines, n_windows;
    int lastsplines, lastsplines_min, lastsplines_max;
    double E_extension, N_extension, edgeE, edgeN;
    struct Cell_head orig;
    int ret = 0;

    G_get_window(&orig);

    E_extension = orig.east - orig.west;
    N_extension = orig.north - orig.south;
    dim->ew_size = *nsplx * pe;
    dim->sn_size = *nsply * pn;
    edgeE = dim->ew_size - dim->overlap - 2 * dim->edge_v;
    edgeN = dim->sn_size - dim->overlap - 2 * dim->edge_h;

    /* number of moving windows: E_extension / edgeE */
    /* remaining steps: total steps - (floor(E_extension / edgeE) * E_extension)
     * / passoE */
    /* remaining steps must be larger than edge_v + overlap + half of overlap
     * window */
    total_splines = ceil(E_extension / pe);
    edge_splines = edgeE / pe;
    n_windows = E_extension / edgeE; /* without last one */
    if (n_windows > 0) {
        /* min size of the last overlap window = half of current overlap window
         */
        /* max size of the last overlap window = elaboration - 3 * edge -
         * overlap */
        lastsplines_min =
            ceil((dim->ew_size / 2.0 - (dim->edge_v + dim->overlap)) / pe);
        lastsplines_max =
            ceil((dim->ew_size - 3 * dim->edge_v - dim->overlap) / pe);
        lastsplines = total_splines - edge_splines * n_windows;
        while (lastsplines > lastsplines_max || lastsplines < lastsplines_min) {
            *nsplx -= 1;
            dim->ew_size = *nsplx * pe;
            edgeE = dim->ew_size - dim->overlap - 2 * dim->edge_v;

            edge_splines = edgeE / pe;
            n_windows = E_extension / edgeE; /* without last one */
            lastsplines = total_splines - edge_splines * n_windows;
            if (ret == 0)
                ret = 1;
        }
    }

    total_splines = ceil(N_extension / pn);
    edge_splines = edgeN / pn;
    n_windows = N_extension / edgeN; /* without last one */
    if (n_windows > 0) {
        /* min size of the last overlap window = half of current overlap window
         */
        /* max size of the last overlap window = elaboration - 3 * edge -
         * overlap */
        lastsplines_min =
            ceil((dim->sn_size / 2.0 - (dim->edge_h + dim->overlap)) / pn);
        lastsplines_max =
            ceil((dim->sn_size - 3 * dim->edge_h - dim->overlap) / pn);
        lastsplines = total_splines - edge_splines * n_windows;
        while (lastsplines > lastsplines_max || lastsplines < lastsplines_min) {
            *nsply -= 1;
            dim->sn_size = *nsply * pn;
            edgeN = dim->sn_size - dim->overlap - 2 * dim->edge_h;

            edge_splines = edgeN / pn;
            n_windows = N_extension / edgeN; /* without last one */
            lastsplines = total_splines - edge_splines * n_windows;
            if (ret < 2)
                ret += 2;
        }
    }

    return ret;
}

/*----------------------------------------------------------------------------------------*/
int P_get_edge(int interpolator, struct Reg_dimens *dim, double pe, double pn)
{
    /* Set the edge regions dimension
     * Returns 1 on success of bilinear; 2 on success of bicubic, 0 on failure
     */
    if (interpolator == P_BILINEAR) {
        /* in case of edge artifacts, increase as multiples of 3 */
        dim->edge_v = 9 * pe;
        dim->edge_h = 9 * pn;
        return 1;
    }
    else if (interpolator == P_BICUBIC) {
        /* in case of edge artifacts, increase as multiples of 4 */
        dim->edge_v = 12 * pe; /*3 */
        dim->edge_h = 12 * pn;
        return 2;
    }
    else
        return 0; /* The interpolator is neither bilinear nor bicubic!! */
}

/*----------------------------------------------------------------------------------------*/
int P_get_BandWidth(int interpolator, int nsplines)
{
    /* Returns the interpolation matrixes BandWidth dimension */

    if (interpolator == P_BILINEAR) {
        return (2 * nsplines + 1);
    }
    else {
        return (4 * nsplines + 3);
    }
}

/*----------------------------------------------------------------------------------------*/
double P_Mean_Calc(struct Cell_head *Elaboration, struct Point *obs,
                   int npoints)
{
    int i, mean_count = 0;
    double mean = 0.0;
    struct bound_box mean_box;

    Vect_region_box(Elaboration, &mean_box);
    mean_box.W -= CONTOUR;
    mean_box.E += CONTOUR;
    mean_box.N += CONTOUR;
    mean_box.S -= CONTOUR;

    for (i = 0; i < npoints; i++) { /*  */
        if (Vect_point_in_box(obs[i].coordX, obs[i].coordY, obs[i].coordZ,
                              &mean_box)) {
            mean_count++;
            mean += obs[i].coordZ;
        }
    }
    if (mean_count == 0)
        mean = .0;
    else
        mean /= (double)mean_count;

    return mean;
}

double P_estimate_splinestep(struct Map_info *Map, double *dens, double *dist)
{
    int type, npoints = 0;
    double xmin = 0, xmax = 0, ymin = 0, ymax = 0;
    double x, y, z;
    struct line_pnts *points;
    struct line_cats *categories;
    struct bound_box region_box;
    struct Cell_head orig;

    G_get_set_window(&orig);
    Vect_region_box(&orig, &region_box);

    points = Vect_new_line_struct();
    categories = Vect_new_cats_struct();

    Vect_rewind(Map);
    while ((type = Vect_read_next_line(Map, points, categories)) > 0) {
        if (!(type & GV_POINT))
            continue;

        x = points->x[0];
        y = points->y[0];
        if (points->z != NULL)
            z = points->z[0];
        else
            z = 0.0;

        /* only use points in current region */
        if (Vect_point_in_box(x, y, z, &region_box)) {
            npoints++;

            if (npoints > 1) {
                if (xmin > x)
                    xmin = x;
                else if (xmax < x)
                    xmax = x;
                if (ymin > y)
                    ymin = y;
                else if (ymax < y)
                    ymax = y;
            }
            else {
                xmin = xmax = x;
                ymin = ymax = y;
            }
        }
    }
    Vect_destroy_cats_struct(categories);
    Vect_destroy_line_struct(points);

    if (npoints > 0) {
        /* estimated average distance between points in map units */
        *dist = sqrt(((xmax - xmin) * (ymax - ymin)) / npoints);
        /* estimated point density as number of points per square map unit */
        *dens = npoints / ((xmax - xmin) * (ymax - ymin));
        return 0;
    }
    else {
        return -1;
    }
}

struct Point *P_Read_Vector_Region_Map(struct Map_info *Map,
                                       struct Cell_head *Elaboration,
                                       int *num_points, int dim_vect, int layer)
{
    int line_num, pippo, npoints, cat, type;
    double x, y, z;
    struct Point *obs;
    struct line_pnts *points;
    struct line_cats *categories;
    struct bound_box elaboration_box;

    pippo = dim_vect;
    obs = (struct Point *)G_calloc(pippo, sizeof(struct Point));

    points = Vect_new_line_struct();
    categories = Vect_new_cats_struct();

    /* Reading points inside elaboration zone */
    Vect_region_box(Elaboration, &elaboration_box);

    npoints = 0;
    line_num = 0;

    Vect_rewind(Map);
    while ((type = Vect_read_next_line(Map, points, categories)) > 0) {

        if (!(type & GV_POINT))
            continue;

        line_num++;

        x = points->x[0];
        y = points->y[0];
        if (points->z != NULL)
            z = points->z[0];
        else
            z = 0.0;

        /* Reading and storing points only if in elaboration_reg */
        if (Vect_point_in_box(x, y, z, &elaboration_box)) {
            npoints++;
            if (npoints >= pippo) {
                pippo += dim_vect;
                obs = (struct Point *)G_realloc(
                    (void *)obs, (signed int)pippo * sizeof(struct Point));
            }

            /* Storing observation vector */
            obs[npoints - 1].coordX = x;
            obs[npoints - 1].coordY = y;
            obs[npoints - 1].coordZ = z;
            obs[npoints - 1].lineID =
                line_num; /* Storing also the line's number */

            Vect_cat_get(categories, layer, &cat);
            obs[npoints - 1].cat = cat;
        }
    }
    Vect_destroy_line_struct(points);
    Vect_destroy_cats_struct(categories);

    *num_points = npoints;
    return obs;
}

struct Point *P_Read_Raster_Region_Map(SEGMENT *in_seg,
                                       struct Cell_head *Elaboration,
                                       struct Cell_head *Original,
                                       int *num_points, int dim_vect)
{
    int col, row, startcol, endcol, startrow, endrow, nrows, ncols;
    int pippo, npoints;
    double x, y, z;
    struct Point *obs;
    struct bound_box elaboration_box;

    pippo = dim_vect;
    obs = (struct Point *)G_calloc(pippo, sizeof(struct Point));

    /* Reading points inside elaboration zone */
    Vect_region_box(Elaboration, &elaboration_box);

    npoints = 0;
    nrows = Original->rows;
    ncols = Original->cols;

    if (Original->north > Elaboration->north)
        startrow =
            (Original->north - Elaboration->north) / Original->ns_res - 1;
    else
        startrow = 0;
    if (Original->north > Elaboration->south) {
        endrow = (Original->north - Elaboration->south) / Original->ns_res + 1;
        if (endrow > nrows)
            endrow = nrows;
    }
    else
        endrow = nrows;
    if (Elaboration->west > Original->west)
        startcol = (Elaboration->west - Original->west) / Original->ew_res - 1;
    else
        startcol = 0;
    if (Elaboration->east > Original->west) {
        endcol = (Elaboration->east - Original->west) / Original->ew_res + 1;
        if (endcol > ncols)
            endcol = ncols;
    }
    else
        endcol = ncols;

    for (row = startrow; row < endrow; row++) {
        for (col = startcol; col < endcol; col++) {

            Segment_get(in_seg, &z, row, col);

            if (!Rast_is_d_null_value(&z)) {

                x = Rast_col_to_easting((double)(col) + 0.5, Original);
                y = Rast_row_to_northing((double)(row) + 0.5, Original);

                if (Vect_point_in_box(x, y, 0, &elaboration_box)) {
                    npoints++;
                    if (npoints >= pippo) {
                        pippo += dim_vect;
                        obs = (struct Point *)G_realloc(
                            (void *)obs,
                            (signed int)pippo * sizeof(struct Point));
                    }

                    /* Storing observation vector */
                    obs[npoints - 1].coordX = x;
                    obs[npoints - 1].coordY = y;
                    obs[npoints - 1].coordZ = z;
                }
            }
        }
    }

    *num_points = npoints;
    return obs;
}

/*------------------------------------------------------------------------------------------------*/
int P_Create_Aux2_Table(dbDriver *driver, char *tab_name)
{
    dbTable *auxiliar_tab;
    dbColumn *column;

    auxiliar_tab = db_alloc_table(2);
    db_set_table_name(auxiliar_tab, tab_name);
    db_set_table_description(auxiliar_tab, "Intermediate interpolated values");

    column = db_get_table_column(auxiliar_tab, 0);
    db_set_column_name(column, "ID");
    db_set_column_sqltype(column, DB_SQL_TYPE_INTEGER);

    column = db_get_table_column(auxiliar_tab, 1);
    db_set_column_name(column, "Interp");
    db_set_column_sqltype(column, DB_SQL_TYPE_REAL);

    if (db_create_table(driver, auxiliar_tab) == DB_OK) {
        G_debug(1, _("<%s> created in database."), tab_name);
        return TRUE;
    }
    else
        G_warning(_("<%s> has not been created in database."), tab_name);

    return FALSE;
}

/*------------------------------------------------------------------------------------------------*/
int P_Create_Aux4_Table(dbDriver *driver, char *tab_name)
{
    dbTable *auxiliar_tab;
    dbColumn *column;

    auxiliar_tab = db_alloc_table(4);
    db_set_table_name(auxiliar_tab, tab_name);
    db_set_table_description(auxiliar_tab, "Intermediate interpolated values");

    column = db_get_table_column(auxiliar_tab, 0);
    db_set_column_name(column, "ID");
    db_set_column_sqltype(column, DB_SQL_TYPE_INTEGER);

    column = db_get_table_column(auxiliar_tab, 1);
    db_set_column_name(column, "Interp");
    db_set_column_sqltype(column, DB_SQL_TYPE_REAL);

    column = db_get_table_column(auxiliar_tab, 2);
    db_set_column_name(column, "X");
    db_set_column_sqltype(column, DB_SQL_TYPE_DOUBLE_PRECISION);

    column = db_get_table_column(auxiliar_tab, 3);
    db_set_column_name(column, "Y");
    db_set_column_sqltype(column, DB_SQL_TYPE_DOUBLE_PRECISION);

    if (db_create_table(driver, auxiliar_tab) == DB_OK) {
        G_debug(1, _("<%s> created in database."), tab_name);
        return TRUE;
    }
    else
        G_warning(_("<%s> has not been created in database."), tab_name);

    return FALSE;
}

/*------------------------------------------------------------------------------------------------*/
int P_Drop_Aux_Table(dbDriver *driver, char *tab_name)
{
    dbString drop;

    db_init_string(&drop);
    db_append_string(&drop, "drop table ");
    db_append_string(&drop, tab_name);
    return db_execute_immediate(driver, &drop);
}

/*---------------------------------------------------------------------------------------*/
void P_Aux_to_Raster(double **matrix, int fd)
{
    int ncols, col, nrows, row;
    void *ptr, *raster;

    nrows = Rast_window_rows();
    ncols = Rast_window_cols();

    raster = Rast_allocate_buf(DCELL_TYPE);

    for (row = 0; row < nrows; row++) {
        G_percent(row, nrows, 2);

        Rast_set_d_null_value(raster, ncols);

        for (col = 0, ptr = raster; col < ncols;
             col++, ptr = G_incr_void_ptr(ptr, Rast_cell_size(DCELL_TYPE))) {
            Rast_set_d_value(ptr, (DCELL)(matrix[row][col]), DCELL_TYPE);
        }
        Rast_put_d_row(fd, raster);
    }
    G_percent(row, nrows, 2);
}

/*------------------------------------------------------------------------------------------------*/
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void P_Aux_to_Vector(struct Map_info *Map, struct Map_info *Out,
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
void P_Aux_to_Vector(struct Map_info *Map, struct Map_info *Out,
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
void P_Aux_to_Vector(struct Map_info *Map UNUSED, struct Map_info *Out,
>>>>>>> osgeo-main
                     dbDriver *driver, char *tab_name)
{

    int more, type;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
void P_Aux_to_Vector(struct Map_info *Map, struct Map_info *Out,
                     dbDriver *driver, char *tab_name)
{

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
    int more, type, count = 0;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
void P_Aux_to_Vector(struct Map_info *Map, struct Map_info *Out,
                     dbDriver *driver, char *tab_name)
{

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
    int more, type, count = 0;
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
    int more, type;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
=======
    int more, type;
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
void P_Aux_to_Vector(struct Map_info *Map, struct Map_info *Out,
                     dbDriver *driver, char *tab_name)
{

>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
    int more, type, count = 0;
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
    int more, type, count = 0;
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    int more, type;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
=======
    int more, type;
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
    int more, type, count = 0;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
    int more, type, count = 0;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int more, type;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    int more, type, count = 0;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
    int more, type, count = 0;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int more, type;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    int more, type, count = 0;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
    int more, type, count = 0;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int more, type;
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
=======
>>>>>>> osgeo-main
=======
    int more, type, count = 0;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
    int more, type, count = 0;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int more, type;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
void P_Aux_to_Vector(struct Map_info *Map, struct Map_info *Out,
                     dbDriver *driver, char *tab_name)
{

<<<<<<< HEAD
    int more, type, count = 0;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
void P_Aux_to_Vector(struct Map_info *Map, struct Map_info *Out,
                     dbDriver *driver, char *tab_name)
{

<<<<<<< HEAD
    int more, type, count = 0;
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int more, type;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
=======
    int more, type;
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
    int more, type, count = 0;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
    int more, type, count = 0;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    int more, type;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
    int more, type, count = 0;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int more, type, count = 0;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    int more, type;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
    int more, type, count = 0;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int more, type, count = 0;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    int more, type;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
    int more, type, count = 0;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    int more, type, count = 0;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    int more, type;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
    int more, type, count = 0;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int more, type, count = 0;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
    double coordX, coordY, coordZ;

    struct line_pnts *point;
    struct line_cats *cat;
    dbTable *table;
    dbColumn *column;
    dbValue *value;
    dbCursor cursor;
    dbString sql;

    char buf[1024];

    point = Vect_new_line_struct();
    cat = Vect_new_cats_struct();

    db_init_string(&sql);
    db_zero_string(&sql);

    sprintf(buf, "select ID, X, Y, sum(Interp) from %s group by ID, X, Y",
            tab_name);

    db_append_string(&sql, buf);
    db_open_select_cursor(driver, &sql, &cursor, DB_SEQUENTIAL);

    while (db_fetch(&cursor, DB_NEXT, &more) == DB_OK && more) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
        count++;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        count++;
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
        count++;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
        count++;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
        count++;
=======
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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
        count++;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
        count++;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
        count++;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
=======
>>>>>>> osgeo-main
=======
=======
        count++;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
        count++;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
        count++;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
        count++;
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
        count++;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        count++;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
=======
        count++;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
=======
        count++;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
        table = db_get_cursor_table(&cursor);

        column = db_get_table_column(table, 0);
        type = db_sqltype_to_Ctype(db_get_column_sqltype(column));
        if (type == DB_C_TYPE_INT)
            value = db_get_column_value(column);
        else
            continue;

        column = db_get_table_column(table, 1);
        type = db_sqltype_to_Ctype(db_get_column_sqltype(column));
        if (type == DB_C_TYPE_DOUBLE)
            value = db_get_column_value(column);
        else
            continue;
        coordZ = db_get_value_double(value);

        column = db_get_table_column(table, 2);
        type = db_sqltype_to_Ctype(db_get_column_sqltype(column));
        if (type == DB_C_TYPE_DOUBLE)
            value = db_get_column_value(column);
        else
            continue;
        coordX = db_get_value_double(value);

        column = db_get_table_column(table, 3);
        type = db_sqltype_to_Ctype(db_get_column_sqltype(column));
        if (type == DB_C_TYPE_DOUBLE)
            value = db_get_column_value(column);
        else
            continue;
        coordY = db_get_value_double(value);

        Vect_copy_xyz_to_pnts(point, &coordX, &coordY, &coordZ, 1);
        Vect_reset_cats(cat);
        Vect_cat_set(cat, 1, 1);
        Vect_write_line(Out, GV_POINT, point, cat);
    }
    return;
}

/*! DEFINITION OF THE SUBZONES

   5: inside Overlap region
   all others: inside General region but outside Overlap region

   ---------------------------------
   | |       | |       | |       | |
   ---------------------------------
   | |       | |       | |       | |
   | |       | |       | |       | |
   | |       | |       | |       | |
   ---------------------------------
   | |       |4|   3   |3|       | |
   ---------------------------------
   | |       | |       | |       | |
   | |       |2|   5   |1|       | |
   | |       | |       | |       | |
   ---------------------------------
   | |       |2|   1   |1|       | |
   ---------------------------------
   | |       | |       | |       | |
   | |       | |       | |       | |
   | |       | |       | |       | |
   ---------------------------------
   | |       | |       | |       | |
   ---------------------------------
 */
