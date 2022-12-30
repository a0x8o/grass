#include <inttypes.h>
#include <stdlib.h>
#include <math.h>
#include <grass/raster.h>
#include <grass/glocale.h>
#include "local_proto.h"

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
#define GET_PARENT(c) ((((GW_LARGE_INT)(c) - 2) >> 3) + 1)
=======
#define GET_PARENT(c) ((((GW_LARGE_INT)(c)-2) >> 3) + 1)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
#define GET_PARENT(c) ((((GW_LARGE_INT)(c)-2) >> 3) + 1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
#define GET_PARENT(c) ((((GW_LARGE_INT)(c)-2) >> 3) + 1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
#define GET_CHILD(p)  (((GW_LARGE_INT)(p) << 3) - 6)

HEAP_PNT heap_drop(void);
static double get_slope(CELL, CELL, double);

int do_astar(void)
{
    int r, c, r_nbr, c_nbr, ct_dir;
    GW_LARGE_INT first_cum, count;
    int nextdr[8] = {1, -1, 0, 0, -1, 1, 1, -1};
    int nextdc[8] = {0, 0, -1, 1, 1, -1, 1, -1};
    CELL ele_val, ele_up, ele_nbr[8];
    WAT_ALT wa;
    ASP_FLAG af;
    char is_in_list, is_worked;
    HEAP_PNT heap_p;

    /* sides
     * |7|1|4|
     * |2| |3|
     * |5|0|6|
     */
    int nbr_ew[8] = {0, 1, 2, 3, 1, 0, 0, 1};
    int nbr_ns[8] = {0, 1, 2, 3, 3, 2, 3, 2};
    double dx, dy, dist_to_nbr[8], ew_res, ns_res;
    double slope[8];
    struct Cell_head window;
    int skip_diag;

    count = 0;

    first_cum = n_points;

    G_message(_("A* Search..."));

    Rast_get_window(&window);

    for (ct_dir = 0; ct_dir < sides; ct_dir++) {
        /* get r, c (r_nbr, c_nbr) for neighbours */
        r_nbr = nextdr[ct_dir];
        c_nbr = nextdc[ct_dir];
        /* account for rare cases when ns_res != ew_res */
        dy = abs(r_nbr) * window.ns_res;
        dx = abs(c_nbr) * window.ew_res;
        if (ct_dir < 4)
            dist_to_nbr[ct_dir] = dx + dy;
        else
            dist_to_nbr[ct_dir] = sqrt(dx * dx + dy * dy);
    }
    ew_res = window.ew_res;
    ns_res = window.ns_res;

    while (heap_size > 0) {
        G_percent(count++, n_points, 1);
        if (count > n_points)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("%" PRI_OFF_T " surplus points"), heap_size);

        if (heap_size > n_points)
            G_fatal_error(_("Too many points in heap %" PRI_OFF_T
                            ", should be %" PRI_OFF_T ""),
                          heap_size, n_points);
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("%" PRId64 " surplus points"), heap_size);

        if (heap_size > n_points)
            G_fatal_error(
                _("Too many points in heap %" PRId64 ", should be %" PRId64 ""),
                heap_size, n_points);
