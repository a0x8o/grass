MODULE_TOPDIR = ..

SUBDIRS = timer g.html2man

include $(MODULE_TOPDIR)/include/Make/Dir.make
include $(MODULE_TOPDIR)/include/Make/Compile.make

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
default: parsubdirs $(UTILSDIR)/mkhtml.py \
	$(UTILSDIR)/generate_last_commit_file.py \
	$(UTILSDIR)/g.echo$(EXE)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

$(UTILSDIR)/mkhtml.py: mkhtml.py
	$(INSTALL) $< $@

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
$(UTILSDIR)/mkmarkdown.py: mkmarkdown.py
	$(INSTALL) $< $@

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
$(UTILSDIR)/generate_last_commit_file.py: generate_last_commit_file.py
	$(INSTALL) $< $@

$(UTILSDIR)/g.echo$(EXE): $(OBJDIR)/g.echo.o
	$(call linker_base,$(LINK),$(LDFLAGS) $(EXTRA_LDFLAGS),$(MANIFEST_OBJ))
