/* ransurf.h                                                            */

#include <stdio.h>
#include <math.h>
#include <grass/raster.h>
#include "flag.h"

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
#define ODD(a)     ((a) & 1)
=======
#define ODD(a)     ((a)&1)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
#define ODD(a)     ((a)&1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
#define ODD(a)     ((a)&1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

#define PI         M_PI

#define CELLSORTER struct cell_sorter_
CELLSORTER
{
    int R, C;
    double Value;
};

extern double NS, EW;
extern int CellCount, Rs, Cs;
extern double MaxDist, MaxDistSq;
extern FLAG *Cells;
extern CELLSORTER *DoNext;
extern CELL **Out, *CellBuffer;
extern int Seed, OutFD;
extern int MaxCellsNum;
extern struct Flag *Verbose;
extern struct Option *Distance;
extern struct Option *Output;
extern struct Option *SeedStuff;
extern struct Option *MaxCells;
