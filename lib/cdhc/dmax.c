#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "local_proto.h"

double *Cdhc_dmax(double *x, int n)
{
    static double y[2];
    double *xcopy, sqrt2, mean = 0.0, sdx = 0.0, fx;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f769754a24 (lib: Fixed uninitialized variable warning in dmax.c by initializing dp, dp_max, dm, and dm_max to 0.0 (#3995))
    double dp = 0.0, dp_max = 0.0, dm = 0.0, dm_max = 0.0;
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    double dp, dp_max, dm, dm_max;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    double dp = 0.0, dp_max = 0.0, dm = 0.0, dm_max = 0.0;
>>>>>>> a0dacc4619 (lib: Fixed uninitialized variable warning in dmax.c by initializing dp, dp_max, dm, and dm_max to 0.0 (#3995))
<<<<<<< HEAD
=======
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    double dp = 0.0, dp_max = 0.0, dm = 0.0, dm_max = 0.0;
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    double dp, dp_max, dm, dm_max;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> f769754a24 (lib: Fixed uninitialized variable warning in dmax.c by initializing dp, dp_max, dm, and dm_max to 0.0 (#3995))
    int i;

    if ((xcopy = (double *)malloc(n * sizeof(double))) == NULL) {
        fprintf(stderr, "Memory error in Cdhc_dmax\n");
        exit(EXIT_FAILURE);
    }

    sqrt2 = sqrt((double)2.0);

    for (i = 0; i < n; ++i) {
        xcopy[i] = x[i];
        mean += x[i];
        sdx += x[i] * x[i];
    }
    sdx = sqrt((n * sdx - mean * mean) / (n * (n - 1.0)));
    mean /= n;

    qsort(xcopy, n, sizeof(double), Cdhc_dcmp);

    for (i = 0; i < n; ++i) {
        xcopy[i] = (xcopy[i] - mean) / sdx;
        fx = 0.5 + Cdhc_normp(xcopy[i] / sqrt2) / 2.0;
        if (fx <= 1e-5)
            fx = 1e-5;

        if (fx >= 0.99999)
            fx = 0.99999;

        dp = (double)(i + 1) / (double)n - fx;
        dm = fx - i / (double)n;
        if (i == 0 || dp > dp_max)
            dp_max = dp;

        if (i == 0 || dm > dm_max)
            dm_max = dm;
    }

    y[0] = dp_max;
    y[1] = dm_max;

    free(xcopy);

    return y;
}
