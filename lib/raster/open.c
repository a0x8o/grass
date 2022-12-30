/*!
 * \file lib/raster/open.c
 *
 * \brief Raster Library - Open raster file
 *
 * (C) 1999-2009 by the GRASS Development Team
 *
 * This program is free software under the GNU General Public
 * License (>=v2). Read the file COPYING that comes with GRASS
 * for details.
 *
 * \author USACERL and many others
 */

#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>

#include <grass/config.h>
#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/glocale.h>

#include "R.h"
#define FORMAT_FILE "f_format"
#define NULL_FILE   "null"
/* cmpressed null file */
#define NULLC_FILE  "nullcmpr"

static int new_fileinfo(void)
{
    int oldsize = R__.fileinfo_count;
    int newsize = oldsize;
    int i;

    for (i = 0; i < oldsize; i++)
        if (R__.fileinfo[i].open_mode <= 0) {
            memset(&R__.fileinfo[i], 0, sizeof(struct fileinfo));
            R__.fileinfo[i].open_mode = -1;
            return i;
        }

    if (newsize < 20)
        newsize += 20;
    else
        newsize *= 2;

    R__.fileinfo = G_realloc(R__.fileinfo, newsize * sizeof(struct fileinfo));

    /* Mark all cell files as closed */
    for (i = oldsize; i < newsize; i++) {
        memset(&R__.fileinfo[i], 0, sizeof(struct fileinfo));
        R__.fileinfo[i].open_mode = -1;
    }

    R__.fileinfo_count = newsize;

    return oldsize;
}

/*!
 * \brief Open raster file
 *
 * Arrange for the NULL-value bitmap to be read as well as the raster
 * map. If no NULL-value bitmap exists, arrange for the production of
 * NULL-values based on zeros in the raster map. If the map is
 * floating-point, arrange for quantization to integer for
 * Rast_get_c_row(), et. al., by reading the quantization rules
 * for the map using Rast_read_quant(). If the programmer wants to read
 * the floating point map using uing quant rules other than the ones
 * stored in map's quant file, he/she should call Rast_set_quant_rules()
 * after the call to Rast_open_old().
 *
 * \param name map name
 * \param open_mode mode
 * \param map_type map type (CELL, FCELL, DCELL)
 *
 * \return open file descriptor ( >= 0) if successful
 */

static int open_raster_new(const char *name, int open_mode,
                           RASTER_MAP_TYPE map_type);

/*!
   \brief Open an existing integer raster map (cell)

   Opens the existing cell file <i>name</i> in the <i>mapset</i> for
   reading by Rast_get_row() with mapping into the current window.

   This routine opens the raster map <i>name</i> in <i>mapset</i> for
   reading. A nonnegative file descriptor is returned if the open is
   successful. Otherwise a diagnostic message is printed and a negative
   value is returned. This routine does quite a bit of work. Since
   GRASS users expect that all raster maps will be resampled into the
   current region, the resampling index for the raster map is prepared
   by this routine after the file is opened. The resampling is based on
   the active module region (see also \ref The_Region}. Preparation
   required for reading the various raster file formats (see \ref
   Raster_File_Format for an explanation of the various raster file
   formats) is also done.

   Diagnostics: warning message printed if open fails.

   \param name map name
   \param mapset mapset name where raster map <i>name</i> lives

   \return nonnegative file descriptor (int)
 */
int Rast_open_old(const char *name, const char *mapset)
{
    int fd = Rast__open_old(name, mapset);

    /* turn on auto masking, if not already on */
    Rast__check_for_auto_masking();
    /*
       if(R__.auto_mask <= 0)
       R__.mask_buf = Rast_allocate_c_buf();
       now we don't ever free it!, so no need to allocate it  (Olga)
     */
    /* mask_buf is used for reading MASK file when mask is set and
       for reading map rows when the null file doesn't exist */

    return fd;
}

/*!  \brief Lower level function, open cell files, supercell files,
   and the MASK file.

   Actions:
   - opens the named cell file, following reclass reference if
   named layer is a reclass layer.
   - creates the required mapping between the data and the window
   for use by the get_map_row family of routines.

   Diagnostics: Errors other than actual open failure will cause a
   diagnostic to be delivered through G_warning() open failure messages
   are left to the calling routine since the masking logic will want to
   issue a different warning.

   Note: This routine does NOT open the MASK layer. If it did we would
   get infinite recursion.  This routine is called to open the mask by
   Rast__check_for_auto_masking() which is called by Rast_open_old().

   \param name map name
   \param mapset mapset of cell file to be opened

   \return open file descriptor
 */