=======
            G_fatal_error(_("%" PRI_OFF_T " surplus points"), heap_size);

        if (heap_size > n_points)
            G_fatal_error(_("Too many points in heap %" PRI_OFF_T
                            ", should be %" PRI_OFF_T ""),
                          heap_size, n_points);
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
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))

        heap_p = heap_drop();

        r = heap_p.pnt.r;
        c = heap_p.pnt.c;

        ele_val = heap_p.ele;

        for (ct_dir = 0; ct_dir < sides; ct_dir++) {
            /* get r, c (r_nbr, c_nbr) for neighbours */
            r_nbr = r + nextdr[ct_dir];
            c_nbr = c + nextdc[ct_dir];
            slope[ct_dir] = -1;
            ele_nbr[ct_dir] = 0;
            skip_diag = 0;

            /* check that neighbour is within region */
            if (r_nbr < 0 || r_nbr >= nrows || c_nbr < 0 || c_nbr >= ncols)
                continue;

            seg_get(&aspflag, (char *)&af, r_nbr, c_nbr);
            is_in_list = FLAG_GET(af.flag, INLISTFLAG);
            is_worked = FLAG_GET(af.flag, WORKEDFLAG);
            if (!is_worked) {
                seg_get(&watalt, (char *)&wa, r_nbr, c_nbr);
                ele_nbr[ct_dir] = wa.ele;
                slope[ct_dir] =
                    get_slope(ele_val, ele_nbr[ct_dir], dist_to_nbr[ct_dir]);
            }
            /* avoid diagonal flow direction bias */
            if (!is_in_list || (!is_worked && af.asp < 0)) {
                if (ct_dir > 3 && slope[ct_dir] > 0) {
                    if (slope[nbr_ew[ct_dir]] >= 0) {
                        /* slope to ew nbr > slope to center */
                        if (slope[ct_dir] < get_slope(ele_nbr[nbr_ew[ct_dir]],
                                                      ele_nbr[ct_dir], ew_res))
                            skip_diag = 1;
                    }
                    if (!skip_diag && slope[nbr_ns[ct_dir]] >= 0) {
                        /* slope to ns nbr > slope to center */
                        if (slope[ct_dir] < get_slope(ele_nbr[nbr_ns[ct_dir]],
                                                      ele_nbr[ct_dir], ns_res))
                            skip_diag = 1;
                    }
                }
            }

            if (!skip_diag) {
                if (!is_in_list) {
                    ele_up = ele_nbr[ct_dir];
                    af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                    heap_add(r_nbr, c_nbr, ele_up);
                    FLAG_SET(af.flag, INLISTFLAG);
                    seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                }
                else if (!is_worked) {
                    if (FLAG_GET(af.flag, EDGEFLAG)) {
                        /* neighbour is edge in list, not yet worked */
                        if (af.asp < 0 && slope[ct_dir] > 0) {
                            /* adjust flow direction for edge cell */
                            af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                            seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                        }
                    }
                    else if (FLAG_GET(af.flag, DEPRFLAG)) {
                        G_debug(3, "real depression");
                        /* neighbour is inside real depression, not yet worked
                         */
                        if (af.asp == 0 && ele_val <= ele_nbr[ct_dir]) {
                            af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                            FLAG_UNSET(af.flag, DEPRFLAG);
                            seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                        }
                    }
                }
            }
        } /* end neighbours */
        /* add astar points to sorted list for flow accumulation and stream
         * extraction */
        first_cum--;
        seg_put(&astar_pts, (char *)&heap_p.pnt, 0, first_cum);
        seg_get(&aspflag, (char *)&af, r, c);
        FLAG_SET(af.flag, WORKEDFLAG);
        seg_put(&aspflag, (char *)&af, r, c);
    } /* end A* search */

=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("%" PRI_OFF_T " surplus points"), heap_size);

        if (heap_size > n_points)
            G_fatal_error(_("Too many points in heap %" PRI_OFF_T
                            ", should be %" PRI_OFF_T ""),
                          heap_size, n_points);
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("%" PRId64 " surplus points"), heap_size);

        if (heap_size > n_points)
            G_fatal_error(
                _("Too many points in heap %" PRId64 ", should be %" PRId64 ""),
                heap_size, n_points);
