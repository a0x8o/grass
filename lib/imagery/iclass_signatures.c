/*!
   \file lib/imagery/iclass_statistics.c

   \brief Imagery library - functions for wx.iclass

   Computation based on training areas for supervised classification.
   Based on i.class module (GRASS 6).

   Computation and writing signatures to file.

   Copyright (C) 1999-2007, 2011 by the GRASS Development Team

   This program is free software under the GNU General Public License
   (>=v2).  Read the file COPYING that comes with GRASS for details.

   \author David Satnik, Central Washington University (original author)
   \author Markus Neteler <neteler itc.it> (i.class module)
   \author Bernhard Reiter <bernhard intevation.de> (i.class module)
   \author Brad Douglas <rez touchofmadness.com>(i.class module)
   \author Glynn Clements <glynn gclements.plus.com> (i.class module)
   \author Hamish Bowman <hamish_b yahoo.com> (i.class module)
   \author Jan-Oliver Wagner <jan intevation.de> (i.class module)
   \author Anna Kratochvilova <kratochanna gmail.com> (rewriting for wx.iclass)
   \author Vaclav Petras <wenzeslaus gmail.com> (rewriting for wx.iclass)
 */

#include <string.h>
#include <stdio.h>

#include <grass/imagery.h>
#include <grass/glocale.h>
#include <grass/colors.h>

#include "iclass_local_proto.h"

/*!
   \brief Initialize signatures.

   \param[out] sigs pointer to signatures
   \param refer pointer to band files structure

   \return 1 on success
   \return 0 on failure
 */
int I_iclass_init_signatures(struct Signature *sigs, struct Ref *refer)
{
    G_debug(3, "I_iclass_init_signatures()");

    I_init_signatures(sigs, refer->nfiles);
    for (unsigned int i = refer->nfiles; i--;) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
>>>>>>> osgeo-main
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
>>>>>>> osgeo-main
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
>>>>>>> osgeo-main
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> osgeo-main
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
>>>>>>> osgeo-main
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
>>>>>>> osgeo-main
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
>>>>>>> osgeo-main
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
>>>>>>> osgeo-main
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
>>>>>>> osgeo-main
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
>>>>>>> osgeo-main
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
=======
>>>>>>> osgeo-main
        sigs->bandrefs[i] = Rast_read_bandref(refer->file[i].name, refer->file[i].mapset);
        if (!sigs->bandrefs[i]) {
            G_warning(_("Raster map <%s@%s> lacks band reference"),
                refer->file[i].name, refer->file[i].mapset);
            return 0;
        }
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        sigs->semantic_labels[i] = Rast_get_semantic_label_or_name(
            refer->file[i].name, refer->file[i].mapset);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> main
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    }

    return 1;
}

/*!
   \brief Add one signature.

   \param[out] sigs pointer to signatures
   \param statistics pointer to statistics structure
 */
void I_iclass_add_signature(struct Signature *sigs,
                            IClass_statistics *statistics)
{
    int sn;

    int b1, b2;

    int r, g, b;

    G_debug(3, "I_iclass_add_signature()");

    G_str_to_color(statistics->color, &r, &g, &b);

    /* get a new signature */
    I_new_signature(sigs);

    /* save the signature in a Sig structure */
    sn = sigs->nsigs;
    strcpy(sigs->sig[sn - 1].desc, statistics->name);
    sigs->sig[sn - 1].npoints = statistics->ncells;
    sigs->sig[sn - 1].status = 1;

    sigs->sig[sn - 1].have_color = 1;
    sigs->sig[sn - 1].r = r;
    sigs->sig[sn - 1].g = g;
    sigs->sig[sn - 1].b = b;

    for (b1 = 0; b1 < sigs->nbands; b1++) {
        sigs->sig[sn - 1].mean[b1] = statistics->band_mean[b1];
        for (b2 = 0; b2 <= b1; b2++) {
            sigs->sig[sn - 1].var[b1][b2] = var_signature(statistics, b1, b2);
        }
    }
}

/*!
   \brief Write signtures to signature file.

   \param sigs pointer to signatures
   \param file_name name of signature file

   \return 1 on success
   \return 0 on failure
 */
int I_iclass_write_signatures(struct Signature *sigs, const char *file_name)
{
    FILE *outsig_fd;

    G_debug(3, "I_write_signatures(): file_name=%s", file_name);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    if (!(outsig_fd = I_fopen_signature_file_new(file_name))) {
        G_warning(_("Unable to open output signature file '%s'"), file_name);
        return 0;
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> main
    if (!(outsig_fd = I_fopen_signature_file_new(file_name))) {
        G_warning(_("Unable to open output signature file '%s'"), file_name);
        return 0;
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    if (!
	(outsig_fd =
	 I_fopen_signature_file_new(file_name))) {
	G_warning(_("Unable to open output signature file '%s'"), file_name);
	return 0;
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    if (!(outsig_fd = I_fopen_signature_file_new(file_name))) {
        G_warning(_("Unable to open output signature file '%s'"), file_name);
        return 0;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    if (!(outsig_fd = I_fopen_signature_file_new(file_name))) {
        G_warning(_("Unable to open output signature file '%s'"), file_name);
        return 0;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> main
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    }

    I_write_signatures(outsig_fd, sigs);
    fclose(outsig_fd);

    return 1;
}
