#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <grass/raster.h>
#include <grass/glocale.h>
#include "global.h"

#define INCR 20

int read_range(void)
{
    struct FPRange drange;
    struct Range range;
    CELL tmp_min, tmp_max;
    DCELL tmp_dmin, tmp_dmax;
    char buff[1024];
    int i;

    /* read the fpranges and ranges of all input maps */
    for (i = 0; i < noi; i++) {
        if (Rast_read_fp_range(name[i], G_mapset(), &drange) <= 0) {
            sprintf(buff, "Can't read f_range for map %s", name[i]);
            G_fatal_error("%s", buff);
        }
        Rast_get_fp_range_min_max(&drange, &tmp_dmin, &tmp_dmax);

        if (Rast_read_range(name[i], G_mapset(), &range) <= 0) {
            sprintf(buff, "Can't read range for map %s", name[i]);
            G_fatal_error("%s", buff);
        }
        Rast_get_range_min_max(&range, &tmp_min, &tmp_max);
        if (!i || tmp_max > old_max || Rast_is_c_null_value(&old_max))
            old_max = tmp_max;
        if (!i || tmp_min < old_min || Rast_is_c_null_value(&old_min))
            old_min = tmp_min;
        if (!i || tmp_dmax > old_dmax || Rast_is_d_null_value(&old_dmax))
            old_dmax = tmp_dmax;
        if (!i || tmp_dmin < old_dmin || Rast_is_d_null_value(&old_dmin))
            old_dmin = tmp_dmin;
    } /* for loop */

    return 0;
}

int report_range(void)
{
    char buff[300], buff2[300];

    if (Rast_is_d_null_value(&old_dmin) || Rast_is_d_null_value(&old_dmax))
        G_message(_("Old data range is empty"));
    else {
        sprintf(buff, "%.15g", old_dmin);
        sprintf(buff2, "%.15g", old_dmax);
        G_trim_decimal(buff);
        G_trim_decimal(buff2);
        G_message(_("Old data range is %s to %s"), buff, buff2);
    }
    if (Rast_is_c_null_value(&old_min) || Rast_is_c_null_value(&old_max))
        G_message(_("Old integer data range is empty"));
    else
        G_message(_("Old integer data range is %d to %d"), (int)old_min,
                  (int)old_max);

    return 0;
}

int read_rules(const char *filename)
{
    char buf[1024];
    DCELL dLow, dHigh;
    CELL iLow, iHigh;
    int n, nrules = 0;
    int first = 1;
    DCELL dmin, dmax;
    CELL cmin, cmax;
    FILE *fp;

    if (strcmp(filename, "-") == 0)
        fp = stdin;
    else {
        fp = fopen(filename, "r");
        if (!fp)
            G_fatal_error(_("unable to open input file <%s>"), filename);
    }

    read_range();
    report_range();
    if (isatty(fileno(fp)))
        fprintf(stderr, _("\nEnter the rule or 'help' for the format "
                          "description or 'end' to exit:\n"));
    Rast_quant_init(&quant_struct);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
    for (;;) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    for (;;) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    for (;;) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    for (;;) {
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
>>>>>>> osgeo-main
    for (line = 1;; line++) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    for (;;) {
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
>>>>>>> osgeo-main
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
    for (line = 1;; line++) {
=======
    for (;;) {
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
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
    for (line = 1;; line++) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    for (;;) {
=======
    for (line = 1;; line++) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    for (;;) {
=======
    for (line = 1;; line++) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
=======
>>>>>>> osgeo-main
=======
    for (;;) {
=======
    for (line = 1;; line++) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    for (;;) {
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
    for (line = 1;; line++) {
=======
    for (;;) {
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
    for (;;) {
=======
    for (line = 1;; line++) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
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
    for (;;) {
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
    for (;;) {
=======
    for (line = 1;; line++) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    for (;;) {
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
    for (;;) {
=======
    for (line = 1;; line++) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    for (;;) {
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
    for (;;) {
=======
    for (line = 1;; line++) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
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
    for (;;) {
=======
    for (line = 1;; line++) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
        if (isatty(fileno(fp)))
            fprintf(stderr, "> ");
        if (!G_getl2(buf, sizeof(buf), fp))
            break;
        for (n = 0; buf[n]; n++)
            if (buf[n] == ',')
                buf[n] = ' ';
        G_strip(buf);
        G_chop(buf);
        if (*buf == 0)
            continue;
        if (*buf == '#')
            continue;
        if (strcmp(buf, "end") == 0) {
            if (nrules == 0)
                break; /* if no new rules have been specified */

            /* give warning when quant rules do not cover the whole range of map
             */
            Rast_quant_get_limits(&quant_struct, &dmin, &dmax, &cmin, &cmax);
            if ((dmin > old_dmin || dmax < old_dmax) && !first)
                G_warning(_("quant rules do not cover the whole range map"));
            break;
        }

        if (strcmp(buf, "help") == 0) {
            fprintf(
                stderr,
                "Enter a rule in one of these formats:\n"
                "float_low:float_high:int_low:int_high\n"
                "float_low:float_high:int_val  (i.e. int_high == int_low)\n"
                "*:float_val:int_val           (interval [inf, float_val])\n"
                "float_val:*:int_val           (interval [float_val, inf])\n");
        }

        /* we read and record into quant table all values, even int as doubles
           we convert the range and domain values to the right format when we
           lookup the values in the quant table */
        switch (sscanf(buf, "%lf:%lf:%d:%d", &dLow, &dHigh, &iLow, &iHigh)) {
        case 3:
            Rast_quant_add_rule(&quant_struct, dLow, dHigh, iLow, iLow);
            nrules++;
            first = 0;
            break;

        case 4:
            Rast_quant_add_rule(&quant_struct, dLow, dHigh, iLow, iHigh);
            nrules++;
            first = 0;
            break;

        default:
            if (sscanf(buf, "%lf:*:%d", &dLow, &iLow) == 2) {
                Rast_quant_set_pos_infinite_rule(&quant_struct, dLow, iLow);
                nrules++;
                first = 0;
            }

            else if (sscanf(buf, "*:%lf:%d", &dHigh, &iLow) == 2) {
                Rast_quant_set_neg_infinite_rule(&quant_struct, dHigh, iLow);
                nrules++;
                first = 0;
            }

            else if (strcmp(buf, "help") == 0)
                break;

            else
                G_warning(_("%s is not a valid rule"), buf);
            break;
        } /* switch */
<<<<<<< HEAD
<<<<<<< HEAD
    } /* loop */
=======
    }     /* loop */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    }     /* loop */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    if (fp != stdin)
        fclose(fp);

    return nrules;
}