=======
            G_fatal_error(_("%" PRI_OFF_T " surplus points"), heap_size);

        if (heap_size > n_points)
            G_fatal_error(_("Too many points in heap %" PRI_OFF_T
                            ", should be %" PRI_OFF_T ""),
                          heap_size, n_points);
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))

        heap_p = heap_drop();

        r = heap_p.pnt.r;
        c = heap_p.pnt.c;

        ele_val = heap_p.ele;

        for (ct_dir = 0; ct_dir < sides; ct_dir++) {
            /* get r, c (r_nbr, c_nbr) for neighbours */
            r_nbr = r + nextdr[ct_dir];
            c_nbr = c + nextdc[ct_dir];
            slope[ct_dir] = -1;
            ele_nbr[ct_dir] = 0;
            skip_diag = 0;

            /* check that neighbour is within region */
            if (r_nbr < 0 || r_nbr >= nrows || c_nbr < 0 || c_nbr >= ncols)
                continue;

            seg_get(&aspflag, (char *)&af, r_nbr, c_nbr);
            is_in_list = FLAG_GET(af.flag, INLISTFLAG);
            is_worked = FLAG_GET(af.flag, WORKEDFLAG);
            if (!is_worked) {
                seg_get(&watalt, (char *)&wa, r_nbr, c_nbr);
                ele_nbr[ct_dir] = wa.ele;
                slope[ct_dir] =
                    get_slope(ele_val, ele_nbr[ct_dir], dist_to_nbr[ct_dir]);
            }
            /* avoid diagonal flow direction bias */
            if (!is_in_list || (!is_worked && af.asp < 0)) {
                if (ct_dir > 3 && slope[ct_dir] > 0) {
                    if (slope[nbr_ew[ct_dir]] >= 0) {
                        /* slope to ew nbr > slope to center */
                        if (slope[ct_dir] < get_slope(ele_nbr[nbr_ew[ct_dir]],
                                                      ele_nbr[ct_dir], ew_res))
                            skip_diag = 1;
                    }
                    if (!skip_diag && slope[nbr_ns[ct_dir]] >= 0) {
                        /* slope to ns nbr > slope to center */
                        if (slope[ct_dir] < get_slope(ele_nbr[nbr_ns[ct_dir]],
                                                      ele_nbr[ct_dir], ns_res))
                            skip_diag = 1;
                    }
                }
            }

            if (!skip_diag) {
                if (!is_in_list) {
                    ele_up = ele_nbr[ct_dir];
                    af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                    heap_add(r_nbr, c_nbr, ele_up);
                    FLAG_SET(af.flag, INLISTFLAG);
                    seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                }
                else if (!is_worked) {
                    if (FLAG_GET(af.flag, EDGEFLAG)) {
                        /* neighbour is edge in list, not yet worked */
                        if (af.asp < 0 && slope[ct_dir] > 0) {
                            /* adjust flow direction for edge cell */
                            af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                            seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                        }
                    }
                    else if (FLAG_GET(af.flag, DEPRFLAG)) {
                        G_debug(3, "real depression");
                        /* neighbour is inside real depression, not yet worked
                         */
                        if (af.asp == 0 && ele_val <= ele_nbr[ct_dir]) {
                            af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                            FLAG_UNSET(af.flag, DEPRFLAG);
                            seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                        }
                    }
                }
            }
        } /* end neighbours */
        /* add astar points to sorted list for flow accumulation and stream
         * extraction */
        first_cum--;
        seg_put(&astar_pts, (char *)&heap_p.pnt, 0, first_cum);
        seg_get(&aspflag, (char *)&af, r, c);
        FLAG_SET(af.flag, WORKEDFLAG);
        seg_put(&aspflag, (char *)&af, r, c);
    } /* end A* search */

>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("%" PRId64 " surplus points"), heap_size);

        if (heap_size > n_points)
            G_fatal_error(
                _("Too many points in heap %" PRId64 ", should be %" PRId64 ""),
                heap_size, n_points);
