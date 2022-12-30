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

#ifndef _AMI_STREAM_H
#define _AMI_STREAM_H

#include <grass/config.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>

#include <cstring>
#include <iostream>
using std::cerr;
using std::cout;
using std::endl;
using std::istream;
using std::ofstream;
using std::ostream;

extern "C" {
#include <grass/gis.h>
}

#define MAX_STREAMS_OPEN 200

#include "mm.h" // Get the memory manager.

#define DEBUG_DELETE       if (0)
#define DEBUG_STREAM_LEN   if (0)
#define DEBUG_ASSERT       if (0)

// The name of the environment variable which keeps the name of the
// directory where streams are stored
#define STREAM_TMPDIR      "STREAM_DIR"

// All streams will be names STREAM_*****
#define BASE_NAME          "STREAM"

#define STREAM_BUFFER_SIZE (1 << 18)

//
// AMI error codes are returned using the AMI_err type.
//
enum AMI_err {
    AMI_ERROR_NO_ERROR = 0,
    AMI_ERROR_IO_ERROR,
    AMI_ERROR_END_OF_STREAM,
    AMI_ERROR_OUT_OF_RANGE,
    AMI_ERROR_READ_ONLY,
    AMI_ERROR_OS_ERROR,
    AMI_ERROR_MM_ERROR,
    AMI_ERROR_OBJECT_INITIALIZATION,
    AMI_ERROR_PERMISSION_DENIED,
    AMI_ERROR_INSUFFICIENT_MAIN_MEMORY,
    AMI_ERROR_INSUFFICIENT_AVAILABLE_STREAMS,
    AMI_ERROR_ENV_UNDEFINED,
    AMI_ERROR_NO_MAIN_MEMORY_OPERATION,
};

extern const char *ami_str_error[];

//
// AMI stream types passed to constructors
//
enum AMI_stream_type {
    AMI_READ_STREAM = 1,    // Open existing stream for reading
    AMI_WRITE_STREAM,       // Open for writing.  Create if non-existent
    AMI_APPEND_STREAM,      // Open for writing at end.  Create if needed.
    AMI_READ_WRITE_STREAM,  // Open to read and write.
    AMI_APPEND_WRITE_STREAM // Open for writing at end (write only mode).
};

enum persistence {
    // Delete the stream from the disk when it is destructed.
    PERSIST_DELETE = 0,
    // Do not delete the stream from the disk when it is destructed.
    PERSIST_PERSISTENT,
    // Delete each block of data from the disk as it is read.
    PERSIST_READ_ONCE
};

/* an un-templated version makes for easier debugging */
class UntypedStream {
protected:
    FILE *fp;
    int fildes; // descriptor of file
    AMI_stream_type access_mode;
    char path[BUFSIZ];
    persistence per;

    // 0 for streams, positive for substreams
    unsigned int substream_level;

    // If this stream is actually a substream, these will be set to
    // indicate the portion of the file that is part of this stream.  If
    // the stream is the whole file, they will be set to -1. Both are in
    // T units.
    off_t logical_bos;
    off_t logical_eos;

    // stream buffer passed in the call to setvbuf when file is opened
    char *buf;
    int eof_reached;

public:
    static unsigned int get_block_length()
    {
        return STREAM_BUFFER_SIZE;
        // return getpagesize();
    };
};

template <class T>
class AMI_STREAM : public UntypedStream {

protected:
    T read_tmp; /* this is ugly... RW */

public:
    // An AMI_stream with default name
    AMI_STREAM();

    // An AMI stream based on a specific path name.
    AMI_STREAM(const char *path_name,
               AMI_stream_type st = AMI_READ_WRITE_STREAM);

    // convenience function with split path_name
    // AMI_STREAM(const char *dir_name, const char *file_name, AMI_stream_type
    // st);

    // A psuedo-constructor for substreams.
    AMI_err new_substream(AMI_stream_type st, off_t sub_begin, off_t sub_end,
                          AMI_STREAM<T> **sub_stream);

    // Destructor
    ~AMI_STREAM(void);

    // Read and write elements.
    AMI_err read_item(T **elt);
    AMI_err write_item(const T &elt);
    AMI_err read_array(T *data, off_t len, off_t *lenp = NULL);
    AMI_err write_array(const T *data, off_t len);

    // Return the number of items in the stream.
    off_t stream_len(void);

    // Return the path name of this stream.
    AMI_err name(char **stream_name);
    const char *name() const;

    // Move to a specific item in the stream.
    AMI_err seek(off_t offset);

    // Query memory usage
    static AMI_err
    main_memory_usage(size_t *usage,
                      MM_stream_usage usage_type = MM_STREAM_USAGE_OVERHEAD);

