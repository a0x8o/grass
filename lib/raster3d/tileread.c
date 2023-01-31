#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

#include <grass/raster.h>
#include "raster3d_intern.h"

static int Rast3d_xdrTile2tile(RASTER3D_Map *map, void *tile, int rows,
                               int cols, int depths, int xRedundant,
                               int yRedundant, int zRedundant, int nofNum,
                               int type)
{
    int y, z, xLength, yLength, length;

    if (!Rast3d_init_copy_from_xdr(map, type)) {
        Rast3d_error("Rast3d_xdrTile2tile: error in Rast3d_init_copy_from_xdr");
        return 0;
    }

    if (nofNum == map->tileSize) {
        if (!Rast3d_copy_from_xdr(map->tileSize, tile)) {
            Rast3d_error("Rast3d_xdrTile2tile: error in Rast3d_copy_from_xdr");
            return 0;
        }
        return 1;
    }

    length = Rast3d_length(type);
    xLength = xRedundant * length;
    yLength = map->tileX * yRedundant * length;

    if (xRedundant) {
        for (z = 0; z < depths; z++) {
            for (y = 0; y < rows; y++) {
                if (!Rast3d_copy_from_xdr(cols, tile)) {
                    Rast3d_error(
                        "Rast3d_xdrTile2tile: error in Rast3d_copy_from_xdr");
                    return 0;
                }
                tile = G_incr_void_ptr(tile, cols * length);
                Rast3d_set_null_value(tile, xRedundant, type);
                tile = G_incr_void_ptr(tile, xLength);
            }
            if (yRedundant) {
                Rast3d_set_null_value(tile, map->tileX * yRedundant, type);
                tile = G_incr_void_ptr(tile, yLength);
            }
        }
        if (!zRedundant)
            return 1;

        Rast3d_set_null_value(tile, map->tileXY * zRedundant, type);
        return 1;
    }

    if (yRedundant) {
        for (z = 0; z < depths; z++) {
            if (!Rast3d_copy_from_xdr(map->tileX * rows, tile)) {
                Rast3d_error(
                    "Rast3d_xdrTile2tile: error in Rast3d_copy_from_xdr");
                return 0;
            }
            tile = G_incr_void_ptr(tile, map->tileX * rows * length);
            Rast3d_set_null_value(tile, map->tileX * yRedundant, type);
            tile = G_incr_void_ptr(tile, yLength);
        }
        if (!zRedundant)
            return 1;

        Rast3d_set_null_value(tile, map->tileXY * zRedundant, type);
        return 1;
    }

    if (!Rast3d_copy_from_xdr(map->tileXY * depths, tile)) {
        Rast3d_error("Rast3d_xdrTile2tile: error in Rast3d_copy_from_xdr");
        return 0;
    }

    if (!zRedundant)
        return 1;

    tile = G_incr_void_ptr(tile, map->tileXY * depths * length);
    Rast3d_set_null_value(tile, map->tileXY * zRedundant, type);

    return 1;
}

/*---------------------------------------------------------------------------*/

