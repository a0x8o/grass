MODULE_TOPDIR = ..

SUBDIRS = timer g.html2man

include $(MODULE_TOPDIR)/include/Make/Dir.make
include $(MODULE_TOPDIR)/include/Make/Compile.make

<<<<<<< HEAD
default: parsubdirs $(UTILSDIR)/mkdocs.py $(UTILSDIR)/mkhtml.py $(UTILSDIR)/mkmarkdown.py \
	$(UTILSDIR)/generate_last_commit_file.py \
	$(UTILSDIR)/g.echo$(EXE)

$(UTILSDIR)/mkdocs.py: mkdocs.py
	$(INSTALL) $< $@
=======
default: parsubdirs $(UTILSDIR)/mkhtml.py \
	$(UTILSDIR)/generate_last_commit_file.py \
	$(UTILSDIR)/g.echo$(EXE)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

$(UTILSDIR)/mkhtml.py: mkhtml.py
	$(INSTALL) $< $@

<<<<<<< HEAD
$(UTILSDIR)/mkmarkdown.py: mkmarkdown.py
	$(INSTALL) $< $@

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
$(UTILSDIR)/generate_last_commit_file.py: generate_last_commit_file.py
	$(INSTALL) $< $@

$(UTILSDIR)/g.echo$(EXE): $(OBJDIR)/g.echo.o
	$(call linker_base,$(LINK),$(LDFLAGS) $(EXTRA_LDFLAGS),$(MANIFEST_OBJ))