int Rast__open_old(const char *name, const char *mapset)
{
    struct fileinfo *fcb;
    int cell_fd, fd;
    char *cell_dir;
    const char *r_name;
    const char *r_mapset;
    struct Cell_head cellhd;
    int CELL_nbytes = 0; /* bytes per cell in CELL map */
    int reclass_flag;
    int MAP_NBYTES;
    RASTER_MAP_TYPE MAP_TYPE;
    struct Reclass reclass;
    char xname[GNAME_MAX], xmapset[GMAPSET_MAX];
    struct GDAL_link *gdal;
    struct R_vrt *vrt;

    Rast__init();

    G_unqualified_name(name, mapset, xname, xmapset);
    name = xname;
    mapset = xmapset;

    if (!G_find_raster2(name, mapset))
        G_fatal_error(_("Raster map <%s> not found"),
                      G_fully_qualified_name(name, mapset));

    /* Check for reclassification */
    reclass_flag = Rast_get_reclass(name, mapset, &reclass);

    switch (reclass_flag) {
    case 0:
        r_name = name;
        r_mapset = mapset;
        break;
    case 1:
        r_name = reclass.name;
        r_mapset = reclass.mapset;
        if (!G_find_raster2(r_name, r_mapset))
            G_fatal_error(
                _("Unable to open raster map <%s@%s> since it is a reclass "
                  "of raster map <%s@%s> which does not exist"),
                name, mapset, r_name, r_mapset);
        break;
    default: /* Error reading cellhd/reclass file */
        G_fatal_error(_("Error reading reclass file for raster map <%s>"),
                      G_fully_qualified_name(name, mapset));
        break;
    }

    /* read the cell header */
    Rast_get_cellhd(r_name, r_mapset, &cellhd);

    /* now check the type */
    MAP_TYPE = Rast_map_type(r_name, r_mapset);
    if (MAP_TYPE < 0)
        G_fatal_error(_("Error reading map type for raster map <%s>"),
                      G_fully_qualified_name(name, mapset));

    if (MAP_TYPE == CELL_TYPE)
    /* set the number of bytes for CELL map */
    {
        CELL_nbytes = cellhd.format + 1;
        if (CELL_nbytes < 1)
            G_fatal_error(
                _("Raster map <%s@%s>: format field in header file invalid"),
                r_name, r_mapset);
    }

    /* compressor */
    if (MAP_TYPE != CELL_TYPE) {
        /* fp maps do not use RLE */
        /* previously, compressed simply meant yes (ZLIB) or no
         * now compressed encodes compressor type
         * 0: not compressed
         * 1, 2: ZLIB
         * 3: LZ4
         * 4: BZIP2
         * etc */
        if (cellhd.compressed == 1)
            cellhd.compressed = 2;
    }
    /* test if compressor type is supported */
    if (!G_check_compressor(cellhd.compressed)) {
        G_fatal_error(_("Compression with %s is not supported in this GRASS "
                        "GIS installation"),
                      G_compressor_name(cellhd.compressed));
    }

    if (cellhd.proj != R__.rd_window.proj)
        G_fatal_error(
            _("Raster map <%s> is in different projection than current region. "
              "Found <%s>, should be <%s>."),
            G_fully_qualified_name(name, mapset),
            G_projection_name(cellhd.proj),
            G_projection_name(R__.rd_window.proj));

    if (cellhd.zone != R__.rd_window.zone)
        G_fatal_error(_("Raster map <%s> is in different zone (%d) than "
                        "current region (%d)"),
                      G_fully_qualified_name(name, mapset), cellhd.zone,
                      R__.rd_window.zone);

    /* when map is int warn if too large cell size */
    if (MAP_TYPE == CELL_TYPE && (unsigned int)CELL_nbytes > sizeof(CELL))
        G_fatal_error(_("Raster map <%s>: bytes per cell (%d) too large"),
                      G_fully_qualified_name(name, mapset), CELL_nbytes);

    /* record number of bytes per cell */
    if (MAP_TYPE == FCELL_TYPE) {
        cell_dir = "fcell";
        MAP_NBYTES = XDR_FLOAT_NBYTES;
    }
    else if (MAP_TYPE == DCELL_TYPE) {
        cell_dir = "fcell";
        MAP_NBYTES = XDR_DOUBLE_NBYTES;
    }
    else { /* integer */
        cell_dir = "cell";
        MAP_NBYTES = CELL_nbytes;
    }

    gdal = Rast_get_gdal_link(r_name, r_mapset);
    vrt = Rast_get_vrt(r_name, r_mapset);
    cell_fd = -1;
    if (gdal) {
#ifdef HAVE_GDAL
        cell_fd = -1;
#else
        G_fatal_error(_("Raster map <%s@%s> is a GDAL link but GRASS is "
                        "compiled without GDAL support"),
                      r_name, r_mapset);
#endif
    }
    else if (vrt) {
        cell_fd = -1;
    }
    else {
        /* now actually open file for reading */
        cell_fd = G_open_old(cell_dir, r_name, r_mapset);
        if (cell_fd < 0)
            G_fatal_error(_("Unable to open %s file for raster map <%s@%s>"),
                          cell_dir, r_name, r_mapset);
    }

    fd = new_fileinfo();
    fcb = &R__.fileinfo[fd];
    fcb->data_fd = cell_fd;

    fcb->map_type = MAP_TYPE;

    /* Save cell header */
    fcb->cellhd = cellhd;

    /* allocate null bitstream buffers for reading null rows */
    fcb->null_fd = -1;
    fcb->null_cur_row = -1;
    fcb->null_bits = Rast__allocate_null_bits(cellhd.cols);

    /* mark closed */
    fcb->open_mode = -1;

    /* save name and mapset */
    fcb->name = G_store(name);
    fcb->mapset = G_store(mapset);

    /* mark no data row in memory  */
    fcb->cur_row = -1;

    /* if reclass, copy reclass structure */
    if ((fcb->reclass_flag = reclass_flag))
        fcb->reclass = reclass;

    fcb->gdal = gdal;
    fcb->vrt = vrt;
    if (!gdal && !vrt) {
        /* check for compressed data format, making initial reads if necessary
         */
        if (Rast__check_format(fd) < 0) {
            close(cell_fd); /* warning issued by check_format() */
            G_fatal_error(_("Error reading format for <%s@%s>"), r_name,
                          r_mapset);
        }
    }

    if (!vrt) {
        /* create the mapping from cell file to window */
        Rast__create_window_mapping(fd);
    }

    /*
     * allocate the data buffer
     * number of bytes per cell is cellhd.format+1
     */

    /* for reading fcb->data is allocated to be fcb->cellhd.cols * fcb->nbytes
       (= XDR_FLOAT/DOUBLE_NBYTES) */
    fcb->data = (unsigned char *)G_calloc(fcb->cellhd.cols, MAP_NBYTES);

    /* initialize/read in quant rules for float point maps */
    if (fcb->map_type != CELL_TYPE) {
        if (fcb->reclass_flag)
            Rast_read_quant(fcb->reclass.name, fcb->reclass.mapset,
                            &(fcb->quant));
        else
            Rast_read_quant(fcb->name, fcb->mapset, &(fcb->quant));
    }

    /* now mark open for read: this must follow create_window_mapping() */
    fcb->open_mode = OPEN_OLD;
    fcb->io_error = 0;
    fcb->map_type = MAP_TYPE;
    fcb->nbytes = MAP_NBYTES;
    fcb->null_row_ptr = NULL;

    if (!gdal && !vrt) {
        /* First, check for compressed null file */
        fcb->null_fd =
            G_open_old_misc("cell_misc", NULL_FILE, r_name, r_mapset);
        if (fcb->null_fd < 0) {
            fcb->null_fd =
                G_open_old_misc("cell_misc", NULLC_FILE, r_name, r_mapset);
            if (fcb->null_fd >= 0) {
                fcb->null_row_ptr =
                    G_calloc(fcb->cellhd.rows + 1, sizeof(off_t));
                if (Rast__read_null_row_ptrs(fd, fcb->null_fd) < 0) {
                    close(fcb->null_fd);
                    fcb->null_fd = -1;
                    G_free(fcb->null_row_ptr);
                    fcb->null_row_ptr = NULL;
                }
            }
        }
        fcb->null_file_exists = fcb->null_fd >= 0;
    }

    return fd;
}

