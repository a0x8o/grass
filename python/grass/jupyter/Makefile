MODULE_TOPDIR = ../../..

include $(MODULE_TOPDIR)/include/Make/Other.make
include $(MODULE_TOPDIR)/include/Make/Python.make

DSTDIR = $(ETC)/python/grass/jupyter

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4625684fca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> cb0f743d05 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
MODULES = \
	setup \
	map \
	interactivemap \
	region \
	map3d \
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	reprojection_renderer \
	utils \
	timeseriesmap
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
	seriesmap \
	reprojection_renderer \
	utils \
<<<<<<< HEAD
<<<<<<< HEAD
	timeseriesmap
=======
MODULES = setup
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
MODULES = setup
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
MODULES = setup display
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
MODULES = \
	setup \
<<<<<<< HEAD
	display \
<<<<<<< HEAD
	interact_display
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
	interact_display \
	utils
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
	map \
	interactivemap \
	region \
	map3d \
	reprojection_renderer \
	utils \
	timeseriesmap
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
	reprojection_renderer \
	utils \
	timeseriesmap
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
	timeseriesmap \
	baseseriesmap
>>>>>>> 2653d7b383 (grass.jupyter: Create BaseSeriesMap to remove redundancies in SeriesMap and TimeSeriesMap  (#3468))
=======
	timeseriesmap \
	baseseriesmap
=======
	timeseriesmap
=======
MODULES = setup
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> a05b13298f (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
<<<<<<< HEAD
>>>>>>> 4625684fca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
=======
=======
MODULES = setup
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
<<<<<<< HEAD
>>>>>>> dc994d1258 (Add session initiations functions for Jupyter Notebooks (#1629))
<<<<<<< HEAD
>>>>>>> cb0f743d05 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
=======
=======
MODULES = setup display
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
MODULES = \
	setup \
	display \
	interact_display
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))

PYFILES := $(patsubst %,$(DSTDIR)/%.py,$(MODULES) __init__)
PYCFILES := $(patsubst %,$(DSTDIR)/%.pyc,$(MODULES) __init__)

default: $(PYFILES) $(PYCFILES)

$(DSTDIR):
	$(MKDIR) $@

$(DSTDIR)/%: % | $(DSTDIR)
	$(INSTALL_DATA) $< $@
