/*****************************************************************************
 *
 * MODULE:       r.in.png
 * AUTHOR(S):    Michael Shapiro - CERL
 *               Alex Shevlakov - sixote@yahoo.com
 *               Glynn Clements
 * PURPOSE:      Import non-georeferenced Images in PNG format.
 * COPYRIGHT:    (C) 2000-2002, 2010-2011 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 *****************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <png.h>

#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/glocale.h>

typedef struct {
    const char suffix[4];
    int active;
    int fd;
    CELL *buf;
    FCELL *fbuf;
    CELL maxval;
    char name[256];
} channel;

#define C_Y 0
#define C_P 1
#define C_R 2
#define C_G 3
#define C_B 4
#define C_A 5

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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
static channel channels[6] = {{.suffix = ""},   {.suffix = ""},
                              {.suffix = ".r"}, {.suffix = ".g"},
                              {.suffix = ".b"}, {.suffix = ".a"}};
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
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
static channel channels[6] = {{.suffix = ""},   {.suffix = ""},
                              {.suffix = ".r"}, {.suffix = ".g"},
                              {.suffix = ".b"}, {.suffix = ".a"}};
=======
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
static channel channels[6] = {{""}, {""}, {".r"}, {".g"}, {".b"}, {".a"}};
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
static channel channels[6] = {{""}, {""}, {".r"}, {".g"}, {".b"}, {".a"}};
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
static channel channels[6] = {{""}, {""}, {".r"}, {".g"}, {".b"}, {".a"}};
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
static channel channels[6] = {{""}, {""}, {".r"}, {".g"}, {".b"}, {".a"}};
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
static channel channels[6] = {{""}, {""}, {".r"}, {".g"}, {".b"}, {".a"}};
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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
static channel channels[6] = {{""}, {""}, {".r"}, {".g"}, {".b"}, {".a"}};
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
static channel channels[6] = {{.suffix = ""},   {.suffix = ""},
                              {.suffix = ".r"}, {.suffix = ".g"},
                              {.suffix = ".b"}, {.suffix = ".a"}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
static channel channels[6] = {{""}, {""}, {".r"}, {".g"}, {".b"}, {".a"}};
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
static channel channels[6] = {{""}, {""}, {".r"}, {".g"}, {".b"}, {".a"}};
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
static channel channels[6] = {{""}, {""}, {".r"}, {".g"}, {".b"}, {".a"}};
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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

static int Header;
static int Float;

static char *input, *output, *title;
static double f_gamma, d_gamma, alpha, t_gamma;
static int ialpha;

static png_structp png_ptr;
static png_infop info_ptr;

static png_uint_32 width, height;
static int bit_depth, color_type, interlace_type, compression_type, filter_type;

static double gamma_correct(double k)
{
    return pow(k, 1.0 / t_gamma);
}

static int intensity(double k)
{
    return (int)(gamma_correct(k) * 255 + 0.5);
}

static int get_byte(png_bytep *pp)
{
    return *(*pp)++;
}

static int get_png_val(png_bytep *pp, int bit_depth)
{
    return (bit_depth == 16) ? (get_byte(pp) << 8) | get_byte(pp)
                             : get_byte(pp);
}

static void init_channel(channel *c)
{
    sprintf(c->name, "%s%s", output, c->suffix);

    if (Float) {
        c->fd = Rast_open_fp_new(c->name);
        c->fbuf = Rast_allocate_f_buf();
    }
    else {
        c->fd = Rast_open_c_new(c->name);
        c->buf = Rast_allocate_c_buf();
    }

    c->active = 1;
}

static void write_row_int(png_bytep p)
{
    unsigned int x, c;
    channel *ch;

    for (x = 0; x < width; x++)
        for (c = 0; c < 6; c++) {
            ch = &channels[c];
            if (ch->active)
                ch->buf[x] = (CELL)get_png_val(&p, bit_depth);
        }

    if (channels[C_A].active && ialpha > 0)
        for (c = 0; c < 6; c++) {
            ch = &channels[c];
            if (c != C_A && ch->active)
                for (x = 0; x < width; x++)
                    if (channels[C_A].buf[x] <= ialpha)
                        Rast_set_c_null_value(&ch->buf[x], 1);
        }

    for (c = 0; c < 6; c++) {
        ch = &channels[c];
        if (ch->active)
            Rast_put_c_row(ch->fd, ch->buf);
    }
}

static void write_row_float(png_bytep p)
{
    unsigned int x, c;
    channel *ch;

    for (x = 0; x < width; x++)
        for (c = 0; c < 6; c++) {
            ch = &channels[c];
            if (ch->active)
                ch->fbuf[x] = (FCELL)get_png_val(&p, bit_depth) / ch->maxval;
        }

    if (t_gamma != 1.0)
        for (c = 0; c < 6; c++) {
            ch = &channels[c];
            if (c != C_A && ch->active)
                for (x = 0; x < width; x++)
                    ch->fbuf[x] = gamma_correct(ch->fbuf[x]);
        }

    if (channels[C_A].active && ialpha > 0)
        for (c = 0; c < 6; c++) {
            ch = &channels[c];
            if (c != C_A && ch->active)
                for (x = 0; x < width; x++)
                    if (channels[C_A].fbuf[x] <= alpha)
                        Rast_set_f_null_value(&ch->fbuf[x], 1);
        }

    for (c = 0; c < 6; c++) {
        ch = &channels[c];
        if (ch->active)
            Rast_put_f_row(ch->fd, ch->fbuf);
    }
}

static void write_colors_int(int c)
{
    channel *ch = &channels[c];
    CELL i0 = 0;
    CELL i1 = ch->maxval;
    struct Colors colors;
    int i;

    Rast_init_colors(&colors);

    if (color_type == PNG_COLOR_TYPE_PALETTE) {
        png_colorp palette;
        int num_palette;

        png_get_PLTE(png_ptr, info_ptr, &palette, &num_palette);

        for (i = 0; i < num_palette; i++) {
            png_colorp col = &palette[i];

            Rast_set_c_color((CELL)i, col->red, col->green, col->blue, &colors);
        }
    }
    else if (c == C_A || t_gamma == 1.0)
        Rast_add_c_color_rule(&i0, 0, 0, 0, &i1, 255, 255, 255, &colors);
    else
        for (i = 0; i <= i1; i++) {
            int v = intensity((double)i / i1);

            Rast_set_c_color((CELL)i, v, v, v, &colors);
        }

    Rast_write_colors(ch->name, G_mapset(), &colors);
}

static void write_colors_float(int c)
{
    channel *ch = &channels[c];
    FCELL i0 = 0.0;
    FCELL i1 = 1.0;
    struct Colors colors;

    Rast_init_colors(&colors);

    Rast_add_f_color_rule(&i0, 0, 0, 0, &i1, 255, 255, 255, &colors);

    Rast_write_colors(ch->name, G_mapset(), &colors);
}

static void print_header(void)
{
    char gamma_string[80] = "";
    const char *type_string = "";
    const char *alpha_string = "";

    switch (color_type) {
    case PNG_COLOR_TYPE_GRAY:
        type_string = "gray";
        alpha_string = "";
        break;

    case PNG_COLOR_TYPE_GRAY_ALPHA:
        type_string = "gray";
        alpha_string = "+alpha";
        break;

    case PNG_COLOR_TYPE_PALETTE:
        type_string = "palette";
        alpha_string = "";
        break;

    case PNG_COLOR_TYPE_RGB:
        type_string = "truecolor";
        alpha_string = "";
        break;

    case PNG_COLOR_TYPE_RGB_ALPHA:
        type_string = "truecolor";
        alpha_string = "+alpha";
        break;
    }

    if (png_get_valid(png_ptr, info_ptr, PNG_INFO_tRNS))
        alpha_string = "+transparency";

    if (png_get_valid(png_ptr, info_ptr, PNG_INFO_gAMA))
        sprintf(gamma_string, ", image gamma = %4.2f", f_gamma);

    fprintf(stderr, "%lu x %lu image, %d bit%s %s%s%s%s\n",
            (unsigned long)width, (unsigned long)height, bit_depth,
            bit_depth > 1 ? "s" : "", type_string, alpha_string, gamma_string,
            interlace_type ? ", Adam7 interlaced" : "");
}

static void read_png(void)
{
    unsigned char sig_buf[8];
    png_bytep png_buffer;
    png_bytep *png_rows;
    int linesize;
    struct Cell_head cellhd;
    unsigned int y, c;
    png_color_8p sig_bit;
    int sbit, interlace;
    FILE *ifp;

    /* initialize input stream and PNG library */

    ifp = fopen(input, "rb");
    if (!ifp)
        G_fatal_error(_("Unable to open PNG file '%s'"), input);

    if (fread(sig_buf, sizeof(sig_buf), 1, ifp) != 1)
        G_fatal_error(_("Input file empty or too short"));

    if (png_sig_cmp(sig_buf, 0, sizeof(sig_buf)) != 0)
        G_fatal_error(_("Input file not a PNG file"));

    png_ptr = png_create_read_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);
    if (!png_ptr)
        G_fatal_error(_("Unable to allocate PNG structure"));

    info_ptr = png_create_info_struct(png_ptr);
    if (!info_ptr)
        G_fatal_error(_("Unable to allocate PNG structure"));

    if (setjmp(png_jmpbuf(png_ptr)))
        G_fatal_error(_("PNG error"));

    png_init_io(png_ptr, ifp);
    png_set_sig_bytes(png_ptr, sizeof(sig_buf));

    png_read_info(png_ptr, info_ptr);

    png_get_IHDR(png_ptr, info_ptr, &width, &height, &bit_depth, &color_type,
                 &interlace_type, &compression_type, &filter_type);

    if (Header || G_verbose() == G_verbose_max())
        print_header();

    if (Header) {
        fclose(ifp);
        exit(0);
    }

    /* read image parameters and set up data conversions */

    if (png_get_bit_depth(png_ptr, info_ptr) < 8)
        png_set_packing(png_ptr);

    sbit = png_get_sBIT(png_ptr, info_ptr, &sig_bit);
    if (sbit)
        png_set_shift(png_ptr, sig_bit);

    if (!png_get_gAMA(png_ptr, info_ptr, &f_gamma))
        f_gamma = 0.0;

    if (png_get_valid(png_ptr, info_ptr, PNG_INFO_tRNS))
        png_set_tRNS_to_alpha(png_ptr);

    if (Float && color_type == PNG_COLOR_TYPE_PALETTE)
        png_set_palette_to_rgb(png_ptr);

    png_read_update_info(png_ptr, info_ptr);

    interlace = (interlace_type != PNG_INTERLACE_NONE);

    ialpha = (int)(alpha * channels[C_A].maxval);

    t_gamma = (f_gamma != 0.0 && d_gamma != 0.0) ? f_gamma * d_gamma : 1.0;

    /* allocate input buffer */

    linesize = png_get_rowbytes(png_ptr, info_ptr);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