/*!
   \brief Opens a new cell file in a database (compressed)

   Opens a new cell file <i>name</i> in the current mapset for writing
   by Rast_put_row().

   The file is created and filled with no data it is assumed that the
   new cell file is to conform to the current window.

   The file must be written sequentially. Use Rast_open_new_random()
   for non sequential writes.

   Note: the open actually creates a temporary file Rast_close() will
   move the temporary file to the cell file and write out the necessary
   support files (cellhd, cats, hist, etc.).

   Diagnostics: warning message printed if open fails

   Warning: calls to Rast_set_window() made after opening a new cell file
   may create confusion and should be avoided the new cell file will be
   created to conform to the window at the time of the open.

   \param name map name

   \return open file descriptor ( >= 0) if successful
   \return negative integer if error
 */
int Rast_open_c_new(const char *name)
{
    return open_raster_new(name, OPEN_NEW_COMPRESSED, CELL_TYPE);
}

/*!
   \brief Opens a new cell file in a database (uncompressed)

   See also Rast_open_new().

   \param name map name

   \return open file descriptor ( >= 0) if successful
   \return negative integer if error
 */
int Rast_open_c_new_uncompressed(const char *name)
{
    return open_raster_new(name, OPEN_NEW_UNCOMPRESSED, CELL_TYPE);
}

