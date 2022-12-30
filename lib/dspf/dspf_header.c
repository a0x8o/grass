#include <string.h>
#include <grass/gis.h>
#include "viz.h"

/*================= DOCUMENT RETURN VALUES! =================*/

int dfwrite_header(file_info *headp)
{
    int isize, flsize;
    cmndln_info *linep;
    FILE *fp;
    long Where_dataoff;

    linep = &(headp->linefax);
    fp = headp->dspfoutfp;

    isize = sizeof(int);
    flsize = sizeof(float);
    /* print the header code on first line of file */
    if (!fwrite(DSPF_ID, strlen(DSPF_ID), 1, fp))
        return (-1);
    /* the dimensions of the data */
    if (1 != fwrite(&headp->xdim, isize, 1, fp))
        return (-1);
    if (1 != fwrite(&headp->ydim, isize, 1, fp))
        return (-1);
    if (1 != fwrite(&headp->zdim, isize, 1, fp))
        return (-1);

    /* print out code for min and max values */
    if (1 != fwrite(&headp->min, flsize, 1, fp))
        return (-1);
    if (1 != fwrite(&headp->max, flsize, 1, fp))
        return (-1);

    /* the litmodel stored for each polygon */
    if (1 != fwrite(&linep->litmodel, isize, 1, fp))
        return (-1);

    /* write the total number of thresholds to be searched for */
    if (1 != fwrite(&linep->nthres, isize, 1, fp))
        return (-1);
    /* write the array of thresholds out */
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> main
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
>>>>>>> osgeo-main
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) != linep->nthres) {
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) != linep->nthres) {
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) != linep->nthres) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) != linep->nthres) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) != linep->nthres) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
>>>>>>> osgeo-main
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) !=
        (size_t)linep->nthres) {
=======
    if ((fwrite(linep->tvalue, flsize, linep->nthres, fp)) != linep->nthres) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
        fprintf(stderr, "ERROR: fwrite in dspf_header.c\n");
        return (-1);
    }

    /* write the offset to the lookup table */
    /* the first time this number is set to 0 */
    /*this information will be overwritten after dspf is done */
    /* G_ftell keeps track of where this information is to be placed */
    headp->Lookoff = 0;
    if (1 != fwrite(&headp->Lookoff, sizeof(long), 1, fp))
        return (-1);

    /* code to determine the length of the binary file header */
    /* Dataoff = length of the header */
    /*Dataoff = strlen (DSPF_ID) + 7*isize + 5*flsize + linep->nthres*flsize; */
    Where_dataoff = G_ftell(fp);
    headp->Dataoff = 0;
    if (1 != fwrite(&headp->Dataoff, sizeof(long), 1, fp))
        return (-1);

    /* End of header,  now go back and fill in what we can */
    headp->Dataoff = G_ftell(fp);
    G_fseek(fp, Where_dataoff, 0);
    if (1 != fwrite(&headp->Dataoff, sizeof(long), 1, fp))
        return (-1);

    G_fseek(fp, headp->Dataoff, 0); /* and return to begin writing data */

    /* will still have to come back once more to fill in Lookup offset */

    return (0);
}

/**************************** dfread_header **********************************/

/**************************** dfread_header **********************************/

/**************************** dfread_header **********************************/

int dfread_header(file_info *headp)
{
    int isize, flsize;
    FILE *fp;
    cmndln_info *linep;
    char buf[80];
    int len;

    fp = headp->dspfinfp;

    len = strlen(DSPF_ID);
    G_fseek(fp, 0L, 0); /* rewind file */
    /*read in header information and store in File_info struct */

    if (!fread(buf, 1, len, fp))
        return (-1);
    buf[len] = 0;
    if (strncmp(DSPF_ID, buf, len)) {
        if (!strncmp("dspf003.01", buf, len))
            return (dfread_header_old(headp, fp));

        fprintf(stderr, "Error: header mismatch '%s' - '%s'\n", DSPF_ID, buf);
        return (-1);
    }
    linep = &(headp->linefax);
    isize = sizeof(int);
    flsize = sizeof(float);

    if (!fread(&headp->xdim, isize, 1, fp))
        return (-1);
    if (!fread(&headp->ydim, isize, 1, fp))
        return (-1);
    if (!fread(&headp->zdim, isize, 1, fp))
        return (-1);
    if (!fread(&headp->min, flsize, 1, fp))
        return (-1);
    if (!fread(&headp->max, flsize, 1, fp))
        return (-1);
    if (!fread(&linep->litmodel, isize, 1, fp))
        return (-1);
    if (!fread(&linep->nthres, isize, 1, fp))
        return (-1);
    if (!fread(linep->tvalue, flsize, linep->nthres, fp))
        return (-1);
    if (!fread(&headp->Lookoff, isize, 1, fp))
        return (-1);
    if (!fread(&headp->Dataoff, isize, 1, fp))
        return (-1);

    print_head_info(headp);

    return (1);
}

int dfread_header_old(file_info *headp, FILE *fp)
{
    int isize, flsize;
    cmndln_info *linep;
    float tmp;

    linep = &(headp->linefax);
    isize = sizeof(int);
    flsize = sizeof(float);

    if (!fread(&headp->xdim, isize, 1, fp))
        return (-1);
    if (!fread(&headp->ydim, isize, 1, fp))
        return (-1);
    if (!fread(&headp->zdim, isize, 1, fp))
        return (-1);
    if (!fread(&tmp, flsize, 1, fp))
        return (-1);
    if (!fread(&tmp, flsize, 1, fp))
        return (-1);
    if (!fread(&tmp, flsize, 1, fp))
        return (-1);
    if (!fread(&headp->min, flsize, 1, fp))
        return (-1);
    if (!fread(&headp->max, flsize, 1, fp))
        return (-1);
    if (!fread(&linep->litmodel, isize, 1, fp))
        return (-1);
    if (!fread(&linep->nthres, isize, 1, fp))
        return (-1);
    if (!fread(linep->tvalue, flsize, linep->nthres, fp))
        return (-1);
    if (!fread(&headp->Lookoff, isize, 1, fp))
        return (-1);
    if (!fread(&headp->Dataoff, isize, 1, fp))
        return (-1);

    print_head_info(headp);

    return (1);
}
