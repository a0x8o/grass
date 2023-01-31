
MODULE_TOPDIR = ../..

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
LIBES2 = $(RASTERLIB) $(GISLIB) $(MATHLIB) $(OPENMP_LIBPATH) $(OPENMP_LIB)
LIBES3 = $(RASTER3DLIB) $(RASTERLIB) $(GISLIB) $(MATHLIB) $(OPENMP_LIBPATH) $(OPENMP_LIB)
DEPENDENCIES = $(RASTER3DDEP) $(GISDEP) $(RASTERDEP)
EXTRA_CFLAGS = $(OPENMP_CFLAGS)
EXTRA_INC = $(OPENMP_INCPATH)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
LIBES2 = $(RASTERLIB) $(GISLIB) $(MATHLIB) $(OMPLIB)
LIBES3 = $(RASTER3DLIB) $(RASTERLIB) $(GISLIB) $(MATHLIB) $(OMPLIB)
DEPENDENCIES = $(RASTER3DDEP) $(GISDEP) $(RASTERDEP)
EXTRA_CFLAGS = $(OMPCFLAGS)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
LIBES2 = $(RASTERLIB) $(GISLIB) $(MATHLIB) $(OMPLIB)
LIBES3 = $(RASTER3DLIB) $(RASTERLIB) $(GISLIB) $(MATHLIB) $(OMPLIB)
DEPENDENCIES = $(RASTER3DDEP) $(GISDEP) $(RASTERDEP)
EXTRA_CFLAGS = $(OMPCFLAGS)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
LIBES2 = $(RASTERLIB) $(GISLIB) $(MATHLIB) $(OPENMP_LIBPATH) $(OPENMP_LIB)
LIBES3 = $(RASTER3DLIB) $(RASTERLIB) $(GISLIB) $(MATHLIB) $(OPENMP_LIBPATH) $(OPENMP_LIB)
DEPENDENCIES = $(RASTER3DDEP) $(GISDEP) $(RASTERDEP)
EXTRA_CFLAGS = $(OPENMP_CFLAGS)
EXTRA_INC = $(OPENMP_INCPATH)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
LIBES2 = $(RASTERLIB) $(GISLIB) $(MATHLIB) $(OMPLIB)
LIBES3 = $(RASTER3DLIB) $(RASTERLIB) $(GISLIB) $(MATHLIB) $(OMPLIB)
DEPENDENCIES = $(RASTER3DDEP) $(GISDEP) $(RASTERDEP)
EXTRA_CFLAGS = $(OMPCFLAGS)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))

PROGRAMS = r.univar r3.univar

r_univar_OBJS = r.univar_main.o sort.o stats.o
r3_univar_OBJS = r3.univar_main.o sort.o stats.o

include $(MODULE_TOPDIR)/include/Make/Multi.make

default: multi

$(BIN)/r.univar$(EXE): LIBES = $(LIBES2)
$(BIN)/r3.univar$(EXE): LIBES = $(LIBES3)
