#ifndef __FLAG_H__
#define __FLAG_H__

/* flag.[ch] is a set of routines which will set up an array of bits
 ** that allow the programmer to "flag" cells in a raster map.
 **
 ** FLAG *
 ** flag_create(nrows,ncols)
 ** int nrows, ncols;
 **     opens the structure flag.
 **     The flag structure will be a two dimensional array of bits the
 **     size of nrows by ncols.  Will initialize flags to zero (unset).
 **
 ** flag_destroy(flags)
 ** FLAG *flags;
 **     closes flags and gives the memory back to the system.
 **
 ** flag_clear_all(flags)
 ** FLAG *flags;
 **     sets all values in flags to zero.
 **
 ** flag_unset(flags, row, col)
 ** FLAG *flags;
 ** int row, col;
 **     sets the value of (row, col) in flags to zero.
 **
 ** flag_set(flags, row, col)
 ** FLAG *flags;
 ** int row, col;
 **     will set the value of (row, col) in flags to one.
 **
 ** int
 ** flag_get(flags, row, col)
 ** FLAG *flags;
 ** int row, col;
 **     returns the value in flags that is at (row, col).
 **
 ** idea by Michael Shapiro
 ** code by Chuck Ehlschlaeger
 ** April 03, 1989
 */
#define FLAG struct _flagsss_
FLAG
{
    int nrows, ncols, leng;
    unsigned char **array;
};

#define FLAG_UNSET(flags, row, col) \
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    (flags)->array[(row)][(col) >> 3] &= ~(1 << ((col) & 7))

#define FLAG_SET(flags, row, col) \
    (flags)->array[(row)][(col) >> 3] |= (1 << ((col) & 7))

#define FLAG_GET(flags, row, col) \
    (flags)->array[(row)][(col) >> 3] & (1 << ((col) & 7))
=======
    (flags)->array[(row)][(col) >> 3] &= ~(1 << ((col)&7))

#define FLAG_SET(flags, row, col) \
    (flags)->array[(row)][(col) >> 3] |= (1 << ((col)&7))

#define FLAG_GET(flags, row, col) \
    (flags)->array[(row)][(col) >> 3] & (1 << ((col)&7))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
    (flags)->array[(row)][(col) >> 3] &= ~(1 << ((col)&7))

#define FLAG_SET(flags, row, col) \
    (flags)->array[(row)][(col) >> 3] |= (1 << ((col)&7))

#define FLAG_GET(flags, row, col) \
    (flags)->array[(row)][(col) >> 3] & (1 << ((col)&7))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

/* flag_clr_all.c */
int flag_clear_all(FLAG *);

/* flag_create.c */
FLAG *flag_create(int, int);

/* flag_destroy.c */
int flag_destroy(FLAG *);

/* flag_get.c */
int flag_get(FLAG *, int, int);

/* flag_set.c */
int flag_set(FLAG *, int, int);

/* flag_unset.c */
int flag_unset(FLAG *, int, int);

#endif /* __FLAG_H__ */
