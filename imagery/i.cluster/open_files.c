#include <stdlib.h>
#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/glocale.h>
#include "global.h"

int open_files(void)
{
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
    char *name, *mapset, **err, *semantic_label;
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    char *name, *mapset, **err, *semantic_label;
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    char *name, *mapset, **err, *semantic_label;
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    char *name, *mapset, **err, *semantic_label;
=======
>>>>>>> osgeo-main
=======
    char *name, *mapset, **err, *semantic_label;
=======
>>>>>>> osgeo-main
=======
    char *name, *mapset, **err, *semantic_label;
=======
>>>>>>> osgeo-main
    char *name, *mapset, **err, *bandref;
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
    char *name, *mapset, **err, *semantic_label;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    char *name, *mapset, **err, *semantic_label;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
    char *name, *mapset, **err, *semantic_label;
=======
    char *name, *mapset, **err, *bandref;
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
    char *name, *mapset, **err, *semantic_label;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    FILE *fd;
    int n, missing;

    I_init_group_ref(&ref);
    I_free_group_ref(&ref);
    I_get_subgroup_ref(group, subgroup, &ref);

<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
    semantic_labels = (char **)G_malloc(ref.nfiles * sizeof(char **));
    missing = 0;
    for (n = 0; n < ref.nfiles; n++) {
        name = ref.file[n].name;
        mapset = ref.file[n].mapset;
        if (G_find_raster(name, mapset) == NULL) {
            missing = 1;
            G_warning(_("Raster map <%s> do not exists in subgroup <%s>"),
                      G_fully_qualified_name(name, mapset), subgroup);
        }
        semantic_label = Rast_get_semantic_label_or_name(ref.file[n].name,
                                                         ref.file[n].mapset);
        semantic_labels[n] = G_store(semantic_label);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    bandrefs = (char **)G_malloc(ref.nfiles * sizeof(char **));
=======
    semantic_labels = (char **)G_malloc(ref.nfiles * sizeof(char **));
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    missing = 0;
    for (n = 0; n < ref.nfiles; n++) {
        name = ref.file[n].name;
        mapset = ref.file[n].mapset;
        if (G_find_raster(name, mapset) == NULL) {
            missing = 1;
            G_warning(_("Raster map <%s> do not exists in subgroup <%s>"),
                      G_fully_qualified_name(name, mapset), subgroup);
        }
<<<<<<< HEAD
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    bandrefs = (char **)G_malloc(ref.nfiles * sizeof(char **));
=======
    semantic_labels = (char **)G_malloc(ref.nfiles * sizeof(char **));
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    missing = 0;
    for (n = 0; n < ref.nfiles; n++) {
        name = ref.file[n].name;
        mapset = ref.file[n].mapset;
        if (G_find_raster(name, mapset) == NULL) {
            missing = 1;
            G_warning(_("Raster map <%s> do not exists in subgroup <%s>"),
                      G_fully_qualified_name(name, mapset), subgroup);
        }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
        bandref = Rast_read_bandref(ref.file[n].name, ref.file[n].mapset);
        if (!bandref)
            G_fatal_error(_("Raster map <%s@%s> lacks band reference"),
                            ref.file[n].name, ref.file[n].mapset);
        bandrefs[n] = G_store(bandref);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        semantic_label = Rast_get_semantic_label_or_name(ref.file[n].name,
                                                         ref.file[n].mapset);
        semantic_labels[n] = G_store(semantic_label);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
    }
    if (missing)
        G_fatal_error(_("No raster maps found"));

    if (ref.nfiles <= 1) {
        if (ref.nfiles <= 0)
            G_warning(_("Subgroup <%s> doesn't have any raster maps"),
                      subgroup);
        else
            G_warning(_("Subgroup <%s> only has 1 raster map"), subgroup);
        G_fatal_error(_("Subgroup must have at least 2 raster maps"));
    }

    cell = (DCELL **)G_malloc(ref.nfiles * sizeof(DCELL *));
    cellfd = (int *)G_malloc(ref.nfiles * sizeof(int));
    for (n = 0; n < ref.nfiles; n++) {
        cell[n] = Rast_allocate_d_buf();

        name = ref.file[n].name;
        mapset = ref.file[n].mapset;
        cellfd[n] = Rast_open_old(name, mapset);
    }

    if (insigfile) {
<<<<<<< HEAD
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
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
        fd = I_fopen_signature_file_old(insigfile);
        if (fd == NULL)
            G_fatal_error(_("Unable to open seed signature file <%s>"),
                          insigfile);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
	fd = I_fopen_signature_file_old(insigfile);
	if (fd == NULL)
	    G_fatal_error(_("Unable to open seed signature file <%s>"),
			  insigfile);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

        n = I_read_signatures(fd, &in_sig);
        fclose(fd);
        if (n < 0)
            G_fatal_error(_("Unable to read signature file <%s>"), insigfile);

        if (in_sig.nsigs > 255)
            G_fatal_error(_("<%s> has too many signatures (limit is 255)"),
                          insigfile);

<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
        err = I_sort_signatures_by_semantic_label(&in_sig, &ref);
        if (err)
            G_fatal_error(
                _("Signature - group member semantic label mismatch.\n"
                  "Extra signatures for bands: %s\n"
                  "Imagery group bands without signatures: %s"),
                err[0] ? err[0] : _("none"), err[1] ? err[1] : _("none"));

        maxclass = in_sig.nsigs;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
        err = I_sort_signatures_by_bandref(&in_sig, &ref);
=======
        err = I_sort_signatures_by_semantic_label(&in_sig, &ref);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        if (err)
            G_fatal_error(
                _("Signature - group member semantic label mismatch.\n"
                  "Extra signatures for bands: %s\n"
                  "Imagery group bands without signatures: %s"),
                err[0] ? err[0] : _("none"), err[1] ? err[1] : _("none"));

<<<<<<< HEAD
	maxclass = in_sig.nsigs;
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
        maxclass = in_sig.nsigs;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
        err = I_sort_signatures_by_bandref(&in_sig, &ref);
=======
        err = I_sort_signatures_by_semantic_label(&in_sig, &ref);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        if (err)
            G_fatal_error(
                _("Signature - group member semantic label mismatch.\n"
                  "Extra signatures for bands: %s\n"
                  "Imagery group bands without signatures: %s"),
                err[0] ? err[0] : _("none"), err[1] ? err[1] : _("none"));

<<<<<<< HEAD
	maxclass = in_sig.nsigs;
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
        maxclass = in_sig.nsigs;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    }

    return 0;
}