    void persist(persistence p);

    char *sprint();

    // have we hit the end of the stream
    int eof();
};

/**********************************************************************/

/**********************************************************************/
/* creates a random file name, opens the file for reading and writing
   and and returns a file descriptor */
/* int ami_single_temp_name(char *base, char* tmp_path); */
/* fix from Andy Danner */
int ami_single_temp_name(const std::string &base, char *tmp_path);

/**********************************************************************/
/* given fd=fide descriptor, associates with it a stream aopened in
   access_mode and returns it */
FILE *open_stream(int fd, AMI_stream_type st);

/**********************************************************************/
/* open the file whose name is pathname in access mode */
FILE *open_stream(char *pathname, AMI_stream_type st);

/********************************************************************/
//  An  AMI stream with default name.
template <class T>
AMI_STREAM<T>::AMI_STREAM()
{

    access_mode = AMI_READ_WRITE_STREAM;
    int fd = ami_single_temp_name(BASE_NAME, path);
    fildes = fd;
    fp = open_stream(fd, access_mode);

    /* a stream is by default buffered with a buffer of size BUFSIZ=1K */
    buf = new char[STREAM_BUFFER_SIZE];
    if (setvbuf(fp, buf, _IOFBF, STREAM_BUFFER_SIZE) != 0) {
        cerr << "ERROR: setvbuf failed (stream " << path
             << ") with: " << strerror(errno) << endl;
        exit(1);
    }

    // By default, all streams are deleted at destruction time.
    per = PERSIST_DELETE;

    // Not a substream.
    substream_level = 0;
    logical_bos = logical_eos = -1;

    // why is this here in the first place?? -RW
    seek(0);

    eof_reached = 0;

    // Register memory usage before returning.
    // size_t usage;
    // main_memory_usage(&usage,  MM_STREAM_USAGE_CURRENT);
    // MM_manager.register_allocation(usage);
}

/**********************************************************************/
// An AMI stream based on a specific path name.
template <class T>
AMI_STREAM<T>::AMI_STREAM(const char *path_name, AMI_stream_type st)
{

    access_mode = st;

    if (path_name == NULL) {
        int fd = ami_single_temp_name(BASE_NAME, path);
        fildes = fd;
        fp = open_stream(fd, access_mode);
    }
    else {
        strcpy(path, path_name);
        fp = open_stream(path, st);
        fildes = -1;
    }

    /* a stream is by default buffered with a buffer of size BUFSIZ=1K */
    buf = new char[STREAM_BUFFER_SIZE];
    if (setvbuf(fp, buf, _IOFBF, STREAM_BUFFER_SIZE) != 0) {
        cerr << "ERROR: setvbuf failed (stream " << path
             << ") with: " << strerror(errno) << endl;
        exit(1);
    }

    eof_reached = 0;

    // By default, all streams are deleted at destruction time.
    if (st == AMI_READ_STREAM) {
        per = PERSIST_PERSISTENT;
    }
    else {
        per = PERSIST_DELETE;
    }

    // Not a substream.
    substream_level = 0;
    logical_bos = logical_eos = -1;

    seek(0);

    // Register memory usage before returning.
    // size_t usage;
    // main_memory_usage(&usage,  MM_STREAM_USAGE_CURRENT);
    // MM_manager.register_allocation(usage);
}

/**********************************************************************/
// A psuedo-constructor for substreams.
template <class T>
AMI_err AMI_STREAM<T>::new_substream(AMI_stream_type st, off_t sub_begin,
                                     off_t sub_end, AMI_STREAM<T> **sub_stream)
{

    // assume this for now
    assert(st == AMI_READ_STREAM);

#ifdef __MINGW32__
    /* MINGW32: reopen file here for stream_len() below */
    // reopen the file
    AMI_STREAM<T> *substr = new AMI_STREAM<T>(path, st);
#endif

    // check range
    if (substream_level) {
        if ((sub_begin >= (logical_eos - logical_bos)) ||
            (sub_end >= (logical_eos - logical_bos))) {

            return AMI_ERROR_OUT_OF_RANGE;
        }
    }
    else {
        off_t len = stream_len();
        if (sub_begin > len || sub_end > len) {

            return AMI_ERROR_OUT_OF_RANGE;
        }
    }

#ifndef __MINGW32__
    // reopen the file
    AMI_STREAM<T> *substr = new AMI_STREAM<T>(path, st);
#endif

    // Set up the beginning and end positions.
    if (substream_level) {
        substr->logical_bos = logical_bos + sub_begin;
        substr->logical_eos = logical_bos + sub_end + 1;
    }
    else {
        substr->logical_bos = sub_begin;
        substr->logical_eos = sub_end + 1;
    }

    // Set the current position.
    substr->seek(0);

    substr->eof_reached = 0;

    // set substream level
    substr->substream_level = substream_level + 1;

    substr->per = per; // set persistence

    //*sub_stream = (AMI_base_stream < T > *)substr;
    *sub_stream = substr;
    return AMI_ERROR_NO_ERROR;
}