=======
            G_fatal_error(_("%" PRI_OFF_T " surplus points"), heap_size);

        if (heap_size > n_points)
            G_fatal_error(_("Too many points in heap %" PRI_OFF_T
                            ", should be %" PRI_OFF_T ""),
                          heap_size, n_points);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

        heap_p = heap_drop();

        r = heap_p.pnt.r;
        c = heap_p.pnt.c;

        ele_val = heap_p.ele;

        for (ct_dir = 0; ct_dir < sides; ct_dir++) {
            /* get r, c (r_nbr, c_nbr) for neighbours */
            r_nbr = r + nextdr[ct_dir];
            c_nbr = c + nextdc[ct_dir];
            slope[ct_dir] = -1;
            ele_nbr[ct_dir] = 0;
            skip_diag = 0;

            /* check that neighbour is within region */
            if (r_nbr < 0 || r_nbr >= nrows || c_nbr < 0 || c_nbr >= ncols)
                continue;

            seg_get(&aspflag, (char *)&af, r_nbr, c_nbr);
            is_in_list = FLAG_GET(af.flag, INLISTFLAG);
            is_worked = FLAG_GET(af.flag, WORKEDFLAG);
            if (!is_worked) {
                seg_get(&watalt, (char *)&wa, r_nbr, c_nbr);
                ele_nbr[ct_dir] = wa.ele;
                slope[ct_dir] =
                    get_slope(ele_val, ele_nbr[ct_dir], dist_to_nbr[ct_dir]);
            }
            /* avoid diagonal flow direction bias */
            if (!is_in_list || (!is_worked && af.asp < 0)) {
                if (ct_dir > 3 && slope[ct_dir] > 0) {
                    if (slope[nbr_ew[ct_dir]] >= 0) {
                        /* slope to ew nbr > slope to center */
                        if (slope[ct_dir] < get_slope(ele_nbr[nbr_ew[ct_dir]],
                                                      ele_nbr[ct_dir], ew_res))
                            skip_diag = 1;
                    }
                    if (!skip_diag && slope[nbr_ns[ct_dir]] >= 0) {
                        /* slope to ns nbr > slope to center */
                        if (slope[ct_dir] < get_slope(ele_nbr[nbr_ns[ct_dir]],
                                                      ele_nbr[ct_dir], ns_res))
                            skip_diag = 1;
                    }
                }
            }

            if (!skip_diag) {
                if (!is_in_list) {
                    ele_up = ele_nbr[ct_dir];
                    af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                    heap_add(r_nbr, c_nbr, ele_up);
                    FLAG_SET(af.flag, INLISTFLAG);
                    seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                }
                else if (!is_worked) {
                    if (FLAG_GET(af.flag, EDGEFLAG)) {
                        /* neighbour is edge in list, not yet worked */
                        if (af.asp < 0 && slope[ct_dir] > 0) {
                            /* adjust flow direction for edge cell */
                            af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                            seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                        }
                    }
                    else if (FLAG_GET(af.flag, DEPRFLAG)) {
                        G_debug(3, "real depression");
                        /* neighbour is inside real depression, not yet worked
                         */
                        if (af.asp == 0 && ele_val <= ele_nbr[ct_dir]) {
                            af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                            FLAG_UNSET(af.flag, DEPRFLAG);
                            seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                        }
                    }
                }
            }
        } /* end neighbours */
        /* add astar points to sorted list for flow accumulation and stream
         * extraction */
        first_cum--;
        seg_put(&astar_pts, (char *)&heap_p.pnt, 0, first_cum);
        seg_get(&aspflag, (char *)&af, r, c);
        FLAG_SET(af.flag, WORKEDFLAG);
        seg_put(&aspflag, (char *)&af, r, c);
    } /* end A* search */

