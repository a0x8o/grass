MODULE_TOPDIR = ../../..

PGM=r.sim.water

EXTRA_CLEAN_DIRS=doxygenhtml

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
LIBES     = $(SIMLIB) $(GMATHLIB) $(GISLIB) $(RASTERLIB) $(OPENMP_LIBPATH) $(OPENMP_LIB)
DEPENDENCIES = $(SIMDEP) $(GMATHDEP) $(GISDEP) $(RASTERDEP)
=======
LIBES     = $(SIMLIB) $(GMATHLIB) $(GISLIB) $(OPENMP_LIBPATH) $(OPENMP_LIB)
DEPENDENCIES = $(SIMDEP) $(GMATHDEP) $(GISDEP)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
LIBES     = $(SIMLIB) $(GMATHLIB) $(GISLIB) $(OPENMP_LIBPATH) $(OPENMP_LIB)
DEPENDENCIES = $(SIMDEP) $(GMATHDEP) $(GISDEP)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
EXTRA_INC = $(VECT_INC) $(OPENMP_INCPATH)
EXTRA_CFLAGS = -I ../simlib $(VECT_CFLAGS) $(OPENMP_CFLAGS)

include $(MODULE_TOPDIR)/include/Make/Module.make

default: cmd

man:
	doxygen $(MODULE_TOPDIR)/Doxyfile
