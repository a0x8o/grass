#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <grass/gis.h>

struct glyph {
    unsigned int offset : 20;
    unsigned int count : 12;
};

static struct glyph *glyphs;
static int glyphs_alloc;

static unsigned char *xcoords, *ycoords;
static int coords_offset;
static int coords_alloc;

static int fontmap[1024];
static int num_chars;

static char current_font[16];
static int font_loaded;

static struct glyph *glyph_slot(int idx)
{
    if (glyphs_alloc <= idx) {
        int new_alloc = idx + ((glyphs_alloc > 0) ? 1000 : 4000);

        glyphs = G_realloc(glyphs, new_alloc * sizeof(struct glyph));
        memset(&glyphs[glyphs_alloc], 0,
               (new_alloc - glyphs_alloc) * sizeof(struct glyph));
        glyphs_alloc = new_alloc;
    }

    return &glyphs[idx];
}

static int coord_slots(int count)
{
    int n;

    if (coords_alloc < coords_offset + count) {
        coords_alloc =
            coords_offset + count + ((coords_alloc > 0) ? 10000 : 60000);
        xcoords = G_realloc(xcoords, coords_alloc);
        ycoords = G_realloc(ycoords, coords_alloc);
    }

    n = coords_offset;
    coords_offset += count;

    return n;
}

static void read_hersh(const char *filename)
{
    FILE *fp = fopen(filename, "r");

    if (!fp)
        return;

    while (!feof(fp)) {
        char buf[8];
        struct glyph *glyph;
        int coords;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        unsigned int i, idx, count;
        int c;
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        unsigned int i, idx, count;
        int c;
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        unsigned int i, idx, count;
        int c;
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        unsigned int i, idx, count;
        int c;
=======
>>>>>>> osgeo-main
=======
        unsigned int i, idx, count;
        int c;
=======
>>>>>>> osgeo-main
=======
        unsigned int i, idx, count;
        int c;
=======
>>>>>>> osgeo-main
=======
        unsigned int i, idx, count;
        int c;
=======
>>>>>>> osgeo-main
=======
        unsigned int i, idx, count;
        int c;
=======
>>>>>>> osgeo-main
=======
        unsigned int i, idx, count;
        int c;
=======
>>>>>>> osgeo-main
=======
        unsigned int i, idx, count;
        int c;
=======
>>>>>>> osgeo-main
=======
        unsigned int i, idx, count;
        int c;
=======
>>>>>>> osgeo-main
=======
        unsigned int i, idx, count;
        int c;
=======
>>>>>>> osgeo-main
=======
        unsigned int i, idx, count;
        int c;
=======
>>>>>>> osgeo-main
=======
        unsigned int i, idx, count;
        int c;
=======
>>>>>>> osgeo-main
=======
        unsigned int i, idx, count;
        int c;
=======
>>>>>>> osgeo-main
        unsigned int idx, count;
        int c, i;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        unsigned int idx, count;
        int c, i;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        unsigned int i, idx, count;
        int c;
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
        unsigned int idx, count;
        int c, i;
=======
        unsigned int i, idx, count;
        int c;
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
        unsigned int i, idx, count;
        int c;
=======
        unsigned int idx, count;
        int c, i;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
        unsigned int idx, count;
        int c, i;
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
        unsigned int i, idx, count;
        int c;
=======
        unsigned int idx, count;
        int c, i;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        unsigned int i, idx, count;
        int c;
=======
        unsigned int idx, count;
        int c, i;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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

        switch (c = fgetc(fp)) {
        case '\r':
            fgetc(fp);
            continue;
        case '\n':
            continue;
        default:
            ungetc(c, fp);
            break;
        }

        if (fread(buf, 1, 5, fp) != 5)
            break;

        buf[5] = 0;
        idx = atoi(buf);

        if (fread(buf, 1, 3, fp) != 3)
            break;

        buf[3] = 0;
        count = atoi(buf);

        glyph = glyph_slot(idx);
        coords = coord_slots(count);

        glyph->offset = coords;
        glyph->count = count;

        for (i = 0; i < count; i++) {
            if ((i + 4) % 36 == 0) {
                /* skip newlines? */
                if (fgetc(fp) == '\r')
                    fgetc(fp);
            }

            xcoords[coords + i] = fgetc(fp);
            ycoords[coords + i] = fgetc(fp);
        }

        if (fgetc(fp) == '\r')
            fgetc(fp);
    }

    fclose(fp);
}

static void load_glyphs(void)
{
    int i;

    if (glyphs)
        return;

    for (i = 1; i <= 4; i++) {
        char buf[GPATH_MAX];

        sprintf(buf, "%s/fonts/hersh.oc%d", G_gisbase(), i);
        read_hersh(buf);
    }
}

static void read_fontmap(const char *name)
{
    char buf[GPATH_MAX];
    FILE *fp;

    num_chars = 0;
    memset(fontmap, 0, sizeof(fontmap));

    sprintf(buf, "%s/fonts/%s.hmp", G_gisbase(), name);

    fp = fopen(buf, "r");
    if (!fp) {
        G_warning("Unable to open font map '%s': %s. "
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                  "Try running 'g.mkfontcap -o'",
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
                  "Try running 'g.mkfontcap --overwrite'",
=======
                  "Try running 'g.mkfontcap -o'",
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
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                  "Try running 'g.mkfontcap -o'",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
                  buf, strerror(errno));
        return;
    }

    while (fscanf(fp, "%s", buf) == 1) {
        int a, b;

        if (sscanf(buf, "%d-%d", &a, &b) == 2)
            while (a <= b)
                fontmap[num_chars++] = a++;
        else if (sscanf(buf, "%d", &a) == 1)
            fontmap[num_chars++] = a;
    }

    fclose(fp);
}

static void load_font(void)
{
    if (font_loaded)
        return;

    if (!glyphs)
        load_glyphs();

    read_fontmap(current_font);

    font_loaded = 1;
}

int font_init(const char *name)
{
    if (strcmp(name, current_font) == 0)
        return 0;

    strcpy(current_font, name);
    font_loaded = 0;

    return 0;
}

int get_char_vects(unsigned char achar, int *n, unsigned char **X,
                   unsigned char **Y)
{
    struct glyph *glyph;
    int i;

    if (!font_loaded)
        load_font();

    i = (int)achar - 040; /* translate achar to char# in font index */
    if (i <= 0 || i >= num_chars) {
        *n = 0;
        return 1;
    }

    glyph = &glyphs[fontmap[i]];

    *n = glyph->count;
    *X = &xcoords[glyph->offset];
    *Y = &ycoords[glyph->offset];

    return 0;
}