=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("%" PRI_OFF_T " surplus points"), heap_size);

        if (heap_size > n_points)
            G_fatal_error(_("Too many points in heap %" PRI_OFF_T
                            ", should be %" PRI_OFF_T ""),
                          heap_size, n_points);

        heap_p = heap_drop();

        r = heap_p.pnt.r;
        c = heap_p.pnt.c;

        ele_val = heap_p.ele;

        for (ct_dir = 0; ct_dir < sides; ct_dir++) {
            /* get r, c (r_nbr, c_nbr) for neighbours */
            r_nbr = r + nextdr[ct_dir];
            c_nbr = c + nextdc[ct_dir];
            slope[ct_dir] = -1;
            ele_nbr[ct_dir] = 0;
            skip_diag = 0;

            /* check that neighbour is within region */
            if (r_nbr < 0 || r_nbr >= nrows || c_nbr < 0 || c_nbr >= ncols)
                continue;

            seg_get(&aspflag, (char *)&af, r_nbr, c_nbr);
            is_in_list = FLAG_GET(af.flag, INLISTFLAG);
            is_worked = FLAG_GET(af.flag, WORKEDFLAG);
            if (!is_worked) {
                seg_get(&watalt, (char *)&wa, r_nbr, c_nbr);
                ele_nbr[ct_dir] = wa.ele;
                slope[ct_dir] =
                    get_slope(ele_val, ele_nbr[ct_dir], dist_to_nbr[ct_dir]);
            }
            /* avoid diagonal flow direction bias */
            if (!is_in_list || (!is_worked && af.asp < 0)) {
                if (ct_dir > 3 && slope[ct_dir] > 0) {
                    if (slope[nbr_ew[ct_dir]] >= 0) {
                        /* slope to ew nbr > slope to center */
                        if (slope[ct_dir] < get_slope(ele_nbr[nbr_ew[ct_dir]],
                                                      ele_nbr[ct_dir], ew_res))
                            skip_diag = 1;
                    }
                    if (!skip_diag && slope[nbr_ns[ct_dir]] >= 0) {
                        /* slope to ns nbr > slope to center */
                        if (slope[ct_dir] < get_slope(ele_nbr[nbr_ns[ct_dir]],
                                                      ele_nbr[ct_dir], ns_res))
                            skip_diag = 1;
                    }
                }
            }

            if (!skip_diag) {
                if (!is_in_list) {
                    ele_up = ele_nbr[ct_dir];
                    af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                    heap_add(r_nbr, c_nbr, ele_up);
                    FLAG_SET(af.flag, INLISTFLAG);
                    seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                }
                else if (!is_worked) {
                    if (FLAG_GET(af.flag, EDGEFLAG)) {
                        /* neighbour is edge in list, not yet worked */
                        if (af.asp < 0 && slope[ct_dir] > 0) {
                            /* adjust flow direction for edge cell */
                            af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                            seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                        }
                    }
                    else if (FLAG_GET(af.flag, DEPRFLAG)) {
                        G_debug(3, "real depression");
                        /* neighbour is inside real depression, not yet worked
                         */
                        if (af.asp == 0 && ele_val <= ele_nbr[ct_dir]) {
                            af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                            FLAG_UNSET(af.flag, DEPRFLAG);
                            seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                        }
                    }
                }
            }
        } /* end neighbours */
        /* add astar points to sorted list for flow accumulation and stream
         * extraction */
        first_cum--;
        seg_put(&astar_pts, (char *)&heap_p.pnt, 0, first_cum);
        seg_get(&aspflag, (char *)&af, r, c);
        FLAG_SET(af.flag, WORKEDFLAG);
        seg_put(&aspflag, (char *)&af, r, c);
    } /* end A* search */

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
            G_fatal_error(_("%" PRI_OFF_T " surplus points"), heap_size);

        if (heap_size > n_points)
            G_fatal_error(_("Too many points in heap %" PRI_OFF_T
                            ", should be %" PRI_OFF_T ""),
                          heap_size, n_points);

        heap_p = heap_drop();

        r = heap_p.pnt.r;
        c = heap_p.pnt.c;

        ele_val = heap_p.ele;

        for (ct_dir = 0; ct_dir < sides; ct_dir++) {
            /* get r, c (r_nbr, c_nbr) for neighbours */
            r_nbr = r + nextdr[ct_dir];
            c_nbr = c + nextdc[ct_dir];
            slope[ct_dir] = -1;
            ele_nbr[ct_dir] = 0;
            skip_diag = 0;

            /* check that neighbour is within region */
            if (r_nbr < 0 || r_nbr >= nrows || c_nbr < 0 || c_nbr >= ncols)
                continue;

            seg_get(&aspflag, (char *)&af, r_nbr, c_nbr);
            is_in_list = FLAG_GET(af.flag, INLISTFLAG);
            is_worked = FLAG_GET(af.flag, WORKEDFLAG);
            if (!is_worked) {
                seg_get(&watalt, (char *)&wa, r_nbr, c_nbr);
                ele_nbr[ct_dir] = wa.ele;
                slope[ct_dir] =
                    get_slope(ele_val, ele_nbr[ct_dir], dist_to_nbr[ct_dir]);
            }
            /* avoid diagonal flow direction bias */
            if (!is_in_list || (!is_worked && af.asp < 0)) {
                if (ct_dir > 3 && slope[ct_dir] > 0) {
                    if (slope[nbr_ew[ct_dir]] >= 0) {
                        /* slope to ew nbr > slope to center */
                        if (slope[ct_dir] < get_slope(ele_nbr[nbr_ew[ct_dir]],
                                                      ele_nbr[ct_dir], ew_res))
                            skip_diag = 1;
                    }
                    if (!skip_diag && slope[nbr_ns[ct_dir]] >= 0) {
                        /* slope to ns nbr > slope to center */
                        if (slope[ct_dir] < get_slope(ele_nbr[nbr_ns[ct_dir]],
                                                      ele_nbr[ct_dir], ns_res))
                            skip_diag = 1;
                    }
                }
            }

            if (!skip_diag) {
                if (!is_in_list) {
                    ele_up = ele_nbr[ct_dir];
                    af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                    heap_add(r_nbr, c_nbr, ele_up);
                    FLAG_SET(af.flag, INLISTFLAG);
                    seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                }
                else if (!is_worked) {
                    if (FLAG_GET(af.flag, EDGEFLAG)) {
                        /* neighbour is edge in list, not yet worked */
                        if (af.asp < 0 && slope[ct_dir] > 0) {
                            /* adjust flow direction for edge cell */
                            af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                            seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                        }
                    }
                    else if (FLAG_GET(af.flag, DEPRFLAG)) {
                        G_debug(3, "real depression");
                        /* neighbour is inside real depression, not yet worked
                         */
                        if (af.asp == 0 && ele_val <= ele_nbr[ct_dir]) {
                            af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                            FLAG_UNSET(af.flag, DEPRFLAG);
                            seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                        }
                    }
                }
            }
        } /* end neighbours */
        /* add astar points to sorted list for flow accumulation and stream
         * extraction */
        first_cum--;
        seg_put(&astar_pts, (char *)&heap_p.pnt, 0, first_cum);
        seg_get(&aspflag, (char *)&af, r, c);
        FLAG_SET(af.flag, WORKEDFLAG);
        seg_put(&aspflag, (char *)&af, r, c);
    } /* end A* search */

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("%" PRI_OFF_T " surplus points"), heap_size);

        if (heap_size > n_points)
            G_fatal_error(_("Too many points in heap %" PRI_OFF_T
                            ", should be %" PRI_OFF_T ""),
                          heap_size, n_points);

        heap_p = heap_drop();

        r = heap_p.pnt.r;
        c = heap_p.pnt.c;

        ele_val = heap_p.ele;

        for (ct_dir = 0; ct_dir < sides; ct_dir++) {
            /* get r, c (r_nbr, c_nbr) for neighbours */
            r_nbr = r + nextdr[ct_dir];
            c_nbr = c + nextdc[ct_dir];
            slope[ct_dir] = -1;
            ele_nbr[ct_dir] = 0;
            skip_diag = 0;

            /* check that neighbour is within region */
            if (r_nbr < 0 || r_nbr >= nrows || c_nbr < 0 || c_nbr >= ncols)
                continue;

            seg_get(&aspflag, (char *)&af, r_nbr, c_nbr);
            is_in_list = FLAG_GET(af.flag, INLISTFLAG);
            is_worked = FLAG_GET(af.flag, WORKEDFLAG);
            if (!is_worked) {
                seg_get(&watalt, (char *)&wa, r_nbr, c_nbr);
                ele_nbr[ct_dir] = wa.ele;
                slope[ct_dir] =
                    get_slope(ele_val, ele_nbr[ct_dir], dist_to_nbr[ct_dir]);
            }
            /* avoid diagonal flow direction bias */
            if (!is_in_list || (!is_worked && af.asp < 0)) {
                if (ct_dir > 3 && slope[ct_dir] > 0) {
                    if (slope[nbr_ew[ct_dir]] >= 0) {
                        /* slope to ew nbr > slope to center */
                        if (slope[ct_dir] < get_slope(ele_nbr[nbr_ew[ct_dir]],
                                                      ele_nbr[ct_dir], ew_res))
                            skip_diag = 1;
                    }
                    if (!skip_diag && slope[nbr_ns[ct_dir]] >= 0) {
                        /* slope to ns nbr > slope to center */
                        if (slope[ct_dir] < get_slope(ele_nbr[nbr_ns[ct_dir]],
                                                      ele_nbr[ct_dir], ns_res))
                            skip_diag = 1;
                    }
                }
            }

            if (!skip_diag) {
                if (!is_in_list) {
                    ele_up = ele_nbr[ct_dir];
                    af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                    heap_add(r_nbr, c_nbr, ele_up);
                    FLAG_SET(af.flag, INLISTFLAG);
                    seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                }
                else if (!is_worked) {
                    if (FLAG_GET(af.flag, EDGEFLAG)) {
                        /* neighbour is edge in list, not yet worked */
                        if (af.asp < 0 && slope[ct_dir] > 0) {
                            /* adjust flow direction for edge cell */
                            af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                            seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                        }
                    }
                    else if (FLAG_GET(af.flag, DEPRFLAG)) {
                        G_debug(3, "real depression");
                        /* neighbour is inside real depression, not yet worked
                         */
                        if (af.asp == 0 && ele_val <= ele_nbr[ct_dir]) {
                            af.asp = drain[r_nbr - r + 1][c_nbr - c + 1];
                            FLAG_UNSET(af.flag, DEPRFLAG);
                            seg_put(&aspflag, (char *)&af, r_nbr, c_nbr);
                        }
                    }
                }
            }
        } /* end neighbours */
        /* add astar points to sorted list for flow accumulation and stream
         * extraction */
        first_cum--;
        seg_put(&astar_pts, (char *)&heap_p.pnt, 0, first_cum);
        seg_get(&aspflag, (char *)&af, r, c);
        FLAG_SET(af.flag, WORKEDFLAG);
        seg_put(&aspflag, (char *)&af, r, c);
    } /* end A* search */

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
    G_percent(n_points, n_points, 1); /* finish it */

    return 1;
}