/**********************************************************************/
// Return the number of items in the stream.
template <class T>
off_t AMI_STREAM<T>::stream_len(void)
{

    fflush(fp);

#ifdef __MINGW32__
    // stat() fails on MS Windows if the file is open, so try G_ftell() instead.
    // FIXME: not 64bit safe, but WinGrass isn't either right now.
    off_t posn_save, st_size;

    posn_save = G_ftell(fp);
    if (posn_save == -1) {
        perror("ERROR: AMI_STREAM::stream_len(): ftell(fp) failed ");
        perror(path);
        exit(1);
    }

    G_fseek(fp, 0, SEEK_END);
    st_size = G_ftell(fp);
    if (st_size == -1) {
        perror("ERROR: AMI_STREAM::stream_len(): ftell[SEEK_END] failed ");
        perror(path);
        exit(1);
    }

    G_fseek(fp, posn_save, SEEK_SET);

    // debug stream_len:
    DEBUG_STREAM_LEN fprintf(stderr, "%s: length = %lld   sizeof(T)=%d\n", path,
                             st_size, sizeof(T));

    return (st_size / sizeof(T));
#else
    struct stat statbuf;
    if (stat(path, &statbuf) == -1) {
        perror("AMI_STREAM::stream_len(): fstat failed ");
        DEBUG_ASSERT assert(0);
        exit(1);
    }

    // debug stream_len:
    DEBUG_STREAM_LEN fprintf(stderr, "%s: length = %lld   sizeof(T)=%lud\n",
                             path, (long long int)statbuf.st_size, sizeof(T));

    return (statbuf.st_size / sizeof(T));
#endif
}

/**********************************************************************/
// Return the path name of this stream.
template <class T>
AMI_err AMI_STREAM<T>::name(char **stream_name)
{

    *stream_name = new char[strlen(path) + 1];
    strcpy(*stream_name, path);

    return AMI_ERROR_NO_ERROR;
}

// Return the path name of this stream.
template <class T>
const char *AMI_STREAM<T>::name() const
{
    return path;
}

/**********************************************************************/
// Move to a specific offset within the (sub)stream.
template <class T>
AMI_err AMI_STREAM<T>::seek(off_t offset)
{

    off_t seek_offset;

    if (substream_level) { // substream
        if (offset > (unsigned)(logical_eos - logical_bos)) {
            // offset out of range
            cerr << "ERROR: AMI_STREAM::seek bos=" << logical_bos
                 << ", eos=" << logical_eos << ", offset " << offset
                 << " out of range.\n";
            DEBUG_ASSERT assert(0);
            exit(1);
        }
        else {
            // offset in range
            seek_offset = (logical_bos + offset) * sizeof(T);
        }
    }
    else {
        // not a substream
        seek_offset = offset * sizeof(T);
    }

    G_fseek(fp, seek_offset, SEEK_SET);

    return AMI_ERROR_NO_ERROR;
}

/**********************************************************************/
// Query memory usage
template <class T>
AMI_err AMI_STREAM<T>::main_memory_usage(size_t *usage,
                                         MM_stream_usage usage_type)
{

    switch (usage_type) {
    case MM_STREAM_USAGE_OVERHEAD:
        *usage = sizeof(AMI_STREAM<T>);
        break;
    case MM_STREAM_USAGE_BUFFER:
        // *usage = get_block_length();
        *usage = STREAM_BUFFER_SIZE * sizeof(char);
        break;
    case MM_STREAM_USAGE_CURRENT:
    case MM_STREAM_USAGE_MAXIMUM:
        // *usage = sizeof (*this) + get_block_length();
        *usage = sizeof(AMI_STREAM<T>) + STREAM_BUFFER_SIZE * sizeof(char);
        break;
    }
    return AMI_ERROR_NO_ERROR;
}

/**********************************************************************/
template <class T>
AMI_STREAM<T>::~AMI_STREAM(void)
{

    DEBUG_DELETE cerr << "~AMI_STREAM: " << path << "(" << this << ")\n";
    assert(fp);
    fclose(fp);
    delete buf;

    // Get rid of the file if not persistent and if not substream.
    if ((per != PERSIST_PERSISTENT) && (substream_level == 0)) {
        if (unlink(path) == -1) {
            cerr << "ERROR: AMI_STREAM: failed to unlink " << path << endl;
            perror("cannot unlink: ");
            DEBUG_ASSERT assert(0);
            exit(1);
        }
    }
    // Register memory deallocation before returning.
    // size_t usage;
    // main_memory_usage(&usage,  MM_STREAM_USAGE_CURRENT);
    // MM_manager.register_deallocation(usage);
}

