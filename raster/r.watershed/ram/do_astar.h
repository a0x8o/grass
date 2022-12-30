#ifndef __DO_ASTAR_H__
#define __DO_ASTAR_H__

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
#define GET_PARENT(p, c) ((p) = (int)(((c) - 2) / 3 + 1))
#define GET_CHILD(c, p)  ((c) = (int)(((p) * 3) - 1))
=======
#define GET_PARENT(p, c) ((p) = (int)(((c)-2) / 3 + 1))
#define GET_CHILD(c, p)  ((c) = (int)(((p)*3) - 1))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
#define GET_PARENT(p, c) ((p) = (int)(((c)-2) / 3 + 1))
#define GET_CHILD(c, p)  ((c) = (int)(((p)*3) - 1))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)

#endif /* __DO_ASTAR_H__ */
