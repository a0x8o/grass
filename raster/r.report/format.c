/***************************************************
 * these routines determine the printf format used
 * by floating point values
 *
 * format_parms() is called for each value.
 *     before first call set eformat=0,dp=6
 *
 * format_double() does the formatting with the
 *     parms determined by format_parms()
 ***************************************************/

#include <string.h>
#include "global.h"

int format_parms(double v, int *n, int *dp, int *eformat, int e_option)
{
    char buf[50];
    int scient_dp;

    scient_dp = *dp;
    for (;;) {
        if (!*eformat)
            format_double(v, buf, *n, *dp);
        else
            scient_format(v, buf, *n, *dp);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
        if ((int)strlen(buf) <= *n)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if ((int)strlen(buf) <= *n)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if ((int)strlen(buf) <= *n)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        if ((int)strlen(buf) <= *n)
=======
>>>>>>> osgeo-main
=======
        if ((int)strlen(buf) <= *n)
=======
>>>>>>> osgeo-main
=======
        if ((int)strlen(buf) <= *n)
=======
>>>>>>> osgeo-main
=======
        if ((int)strlen(buf) <= *n)
=======
>>>>>>> osgeo-main
=======
        if ((int)strlen(buf) <= *n)
=======
>>>>>>> osgeo-main
=======
        if ((int)strlen(buf) <= *n)
=======
>>>>>>> osgeo-main
=======
        if ((int)strlen(buf) <= *n)
=======
>>>>>>> osgeo-main
=======
        if ((int)strlen(buf) <= *n)
=======
>>>>>>> osgeo-main
=======
        if ((int)strlen(buf) <= *n)
=======
>>>>>>> osgeo-main
=======
        if ((int)strlen(buf) <= *n)
=======
>>>>>>> osgeo-main
=======
        if ((int)strlen(buf) <= *n)
=======
>>>>>>> osgeo-main
=======
        if ((int)strlen(buf) <= *n)
=======
>>>>>>> osgeo-main
=======
        if ((int)strlen(buf) <= *n)
=======
>>>>>>> osgeo-main
        if (strlen(buf) <= *n)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (strlen(buf) <= *n)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        if ((int)strlen(buf) <= *n)
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        if (strlen(buf) <= *n)
=======
        if ((int)strlen(buf) <= *n)
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
        if ((int)strlen(buf) <= *n)
=======
        if (strlen(buf) <= *n)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (strlen(buf) <= *n)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        if ((int)strlen(buf) <= *n)
=======
        if (strlen(buf) <= *n)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (strlen(buf) <= *n)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        if ((int)strlen(buf) <= *n)
=======
        if (strlen(buf) <= *n)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (strlen(buf) <= *n)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
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
            break;

        if (*dp) {
            *dp -= 1;
        }
        else {
            if ((e_option) && (!*eformat)) {
                *eformat = 1;
                *dp = scient_dp;
            }
            else
                *n = strlen(buf);
        }
    }

    return 0;
}

int scient_format(double v, char *buf, int n, int dp)
{
    char temp[50];
    int i;

    sprintf(temp, "%#.*g", dp, v);
    for (i = 0; i <= n && temp[i] == ' '; i++) {
    }
    strcpy(buf, temp + i);

    return 0;
}

int format_double(double v, char *buf, int n, int dp)
{
    char fmt[15];
    char temp[100];
    int i, ncommas;

    sprintf(fmt, "%%%d.%df", n, dp);
    sprintf(temp, fmt, v);
    strcpy(buf, temp);
    G_insert_commas(temp);
    ncommas = strlen(temp) - strlen(buf);
    for (i = 0; i < ncommas && temp[i] == ' '; i++) {
    }
    strcpy(buf, temp + i);

    return 0;
}

void compute_unit_format(int unit1, int unit2, enum OutputFormat format)
{
    int i, ns, len;
    char num[100];
    int need_format;

    /* examine units, determine output format */
    for (i = unit1; i <= unit2; i++) {
        if (format == PLAIN) {
            need_format = 1;
        }
        else {
            need_format = 0;
        }
        unit[i].label[0] = "";
        unit[i].label[1] = "";

        switch (unit[i].type) {
        case CELL_COUNTS:
            unit[i].label[0] = " cell";
            unit[i].label[1] = "count";

            if (need_format) {
                need_format = 0;
                unit[i].len = 5;
                ns = 0;
                snprintf(num, sizeof(num), "%ld", count_sum(&ns, -1));
                len = strlen(num);
                if (len > unit[i].len)
                    unit[i].len = len;
            }
            break;

        case PERCENT_COVER:
            unit[i].label[0] = "  %  ";
            unit[i].label[1] = "cover";

            if (need_format) {
                need_format = 0;
                unit[i].dp = 2;
                unit[i].len = 6;
                unit[i].eformat = 0;
            }
            break;

        case SQ_METERS:
            unit[i].label[0] = "square";
            unit[i].label[1] = "meters";
            unit[i].factor = 1.0;
            break;

        case SQ_KILOMETERS:
            unit[i].label[0] = "  square  ";
            unit[i].label[1] = "kilometers";
            unit[i].factor = 1.0e-6;
            break;

        case ACRES:
            unit[i].label[0] = "";
            unit[i].label[1] = "acres";
            unit[i].factor = 2.47105381467165e-4; /* 640 acres in a sq mile */
            break;

        case HECTARES:
            unit[i].label[0] = "";
            unit[i].label[1] = "hectares";
            unit[i].factor = 1.0e-4;
            break;

        case SQ_MILES:
            unit[i].label[0] = "square";
            unit[i].label[1] = " miles";
            unit[i].factor = 3.86102158542446e-7; /* 1 / ( (0.0254m/in * 12in/ft
                                                   * 5280ft/mi)^2 ) */
            break;

        default:
            G_fatal_error("Unit %d not yet supported", unit[i].type);
        }
        if (need_format) {
            unit[i].dp = 6;
            unit[i].len = 10;
            unit[i].eformat = 0;
            ns = 0;
            format_parms(area_sum(&ns, -1) * unit[i].factor, &unit[i].len,
                         &unit[i].dp, &(unit[i].eformat), e_format);
        }
    }
}