/*!
   \brief Save histogram for newly create raster map (cell)

   If newly created cell files should have histograms, set flag=1
   otherwise set flag=0. Applies to subsequent opens.

   \param flag flag indicator
 */
void Rast_want_histogram(int flag)
{
    R__.want_histogram = flag;
}

/*!
   \brief Sets the format for subsequent opens on new integer cell files
   (uncompressed and random only).

   Warning: subsequent put_row calls will only write n+1 bytes per
   cell. If the data requires more, the cell file will be written
   incorrectly (but with n+1 bytes per cell)

   When writing float map: format is -1

   \param n format
 */
void Rast_set_cell_format(int n)
/* sets the format for integer raster map */
{
    R__.nbytes = n + 1;
    if (R__.nbytes <= 0)
        R__.nbytes = 1;
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
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d01c2a12f1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4130b8db48 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e5aeb1393 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7ef6112573 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d365e50fab (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dc8416910a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b2d4dc1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae49d6292b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 060d4359ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2727f115f1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d8b2703006 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
>>>>>>> 51c6907b22 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9eb4ab8390 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 576b696e91 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 50e307f19e (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81fd408422 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7b9fb7e19e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6007b09add (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 50fc95a76f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c2460610a9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
    if (R__.nbytes > (int)sizeof(CELL))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    if (R__.nbytes > (int)sizeof(CELL))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
    if (R__.nbytes > sizeof(CELL))
=======
    if (R__.nbytes > (int)sizeof(CELL))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    if (R__.nbytes > (int)sizeof(CELL))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5952770ec6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d01c2a12f1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 4130b8db48 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f76eb8a5c2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3e5aeb1393 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 7ef6112573 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 10cb905c76 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d365e50fab (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dc8416910a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d3f123638e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 268b2d4dc1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 580af7cb72 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ae49d6292b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c7104d8e5e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 060d4359ef (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 51c6907b22 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2656f886ff (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2727f115f1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1a771fd4a9 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d8b2703006 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c66f377132 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
>>>>>>> 9eb4ab8390 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
>>>>>>> 576b696e91 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
>>>>>>> 50e307f19e (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
    if (R__.nbytes > (int)sizeof(CELL))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if (R__.nbytes > (int)sizeof(CELL))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
>>>>>>> osgeo-main
    if (R__.nbytes > sizeof(CELL))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    if (R__.nbytes > (int)sizeof(CELL))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
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
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 576b696e91 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 50e307f19e (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
    if (R__.nbytes > sizeof(CELL))
=======
    if (R__.nbytes > (int)sizeof(CELL))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
    if (R__.nbytes > (int)sizeof(CELL))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cd91d8b03 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
    if (R__.nbytes > (int)sizeof(CELL))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    if (R__.nbytes > (int)sizeof(CELL))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (R__.nbytes > sizeof(CELL))
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
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
    if (R__.nbytes > (int)sizeof(CELL))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (R__.nbytes > sizeof(CELL))
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
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (R__.nbytes > (int)sizeof(CELL))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
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
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d01c2a12f1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4130b8db48 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3e5aeb1393 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7ef6112573 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d365e50fab (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dc8416910a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b2d4dc1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ae49d6292b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 060d4359ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 51c6907b22 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2727f115f1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d8b2703006 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9eb4ab8390 (r.horizon manual - fix typo (#2794))
=======
    if (R__.nbytes > sizeof(CELL))
=======
    if (R__.nbytes > (int)sizeof(CELL))
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
    if (R__.nbytes > (int)sizeof(CELL))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5952770ec6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d01c2a12f1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 4130b8db48 (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f76eb8a5c2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3e5aeb1393 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 7ef6112573 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 10cb905c76 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d365e50fab (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dc8416910a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d3f123638e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 268b2d4dc1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 580af7cb72 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ae49d6292b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c7104d8e5e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 060d4359ef (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 51c6907b22 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2656f886ff (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2727f115f1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1a771fd4a9 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d8b2703006 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (R__.nbytes > (int)sizeof(CELL))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 6cd91d8b03 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (R__.nbytes > (int)sizeof(CELL))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> c66f377132 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
>>>>>>> 9eb4ab8390 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
>>>>>>> 576b696e91 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
>>>>>>> 50e307f19e (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
>>>>>>> 81fd408422 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 7b9fb7e19e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 6007b09add (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
=======
=======
    if (R__.nbytes > (int)sizeof(CELL))
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
=======
    if (R__.nbytes > sizeof(CELL))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 50fc95a76f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
>>>>>>> c2460610a9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
        R__.nbytes = sizeof(CELL);
}

/*!
   \brief Get cell value format

   \param v cell

   \return cell format
 */
int Rast_get_cell_format(CELL v)
{
    unsigned int i;

    if (v >= 0)
        for (i = 0; i < sizeof(CELL); i++)
            if (!(v /= 256))
                return i;
    return sizeof(CELL) - 1;
}

/*!
   \brief Opens new fcell file in a database

   Opens a new floating-point map <i>name</i> in the current mapset for
   writing. The type of the file (i.e. either double or float) is
   determined and fixed at this point. The default is FCELL_TYPE. In
   order to change this default

   Use Rast_set_fp_type() where type is one of DCELL_TYPE or FCELL_TYPE.

   See warnings and notes for Rast_open_new().

   \param name map name

   \return nonnegative file descriptor (int)
 */
int Rast_open_fp_new(const char *name)
{
    return open_raster_new(name, OPEN_NEW_COMPRESSED, R__.fp_type);
}

/*!
   \brief Opens new fcell file in a database (uncompressed)

   See Rast_open_fp_new() for details.

   \param name map name

   \return nonnegative file descriptor (int)
 */
int Rast_open_fp_new_uncompressed(const char *name)
{
    return open_raster_new(name, OPEN_NEW_UNCOMPRESSED, R__.fp_type);
}

#ifdef HAVE_GDAL
static int open_raster_new_gdal(char *map, char *mapset,
                                RASTER_MAP_TYPE map_type)
{
    int fd;
    struct fileinfo *fcb;

    fd = new_fileinfo();
    fcb = &R__.fileinfo[fd];
    fcb->data_fd = -1;

    /* mark closed */
    fcb->map_type = map_type;
    fcb->open_mode = -1;

    fcb->gdal = Rast_create_gdal_link(map, map_type);
    if (!fcb->gdal)
        G_fatal_error(_("Unable to create GDAL link"));

    fcb->cellhd = R__.wr_window;
    fcb->cellhd.compressed = 0;
    fcb->nbytes = Rast_cell_size(fcb->map_type);
    /* for writing fcb->data is allocated to be R__.wr_window.cols *
       sizeof(CELL or DCELL or FCELL)  */
    fcb->data = G_calloc(R__.wr_window.cols, fcb->nbytes);

    fcb->name = map;
    fcb->mapset = mapset;
    fcb->cur_row = 0;

    fcb->row_ptr = NULL;
    fcb->temp_name = NULL;
    fcb->null_temp_name = NULL;
    fcb->null_cur_row = 0;
    fcb->null_bits = NULL;
    fcb->null_fd = -1;
    fcb->null_row_ptr = NULL;

    if (fcb->map_type != CELL_TYPE)
        Rast_quant_init(&(fcb->quant));

    /* init cell stats */
    /* now works only for int maps */
    if (fcb->map_type == CELL_TYPE)
        if ((fcb->want_histogram = R__.want_histogram))
            Rast_init_cell_stats(&fcb->statf);

    /* init range and if map is double/float init d/f_range */
    Rast_init_range(&fcb->range);

    if (fcb->map_type != CELL_TYPE)
        Rast_init_fp_range(&fcb->fp_range);

    /* mark file as open for write */
    fcb->open_mode = OPEN_NEW_UNCOMPRESSED;
    fcb->io_error = 0;

    return fd;
}
#endif /* HAVE_GDAL */

static int open_raster_new(const char *name, int open_mode,
                           RASTER_MAP_TYPE map_type)
{
    char xname[GNAME_MAX], xmapset[GMAPSET_MAX];
    struct fileinfo *fcb;
    int fd, cell_fd;
    char *tempname;
    char *map;
    char *mapset;
    const char *cell_dir;
    int nbytes;

    Rast__init();

    switch (map_type) {
    case CELL_TYPE:
        cell_dir = "cell";
        nbytes = R__.nbytes;
        break;
    case FCELL_TYPE:
        nbytes = XDR_FLOAT_NBYTES;
        cell_dir = "fcell";
        break;
    case DCELL_TYPE:
        nbytes = XDR_DOUBLE_NBYTES;
        cell_dir = "fcell";
        break;
    default:
        G_fatal_error(_("Invalid map type <%d>"), map_type);
        break;
    }

    if (G_unqualified_name(name, G_mapset(), xname, xmapset) < 0)
        G_fatal_error(_("Raster map <%s> is not in the current mapset (%s)"),
                      name, G_mapset());
    map = G_store(xname);
    mapset = G_store(xmapset);

    /* check for legal grass name */
    if (G_legal_filename(map) < 0)
        G_fatal_error(_("<%s> is an illegal file name"), map);

#ifdef HAVE_GDAL
    if (G_find_file2("", "GDAL", G_mapset()))
        return open_raster_new_gdal(map, mapset, map_type);
#endif

    /* open a tempfile name */
    tempname = G_tempfile();
    cell_fd = creat(tempname, 0666);
    if (cell_fd < 0) {
        int err = errno;

        G_free(mapset);
        G_free(tempname);
        G_free(map);
        G_fatal_error(_("No temp files available: %s"), strerror(err));
    }

    fd = new_fileinfo();
    fcb = &R__.fileinfo[fd];
    fcb->data_fd = cell_fd;

    /*
     * since we are bypassing the normal open logic
     * must create the cell element
     */
    G_make_mapset_object_group(cell_dir);

    /* mark closed */
    fcb->map_type = map_type;
    fcb->open_mode = -1;
    fcb->gdal = NULL;
    fcb->vrt = NULL;

    /* for writing fcb->data is allocated to be R__.wr_window.cols *
       sizeof(CELL or DCELL or FCELL)  */
    fcb->data = (unsigned char *)G_calloc(R__.wr_window.cols,
                                          Rast_cell_size(fcb->map_type));

    /*
     * copy current window into cell header
     * set format to cell/supercell
     * for compressed writing
     *   allocate space to hold the row address array
     */
    fcb->cellhd = R__.wr_window;

    /* change open_mode to OPEN_NEW_UNCOMPRESSED if R__.compression_type == 0 ?
     */

    if (open_mode == OPEN_NEW_COMPRESSED && fcb->map_type == CELL_TYPE) {
        fcb->row_ptr = G_calloc(fcb->cellhd.rows + 1, sizeof(off_t));
        G_zero(fcb->row_ptr, (fcb->cellhd.rows + 1) * sizeof(off_t));
        Rast__write_row_ptrs(fd);
        fcb->cellhd.compressed = R__.compression_type;

        fcb->nbytes = 1; /* to the minimum */
    }
    else {
        fcb->nbytes = nbytes;
        if (open_mode == OPEN_NEW_COMPRESSED) {
            fcb->row_ptr = G_calloc(fcb->cellhd.rows + 1, sizeof(off_t));
            G_zero(fcb->row_ptr, (fcb->cellhd.rows + 1) * sizeof(off_t));
            Rast__write_row_ptrs(fd);
            fcb->cellhd.compressed = R__.compression_type;
        }
        else
            fcb->cellhd.compressed = 0;

        if (fcb->map_type != CELL_TYPE) {
            Rast_quant_init(&(fcb->quant));
        }
    }
    if (open_mode == OPEN_NEW_COMPRESSED && fcb->map_type != CELL_TYPE &&
        fcb->cellhd.compressed == 1) {
        /* fp maps do not use RLE */
        fcb->cellhd.compressed = 2;
    }

    /* save name and mapset, and tempfile name */
    fcb->name = map;
    fcb->mapset = mapset;
    fcb->temp_name = tempname;

    /* next row to be written (in order) is zero */
    fcb->cur_row = 0;

    /* open a null tempfile name */
    tempname = G_tempfile();
    fcb->null_fd = creat(tempname, 0666);
    if (fcb->null_fd < 0) {
        int err = errno;

        G_free(tempname);
        G_free(fcb->name);
        G_free(fcb->mapset);
        G_free(fcb->temp_name);
        close(cell_fd);
        G_fatal_error(_("No temp files available: %s"), strerror(err));
    }

    fcb->null_temp_name = tempname;

    fcb->null_row_ptr = NULL;
    if (R__.compress_nulls) {
        fcb->null_row_ptr = G_calloc(fcb->cellhd.rows + 1, sizeof(off_t));
        G_zero(fcb->null_row_ptr, (fcb->cellhd.rows + 1) * sizeof(off_t));
        Rast__write_null_row_ptrs(fd, fcb->null_fd);
    }

    /* next row to be written (in order) is zero */
    fcb->null_cur_row = 0;

    /* allocate null bitstream buffer for writing */
    fcb->null_bits = Rast__allocate_null_bits(fcb->cellhd.cols);

    /* init cell stats */
    /* now works only for int maps */
    if (fcb->map_type == CELL_TYPE)
        if ((fcb->want_histogram = R__.want_histogram))
            Rast_init_cell_stats(&fcb->statf);

    /* init range and if map is double/float init d/f_range */
    Rast_init_range(&fcb->range);

    if (fcb->map_type != CELL_TYPE)
        Rast_init_fp_range(&fcb->fp_range);

    /* mark file as open for write */
    fcb->open_mode = open_mode;
    fcb->io_error = 0;

    return fd;
}

int Rast__open_null_write(const char *name)
{
    char xname[GNAME_MAX], xmapset[GMAPSET_MAX];
    struct fileinfo *fcb;
    int fd;
    char *tempname;
    char *map;
    char *mapset;

    Rast__init();

    if (!G_find_raster2(name, G_mapset()))
        G_fatal_error(
            _("Raster map <%s> does not exist in the current mapset (%s)"),
            name, G_mapset());

    if (G_unqualified_name(name, G_mapset(), xname, xmapset) < 0)
        G_fatal_error(_("Raster map <%s> is not in the current mapset (%s)"),
                      name, G_mapset());
    map = G_store(xname);
    mapset = G_store(xmapset);

    fd = new_fileinfo();
    fcb = &R__.fileinfo[fd];

    G_zero(fcb, sizeof(*fcb));

    fcb->name = map;
    fcb->mapset = mapset;

    Rast_get_cellhd(map, mapset, &fcb->cellhd);

    /* open a null tempfile name */
    tempname = G_tempfile();
    fcb->null_fd = creat(tempname, 0666);
    if (fcb->null_fd < 0) {
        int err = errno;

        G_free(tempname);
        G_free(fcb->name);
        G_free(fcb->mapset);
        G_fatal_error(_("No temp files available: %s"), strerror(err));
    }
    fcb->null_temp_name = tempname;

    if (R__.compress_nulls) {
        fcb->null_row_ptr = G_calloc(fcb->cellhd.rows + 1, sizeof(off_t));
        G_zero(fcb->null_row_ptr, (fcb->cellhd.rows + 1) * sizeof(off_t));
        Rast__write_null_row_ptrs(fd, fcb->null_fd);
    }

    /* allocate null bitstream buffer for writing */
    fcb->null_bits = Rast__allocate_null_bits(fcb->cellhd.cols);

    return fd;
}

/*!
   \brief Set raster map floating-point data format.

   This controls the storage type for floating-point maps. It affects
   subsequent calls to G_open_fp_map_new(). The <i>type</i> must be
   one of FCELL_TYPE (float) or DCELL_TYPE (double). The use of this
   routine by applications is discouraged since its use would override
   user preferences.

   \param type raster data type

   \return void
 */
void Rast_set_fp_type(RASTER_MAP_TYPE map_type)
{
    Rast__init();

    switch (map_type) {
    case FCELL_TYPE:
    case DCELL_TYPE:
        R__.fp_type = map_type;
        break;
    default:
        G_fatal_error(_("Rast_set_fp_type(): can only be called with "
                        "FCELL_TYPE or DCELL_TYPE"));
        break;
    }
}

/*!
   \brief Check if raster map is floating-point

   Returns true (1) if raster map <i>name</i> in <i>mapset</i>
   is a floating-point dataset; false(0) otherwise.

   \param name map name
   \param mapset mapset name

   \return 1 floating-point
   \return 0 int
 */
int Rast_map_is_fp(const char *name, const char *mapset)
{
    char path[GPATH_MAX];
    const char *xmapset;

    xmapset = G_find_raster2(name, mapset);
    if (!xmapset)
        G_fatal_error(_("Raster map <%s> not found"),
                      G_fully_qualified_name(name, mapset));

    G_file_name(path, "fcell", name, xmapset);
    if (access(path, 0) == 0)
        return 1;

    G_file_name(path, "g3dcell", name, xmapset);
    if (access(path, 0) == 0)
        return 1;

    return 0;
}

/*!
   \brief Determine raster data type

   Determines if the raster map is floating point or integer. Returns
   DCELL_TYPE for double maps, FCELL_TYPE for float maps, CELL_TYPE for
   integer maps, -1 if error has occurred

   \param name map name
   \param mapset mapset where map <i>name</i> lives

   \return raster data type
 */
RASTER_MAP_TYPE Rast_map_type(const char *name, const char *mapset)
{
    char path[GPATH_MAX];
    const char *xmapset;

    xmapset = G_find_raster2(name, mapset);
    if (!xmapset) {
        if (mapset && *mapset)
            G_fatal_error(_("Raster map <%s> not found in mapset <%s>"), name,
                          mapset);
        else
            G_fatal_error(_("Raster map <%s> not found"), name);
    }

    G_file_name(path, "fcell", name, xmapset);

    if (access(path, 0) == 0)
        return Rast__check_fp_type(name, xmapset);

    G_file_name(path, "g3dcell", name, xmapset);

    if (access(path, 0) == 0)
        return DCELL_TYPE;

    return CELL_TYPE;
}

/*!
   \brief Determine raster type from descriptor

   Determines if the raster map is floating point or integer. Returns
   DCELL_TYPE for double maps, FCELL_TYPE for float maps, CELL_TYPE for
   integer maps, -1 if error has occurred

   \param fd file descriptor

   \return raster data type
 */
RASTER_MAP_TYPE Rast_get_map_type(int fd)
{
    struct fileinfo *fcb = &R__.fileinfo[fd];

    return fcb->map_type;
}

/*!
   \brief Determines whether the floating points cell file has double or float
   type

   \param name map name
   \param mapset mapset where map <i>name</i> lives

   \return raster type (fcell, dcell)
 */
RASTER_MAP_TYPE Rast__check_fp_type(const char *name, const char *mapset)
{
    char path[GPATH_MAX];
    struct Key_Value *format_keys;
    const char *str, *str1;
    RASTER_MAP_TYPE map_type;
    const char *xmapset;

    xmapset = G_find_raster2(name, mapset);
    if (!xmapset)
        G_fatal_error(_("Raster map <%s> not found"),
                      G_fully_qualified_name(name, mapset));

    G_file_name_misc(path, "cell_misc", FORMAT_FILE, name, xmapset);

    if (access(path, 0) != 0)
        G_fatal_error(_("Unable to find '%s'"), path);

    format_keys = G_read_key_value_file(path);

    if ((str = G_find_key_value("type", format_keys)) != NULL) {
        if (strcmp(str, "double") == 0)
            map_type = DCELL_TYPE;
        else if (strcmp(str, "float") == 0)
            map_type = FCELL_TYPE;
        else {
            G_free_key_value(format_keys);
            G_fatal_error(_("Invalid type: field '%s' in file '%s'"), str,
                          path);
        }
    }
    else {
        G_free_key_value(format_keys);
        G_fatal_error(_("Missing type: field in file '%s'"), path);
    }

    if ((str1 = G_find_key_value("byte_order", format_keys)) != NULL) {
        if (strcmp(str1, "xdr") != 0)
            G_warning(_("Raster map <%s> is not xdr: byte_order: %s"), name,
                      str);
        /* here read and translate  byte order if not using xdr */
    }
    G_free_key_value(format_keys);
    return map_type;
}

/*!
   \brief Opens a new raster map

   Opens a new raster map of type <i>wr_type</i>

   See warnings and notes for Rast_open_new().

   Supported data types:
   - CELL_TYPE
   - FCELL_TYPE
   - DCELL_TYPE

   On CELL_TYPE calls Rast_open_new() otherwise Rast_open_fp_new().

   \param name map name
   \param wr_type raster data type

   \return nonnegative file descriptor (int)
 */
int Rast_open_new(const char *name, RASTER_MAP_TYPE wr_type)
{
    return open_raster_new(name, OPEN_NEW_COMPRESSED, wr_type);
}

/*!
   \brief Opens a new raster map (uncompressed)

   See Rast_open_new().

   \param name map name
   \param wr_type raster data type

   \return nonnegative file descriptor (int)
 */
int Rast_open_new_uncompressed(const char *name, RASTER_MAP_TYPE wr_type)
{
    return open_raster_new(name, OPEN_NEW_UNCOMPRESSED, wr_type);
}

/*!
   \brief Sets quant translation rules for raster map opened for
   reading.

   Returned by Rast_open_old(). After calling this function,
   Rast_get_c_row() and Rast_get_c_row() will use rules defined by q
   (instead of using rules defined in map's quant file) to convert floats to
   ints.

   \param fd file descriptor (cell file)
   \param q pointer to Quant structure

   \return void
 */
void Rast_set_quant_rules(int fd, struct Quant *q)
{
    struct fileinfo *fcb = &R__.fileinfo[fd];
    CELL cell;
    DCELL dcell;
    struct Quant_table *p;

    if (fcb->open_mode != OPEN_OLD)
        G_fatal_error(_("Rast_set_quant_rules() can be called only for "
                        "raster maps opened for reading"));

    /* copy all info from q to fcb->quant) */
    Rast_quant_init(&fcb->quant);
    if (q->truncate_only) {
        Rast_quant_truncate(&fcb->quant);
        return;
    }

    for (p = &(q->table[q->nofRules - 1]); p >= q->table; p--)
        Rast_quant_add_rule(&fcb->quant, p->dLow, p->dHigh, p->cLow, p->cHigh);
    if (Rast_quant_get_neg_infinite_rule(q, &dcell, &cell) > 0)
        Rast_quant_set_neg_infinite_rule(&fcb->quant, dcell, cell);
    if (Rast_quant_get_pos_infinite_rule(q, &dcell, &cell) > 0)
        Rast_quant_set_pos_infinite_rule(&fcb->quant, dcell, cell);
}
