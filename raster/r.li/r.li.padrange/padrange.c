/****************************************************************************
 *
 * MODULE:       r.li.padrange
 * AUTHOR(S):    Serena Pallecchi (original contributor)
 *                student of Computer Science University of Pisa (Italy)
 *               Commission from Faunalia Pontedera (PI) www.faunalia.it
 *               Fixes: Markus Neteler <neteler itc.it>
 *               Rewrite: Markus Metz
 *               Patch identification: Michael Shapiro - CERL
 *
 * PURPOSE:      calculates calculates standard deviation of patch areas
 * COPYRIGHT:    (C) 2007-2014 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 *****************************************************************************/

#include <stdlib.h>
#include <fcntl.h>
#include <math.h>

#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/glocale.h>

#include "../r.li.daemon/daemon.h"
#include "../r.li.daemon/GenericCell.h"

/* template is patchnum */

/* cell count and type of each patch */
struct pst {
    long count;
    generic_cell type;
};

rli_func patchAreaDistributionRANGE;
int calculate(int fd, struct area_entry *ad, double *result);
int calculateD(int fd, struct area_entry *ad, double *result);
int calculateF(int fd, struct area_entry *ad, double *result);

int main(int argc, char *argv[])
{
    struct Option *raster, *conf, *output;
    struct GModule *module;

    G_gisinit(argv[0]);
    module = G_define_module();
    module->description =
        _("Calculates range of patch area size on a raster map");
    G_add_keyword(_("raster"));
    G_add_keyword(_("landscape structure analysis"));
    G_add_keyword(_("patch index"));

    /* define options */
    raster = G_define_standard_option(G_OPT_R_INPUT);

    conf = G_define_standard_option(G_OPT_F_INPUT);
    conf->key = "config";
    conf->description = _("Configuration file");
    conf->required = YES;

    output = G_define_standard_option(G_OPT_R_OUTPUT);

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);
    return calculateIndex(conf->answer, patchAreaDistributionRANGE, NULL,
                          raster->answer, output->answer);
}