/*
 * compare function for heap
 * returns 1 if point1 < point2 else 0
 */
static int heap_cmp(HEAP_PNT *a, HEAP_PNT *b)
{
    if (a->ele < b->ele)
        return 1;
    else if (a->ele == b->ele) {
        if (a->added < b->added)
            return 1;
    }
    return 0;
}

static int sift_up(GW_LARGE_INT start, HEAP_PNT child_p)
{
    GW_LARGE_INT parent, child;
    HEAP_PNT heap_p;

    child = start;

    while (child > 1) {
        parent = GET_PARENT(child);
        seg_get(&search_heap, (char *)&heap_p, 0, parent);

        /* push parent point down if child is smaller */
        if (heap_cmp(&child_p, &heap_p)) {
            seg_put(&search_heap, (char *)&heap_p, 0, child);
            child = parent;
        }
        else
            /* no more sifting up, found slot for child */
            break;
    }

    /* add child to heap */
    seg_put(&search_heap, (char *)&child_p, 0, child);

    return 0;
}

/*
 * add item to heap
 * returns heap_size
 */
GW_LARGE_INT heap_add(int r, int c, CELL ele)
{
    HEAP_PNT heap_p;

    /* add point to next free position */

    heap_size++;

    heap_p.added = nxt_avail_pt;
    heap_p.ele = ele;
    heap_p.pnt.r = r;
    heap_p.pnt.c = c;

    nxt_avail_pt++;

    /* sift up: move new point towards top of heap */
    sift_up(heap_size, heap_p);

    return heap_size;
}

