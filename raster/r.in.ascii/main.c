/****************************************************************************
 *
 * MODULE:       r.in.ascii
 * AUTHOR(S):    Michael Shapiro, CERL (original contributor)
 *               Markus Neteler <neteler itc.it>,
 *               Hamish Bowman <hamish_b yahoo.com>,
 *               Roberto Flor <flor itc.it>,
 *               Roger Miller <rgrmill rt66 com>,
 *               Brad Douglas <rez touchofmadness.com>,
 *               Huidae Cho <grass4u gmail.com>,
 *               Glynn Clements <glynn gclements.plus.com>
 *               Jachym Cepicky <jachym les-ejk.cz>,
 *               Jan-Oliver Wagner <jan intevation.de>,
 *               Justin Hickey <jhickey hpcc.nectec.or.th>
 * PURPOSE:      Import ASCII or SURFER files
 * COPYRIGHT:    (C) 1999-2006 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 *****************************************************************************/

#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/glocale.h>
#include "local_proto.h"

FILE *Tmp_fd = NULL;
char *Tmp_file = NULL;

const float GS_BLANK = 1.70141E+038;

static int file_cpy(FILE *, FILE *);

int main(int argc, char *argv[])
{
    char *input;
    char *output;
    char *title;
    char *temp;
    FILE *fd, *ft;
    int cf, direction, sz;
    struct Cell_head cellhd;
    struct History history;
    void *rast, *rast_ptr;
    int row, col;
    int nrows, ncols;
    double x;
    char y[128];
    struct GModule *module;
    struct {
        struct Option *input, *output, *title, *mult, *nv, *type;
    } parm;
    struct {
        struct Flag *s;
    } flag;
    char *null_val_str;
    DCELL mult;
    RASTER_MAP_TYPE data_type;

    G_gisinit(argv[0]);

    module = G_define_module();
    G_add_keyword(_("raster"));
    G_add_keyword(_("import"));
    G_add_keyword(_("conversion"));
    G_add_keyword("ASCII");
    module->description =
        _("Converts a GRASS ASCII raster file to binary raster map.");

    parm.input = G_define_standard_option(G_OPT_F_INPUT);
    parm.input->label = _("Name of input file to be imported");
    parm.input->description = _("'-' for standard input");

    parm.output = G_define_standard_option(G_OPT_R_OUTPUT);

    parm.type = G_define_standard_option(G_OPT_R_TYPE);
    parm.type->required = NO;
    parm.type->description =
        _("Default: CELL for integer values, DCELL for floating-point values");

    parm.title = G_define_option();
    parm.title->key = "title";
    parm.title->key_desc = "phrase";
    parm.title->type = TYPE_STRING;
    parm.title->required = NO;
    parm.title->description = _("Title for resultant raster map");

    parm.mult = G_define_option();
    parm.mult->key = "multiplier";
    parm.mult->type = TYPE_DOUBLE;
    parm.mult->description = _("Default: read from header");
    parm.mult->required = NO;
    parm.mult->label = _("Multiplier for ASCII data");

    parm.nv = G_define_standard_option(G_OPT_M_NULL_VALUE);
    parm.nv->description = _("Default: read from header");
    parm.nv->label = _("String representing NULL value data cell");
    parm.nv->guisection = _("NULL data");

    flag.s = G_define_flag();
    flag.s->key = 's';
    flag.s->description =
        _("SURFER (Golden Software) ASCII file will be imported");

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);

    input = parm.input->answer;
    output = parm.output->answer;

    temp = G_tempfile();
    ft = fopen(temp, "w+");
    if (ft == NULL)
        G_fatal_error(_("Unable to open temporary file <%s>"), temp);

    if ((title = parm.title->answer))
        G_strip(title);

    if (!parm.mult->answer)
        Rast_set_d_null_value(&mult, 1);
    else if ((sscanf(parm.mult->answer, "%lf", &mult)) != 1)
        G_fatal_error(_("Wrong entry for multiplier: %s"), parm.mult->answer);

    null_val_str = parm.nv->answer;

    data_type = -1;
    if (parm.type->answer) {
        switch (parm.type->answer[0]) {
        case 'C':
            data_type = CELL_TYPE;
            break;
        case 'F':
            data_type = FCELL_TYPE;
            break;
        case 'D':
            data_type = DCELL_TYPE;
            break;
        }
    }

    if (strcmp(input, "-") == 0) {
        Tmp_file = G_tempfile();
        if (NULL == (Tmp_fd = fopen(Tmp_file, "w+")))
            G_fatal_error(_("Unable to open temporary file <%s>"), Tmp_file);
        unlink(Tmp_file);
        if (0 > file_cpy(stdin, Tmp_fd))
            G_fatal_error(_("Unable to read input from stdin"));
        fd = Tmp_fd;
    }
    else
        fd = fopen(input, "r");

    if (fd == NULL) {
        G_fatal_error(_("Unable to read input from <%s>"), input);
    }

    direction = 1;
    sz = 0;
    if (flag.s->answer) {
        sz = getgrdhead(fd, &cellhd);
        /* for Surfer files, the data type is always FCELL_TYPE,
           the multiplier and the null_val_str are never used */
        data_type = FCELL_TYPE;
        mult = 1.;
        null_val_str = "";
        /* rows in surfer files are ordered from bottom to top,
           opposite of normal GRASS ordering */
        direction = -1;
    }
    else
        sz = gethead(fd, &cellhd, &data_type, &mult, &null_val_str);

    if (!sz)
        G_fatal_error(_("Can't get cell header"));

    nrows = cellhd.rows;
    ncols = cellhd.cols;
    Rast_set_window(&cellhd);

    if (nrows != Rast_window_rows())
        G_fatal_error(_("OOPS: rows changed from %d to %d"), nrows,
                      Rast_window_rows());
    if (ncols != Rast_window_cols())
        G_fatal_error(_("OOPS: cols changed from %d to %d"), ncols,
                      Rast_window_cols());

    rast_ptr = Rast_allocate_buf(data_type);
    rast = rast_ptr;
    cf = Rast_open_new(output, data_type);
    for (row = 0; row < nrows; row++) {
        G_percent(row, nrows, 2);
        for (col = 0; col < ncols; col++) {
            if (fscanf(fd, "%s", y) != 1) {
                Rast_unopen(cf);
                G_fatal_error(_("Data conversion failed at row %d, col %d"),
                              row + 1, col + 1);
            }
            if (strcmp(y, null_val_str)) {
                x = atof(y);
                if ((float)x == GS_BLANK) {
                    Rast_set_null_value(rast_ptr, 1, data_type);
                }
                else {
                    Rast_set_d_value(rast_ptr, (DCELL)(x * mult), data_type);
                }
            }
            else {
                Rast_set_null_value(rast_ptr, 1, data_type);
            }
            rast_ptr = G_incr_void_ptr(rast_ptr, Rast_cell_size(data_type));
        }
        fwrite(rast, Rast_cell_size(data_type), ncols, ft);
        rast_ptr = rast;
    }
    G_percent(nrows, nrows, 2);
    G_debug(1, "Creating support files for %s", output);

    sz = 0;
    if (direction < 0) {
        sz = -ncols * Rast_cell_size(data_type);
        G_fseek(ft, sz, SEEK_END);
        sz *= 2;
    }
    else {
        G_fseek(ft, 0L, SEEK_SET);
    }

    for (row = 0; row < nrows; row += 1) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
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
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
>>>>>>> osgeo-main
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
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
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
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
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
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
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
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
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != (size_t)ncols)
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
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
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        if (fread(rast, Rast_cell_size(data_type), ncols, ft) != ncols)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Read from file error: %s"), strerror(errno));
        Rast_put_row(cf, rast, data_type);
        G_fseek(ft, sz, SEEK_CUR);
    }
    fclose(ft);
    unlink(temp);

    Rast_close(cf);

    if (title)
        Rast_put_cell_title(output, title);

    Rast_short_history(output, "raster", &history);
    Rast_command_history(&history);
    Rast_write_history(output, &history);

    G_done_msg(" ");

    exit(EXIT_SUCCESS);
}

static int file_cpy(FILE *from, FILE *to)
{
    char buf[BUFSIZ];
    size_t size;
    int written = 0;

    while (1) {
        size = fread(buf, 1, BUFSIZ, from);
        if (!size) {
            if (written) {
                fflush(to);
                G_fseek(to, 0L, SEEK_SET);
            }
            return (0);
        }
        if (!fwrite(buf, 1, size, to)) {
            G_warning(_("Unable to write to file"));
            return (-1);
        }
        written = 1;
    }

    /* NOTREACHED */
    return -1;
}
