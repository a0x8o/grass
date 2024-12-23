#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <unistd.h>
#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/glocale.h>
#include "method.h"

#define MEM 1024

/* function prototypes */
static int s_dev(double *, int, double *);

int o_sdev(const char *basemap, const char *covermap, const char *outputmap,
           int usecats, struct Categories *cats)
{
    struct Popen stats_child, reclass_child;
    FILE *stats, *reclass;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c66f377132 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
    int first, i, count = 0;
=======
    int first, i, count;
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
    int first, i, count;
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c66f377132 (r.horizon manual - fix typo (#2794))
=======
=======
    int first, i, count;
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
    size_t mem;
    long basecat, covercat, catb, catc;
    double value, sdev, x;
    double *tab;

    mem = MEM * sizeof(double);
    tab = (double *)G_malloc(mem);

    stats = run_stats(&stats_child, basemap, covermap, "-cn");
    reclass = run_reclass(&reclass_child, basemap, outputmap);

    first = 1;
    while (read_stats(stats, &basecat, &covercat, &value)) {
        if (first) {
            first = 0;
            catb = basecat;
            catc = covercat;
            i = 0;
            count = 0;
        }

        if (basecat != catb) {
            s_dev(tab, count, &sdev);
            fprintf(reclass, "%ld = %ld %f\n", catb, catb, sdev);
            catb = basecat;
            catc = covercat;
            count = 0;
        }

        if (usecats)
            sscanf(Rast_get_c_cat((CELL *)&covercat, cats), "%lf", &x);
        else
            x = covercat;

        for (i = 0; i < value; i++) {
            if (count * sizeof(double) >= mem) {
                mem += MEM * sizeof(double);
                tab = (double *)G_realloc(tab, mem);
                /* fprintf(stderr,"MALLOC: %d KB needed\n",(int)(mem/1024));  */
            }
            tab[count++] = x;
        }
    }
    if (first) {
        catb = catc = 0;
    }

    s_dev(tab, count, &sdev);
    fprintf(reclass, "%ld = %ld %f\n", catb, catb, sdev);
    G_debug(5, "%ld = %ld %f\n", catb, catb, sdev);

    G_popen_close(&stats_child);
    G_popen_close(&reclass_child);

    return 0;
}

/***********************************************************************
 *
 *  Given an array of data[1...n], this routine returns its standard
 *  deviation sdev.
 *
 ************************************************************************/

static int s_dev(double *data, int n, double *sdev)
{
    double ave, var, ep, s;
    int i;

    if (n < 1) {
        G_warning(_("o_var: No data in array"));
        return (1);
    }

    *sdev = 0.0;
    var = 0.0;
    ep = 0.0;
    s = 0.0;

    for (i = 0; i < n; i++) /* First pass to get the mean     */
        s += data[i];
    ave = s / n;

    for (i = 0; i < n; i++) {
        s = data[i] - ave;
        var += s * s;
        ep += s;
    }

    var = (var - ep * ep / n) / (n - 1);

    *sdev = sqrt(var);

    return (0);
}
