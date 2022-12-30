MODULE_TOPDIR = ../..

include $(MODULE_TOPDIR)/include/Make/Dir.make
include $(MODULE_TOPDIR)/include/Make/Python.make

PYDIR = $(ETC)/python/grass

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
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
SUBDIRS = \
	app \
	benchmark \
	exceptions \
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
	experimental \
=======
SUBDIRS = \
	app \
<<<<<<< HEAD
<<<<<<< HEAD
	benchmark \
	exceptions \
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
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
	bandref \
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
	benchmark \
	exceptions \
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
	grassdb \
	gunittest \
	imaging \
	jupyter \
	pydispatch \
	pygrass \
	script \
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
	semantic_label \
	temporal \
	utils
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
	semantic_label \
	temporal \
	utils
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
SUBDIRS = app exceptions script ctypes grassdb temporal pygrass pydispatch imaging gunittest bandref jupyter
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
SUBDIRS = app exceptions script ctypes grassdb temporal pygrass pydispatch imaging gunittest bandref jupyter
>>>>>>> 847046a031 (Add session initiations functions for Jupyter Notebooks (#1629))
<<<<<<< HEAD
<<<<<<< HEAD
=======
SUBDIRS = app benchmark exceptions script ctypes grassdb temporal pygrass pydispatch imaging gunittest bandref jupyter
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
	temporal \
	utils
>>>>>>> 6d691c8cd4 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))
<<<<<<< HEAD
=======
	semantic_label \
	temporal \
	utils
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
SUBDIRS = app exceptions script ctypes grassdb temporal pygrass pydispatch imaging gunittest bandref jupyter
>>>>>>> 584e61d06d (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
>>>>>>> 4625684fca (wxGUI/datacatalog: fix setting output vector/raster format (#1596))
=======
>>>>>>> cb0f743d05 (Add session initiations functions for Jupyter Notebooks (#1629))
=======
=======
SUBDIRS = app benchmark exceptions script ctypes grassdb temporal pygrass pydispatch imaging gunittest bandref jupyter
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 82a986a7e1 (wxGUI/splashscreen: use standard one, try to show it before main app, increase timeout (#1718))

default: $(PYDIR)/__init__.py
	$(MAKE) subdirs

$(PYDIR):
	$(MKDIR) $@

$(PYDIR)/__init__.py: __init__.py | $(PYDIR)
	$(INSTALL_DATA) $< $@
