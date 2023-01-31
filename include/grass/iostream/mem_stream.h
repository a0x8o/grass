/****************************************************************************
 *
 *  MODULE:     iostream
 *

 *  COPYRIGHT (C) 2007 Laura Toma
 *
 *

 *  Iostream is a library that implements streams, external memory
 *  sorting on streams, and an external memory priority queue on
 *  streams. These are the fundamental components used in external
 *  memory algorithms.

 * Credits: The library was developed by Laura Toma.  The kernel of
 * class STREAM is based on the similar class existent in the GPL TPIE
 * project developed at Duke University. The sorting and priority
 * queue have been developed by Laura Toma based on communications
 * with Rajiv Wickremesinghe. The library was developed as part of
 * porting Terraflow to GRASS in 2001.  PEARL upgrades in 2003 by
 * Rajiv Wickremesinghe as part of the Terracost project.

 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *

 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 *  General Public License for more details.  *
 *  **************************************************************************/

#ifndef _MEM_STREAM_H
#define _MEM_STREAM_H

#include <stdlib.h>
#include <assert.h>

#include <cstring>
#include <iostream>

template <class T>
class MEM_STREAM {
private:
    T *data;
    T *curr;
    T *dataend;
    int len;

public:
    MEM_STREAM(T *data, int len);
    ~MEM_STREAM(void);

    // Read and write elements.
    AMI_err read_item(T **elt);

    AMI_err write_item(const T &elt);

    // Return the number of items in the stream.
    off_t stream_len(void);

    // Return the path name of this stream.
    AMI_err name(char **stream_name);

    // Move to a specific item in the stream.
    AMI_err seek(off_t offset);

    char *sprint();
};

/**********************************************************************/

template <class T>
MEM_STREAM<T>::MEM_STREAM(T *datap, int lenv)
{

    data = datap;
    dataend = data + lenv;
    curr = datap;
    len = lenv;
}

/**********************************************************************/
// Return the number of items in the stream.
template <class T>
off_t MEM_STREAM<T>::stream_len(void)
{

    return len;
}

/**********************************************************************/
// Return the path name of this stream.
template <class T>
AMI_err MEM_STREAM<T>::name(char **stream_name)
{

    const char *path = "dummy";

    *stream_name = new char[strlen(path) + 1];
    strcpy(*stream_name, path);

    return AMI_ERROR_NO_ERROR;
}

/**********************************************************************/
// Move to a specific offset within the (sub)stream.
template <class T>
AMI_err MEM_STREAM<T>::seek(off_t offset)
{

    assert(offset <= len);

    curr = data + offset;

    return AMI_ERROR_NO_ERROR;
}

/**********************************************************************/
template <class T>
MEM_STREAM<T>::~MEM_STREAM(void)
{
}

/**********************************************************************/
template <class T>
AMI_err MEM_STREAM<T>::read_item(T **elt)
{

    assert(data);

    if (curr == dataend) {
        return AMI_ERROR_END_OF_STREAM;
    }
    *elt = curr;
    curr++;
    return AMI_ERROR_NO_ERROR;
}

/**********************************************************************/

template <class T>
AMI_err MEM_STREAM<T>::write_item(const T &elt)
{

    assert(data);

    if (curr == dataend) {
        return AMI_ERROR_END_OF_STREAM;
    }
    *curr = elt;
    curr++;
    return AMI_ERROR_NO_ERROR;
}

/**********************************************************************/
// sprint()
// Return a string describing the stream
//
// This function gives easy access to the file name, length.
// It is not reentrant, but this should not be too much of a problem
// if you are careful.
template <class T>
char *MEM_STREAM<T>::sprint()
{
    static char buf[BUFSIZ];
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
>>>>>>> osgeo-main
    sprintf(buf, "[MEM_STREAM %d]", stream_len());
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    sprintf(buf, "[MEM_STREAM %d]", stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    sprintf(buf, "[MEM_STREAM %d]", stream_len());
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
    sprintf(buf, "[MEM_STREAM %d]", stream_len());
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    sprintf(buf, "[MEM_STREAM %d]", stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
    sprintf(buf, "[MEM_STREAM %d]", stream_len());
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    sprintf(buf, "[MEM_STREAM %d]", stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
    sprintf(buf, "[MEM_STREAM %d]", stream_len());
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    sprintf(buf, "[MEM_STREAM %d]", stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> osgeo-main
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
=======
    sprintf(buf, "[MEM_STREAM %d]", stream_len());
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    sprintf(buf, "[MEM_STREAM %d]", stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
    sprintf(buf, "[MEM_STREAM %d]", stream_len());
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    sprintf(buf, "[MEM_STREAM %d]", stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
    sprintf(buf, "[MEM_STREAM %d]", stream_len());
=======
    snprintf(buf, sizeof(buf), "[MEM_STREAM %d]", stream_len());
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
    return buf;
}

#endif // _MEM_STREAM_H
