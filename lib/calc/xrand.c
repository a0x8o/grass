#include <stdlib.h>

#include <grass/config.h>
#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/calc.h>

/****************************************************************
rand(lo,hi) random values between a and b
****************************************************************/

int f_rand(int argc, const int *argt, void **args)
{
    int i;

    if (argc < 2)
        return E_ARG_LO;
    if (argc > 2)
        return E_ARG_HI;

    switch (argt[0]) {
    case CELL_TYPE: {
        CELL *res = args[0];
        CELL *arg1 = args[1];
        CELL *arg2 = args[2];

        for (i = 0; i < columns; i++) {
            unsigned int x = (unsigned int)G_mrand48();
            int lo = arg1[i];
            int hi = arg2[i];

            if (lo > hi) {
                int tmp = lo;

                lo = hi;
                hi = tmp;
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
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
>>>>>>> osgeo-main
=======
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
>>>>>>> osgeo-main
=======
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
>>>>>>> osgeo-main
=======
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
>>>>>>> osgeo-main
=======
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
>>>>>>> osgeo-main
=======
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
>>>>>>> osgeo-main
=======
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
>>>>>>> osgeo-main
=======
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
>>>>>>> osgeo-main
=======
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
>>>>>>> osgeo-main
=======
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
>>>>>>> osgeo-main
=======
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
>>>>>>> osgeo-main
=======
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
>>>>>>> osgeo-main
            res[i] = (lo == hi) ? lo : lo + x % (unsigned int)(hi - lo);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            res[i] = (lo == hi) ? lo : lo + x % (unsigned int)(hi - lo);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
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
            res[i] = (lo == hi) ? lo : lo + x % (unsigned int)(hi - lo);
=======
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
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
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
            res[i] = (lo == hi) ? lo : lo + x % (unsigned int)(hi - lo);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            res[i] = (lo == hi) ? lo : lo + x % (unsigned int)(hi - lo);
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
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
            res[i] = (lo == hi) ? lo : lo + x % (unsigned int)(hi - lo);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            res[i] = (lo == hi) ? lo : lo + x % (unsigned int)(hi - lo);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
            res[i] = (lo == hi) ? lo : (int)(lo + x % (unsigned int)(hi - lo));
=======
            res[i] = (lo == hi) ? lo : lo + x % (unsigned int)(hi - lo);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            res[i] = (lo == hi) ? lo : lo + x % (unsigned int)(hi - lo);
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
        }
        return 0;
    }
    case FCELL_TYPE: {
        FCELL *res = args[0];
        FCELL *arg1 = args[1];
        FCELL *arg2 = args[2];

        for (i = 0; i < columns; i++) {
            double x = G_drand48();
            FCELL lo = arg1[i];
            FCELL hi = arg2[i];

            if (lo > hi) {
                FCELL tmp = lo;

                lo = hi;
                hi = tmp;
            }
            res[i] = (FCELL)(lo + x * (hi - lo));
        }
        return 0;
    }
    case DCELL_TYPE: {
        DCELL *res = args[0];
        DCELL *arg1 = args[1];
        DCELL *arg2 = args[2];

        for (i = 0; i < columns; i++) {
            double x = G_drand48();
            DCELL lo = arg1[i];
            DCELL hi = arg2[i];

            if (lo > hi) {
                DCELL tmp = lo;

                lo = hi;
                hi = tmp;
            }
            res[i] = lo + x * (hi - lo);
        }
        return 0;
    }
    default:
        return E_INV_TYPE;
    }
}
