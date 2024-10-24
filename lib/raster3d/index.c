#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <grass/raster3d.h>
#include "raster3d_intern.h"

/*---------------------------------------------------------------------------*/

static int Rast3d_readIndex(RASTER3D_Map *map)
{
    unsigned char *tmp, *tmp2;
    int dummy1, dummy2, indexLength, tileIndex;
    long indexLast;

    indexLast = lseek(map->data_fd, (long)0, SEEK_END);
    if (indexLast == -1) {
        Rast3d_error("Rast3d_readIndex: can't position file");
        return 0;
    }

    indexLength = indexLast - map->indexOffset;

    if (lseek(map->data_fd, map->indexOffset, SEEK_SET) == -1) {
        Rast3d_error("Rast3d_readIndex: can't position file");
        return 0;
    }

    tmp = Rast3d_malloc(map->indexLongNbytes * map->nTiles);

    if (tmp == NULL) {
        Rast3d_error("Rast3d_readIndex: error in Rast3d_malloc");
        return 0;
    }

    /* The size of the tile index array in the map file */
    if (indexLength == map->indexLongNbytes * map->nTiles) {
        if (read(map->data_fd, tmp, indexLength) != indexLength) {
            Rast3d_error("Rast3d_readIndex: can't read file");
            return 0;
        }
    }
    else
        /* ATTENTION: RLE encoded reading is only supported for backward
         * compatibility */
        if (indexLength <
            map->indexLongNbytes * map->nTiles) { /* RLE encoded? */

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
>>>>>>> osgeo-main
            if (indexLength > sizeof(long) * map->nTiles) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            if (indexLength > sizeof(long) * map->nTiles) {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            if (indexLength > (int)sizeof(long) * map->nTiles) {
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
            if (indexLength > sizeof(long) * map->nTiles) {
=======
            if (indexLength > (int)sizeof(long) * map->nTiles) {
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
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
            if (indexLength > sizeof(long) * map->nTiles) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if (indexLength > sizeof(long) * map->nTiles) {
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
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
            if (indexLength > sizeof(long) * map->nTiles) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if (indexLength > sizeof(long) * map->nTiles) {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
            if (indexLength > (int)sizeof(long) * map->nTiles) {
=======
            if (indexLength > sizeof(long) * map->nTiles) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if (indexLength > sizeof(long) * map->nTiles) {
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

                /*->index large enough? */
                tmp2 = Rast3d_malloc(indexLength);
                if (tmp2 == NULL) {
                    Rast3d_error("Rast3d_readIndex: error in Rast3d_malloc");
                    return 0;
                }
            }
            else /* YES */
                tmp2 = (unsigned char *)map->index;

            if (read(map->data_fd, tmp2, indexLength) != indexLength) {
                Rast3d_error("Rast3d_readIndex: can't read file");
                return 0;
            }

            Rast3d_rle_decode((char *)tmp2, (char *)tmp,
                              map->indexLongNbytes * map->nTiles, 1, &dummy1,
                              &dummy2);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
>>>>>>> osgeo-main
=======
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
>>>>>>> osgeo-main
            if (indexLength > sizeof(long) * map->nTiles)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            if (indexLength > sizeof(long) * map->nTiles)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            if (indexLength > (int)sizeof(long) * map->nTiles)
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
            if (indexLength > sizeof(long) * map->nTiles)
=======
            if (indexLength > (int)sizeof(long) * map->nTiles)
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
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
            if (indexLength > sizeof(long) * map->nTiles)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if (indexLength > sizeof(long) * map->nTiles)
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
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
            if (indexLength > sizeof(long) * map->nTiles)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if (indexLength > sizeof(long) * map->nTiles)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
            if (indexLength > (int)sizeof(long) * map->nTiles)
=======
            if (indexLength > sizeof(long) * map->nTiles)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if (indexLength > sizeof(long) * map->nTiles)
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
                Rast3d_free(tmp2);
        } /* END RLE */

    Rast3d_long_decode(tmp, map->index, map->nTiles, map->indexLongNbytes);

    for (tileIndex = 0; tileIndex < map->nTiles; tileIndex++)
        if (map->index[tileIndex] == 0)
            map->index[tileIndex] = -1;

    Rast3d_free(tmp);

    return 1;
}

/*---------------------------------------------------------------------------*/

int Rast3d_flush_index(RASTER3D_Map *map)
{
    int indexLength, tileIndex;
    unsigned char *tmp;
    long ldummy;

    if (!map->hasIndex)
        return 1;

    map->indexOffset = lseek(map->data_fd, (long)0, SEEK_END);
    if (map->indexOffset == -1) {
        Rast3d_error("Rast3d_flush_index: can't rewind file");
        return 0;
    }

    map->indexNbytesUsed =
        Rast3d_long_encode(&(map->indexOffset), (unsigned char *)&ldummy, 1);

    tmp = Rast3d_malloc(sizeof(long) * map->nTiles);
    if (tmp == NULL) {
        Rast3d_error("Rast3d_flush_index: error in Rast3d_malloc");
        return 0;
    }

    for (tileIndex = 0; tileIndex < map->nTiles; tileIndex++)
        if (map->index[tileIndex] == -1)
            map->index[tileIndex] = 0;

    (void)Rast3d_long_encode(map->index, tmp, map->nTiles);

    indexLength = map->nTiles * sizeof(long);
    if (write(map->data_fd, tmp, indexLength) != indexLength) {
        Rast3d_error("Rast3d_flush_index: can't write file");
        return 0;
    }

    Rast3d_free(tmp);
    if (!Rast3d_readIndex(map)) {
        Rast3d_error("Rast3d_flush_index: error in Rast3d_readIndex");
        return 0;
    }

    return 1;
}

/*---------------------------------------------------------------------------*/

static long *cmpIndex;

static int indexSortCompare(const void *a, const void *b)
{
    long offset1, offset2;

    offset1 = cmpIndex[*((const long *)a)];
    offset2 = cmpIndex[*((const long *)b)];

    if (offset1 > offset2)
        return 1;
    if (offset1 < offset2)
        return -1;
    return 0;
}

/*---------------------------------------------------------------------------*/

int Rast3d_init_index(RASTER3D_Map *map, int hasIndex)
{
    int tile;
    int i0, i1, i2, i3, i4, i5, nofElts;
    long offset;
    long *offsetP;

    map->hasIndex = hasIndex;
    map->index = Rast3d_malloc(sizeof(long) * map->nTiles);
    map->tileLength = Rast3d_malloc(sizeof(int) * map->nTiles);

    if ((map->index == NULL) || (map->tileLength == NULL)) {
        Rast3d_error("Rast3d_init_index: error in Rast3d_malloc");
        return 0;
    }

    if (map->operation == RASTER3D_WRITE_DATA) {
        for (tile = 0; tile < map->nTiles; tile++)
            map->index[tile] = -1;
        return 1;
    }

    if (!map->hasIndex) {
        offset = 0;
        for (tile = 0; tile < map->nTiles; tile++) {
            map->index[tile] = offset * map->numLengthExtern + map->offset;
            nofElts = Rast3d_compute_clipped_tile_dimensions(
                map, tile, &i0, &i1, &i2, &i3, &i4, &i5);
            map->tileLength[tile] = nofElts * map->numLengthExtern;
            offset += nofElts;
        }
        return 1;
    }

    if (!Rast3d_readIndex(map)) {
        Rast3d_error("Rast3d_init_index: error in Rast3d_readIndex");
        return 0;
    }

    offsetP = Rast3d_malloc(sizeof(long) * map->nTiles);
    if (offsetP == NULL) {
        Rast3d_error("Rast3d_init_index: error in Rast3d_malloc");
        return 0;
    }

    for (tile = 0; tile < map->nTiles; tile++)
        offsetP[tile] = tile;
    cmpIndex = map->index;
    qsort(offsetP, map->nTiles, sizeof(long), indexSortCompare);

    for (tile = 0; tile < map->nTiles - 1; tile++) {
        if (map->index[offsetP[tile]] == -1) {
            map->tileLength[offsetP[tile]] = 0;
            continue;
        }

        map->tileLength[offsetP[tile]] =
            map->index[offsetP[tile + 1]] - map->index[offsetP[tile]];
    }

    if (map->index[offsetP[map->nTiles - 1]] == -1)
        map->tileLength[offsetP[map->nTiles - 1]] = 0;
    else
        map->tileLength[offsetP[map->nTiles - 1]] =
            map->indexOffset - map->index[offsetP[map->nTiles - 1]];

    Rast3d_free(offsetP);

    return 1;
}