/*
 * drop item from heap
 * returns heap size
 */
HEAP_PNT heap_drop(void)
{
    GW_LARGE_INT child, childr, parent;
    GW_LARGE_INT i;
    HEAP_PNT child_p, childr_p, last_p, root_p;

    seg_get(&search_heap, (char *)&last_p, 0, heap_size);
    seg_get(&search_heap, (char *)&root_p, 0, 1);

    if (heap_size == 1) {
        heap_size = 0;
        return root_p;
    }

    parent = 1;
    while ((child = GET_CHILD(parent)) < heap_size) {

        seg_get(&search_heap, (char *)&child_p, 0, child);

        if (child < heap_size) {
            childr = child + 1;
            i = child + 8;
            while (childr < heap_size && childr < i) {
                seg_get(&search_heap, (char *)&childr_p, 0, childr);
                if (heap_cmp(&childr_p, &child_p)) {
                    child = childr;
                    child_p = childr_p;
                }
                childr++;
            }
        }

        if (heap_cmp(&last_p, &child_p)) {
            break;
        }

        /* move hole down */
        seg_put(&search_heap, (char *)&child_p, 0, parent);
        parent = child;
    }

    /* fill hole */
    if (parent < heap_size) {
        seg_put(&search_heap, (char *)&last_p, 0, parent);
    }

    /* the actual drop */
    heap_size--;

    return root_p;
}

static double get_slope(CELL ele, CELL up_ele, double dist)
{
    if (ele >= up_ele)
        return 0.0;
    else
        return (double)(up_ele - ele) / dist;
}