static int Rast3d_readTileUncompressed(RASTER3D_Map *map, int tileIndex,
                                       int nofNum)
{
    size_t nofBytes;
    ssize_t res;

    nofBytes = (size_t)nofNum * map->numLengthExtern;
    nofBytes =
        RASTER3D_MIN(nofBytes, (size_t)map->fileEndPtr - map->index[tileIndex]);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
>>>>>>> osgeo-main
    if (read(map->data_fd, xdr, nofBytes) != nofBytes) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    if (read(map->data_fd, xdr, nofBytes) != nofBytes) {
=======
    if (read(map->data_fd, xdr, nofBytes) != nofBytes) {
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
    if (read(map->data_fd, xdr, nofBytes) != nofBytes) {
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
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
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
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
    if (read(map->data_fd, xdr, nofBytes) != nofBytes) {
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
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
    if (read(map->data_fd, xdr, nofBytes) != nofBytes) {
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
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
    if (read(map->data_fd, xdr, nofBytes) != nofBytes) {
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
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
    if (read(map->data_fd, xdr, nofBytes) != nofBytes) {
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
    if (read(map->data_fd, xdr, nofBytes) != nofBytes) {
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
    if (read(map->data_fd, xdr, nofBytes) != nofBytes) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
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
    if ((res = read(map->data_fd, xdr, nofBytes)) < 0 ||
        (size_t)res != nofBytes) {
=======
    if (read(map->data_fd, xdr, nofBytes) != nofBytes) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
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
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
        Rast3d_error("Rast3d_readTileUncompressed: can't read file");
        return 0;
    }

    return 1;
}

/*---------------------------------------------------------------------------*/

static int Rast3d_readTileCompressed(RASTER3D_Map *map, int tileIndex,
                                     int nofNum)
{
    if (!Rast3d_fpcompress_read_xdr_nums(
            map->data_fd, xdr, nofNum, map->tileLength[tileIndex],
            map->precision, tmpCompress, map->type == FCELL_TYPE)) {
        Rast3d_error("Rast3d_readTileCompressed: error in "
                     "Rast3d_fpcompress_read_xdr_nums");
        return 0;
    }

    return 1;
}

/*---------------------------------------------------------------------------*/

/*---------------------------------------------------------------------------*/
/* EXPORTED FUNCTIONS */

/*---------------------------------------------------------------------------*/

/*!
 * \brief
 *
 *
 * Reads tile with index <em>tileIndex</em> into the <em>tile</em> buffer. The
 * cells are stored with type <em>type</em> which must be one of FCELL_TYPE and
 * DCELL_TYPE. If the tile with <em>tileIndex</em> is not stored on the file
 * corresponding to <em>map</em>, and <em>tileIndex</em> is a valid index
 * <em>tile</em> is filled with NULL-values.
 *
 *  \param map
 *  \param tileIndex
 *  \param tile
 *  \param type
 *  \return 1 ... if successful,
 *          0 ... otherwise
 */

int Rast3d_read_tile(RASTER3D_Map *map, int tileIndex, void *tile, int type)
{
    int nofNum, rows, cols, depths, xRedundant, yRedundant, zRedundant;

    if ((tileIndex >= map->nTiles) || (tileIndex < 0))
        Rast3d_fatal_error("Rast3d_read_tile: tile index out of range");

    if (map->index[tileIndex] == -1) {
        Rast3d_set_null_tile_type(map, tile, type);
        return 1;
    }

    nofNum = Rast3d_compute_clipped_tile_dimensions(map, tileIndex, &rows,
                                                    &cols, &depths, &xRedundant,
                                                    &yRedundant, &zRedundant);

    if (lseek(map->data_fd, map->index[tileIndex], SEEK_SET) == -1) {
        Rast3d_error("Rast3d_read_tile: can't position file");
        return 0;
    }

    if (map->compression == RASTER3D_NO_COMPRESSION) {
        if (!Rast3d_readTileUncompressed(map, tileIndex, nofNum)) {
            Rast3d_error(
                "Rast3d_read_tile: error in Rast3d_readTileUncompressed");
            return 0;
        }
    }
    else if (!Rast3d_readTileCompressed(map, tileIndex, nofNum)) {
        Rast3d_error("Rast3d_read_tile: error in Rast3d_readTileCompressed");
        return 0;
    }

    if (!Rast3d_xdrTile2tile(map, tile, rows, cols, depths, xRedundant,
                             yRedundant, zRedundant, nofNum, type)) {
        Rast3d_error("Rast3d_read_tile: error in Rast3d_xdrTile2tile");
        return 0;
    }

    if (Rast3d_mask_is_off(map))
        return 1;

    Rast3d_mask_tile(map, tileIndex, tile, type);
    return 1;
}

/*---------------------------------------------------------------------------*/

/*!
 * \brief
 *
 *  Is equivalent to Rast3d_read_tile (map, tileIndex, tile, FCELL_TYPE).
 *
 *  \param map
 *  \param tileIndex
 *  \param tile
 *  \return int
 */

int Rast3d_read_tile_float(RASTER3D_Map *map, int tileIndex, void *tile)
{
    if (!Rast3d_read_tile(map, tileIndex, tile, FCELL_TYPE)) {
        Rast3d_error("Rast3d_read_tile_float: error in Rast3d_read_tile");
        return 0;
    }

    return 1;
}

/*---------------------------------------------------------------------------*/

/*!
 * \brief
 *
 *  Is equivalent to Rast3d_read_tile (map, tileIndex, tile, DCELL_TYPE).
 *
 *  \param map
 *  \param tileIndex
 *  \param tile
 *  \return int
 */

int Rast3d_read_tile_double(RASTER3D_Map *map, int tileIndex, void *tile)
{
    if (!Rast3d_read_tile(map, tileIndex, tile, DCELL_TYPE)) {
        Rast3d_error("Rast3d_read_tile_double: error in Rast3d_read_tile");
        return 0;
    }

    return 1;
}

/*---------------------------------------------------------------------------*/

/* CACHE-MODE-ONLY FUNCTIONS */

/*---------------------------------------------------------------------------*/

/*!
 * \brief
 *
 *  Locks tile with <em>tileIndex</em> in cache. If after locking fewer than the
 * minimum number of unlocked tiles are unlocked, the lock request is ignored.
 *
 *  \param map
 *  \param tileIndex
 *  \return 1 ... if successful,
 *          -1 ... if request is ignored,
 *          0 ... otherwise.
 */

int Rast3d_lock_tile(RASTER3D_Map *map, int tileIndex)
{
    if (!map->useCache)
        Rast3d_fatal_error(
            "Rast3d_lock_tile: function invalid in non-cache mode");

    if (!Rast3d_cache_lock(map->cache, tileIndex)) {
        Rast3d_error("Rast3d_lock_tile: error in Rast3d_cache_lock");
        return 0;
    }

    return 1;
}

/*---------------------------------------------------------------------------*/

/*!
 * \brief
 *
 *  Unlocks tile with <em>tileIndex</em>.
 *
 *  \param map
 *  \param tileIndex
 *  \return 1 ... if successful,
 *          0 ... otherwise.
 */

int Rast3d_unlock_tile(RASTER3D_Map *map, int tileIndex)
{
    if (!map->useCache)
        Rast3d_fatal_error(
            "Rast3d_unlock_tile: function invalid in non-cache mode");

    if (!Rast3d_cache_unlock(map->cache, tileIndex)) {
        Rast3d_error("Rast3d_unlock_tile: error in Rast3d_cache_unlock");
        return 0;
    }

    return 1;
}

/*---------------------------------------------------------------------------*/

/*!
 * \brief
 *
 * Unlocks every tile in cache of <em>map</em>.
 *
 *  \param map
 *  \return 1 ... if successful,
 *          0 ... otherwise.
 */

int Rast3d_unlock_all(RASTER3D_Map *map)
{
    if (!map->useCache)
        Rast3d_fatal_error(
            "Rast3d_unlock_all: function invalid in non-cache mode");

    if (!Rast3d_cache_unlock_all(map->cache)) {
        Rast3d_error("Rast3d_unlock_all: error in Rast3d_cache_unlock_all");
        return 0;
    }

    return 1;
}

/*---------------------------------------------------------------------------*/

/*!
 * \brief
 *
 * Turns autolock mode on.
 *
 *  \param map
 *  \return void
 */

void Rast3d_autolock_on(RASTER3D_Map *map)
{
    if (!map->useCache)
        Rast3d_fatal_error(
            "Rast3d_autoLockOn: function invalid in non-cache mode");

    Rast3d_cache_autolock_on(map->cache);
}

/*---------------------------------------------------------------------------*/

/*!
 * \brief
 *
 * Turns autolock mode Off.
 *
 *  \param map
 *  \return void
 */

void Rast3d_autolock_off(RASTER3D_Map *map)
{
    if (!map->useCache)
        Rast3d_fatal_error(
            "Rast3d_autoLockOff: function invalid in non-cache mode");

    Rast3d_cache_autolock_off(map->cache);
}

/*---------------------------------------------------------------------------*/

/*!
 * \brief
 *
 * Sets the minimum
 * number of unlocked tiles to <em>minUnlocked</em>.  This function should be
 * used in combination with <tt>Rast3d_unlock_all ()</tt> in order to avoid
 * situations where the new minimum is larger than the actual number of unlocked
 * tiles. <em>minUnlocked</em> must be one of RASTER3D_USE_CACHE_X,
 * RASTER3D_USE_CACHE_Y, RASTER3D_USE_CACHE_Z, RASTER3D_USE_CACHE_XY,
 * RASTER3D_USE_CACHE_XZ, RASTER3D_USE_CACHE_YZ, RASTER3D_USE_CACHE_XYZ, the
 * result of Rast3d_cache_size_encode() (cf.{g3d:G3d.cacheSizeEncode}), or any
 * positive integer which explicitly specifies the number of tiles.
 *
 *  \param map
 *  \param minUnlocked
 *  \return void
 */

void Rast3d_min_unlocked(RASTER3D_Map *map, int minUnlocked)
{
    if (!map->useCache)
        Rast3d_fatal_error(
            "Rast3d_autoLockOff: function invalid in non-cache mode");

    Rast3d_cache_set_min_unlock(map->cache,
                                Rast3d__compute_cache_size(map, minUnlocked));
}

/*---------------------------------------------------------------------------*/

/*!
 * \brief
 *
 *  Starts a new cycle.
 *
 *  \param map
 *  \return 1 ... if successful,
 *          0 ... otherwise.
 */

int Rast3d_begin_cycle(RASTER3D_Map *map)
{
    if (!Rast3d_unlock_all(map)) {
        Rast3d_fatal_error("Rast3d_begin_cycle: error in Rast3d_unlock_all");
        return 0;
    }

    Rast3d_autolock_on(map);
    return 1;
}

/*---------------------------------------------------------------------------*/

/*!
 * \brief
 *
 * Ends a cycle.
 *
 *  \param map
 *  \return 1 ... if successful,
 *          0 ... otherwise.
 */

int Rast3d_end_cycle(RASTER3D_Map *map)
{
    Rast3d_autolock_off(map);
    return 1;
}
