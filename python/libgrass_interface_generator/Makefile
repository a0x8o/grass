MODULE_TOPDIR = ../..

PACKAGE = "grasslibs"

include $(MODULE_TOPDIR)/include/Make/Other.make

MODULES = date gis raster gmath proj imagery vector rtree display stats \
	dbmi raster3d arraystats cluster vedit segment rowio temporal
ifneq ($(USE_OPENGL),)
MODULES += ogsf nviz
endif

date_LIBS       = $(DATETIMELIB)
gis_LIBS        = $(GISLIB)
raster_LIBS     = $(RASTERLIB)
gmath_LIBS      = $(GMATHLIB)
proj_LIBS       = $(GPROJLIB)
imagery_LIBS    = $(IMAGERYLIB)
vector_LIBS     = $(VECTORLIB)
rtree_LIBS      = $(RTREELIB)
display_LIBS    = $(DISPLAYLIB)
stats_LIBS      = $(STATSLIB)
dbmi_LIBS       = $(DBMILIB)
raster3d_LIBS   = $(RASTER3DLIB)
arraystats_LIBS = $(ARRAYSTATSLIB)
cluster_LIBS    = $(CLUSTERLIB)
vedit_LIBS      = $(VEDITLIB)
ogsf_LIBS       = $(OGSFLIB)
nviz_LIBS       = $(NVIZLIB)
segment_LIBS	= $(SEGMENTLIB)
rowio_LIBS	= $(ROWIOLIB)
temporal_LIBS	= $(TEMPORALLIB)

date_HDRS       = datetime.h defs/datetime.h
gis_HDRS        = gis.h defs/gis.h colors.h defs/colors.h
raster_HDRS     = raster.h defs/raster.h
gmath_HDRS      = gmath.h defs/gmath.h
proj_HDRS       = gprojects.h defs/gprojects.h
imagery_HDRS    = imagery.h defs/imagery.h
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
vector_HDRS     = vector.h defs/vector.h vect/dig_structs.h vect/dig_defines.h vect/dig_externs.h
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
vector_HDRS     = vector.h defs/vector.h vect/dig_structs.h vect/dig_defines.h vect/dig_externs.h
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
vector_HDRS     = vector.h defs/vector.h vect/dig_structs.h vect/dig_defines.h vect/dig_externs.h
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
vector_HDRS     = vector.h defs/vector.h vect/dig_structs.h vect/dig_defines.h vect/dig_externs.h
=======
>>>>>>> osgeo-main
=======
vector_HDRS     = vector.h defs/vector.h vect/dig_structs.h vect/dig_defines.h vect/dig_externs.h
=======
>>>>>>> osgeo-main
=======
vector_HDRS     = vector.h defs/vector.h vect/dig_structs.h vect/dig_defines.h vect/dig_externs.h
=======
>>>>>>> osgeo-main
vector_HDRS     = vector.h defs/vector.h vect/dig_structs.h vect/dig_defines.h vect/dig_externs.h 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
vector_HDRS     = vector.h defs/vector.h vect/dig_structs.h vect/dig_defines.h vect/dig_externs.h 
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
vector_HDRS     = vector.h defs/vector.h vect/dig_structs.h vect/dig_defines.h vect/dig_externs.h
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
vector_HDRS     = vector.h defs/vector.h vect/dig_structs.h vect/dig_defines.h vect/dig_externs.h 
=======
vector_HDRS     = vector.h defs/vector.h vect/dig_structs.h vect/dig_defines.h vect/dig_externs.h
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
vector_HDRS     = vector.h defs/vector.h vect/dig_structs.h vect/dig_defines.h vect/dig_externs.h
=======
vector_HDRS     = vector.h defs/vector.h vect/dig_structs.h vect/dig_defines.h vect/dig_externs.h 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
vector_HDRS     = vector.h defs/vector.h vect/dig_structs.h vect/dig_defines.h vect/dig_externs.h 
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
rtree_HDRS	= rtree.h
display_HDRS    = display.h defs/display.h
stats_HDRS      = stats.h defs/stats.h
dbmi_HDRS       = dbmi.h defs/dbmi.h
raster3d_HDRS   = raster3d.h defs/raster3d.h
arraystats_HDRS = arraystats.h defs/arraystats.h
cluster_HDRS    = cluster.h defs/cluster.h
vedit_HDRS      = vedit.h defs/vedit.h
ogsf_HDRS       = ogsf.h defs/ogsf.h
nviz_HDRS       = nviz.h defs/nviz.h
segment_HDRS    = segment.h defs/segment.h
rowio_HDRS      = rowio.h defs/rowio.h
temporal_HDRS   = temporal.h