>>>>>>> osgeo-main
=======
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
>>>>>>> osgeo-main
=======
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
>>>>>>> osgeo-main
=======
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
>>>>>>> osgeo-main
=======
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
>>>>>>> osgeo-main
=======
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
>>>>>>> osgeo-main
=======
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
>>>>>>> osgeo-main
=======
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
>>>>>>> osgeo-main
=======
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
>>>>>>> osgeo-main
=======
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
>>>>>>> osgeo-main
=======
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
>>>>>>> osgeo-main
=======
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
>>>>>>> osgeo-main
    png_buffer = G_malloc(interlace ? height * linesize : linesize);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    png_buffer = G_malloc(interlace ? height * linesize : linesize);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
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
    png_buffer = G_malloc(interlace ? height * linesize : linesize);
=======
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
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
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
    png_buffer = G_malloc(interlace ? height * linesize : linesize);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    png_buffer = G_malloc(interlace ? height * linesize : linesize);
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
=======
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
    png_buffer = G_malloc(interlace ? height * linesize : linesize);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    png_buffer = G_malloc(interlace ? height * linesize : linesize);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    png_buffer = G_malloc((size_t)interlace ? (size_t)height * linesize
                                            : (size_t)linesize);
=======
    png_buffer = G_malloc(interlace ? height * linesize : linesize);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    png_buffer = G_malloc(interlace ? height * linesize : linesize);
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

    if (interlace) {
        png_rows = G_malloc(height * sizeof(png_bytep));
        for (y = 0; y < height; y++)
            png_rows[y] = png_buffer + y * linesize;
    }

    /* initialize cell header */

    Rast_get_window(&cellhd);

    cellhd.rows = height;
    cellhd.cols = width;
    cellhd.north = cellhd.rows;
    cellhd.south = 0.0;
    cellhd.east = cellhd.cols;
    cellhd.west = 0.0;
    cellhd.ns_res = 1;
    cellhd.ew_res = 1;

    Rast_set_window(&cellhd);

    /* initialize channel information */

    switch (color_type) {
    case PNG_COLOR_TYPE_GRAY:
        init_channel(&channels[C_Y]);
        break;

    case PNG_COLOR_TYPE_GRAY_ALPHA:
        init_channel(&channels[C_Y]);
        init_channel(&channels[C_A]);
        break;

    case PNG_COLOR_TYPE_PALETTE:
        init_channel(&channels[C_P]);
        break;

    case PNG_COLOR_TYPE_RGB:
        init_channel(&channels[C_R]);
        init_channel(&channels[C_G]);
        init_channel(&channels[C_B]);
        break;

    case PNG_COLOR_TYPE_RGB_ALPHA:
        init_channel(&channels[C_R]);
        init_channel(&channels[C_G]);
        init_channel(&channels[C_B]);
        init_channel(&channels[C_A]);
        break;
    }

    if (sbit) {
        channels[C_R].maxval = (1 << sig_bit->red) - 1;
        channels[C_G].maxval = (1 << sig_bit->green) - 1;
        channels[C_B].maxval = (1 << sig_bit->blue) - 1;
        channels[C_Y].maxval = (1 << sig_bit->gray) - 1;
        channels[C_A].maxval = (1 << sig_bit->alpha) - 1;
    }
    else {
        channels[C_R].maxval = (1 << bit_depth) - 1;
        channels[C_G].maxval = (1 << bit_depth) - 1;
        channels[C_B].maxval = (1 << bit_depth) - 1;
        channels[C_Y].maxval = (1 << bit_depth) - 1;
        channels[C_A].maxval = (1 << bit_depth) - 1;
    }

    /* read image and write raster layers */

    if (interlace)
        png_read_image(png_ptr, png_rows);

    for (y = 0; y < height; y++) {
        png_bytep p;

        if (interlace)
            p = png_rows[y];
        else {
            png_read_row(png_ptr, png_buffer, NULL);
            p = png_buffer;
        }

        if (Float)
            write_row_float(p);
        else
            write_row_int(p);
    }

    png_read_end(png_ptr, NULL);

    fclose(ifp);

    /* close output files */

    for (c = 0; c < 6; c++) {
        channel *ch = &channels[c];

        if (!ch->active)
            continue;

        Rast_close(ch->fd);

        if (Float)
            G_free(ch->fbuf);
        else
            G_free(ch->buf);
    }

    /* write title and color table */

    G_verbose_message(_("Creating support files for <%s>..."), output);

    for (c = 0; c < 6; c++) {
        channel *ch = &channels[c];

        if (!ch->active)
            continue;

        if (title && *title)
            Rast_put_cell_title(ch->name, title);

        if (Float)
            write_colors_float(c);
        else
            write_colors_int(c);
    }

    G_free(png_buffer);
    if (interlace)
        G_free(png_rows);

    png_destroy_read_struct(&png_ptr, &info_ptr, NULL);
}

