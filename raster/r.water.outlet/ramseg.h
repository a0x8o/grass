#define RAMSEG     int
#define RAMSEGBITS 4
#define DOUBLEBITS 8  /* 2 * ramsegbits       */
#define SEGLENLESS 15 /* 2 ^ ramsegbits - 1   */

#define SEG_INDEX(s, r, c)                                                    \
    (int)(((((r) >> RAMSEGBITS) * (s) + ((c) >> RAMSEGBITS)) << DOUBLEBITS) + \
<<<<<<< HEAD
<<<<<<< HEAD
          (((r) & SEGLENLESS) << RAMSEGBITS) + ((c) & SEGLENLESS))
=======
          (((r)&SEGLENLESS) << RAMSEGBITS) + ((c)&SEGLENLESS))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
          (((r)&SEGLENLESS) << RAMSEGBITS) + ((c)&SEGLENLESS))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
