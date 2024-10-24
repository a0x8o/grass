/*
 *   \AUTHOR: Serena Pallecchi student of Computer Science University of Pisa
 * (Italy) Commission from Faunalia Pontedera (PI) www.faunalia.it
 *
 *   This program is free software under the GPL (>=v2)
 *   Read the COPYING file that comes with GRASS for details.
 *
 */

#include <string.h>

#include <grass/gis.h>
#include <grass/glocale.h>

#include "utility.h"

/*if occurred an error returns NULL */
char *concatena(const char *str1, const char *str2)
{
    char *conc = (char *)G_malloc(strlen(str1) + strlen(str2) + 1);

    if (conc == NULL) {
        return NULL;
    }
    strcpy(conc, str1);
    strcat(conc, str2);
    return conc;
}

/* split_arg  returns  the array of token find in linea separated by separatore
 * presente and write in argc the nummer of find token */
/*if occurred an error returns NULL */
char **split_arg(char *linea, char separatore, long *numerotoken)
{
    char **argv;      /* token array */
    char *copialinea; /* line copy */

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    long i;    /* find token number */
    size_t it; /* iterator */
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    long i;    /* find token number */
    size_t it; /* iterator */
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    long i;    /* find token number */
    size_t it; /* iterator */
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    long i;    /* find token number */
    size_t it; /* iterator */
=======
>>>>>>> osgeo-main
=======
    long i;    /* find token number */
    size_t it; /* iterator */
=======
>>>>>>> osgeo-main
=======
    long i;    /* find token number */
    size_t it; /* iterator */
=======
>>>>>>> osgeo-main
=======
    long i;    /* find token number */
    size_t it; /* iterator */
=======
>>>>>>> osgeo-main
=======
    long i;    /* find token number */
    size_t it; /* iterator */
=======
>>>>>>> osgeo-main
=======
    long i;    /* find token number */
    size_t it; /* iterator */
=======
>>>>>>> osgeo-main
=======
    long i;    /* find token number */
    size_t it; /* iterator */
=======
>>>>>>> osgeo-main
=======
    long i;    /* find token number */
    size_t it; /* iterator */
=======
>>>>>>> osgeo-main
=======
    long i;    /* find token number */
    size_t it; /* iterator */
=======
>>>>>>> osgeo-main
=======
    long i;    /* find token number */
    size_t it; /* iterator */
=======
>>>>>>> osgeo-main
=======
    long i;    /* find token number */
    size_t it; /* iterator */
=======
>>>>>>> osgeo-main
=======
    long i;    /* find token number */
    size_t it; /* iterator */
=======
>>>>>>> osgeo-main
    long i;  /* find token number */
    long it; /* iterator */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    long i;  /* find token number */
    long it; /* iterator */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    long i;    /* find token number */
    size_t it; /* iterator */
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
    long i;  /* find token number */
    long it; /* iterator */
=======
    long i;    /* find token number */
    size_t it; /* iterator */
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
    long i;    /* find token number */
    size_t it; /* iterator */
=======
    long i;  /* find token number */
    long it; /* iterator */
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
    long i;  /* find token number */
    long it; /* iterator */
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
    long i;    /* find token number */
    size_t it; /* iterator */
=======
    long i;  /* find token number */
    long it; /* iterator */
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
    long i;    /* find token number */
    size_t it; /* iterator */
=======
    long i;  /* find token number */
    long it; /* iterator */
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
    long num;

    int term; /* =0 if last token has not /0 */

    i = 0;
    term = 0;

    if (linea == NULL || linea[0] == '\0') {
        *numerotoken = 0;
        return NULL;
    }

    /* copy string */
    copialinea = (char *)G_malloc(strlen(linea) + 1);
    if (copialinea == NULL) {
        return NULL;
    }
    strcpy(copialinea, linea);

    argv = (char **)G_malloc(sizeof(char *));
    if (argv == NULL) {
        return NULL;
    }

    num = 0;
    for (it = 0; it < strlen(copialinea); it++) {
        if (copialinea[it] == separatore) {
            while (copialinea[it + 1] == separatore)
                it++;
            if (i != 0) {
                argv[i - 1] = G_realloc(argv[i - 1], (num + 1) * sizeof(char));
                argv[i - 1][num] = '\0';
                argv = (char **)G_realloc(argv, (i + 1) * sizeof(char *));
                num = 0;
            }
            if ((it + 1) == strlen(copialinea))
                term = 1;
        }
        else {
            if (num == 0) {
                i++;
                argv[i - 1] = G_malloc(sizeof(char));
                if (argv[i - 1] == NULL) {
                    return NULL;
                }
            }
            else {
                argv[i - 1] = G_realloc(argv[i - 1], (num + 1) * sizeof(char));
            }

            argv[i - 1][num] = copialinea[it];
            num++;
        }
    }

    if (!term) {
        argv[i - 1] = G_realloc(argv[i - 1], (num + 1) * sizeof(char));
        argv[i - 1][num] = '\0';
    }

    *numerotoken = i;

    G_free(copialinea);

    return argv;
}