int main(int argc, char *argv[])
{
    struct Option *inopt, *outopt, *titleopt, *gammaopt, *alphaopt;
    struct Flag *fflag, *hflag;
    struct GModule *module;

    G_gisinit(argv[0]);

    module = G_define_module();
    G_add_keyword(_("raster"));
    G_add_keyword(_("import"));
    G_add_keyword("PNG");
    module->description = _("Imports non-georeferenced PNG format image.");

    inopt = G_define_standard_option(G_OPT_F_BIN_INPUT);

    outopt = G_define_standard_option(G_OPT_R_OUTPUT);

    titleopt = G_define_option();
    titleopt->key = "title";
    titleopt->type = TYPE_STRING;
    titleopt->required = NO;
    titleopt->description = _("Title for created raster map");

    gammaopt = G_define_option();
    gammaopt->key = "gamma";
    gammaopt->type = TYPE_DOUBLE;
    gammaopt->required = NO;
    gammaopt->description = _("Display gamma");

    alphaopt = G_define_option();
    alphaopt->key = "alpha";
    alphaopt->type = TYPE_DOUBLE;
    alphaopt->required = NO;
    alphaopt->description = _("Alpha threshold");

    fflag = G_define_flag();
    fflag->key = 'f';
    fflag->description = _("Create floating-point map (0.0 - 1.0)");

    hflag = G_define_flag();
    hflag->key = 'h';
    hflag->description = _("Output image file header only and exit");

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);

    input = inopt->answer;
    output = outopt->answer;
    title = titleopt->answer;
    d_gamma = gammaopt->answer ? atof(gammaopt->answer) : 0.0;
    alpha = alphaopt->answer ? atof(alphaopt->answer) : -1.0;

    Float = fflag->answer;
    Header = hflag->answer;

    read_png();

    exit(EXIT_SUCCESS);
}