/**********************************************************************/
template <class T>
AMI_err AMI_STREAM<T>::read_item(T **elt)
{

    assert(fp);

    // if we go past substream range
    if ((logical_eos >= 0) && G_ftell(fp) >= sizeof(T) * logical_eos) {
        return AMI_ERROR_END_OF_STREAM;
    }
    else {
        if (fread((char *)(&read_tmp), sizeof(T), 1, fp) < 1) {
            if (feof(fp)) {
                eof_reached = 1;
                return AMI_ERROR_END_OF_STREAM;
            }
            else {
                cerr << "ERROR: file=" << path << ":";
                perror("cannot read!");
                return AMI_ERROR_IO_ERROR;
            }
        }

        *elt = &read_tmp;
        return AMI_ERROR_NO_ERROR;
    }
}

/**********************************************************************/
template <class T>
AMI_err AMI_STREAM<T>::read_array(T *data, off_t len, off_t *lenp)
{
    size_t nobj;
    assert(fp);

    // if we go past substream range
    if ((logical_eos >= 0) && G_ftell(fp) >= sizeof(T) * logical_eos) {
        eof_reached = 1;
        return AMI_ERROR_END_OF_STREAM;
    }
    else {
        nobj = fread((void *)data, sizeof(T), len, fp);

        if (nobj < len) { /* some kind of error */
            if (feof(fp)) {
                if (lenp)
                    *lenp = nobj;
                eof_reached = 1;
                return AMI_ERROR_END_OF_STREAM;
            }
            else {
                cerr << "ERROR: file=" << path << ":";
                perror("cannot read!");
                return AMI_ERROR_IO_ERROR;
            }
        }
        if (lenp)
            *lenp = nobj;
        return AMI_ERROR_NO_ERROR;
    }
}

/**********************************************************************/
template <class T>
AMI_err AMI_STREAM<T>::write_item(const T &elt)
{

    assert(fp);
    // if we go past substream range
    if ((logical_eos >= 0) && G_ftell(fp) >= sizeof(T) * logical_eos) {
        return AMI_ERROR_END_OF_STREAM;
    }
    else {
        if (fwrite((char *)(&elt), sizeof(T), 1, fp) < 1) {
            cerr << "ERROR: AMI_STREAM::write_item failed.\n";
            if (*path)
                perror(path);
            else
                perror("AMI_STREAM::write_item: ");
            DEBUG_ASSERT assert(0);
            exit(1);
        }

        return AMI_ERROR_NO_ERROR;
    }
}

/**********************************************************************/
template <class T>
AMI_err AMI_STREAM<T>::write_array(const T *data, off_t len)
{
    size_t nobj;

    assert(fp);
    // if we go past substream range
    if ((logical_eos >= 0) && G_ftell(fp) >= sizeof(T) * logical_eos) {
        return AMI_ERROR_END_OF_STREAM;
    }
    else {
        nobj = fwrite(data, sizeof(T), len, fp);
        if (nobj < len) {
            cerr << "ERROR: AMI_STREAM::write_array failed.\n";
            if (*path)
                perror(path);
            else
                perror("AMI_STREAM::write_array: ");
            DEBUG_ASSERT assert(0);
            exit(1);
        }
        return AMI_ERROR_NO_ERROR;
    }
}

/**********************************************************************/
template <class T>
void AMI_STREAM<T>::persist(persistence p)
{
    per = p;
}

/**********************************************************************/
// sprint()
// Return a string describing the stream
//
// This function gives easy access to the file name, length.
// It is not reentrant, but this should not be too much of a problem
// if you are careful.
template <class T>
char *AMI_STREAM<T>::sprint()
{
    static char desc[BUFSIZ + 256];
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
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
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
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
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
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
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
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
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
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
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
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
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
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
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
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
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
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
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
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
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
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
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
>>>>>>> osgeo-main
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
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
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
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
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
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
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
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
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
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
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
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
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
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
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
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
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
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
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
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
<<<<<<< HEAD
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
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
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
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
    snprintf(desc, sizeof(desc), "[AMI_STREAM %s %ld]", path,
             (long)stream_len());
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
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
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
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
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
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
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
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
=======
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
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
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
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
    sprintf(desc, "[AMI_STREAM %s %ld]", path, (long)stream_len());
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
    return desc;
}

/**********************************************************************/
template <class T>
int AMI_STREAM<T>::eof()
{
    return eof_reached;
}

#endif // _AMI_STREAM_H
