#ifndef __DO_ASTAR_H__
#define __DO_ASTAR_H__

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
#define GET_PARENT(c) (((((GW_LARGE_INT)(c) - 2) >> 2) + 1))
=======
#define GET_PARENT(c) (((((GW_LARGE_INT)(c)-2) >> 2) + 1))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
#define GET_PARENT(c) (((((GW_LARGE_INT)(c)-2) >> 2) + 1))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
#define GET_PARENT(c) (((((GW_LARGE_INT)(c)-2) >> 2) + 1))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
#define GET_CHILD(p)  ((((GW_LARGE_INT)(p) << 2) - 2))

/*
   #define GET_PARENT(c) ((int) (((c) - 2) / 3 + 1))
   #define GET_CHILD(p) ((int) ((p) * 3 - 1))
 */
#endif /* __DO_ASTAR_H__ */