proj_INC        = $(PROJINC)
vector_INC      = $(VECT_INC) $(VECT_CFLAGS)
vedit_INC       = $(VECT_INC) $(VECT_CFLAGS)

ifneq ($(MINGW),)
INTLLIB = -lintl-8
endif

CTYPESGEN = ./run.py
CTYPESFLAGS = --no-embed-preamble --strip-build-path "$(ARCH_DISTDIR)" \
	--cpp "$(CC) -E $(CPPFLAGS) $(LFS_CFLAGS) $(EXTRA_CFLAGS) $(NLS_CFLAGS) $(DEFS) $(EXTRA_INC) $(INC) -D__GLIBC_HAVE_LONG_LONG"
EXTRA_CLEAN_FILES := $(wildcard ctypesgen/*.pyc) $(wildcard ctypesgen/*/*.pyc)
EXTRA_CLEAN_DIRS := $(wildcard ctypesgen/__pycache__) $(wildcard ctypesgen/*/__pycache__)

include $(MODULE_TOPDIR)/include/Make/Python.make

PYDIR = $(ETC)/python
GDIR = $(PYDIR)/grass
DSTDIR = $(GDIR)/lib

PYFILES  := $(patsubst %,$(DSTDIR)/%.py,$(MODULES))
PYCFILES  := $(patsubst %,$(DSTDIR)/%.pyc,$(MODULES))
LPYFILES := $(patsubst %,$(OBJDIR)/%.py,$(MODULES))

COPY_FILES = ctypes_loader ctypes_preamble __init__
PY_COPY_FILES = $(patsubst %,$(DSTDIR)/%.py,$(COPY_FILES))
PYC_COPY_FILES = $(patsubst %,$(DSTDIR)/%.pyc,$(COPY_FILES))

ifeq ($(strip $(GRASS_LIBRARY_TYPE)),shlib)
default:
	$(MAKE) $(DSTDIR)
	$(MAKE) $(LPYFILES) $(PYFILES) $(PYCFILES)
	$(MAKE) $(PY_COPY_FILES) $(PYC_COPY_FILES)
else
default:
	@echo "Cannot build Python wrappers for static libraries" >&2
	exit 1
endif

$(PY_COPY_FILES): | $(DSTDIR)
$(DSTDIR)/__init__.py: libgrass__init__.py
	$(INSTALL_DATA) $< $@
$(DSTDIR)/ctypes_loader.py: $(OBJDIR)/ctypes_loader.py
	$(INSTALL_DATA) $< $@
$(DSTDIR)/ctypes_preamble.py: $(OBJDIR)/ctypes_preamble.py
	$(INSTALL_DATA) $< $@

$(DSTDIR)/%.py: $(OBJDIR)/%.py | $(DSTDIR)
	$(INSTALL_DATA) $< $@

define module_rule
$(1)_DEPS = $$(patsubst %.h,$(ARCH_INCDIR)/%.h,$$($(1)_HDRS))
$(OBJDIR)/$(1).py: $$($(1)_DEPS) | $(OBJDIR)
	$$(call run_grass,$(CTYPESGEN) $(CTYPESFLAGS) $$($(1)_LIBS) $$($(1)_INC) $(EXTRA_LIBS) $$($(1)_DEPS) -o $$@)
endef
$(foreach module,$(MODULES),$(eval $(call module_rule,$(module))))

$(PYDIR):
	$(MKDIR) $@

$(GDIR): | $(PYDIR)
	$(MKDIR) $@

$(DSTDIR): | $(GDIR)
	$(MKDIR) $@

.SECONDARY: $(patsubst %,%.py,$(MODULES)) $(patsubst %,%.py,$(COPY_FILES))
