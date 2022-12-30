#ifndef __DO_ASTAR_H__
#define __DO_ASTAR_H__

<<<<<<< HEAD
#define GET_PARENT(c) (((((GW_LARGE_INT)(c) - 2) >> 2) + 1))
=======
#define GET_PARENT(c) (((((GW_LARGE_INT)(c)-2) >> 2) + 1))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
#define GET_CHILD(p)  ((((GW_LARGE_INT)(p) << 2) - 2))

/*
   #define GET_PARENT(c) ((int) (((c) - 2) / 3 + 1))
   #define GET_CHILD(p) ((int) ((p) * 3 - 1))
 */
#endif /* __DO_ASTAR_H__ */