<<<<<<< HEAD
int patchAreaDistributionRANGE(int fd, char **par UNUSED, struct area_entry *ad,
=======
int patchAreaDistributionRANGE(int fd, char **par, struct area_entry *ad,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
                               double *result)
{
    double indice = 0;
    int ris = RLI_OK;

    switch (ad->data_type) {
    case CELL_TYPE: {
        ris = calculate(fd, ad, &indice);
        break;
    }
    case DCELL_TYPE: {
        ris = calculateD(fd, ad, &indice);
        break;
    }
    case FCELL_TYPE: {
        ris = calculateF(fd, ad, &indice);
        break;
    }
    default: {
        G_fatal_error("data type unknown");
        return RLI_ERRORE;
    }
    }
    if (ris != RLI_OK) {
        *result = -1;
        return RLI_ERRORE;
    }

    *result = indice;

    return RLI_OK;
}

int calculate(int fd, struct area_entry *ad, double *result)
{
    CELL *buf, *buf_sup, *buf_null;
    CELL corrCell, precCell, supCell;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
    long npatch;
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    long npatch;
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    long npatch;
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
    long npatch, area;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    long npatch, area;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    long npatch;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    long npatch, area;
=======
    long npatch;
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
    long npatch;
=======
    long npatch, area;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    long npatch, area;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    long npatch;
=======
    long npatch, area;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    long npatch, area;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    long npatch;
=======
    long npatch, area;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    long npatch, area;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    long pid, old_pid, new_pid, *pid_corr, *pid_sup, *ltmp;
    struct pst *pst;
    long nalloc, incr;
    int i, j, k;
    int connected;
    int mask_fd, *mask_buf, *mask_sup, *mask_tmp, masked;
    struct Cell_head hd;

    Rast_get_window(&hd);

    buf_null = Rast_allocate_c_buf();
    Rast_set_c_null_value(buf_null, Rast_window_cols());
    buf_sup = buf_null;

    /* initialize patch ids */
    pid_corr = G_malloc(Rast_window_cols() * sizeof(long));
    pid_sup = G_malloc(Rast_window_cols() * sizeof(long));

    for (j = 0; j < Rast_window_cols(); j++) {
        pid_corr[j] = 0;
        pid_sup[j] = 0;
    }

    /* open mask if needed */
    mask_fd = -1;
    mask_buf = mask_sup = NULL;
    masked = FALSE;
    if (ad->mask == 1) {
        if ((mask_fd = open(ad->mask_name, O_RDONLY, 0755)) < 0)
            return RLI_ERRORE;
        mask_buf = G_malloc(ad->cl * sizeof(int));
        if (mask_buf == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        mask_sup = G_malloc(ad->cl * sizeof(int));
        if (mask_sup == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        for (j = 0; j < ad->cl; j++)
            mask_buf[j] = 0;

        masked = TRUE;
    }

    /* calculate number of patches */
    npatch = 0;
    pid = 0;

    /* patch size and type */
    incr = 1024;
    if (incr > ad->rl)
        incr = ad->rl;
    if (incr > ad->cl)
        incr = ad->cl;
    if (incr < 2)
        incr = 2;
    nalloc = incr;
    pst = G_malloc(nalloc * sizeof(struct pst));
    for (k = 0; k < nalloc; k++) {
        pst[k].count = 0;
    }

    for (i = 0; i < ad->rl; i++) {
        buf = RLI_get_cell_raster_row(fd, i + ad->y, ad);
        if (i > 0) {
            buf_sup = RLI_get_cell_raster_row(fd, i - 1 + ad->y, ad);
        }

        if (masked) {
            mask_tmp = mask_sup;
            mask_sup = mask_buf;
            mask_buf = mask_tmp;
            if (read(mask_fd, mask_buf, (ad->cl * sizeof(int))) < 0)
                return 0;
        }

        ltmp = pid_sup;
        pid_sup = pid_corr;
        pid_corr = ltmp;

        Rast_set_c_null_value(&precCell, 1);

        connected = 0;
        for (j = 0; j < ad->cl; j++) {
            pid_corr[j + ad->x] = 0;

            corrCell = buf[j + ad->x];
            if (masked && (mask_buf[j] == 0)) {
                Rast_set_c_null_value(&corrCell, 1);
            }

            if (Rast_is_c_null_value(&corrCell)) {
                connected = 0;
                precCell = corrCell;
                continue;
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
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
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
            area++;

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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
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
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_c_null_value(&supCell, 1);
            }

            if (!Rast_is_c_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_c_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

                    old_pid = pid_corr[j + ad->x];
                    new_pid = pid_sup[j + ad->x];
                    pid_corr[j + ad->x] = new_pid;
                    if (old_pid > 0) {
                        /* merge */
                        /* update left side of the current row */
                        for (k = 0; k < j; k++) {
                            if (pid_corr[k + ad->x] == old_pid)
                                pid_corr[k + ad->x] = new_pid;
                        }
                        /* update right side of the previous row */
                        for (k = j + 1; k < ad->cl; k++) {
                            if (pid_sup[k + ad->x] == old_pid)
                                pid_sup[k + ad->x] = new_pid;
                        }
                        pst[new_pid].count += pst[old_pid].count;
                        pst[old_pid].count = 0;

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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
            area++;

>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
            area++;

>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
            area++;

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_c_null_value(&supCell, 1);
            }

            if (!Rast_is_c_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_c_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

<<<<<<< HEAD
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
            area++;

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_c_null_value(&supCell, 1);
            }

            if (!Rast_is_c_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_c_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
            area++;

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_c_null_value(&supCell, 1);
            }

            if (!Rast_is_c_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_c_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
            area++;

            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_c_null_value(&supCell, 1);
            }

            if (!Rast_is_c_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_c_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
                    old_pid = pid_corr[j + ad->x];
                    new_pid = pid_sup[j + ad->x];
                    pid_corr[j + ad->x] = new_pid;
                    if (old_pid > 0) {
                        /* merge */
                        /* update left side of the current row */
                        for (k = 0; k < j; k++) {
                            if (pid_corr[k + ad->x] == old_pid)
                                pid_corr[k + ad->x] = new_pid;
                        }
                        /* update right side of the previous row */
                        for (k = j + 1; k < ad->cl; k++) {
                            if (pid_sup[k + ad->x] == old_pid)
                                pid_sup[k + ad->x] = new_pid;
                        }
                        pst[new_pid].count += pst[old_pid].count;
                        pst[old_pid].count = 0;

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
>>>>>>> osgeo-main
            area++;

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_c_null_value(&supCell, 1);
            }

            if (!Rast_is_c_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_c_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

<<<<<<< HEAD
=======
            area++;

            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_c_null_value(&supCell, 1);
            }

            if (!Rast_is_c_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_c_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
                    old_pid = pid_corr[j + ad->x];
                    new_pid = pid_sup[j + ad->x];
                    pid_corr[j + ad->x] = new_pid;
                    if (old_pid > 0) {
                        /* merge */
                        /* update left side of the current row */
                        for (k = 0; k < j; k++) {
                            if (pid_corr[k + ad->x] == old_pid)
                                pid_corr[k + ad->x] = new_pid;
                        }
                        /* update right side of the previous row */
                        for (k = j + 1; k < ad->cl; k++) {
                            if (pid_sup[k + ad->x] == old_pid)
                                pid_sup[k + ad->x] = new_pid;
                        }
                        pst[new_pid].count += pst[old_pid].count;
                        pst[old_pid].count = 0;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
                        if (old_pid == pid)
                            pid--;
                    }
                    else {
                        pst[new_pid].count++;
                    }
                }
                connected = 1;
            }

            if (!connected) {
                /* start new patch */
                npatch++;
                pid++;
                pid_corr[j + ad->x] = pid;

                if (pid >= nalloc) {
                    pst = (struct pst *)G_realloc(pst, (pid + incr) *
                                                           sizeof(struct pst));

                    for (k = nalloc; k < pid + incr; k++)
                        pst[k].count = 0;

                    nalloc = pid + incr;
                }

                pst[pid].count = 1;
                pst[pid].type.t = CELL_TYPE;
                pst[pid].type.val.c = corrCell;
            }
            precCell = corrCell;
        }
    }

    if (npatch > 0) {
        double EW_DIST1, EW_DIST2, NS_DIST1, NS_DIST2;
        double area_p;
        double cell_size_m;
        double min, max;

        /* calculate distance */
        G_begin_distance_calculations();
        /* EW Dist at North edge */
        EW_DIST1 = G_distance(hd.east, hd.north, hd.west, hd.north);
        /* EW Dist at South Edge */
        EW_DIST2 = G_distance(hd.east, hd.south, hd.west, hd.south);
        /* NS Dist at East edge */
        NS_DIST1 = G_distance(hd.east, hd.north, hd.east, hd.south);
        /* NS Dist at West edge */
        NS_DIST2 = G_distance(hd.west, hd.north, hd.west, hd.south);

        cell_size_m = (((EW_DIST1 + EW_DIST2) / 2) / hd.cols) *
                      (((NS_DIST1 + NS_DIST2) / 2) / hd.rows);

        /* get min and max patch size */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
        min = INFINITY;
        max = -INFINITY;
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        min = INFINITY;
        max = -INFINITY;
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        min = INFINITY;
        max = -INFINITY;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
=======
        min = INFINITY;
        max = -INFINITY;
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        min = INFINITY;
        max = -INFINITY;
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
        min = INFINITY;
        max = -INFINITY;
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        min = INFINITY;
        max = -INFINITY;
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
        for (old_pid = 1; old_pid <= pid; old_pid++) {
            if (pst[old_pid].count > 0) {
                area_p = cell_size_m * pst[old_pid].count / 10000;
                if (min > area_p)
                    min = area_p;
                if (max < area_p)
                    max = area_p;
            }
        }
        *result = max - min;
    }
    else
        Rast_set_d_null_value(result, 1);

    if (masked) {
        close(mask_fd);
        G_free(mask_buf);
        G_free(mask_sup);
    }
    G_free(buf_null);
    G_free(pid_corr);
    G_free(pid_sup);
    G_free(pst);

    return RLI_OK;
}

int calculateD(int fd, struct area_entry *ad, double *result)
{
    DCELL *buf, *buf_sup, *buf_null;
    DCELL corrCell, precCell, supCell;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
    long npatch;
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    long npatch;
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    long npatch;
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
    long npatch, area;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    long npatch, area;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    long npatch;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    long npatch, area;
=======
    long npatch;
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
    long npatch;
=======
    long npatch, area;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    long npatch, area;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    long npatch;
=======
    long npatch, area;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    long npatch, area;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    long npatch;
=======
    long npatch, area;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    long npatch, area;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    long pid, old_pid, new_pid, *pid_corr, *pid_sup, *ltmp;
    struct pst *pst;
    long nalloc, incr;
    int i, j, k;
    int connected;
    int mask_fd, *mask_buf, *mask_sup, *mask_tmp, masked;
    struct Cell_head hd;

    Rast_get_window(&hd);

    buf_null = Rast_allocate_d_buf();
    Rast_set_d_null_value(buf_null, Rast_window_cols());
    buf_sup = buf_null;

    /* initialize patch ids */
    pid_corr = G_malloc(Rast_window_cols() * sizeof(long));
    pid_sup = G_malloc(Rast_window_cols() * sizeof(long));

    for (j = 0; j < Rast_window_cols(); j++) {
        pid_corr[j] = 0;
        pid_sup[j] = 0;
    }

    /* open mask if needed */
    mask_fd = -1;
    mask_buf = mask_sup = NULL;
    masked = FALSE;
    if (ad->mask == 1) {
        if ((mask_fd = open(ad->mask_name, O_RDONLY, 0755)) < 0)
            return RLI_ERRORE;
        mask_buf = G_malloc(ad->cl * sizeof(int));
        if (mask_buf == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        mask_sup = G_malloc(ad->cl * sizeof(int));
        if (mask_sup == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        for (j = 0; j < ad->cl; j++)
            mask_buf[j] = 0;

        masked = TRUE;
    }

    /* calculate number of patches */
    npatch = 0;
    pid = 0;

    /* patch size and type */
    incr = 1024;
    if (incr > ad->rl)
        incr = ad->rl;
    if (incr > ad->cl)
        incr = ad->cl;
    if (incr < 2)
        incr = 2;
    nalloc = incr;
    pst = G_malloc(nalloc * sizeof(struct pst));
    for (k = 0; k < nalloc; k++) {
        pst[k].count = 0;
    }

    for (i = 0; i < ad->rl; i++) {
        buf = RLI_get_dcell_raster_row(fd, i + ad->y, ad);
        if (i > 0) {
            buf_sup = RLI_get_dcell_raster_row(fd, i - 1 + ad->y, ad);
        }

        if (masked) {
            mask_tmp = mask_sup;
            mask_sup = mask_buf;
            mask_buf = mask_tmp;
            if (read(mask_fd, mask_buf, (ad->cl * sizeof(int))) < 0)
                return 0;
        }

        ltmp = pid_sup;
        pid_sup = pid_corr;
        pid_corr = ltmp;

        Rast_set_d_null_value(&precCell, 1);

        connected = 0;
        for (j = 0; j < ad->cl; j++) {
            pid_corr[j + ad->x] = 0;

            corrCell = buf[j + ad->x];
            if (masked && (mask_buf[j] == 0)) {
                Rast_set_d_null_value(&corrCell, 1);
            }

            if (Rast_is_d_null_value(&corrCell)) {
                connected = 0;
                precCell = corrCell;
                continue;
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
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
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
            area++;

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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
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
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_d_null_value(&supCell, 1);
            }

            if (!Rast_is_d_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_d_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

                    old_pid = pid_corr[j + ad->x];
                    new_pid = pid_sup[j + ad->x];
                    pid_corr[j + ad->x] = new_pid;
                    if (old_pid > 0) {
                        /* merge */
                        /* update left side of the current row */
                        for (k = 0; k < j; k++) {
                            if (pid_corr[k + ad->x] == old_pid)
                                pid_corr[k + ad->x] = new_pid;
                        }
                        /* update right side of the previous row */
                        for (k = j + 1; k < ad->cl; k++) {
                            if (pid_sup[k + ad->x] == old_pid)
                                pid_sup[k + ad->x] = new_pid;
                        }
                        pst[new_pid].count += pst[old_pid].count;
                        pst[old_pid].count = 0;

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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
            area++;

>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
            area++;

>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
            area++;

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_d_null_value(&supCell, 1);
            }

            if (!Rast_is_d_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_d_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

<<<<<<< HEAD
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
            area++;

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_d_null_value(&supCell, 1);
            }

            if (!Rast_is_d_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_d_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
            area++;

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_d_null_value(&supCell, 1);
            }

            if (!Rast_is_d_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_d_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
            area++;

            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_d_null_value(&supCell, 1);
            }

            if (!Rast_is_d_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_d_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
                    old_pid = pid_corr[j + ad->x];
                    new_pid = pid_sup[j + ad->x];
                    pid_corr[j + ad->x] = new_pid;
                    if (old_pid > 0) {
                        /* merge */
                        /* update left side of the current row */
                        for (k = 0; k < j; k++) {
                            if (pid_corr[k + ad->x] == old_pid)
                                pid_corr[k + ad->x] = new_pid;
                        }
                        /* update right side of the previous row */
                        for (k = j + 1; k < ad->cl; k++) {
                            if (pid_sup[k + ad->x] == old_pid)
                                pid_sup[k + ad->x] = new_pid;
                        }
                        pst[new_pid].count += pst[old_pid].count;
                        pst[old_pid].count = 0;

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
>>>>>>> osgeo-main
            area++;

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_d_null_value(&supCell, 1);
            }

            if (!Rast_is_d_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_d_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

<<<<<<< HEAD
=======
            area++;

            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_d_null_value(&supCell, 1);
            }

            if (!Rast_is_d_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_d_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
                    old_pid = pid_corr[j + ad->x];
                    new_pid = pid_sup[j + ad->x];
                    pid_corr[j + ad->x] = new_pid;
                    if (old_pid > 0) {
                        /* merge */
                        /* update left side of the current row */
                        for (k = 0; k < j; k++) {
                            if (pid_corr[k + ad->x] == old_pid)
                                pid_corr[k + ad->x] = new_pid;
                        }
                        /* update right side of the previous row */
                        for (k = j + 1; k < ad->cl; k++) {
                            if (pid_sup[k + ad->x] == old_pid)
                                pid_sup[k + ad->x] = new_pid;
                        }
                        pst[new_pid].count += pst[old_pid].count;
                        pst[old_pid].count = 0;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
                        if (old_pid == pid)
                            pid--;
                    }
                    else {
                        pst[new_pid].count++;
                    }
                }
                connected = 1;
            }

            if (!connected) {
                /* start new patch */
                npatch++;
                pid++;
                pid_corr[j + ad->x] = pid;

                if (pid >= nalloc) {
                    pst = (struct pst *)G_realloc(pst, (pid + incr) *
                                                           sizeof(struct pst));

                    for (k = nalloc; k < pid + incr; k++)
                        pst[k].count = 0;

                    nalloc = pid + incr;
                }

                pst[pid].count = 1;
                pst[pid].type.t = CELL_TYPE;
                pst[pid].type.val.c = corrCell;
            }
            precCell = corrCell;
        }
    }

    if (npatch > 0) {
        double EW_DIST1, EW_DIST2, NS_DIST1, NS_DIST2;
        double area_p;
        double cell_size_m;
        double min, max;

        /* calculate distance */
        G_begin_distance_calculations();
        /* EW Dist at North edge */
        EW_DIST1 = G_distance(hd.east, hd.north, hd.west, hd.north);
        /* EW Dist at South Edge */
        EW_DIST2 = G_distance(hd.east, hd.south, hd.west, hd.south);
        /* NS Dist at East edge */
        NS_DIST1 = G_distance(hd.east, hd.north, hd.east, hd.south);
        /* NS Dist at West edge */
        NS_DIST2 = G_distance(hd.west, hd.north, hd.west, hd.south);

        cell_size_m = (((EW_DIST1 + EW_DIST2) / 2) / hd.cols) *
                      (((NS_DIST1 + NS_DIST2) / 2) / hd.rows);

        /* get min and max patch size */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
        min = INFINITY;
        max = -INFINITY;
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        min = INFINITY;
        max = -INFINITY;
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        min = INFINITY;
        max = -INFINITY;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
=======
        min = INFINITY;
        max = -INFINITY;
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        min = INFINITY;
        max = -INFINITY;
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
        min = INFINITY;
        max = -INFINITY;
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        min = INFINITY;
        max = -INFINITY;
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
        for (old_pid = 1; old_pid <= pid; old_pid++) {
            if (pst[old_pid].count > 0) {
                area_p = cell_size_m * pst[old_pid].count / 10000;
                if (min > area_p)
                    min = area_p;
                if (max < area_p)
                    max = area_p;
            }
        }
        *result = max - min;
    }
    else
        Rast_set_d_null_value(result, 1);

    if (masked) {
        close(mask_fd);
        G_free(mask_buf);
        G_free(mask_sup);
    }
    G_free(buf_null);
    G_free(pid_corr);
    G_free(pid_sup);
    G_free(pst);

    return RLI_OK;
}

int calculateF(int fd, struct area_entry *ad, double *result)
{
    FCELL *buf, *buf_sup, *buf_null;
    FCELL corrCell, precCell, supCell;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
    long npatch;
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    long npatch;
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    long npatch;
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
=======
    long npatch;
=======
>>>>>>> osgeo-main
    long npatch, area;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    long npatch, area;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    long npatch;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    long npatch, area;
=======
    long npatch;
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
    long npatch;
=======
    long npatch, area;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    long npatch, area;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    long npatch;
=======
    long npatch, area;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    long npatch, area;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    long npatch;
=======
    long npatch, area;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    long npatch, area;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    long pid, old_pid, new_pid, *pid_corr, *pid_sup, *ltmp;
    struct pst *pst;
    long nalloc, incr;
    int i, j, k;
    int connected;
    int mask_fd, *mask_buf, *mask_sup, *mask_tmp, masked;
    struct Cell_head hd;

    Rast_get_window(&hd);

    buf_null = Rast_allocate_f_buf();
    Rast_set_f_null_value(buf_null, Rast_window_cols());
    buf_sup = buf_null;

    /* initialize patch ids */
    pid_corr = G_malloc(Rast_window_cols() * sizeof(long));
    pid_sup = G_malloc(Rast_window_cols() * sizeof(long));

    for (j = 0; j < Rast_window_cols(); j++) {
        pid_corr[j] = 0;
        pid_sup[j] = 0;
    }

    /* open mask if needed */
    mask_fd = -1;
    mask_buf = mask_sup = NULL;
    masked = FALSE;
    if (ad->mask == 1) {
        if ((mask_fd = open(ad->mask_name, O_RDONLY, 0755)) < 0)
            return RLI_ERRORE;
        mask_buf = G_malloc(ad->cl * sizeof(int));
        if (mask_buf == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        mask_sup = G_malloc(ad->cl * sizeof(int));
        if (mask_sup == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        for (j = 0; j < ad->cl; j++)
            mask_buf[j] = 0;

        masked = TRUE;
    }

    /* calculate number of patches */
    npatch = 0;
    pid = 0;

    /* patch size and type */
    incr = 1024;
    if (incr > ad->rl)
        incr = ad->rl;
    if (incr > ad->cl)
        incr = ad->cl;
    if (incr < 2)
        incr = 2;
    nalloc = incr;
    pst = G_malloc(nalloc * sizeof(struct pst));
    for (k = 0; k < nalloc; k++) {
        pst[k].count = 0;
    }

    for (i = 0; i < ad->rl; i++) {
        buf = RLI_get_fcell_raster_row(fd, i + ad->y, ad);
        if (i > 0) {
            buf_sup = RLI_get_fcell_raster_row(fd, i - 1 + ad->y, ad);
        }

        if (masked) {
            mask_tmp = mask_sup;
            mask_sup = mask_buf;
            mask_buf = mask_tmp;
            if (read(mask_fd, mask_buf, (ad->cl * sizeof(int))) < 0)
                return 0;
        }

        ltmp = pid_sup;
        pid_sup = pid_corr;
        pid_corr = ltmp;

        Rast_set_f_null_value(&precCell, 1);

        connected = 0;
        for (j = 0; j < ad->cl; j++) {
            pid_corr[j + ad->x] = 0;

            corrCell = buf[j + ad->x];
            if (masked && (mask_buf[j] == 0)) {
                Rast_set_f_null_value(&corrCell, 1);
            }

            if (Rast_is_f_null_value(&corrCell)) {
                connected = 0;
                precCell = corrCell;
                continue;
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
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
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
            area++;

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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
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
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_f_null_value(&supCell, 1);
            }

            if (!Rast_is_f_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_f_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

                    old_pid = pid_corr[j + ad->x];
                    new_pid = pid_sup[j + ad->x];
                    pid_corr[j + ad->x] = new_pid;
                    if (old_pid > 0) {
                        /* merge */
                        /* update left side of the current row */
                        for (k = 0; k < j; k++) {
                            if (pid_corr[k + ad->x] == old_pid)
                                pid_corr[k + ad->x] = new_pid;
                        }
                        /* update right side of the previous row */
                        for (k = j + 1; k < ad->cl; k++) {
                            if (pid_sup[k + ad->x] == old_pid)
                                pid_sup[k + ad->x] = new_pid;
                        }
                        pst[new_pid].count += pst[old_pid].count;
                        pst[old_pid].count = 0;

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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
            area++;

>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
            area++;

>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
            area++;

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_f_null_value(&supCell, 1);
            }

            if (!Rast_is_f_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_f_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

<<<<<<< HEAD
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
            area++;

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_f_null_value(&supCell, 1);
            }

            if (!Rast_is_f_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_f_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
            area++;

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_f_null_value(&supCell, 1);
            }

            if (!Rast_is_f_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_f_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
            area++;

            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_f_null_value(&supCell, 1);
            }

            if (!Rast_is_f_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_f_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
                    old_pid = pid_corr[j + ad->x];
                    new_pid = pid_sup[j + ad->x];
                    pid_corr[j + ad->x] = new_pid;
                    if (old_pid > 0) {
                        /* merge */
                        /* update left side of the current row */
                        for (k = 0; k < j; k++) {
                            if (pid_corr[k + ad->x] == old_pid)
                                pid_corr[k + ad->x] = new_pid;
                        }
                        /* update right side of the previous row */
                        for (k = j + 1; k < ad->cl; k++) {
                            if (pid_sup[k + ad->x] == old_pid)
                                pid_sup[k + ad->x] = new_pid;
                        }
                        pst[new_pid].count += pst[old_pid].count;
                        pst[old_pid].count = 0;

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
>>>>>>> osgeo-main
            area++;

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_f_null_value(&supCell, 1);
            }

            if (!Rast_is_f_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_f_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

<<<<<<< HEAD
=======
            area++;

            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_f_null_value(&supCell, 1);
            }

            if (!Rast_is_f_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j + ad->x] = pid_corr[j - 1 + ad->x];
                connected = 1;
                pst[pid_corr[j + ad->x]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_f_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j + ad->x] != pid_sup[j + ad->x]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
                    old_pid = pid_corr[j + ad->x];
                    new_pid = pid_sup[j + ad->x];
                    pid_corr[j + ad->x] = new_pid;
                    if (old_pid > 0) {
                        /* merge */
                        /* update left side of the current row */
                        for (k = 0; k < j; k++) {
                            if (pid_corr[k + ad->x] == old_pid)
                                pid_corr[k + ad->x] = new_pid;
                        }
                        /* update right side of the previous row */
                        for (k = j + 1; k < ad->cl; k++) {
                            if (pid_sup[k + ad->x] == old_pid)
                                pid_sup[k + ad->x] = new_pid;
                        }
                        pst[new_pid].count += pst[old_pid].count;
                        pst[old_pid].count = 0;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
                        if (old_pid == pid)
                            pid--;
                    }
                    else {
                        pst[new_pid].count++;
                    }
                }
                connected = 1;
            }

            if (!connected) {
                /* start new patch */
                npatch++;
                pid++;
                pid_corr[j + ad->x] = pid;

                if (pid >= nalloc) {
                    pst = (struct pst *)G_realloc(pst, (pid + incr) *
                                                           sizeof(struct pst));

                    for (k = nalloc; k < pid + incr; k++)
                        pst[k].count = 0;

                    nalloc = pid + incr;
                }

                pst[pid].count = 1;
                pst[pid].type.t = CELL_TYPE;
                pst[pid].type.val.c = corrCell;
            }
            precCell = corrCell;
        }
    }

    if (npatch > 0) {
        double EW_DIST1, EW_DIST2, NS_DIST1, NS_DIST2;
        double area_p;
        double cell_size_m;
        double min, max;

        /* calculate distance */
        G_begin_distance_calculations();
        /* EW Dist at North edge */
        EW_DIST1 = G_distance(hd.east, hd.north, hd.west, hd.north);
        /* EW Dist at South Edge */
        EW_DIST2 = G_distance(hd.east, hd.south, hd.west, hd.south);
        /* NS Dist at East edge */
        NS_DIST1 = G_distance(hd.east, hd.north, hd.east, hd.south);
        /* NS Dist at West edge */
        NS_DIST2 = G_distance(hd.west, hd.north, hd.west, hd.south);

        cell_size_m = (((EW_DIST1 + EW_DIST2) / 2) / hd.cols) *
                      (((NS_DIST1 + NS_DIST2) / 2) / hd.rows);

        /* get min and max patch size */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
        min = INFINITY;
        max = -INFINITY;
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        min = INFINITY;
        max = -INFINITY;
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
=======
        min = INFINITY;
        max = -INFINITY;
=======
>>>>>>> osgeo-main
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        min = INFINITY;
        max = -INFINITY;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
=======
        min = INFINITY;
        max = -INFINITY;
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        min = INFINITY;
        max = -INFINITY;
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
        min = INFINITY;
        max = -INFINITY;
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        min = INFINITY;
        max = -INFINITY;
=======
        min = 1.0 / 0.0;  /* inf */
        max = -1.0 / 0.0; /* -inf */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
        for (old_pid = 1; old_pid <= pid; old_pid++) {
            if (pst[old_pid].count > 0) {
                area_p = cell_size_m * pst[old_pid].count / 10000;
                if (min > area_p)
                    min = area_p;
                if (max < area_p)
                    max = area_p;
            }
        }
        *result = max - min;
    }
    else
        Rast_set_d_null_value(result, 1);

    if (masked) {
        close(mask_fd);
        G_free(mask_buf);
        G_free(mask_sup);
    }
    G_free(buf_null);
    G_free(pid_corr);
    G_free(pid_sup);
    G_free(pst);

    return RLI_OK;
}
