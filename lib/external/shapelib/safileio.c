/******************************************************************************
 *
 * Project:  Shapelib
 * Purpose:  Default implementation of file io based on stdio.
 * Author:   Frank Warmerdam, warmerdam@pobox.com
 *
 ******************************************************************************
 * Copyright (c) 2007, Frank Warmerdam
 *
 * SPDX-License-Identifier: MIT OR LGPL-2.0-or-later
 ******************************************************************************
 *
 */

#include "shapefil.h"

#include <assert.h>
#include <math.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
<<<<<<< HEAD
=======
#include <stdio.h>

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
SHP_CVSID("$Id: safileio.c,v 1.6 2018-06-15 19:56:32 erouault Exp $")
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))

=======
SHP_CVSID("$Id: safileio.c,v 1.4 2008-01-16 20:05:14 bram Exp $")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
SHP_CVSID("$Id: safileio.c,v 1.4 2008-01-16 20:05:14 bram Exp $")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
SHP_CVSID("$Id: safileio.c,v 1.6 2018-06-15 19:56:32 erouault Exp $")

>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
#ifdef SHPAPI_UTF8_HOOKS
#ifdef SHPAPI_WINDOWS
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX
#include <windows.h>
#pragma comment(lib, "kernel32.lib")
#endif
#endif

<<<<<<< HEAD
static SAFile SADFOpen(const char *pszFilename, const char *pszAccess,
                       void *pvUserData)
=======
/************************************************************************/
/*                              SADFOpen()                              */
/************************************************************************/
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

SAFile SADFOpen(const char *pszFilename, const char *pszAccess)

=======
SAFile SADFOpen(const char *pszFilename, const char *pszAccess)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
SAFile SADFOpen(const char *pszFilename, const char *pszAccess)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

SAFile SADFOpen(const char *pszFilename, const char *pszAccess)

>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
{
    (void)pvUserData;
    return (SAFile)fopen(pszFilename, pszAccess);
}

<<<<<<< HEAD
static SAOffset SADFRead(void *p, SAOffset size, SAOffset nmemb, SAFile file)
=======
/************************************************************************/
/*                              SADFRead()                              */
/************************************************************************/

SAOffset SADFRead(void *p, SAOffset size, SAOffset nmemb, SAFile file)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
{
    return (SAOffset)fread(p, (size_t)size, (size_t)nmemb, (FILE *)file);
}

<<<<<<< HEAD
static SAOffset SADFWrite(const void *p, SAOffset size, SAOffset nmemb,
                          SAFile file)
=======
/************************************************************************/
/*                             SADFWrite()                              */
/************************************************************************/

SAOffset SADFWrite(void *p, SAOffset size, SAOffset nmemb, SAFile file)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
{
    return (SAOffset)fwrite(p, (size_t)size, (size_t)nmemb, (FILE *)file);
}

<<<<<<< HEAD
static SAOffset SADFSeek(SAFile file, SAOffset offset, int whence)
=======
/************************************************************************/
/*                              SADFSeek()                              */
/************************************************************************/

SAOffset SADFSeek(SAFile file, SAOffset offset, int whence)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
{
#if defined(_MSC_VER) && _MSC_VER >= 1400
    return (SAOffset)_fseeki64((FILE *)file, (__int64)offset, whence);
#else
    return (SAOffset)fseek((FILE *)file, (long)offset, whence);
#endif
}

<<<<<<< HEAD
static SAOffset SADFTell(SAFile file)
=======
/************************************************************************/
/*                              SADFTell()                              */
/************************************************************************/

SAOffset SADFTell(SAFile file)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
{
#if defined(_MSC_VER) && _MSC_VER >= 1400
    return (SAOffset)_ftelli64((FILE *)file);
#else
    return (SAOffset)ftell((FILE *)file);
#endif
}

<<<<<<< HEAD
static int SADFFlush(SAFile file)
=======
/************************************************************************/
/*                             SADFFlush()                              */
/************************************************************************/

int SADFFlush(SAFile file)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
{
    return fflush((FILE *)file);
}

<<<<<<< HEAD
static int SADFClose(SAFile file)
=======
/************************************************************************/
/*                             SADFClose()                              */
/************************************************************************/

int SADFClose(SAFile file)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
{
    return fclose((FILE *)file);
}

<<<<<<< HEAD
static int SADRemove(const char *filename, void *pvUserData)
=======
/************************************************************************/
/*                             SADFClose()                              */
/************************************************************************/

int SADRemove(const char *filename)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
{
    (void)pvUserData;
    return remove(filename);
}

<<<<<<< HEAD
static void SADError(const char *message)
=======
/************************************************************************/
/*                              SADError()                              */
/************************************************************************/

void SADError(const char *message)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
{
    fprintf(stderr, "%s\n", message);
}

<<<<<<< HEAD
void SASetupDefaultHooks(SAHooks *psHooks)
=======
/************************************************************************/
/*                        SASetupDefaultHooks()                         */
/************************************************************************/

void SASetupDefaultHooks(SAHooks *psHooks)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
{
    psHooks->FOpen = SADFOpen;
    psHooks->FRead = SADFRead;
    psHooks->FWrite = SADFWrite;
    psHooks->FSeek = SADFSeek;
    psHooks->FTell = SADFTell;
    psHooks->FFlush = SADFFlush;
    psHooks->FClose = SADFClose;
    psHooks->Remove = SADRemove;

    psHooks->Error = SADError;
    psHooks->Atof = atof;
    psHooks->pvUserData = NULL;
}

#ifdef SHPAPI_WINDOWS

<<<<<<< HEAD
static wchar_t *Utf8ToWideChar(const char *pszFilename)
=======
/************************************************************************/
/*                          Utf8ToWideChar                              */
/************************************************************************/

const wchar_t *Utf8ToWideChar(const char *pszFilename)
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
{
    const int nMulti = (int)strlen(pszFilename) + 1;
    const int nWide =
        MultiByteToWideChar(CP_UTF8, 0, pszFilename, nMulti, 0, 0);
    if (nWide == 0) {
        return NULL;
    }
    wchar_t *pwszFileName = (wchar_t *)malloc(nWide * sizeof(wchar_t));
    if (pwszFileName == NULL) {
        return NULL;
    }
    if (MultiByteToWideChar(CP_UTF8, 0, pszFilename, nMulti, pwszFileName,
                            nWide) == 0) {
        free(pwszFileName);
        return NULL;
    }
    return pwszFileName;
}

/************************************************************************/
/*                           SAUtf8WFOpen                               */
/************************************************************************/

static SAFile SAUtf8WFOpen(const char *pszFilename, const char *pszAccess,
                           void *pvUserData)
{
    (void)pvUserData;
    SAFile file = NULL;
<<<<<<< HEAD
    wchar_t *pwszFileName = Utf8ToWideChar(pszFilename);
    wchar_t *pwszAccess = Utf8ToWideChar(pszAccess);
=======
    const wchar_t *pwszFileName, *pwszAccess;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    pwszFileName = Utf8ToWideChar(pszFilename);
    pwszAccess = Utf8ToWideChar(pszAccess);
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
    if (pwszFileName != NULL && pwszAccess != NULL) {
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    pwszFileName = Utf8ToWideChar(pszFilename);
    pwszAccess = Utf8ToWideChar(pszAccess);
    if (pwszFileName != NULL && pwszFileName != NULL) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    pwszFileName = Utf8ToWideChar(pszFilename);
    pwszAccess = Utf8ToWideChar(pszAccess);
    if (pwszFileName != NULL && pwszAccess != NULL) {
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
        file = (SAFile)_wfopen(pwszFileName, pwszAccess);
    }
    free(pwszFileName);
    free(pwszAccess);
    return file;
}

<<<<<<< HEAD
static int SAUtf8WRemove(const char *pszFilename, void *pvUserData)
=======
/************************************************************************/
/*                             SAUtf8WRemove()                          */
/************************************************************************/

int SAUtf8WRemove(const char *pszFilename)
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
{
    (void)pvUserData;
    wchar_t *pwszFileName = Utf8ToWideChar(pszFilename);
    int rc = -1;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    if (pwszFileName != NULL) {
        rc = _wremove(pwszFileName);
    }
    free(pwszFileName);
    return rc;
}

#endif

#ifdef SHPAPI_UTF8_HOOKS
<<<<<<< HEAD
#ifndef SHPAPI_WINDOWS
#error "no implementations of UTF-8 hooks available for this platform"
#endif
=======

/************************************************************************/
/*                          SASetupUtf8Hooks()                          */
/************************************************************************/
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))

void SASetupUtf8Hooks(SAHooks *psHooks)
{
    psHooks->FOpen = SAUtf8WFOpen;
    psHooks->Remove = SAUtf8WRemove;
    psHooks->FRead = SADFRead;
    psHooks->FWrite = SADFWrite;
    psHooks->FSeek = SADFSeek;
    psHooks->FTell = SADFTell;
    psHooks->FFlush = SADFFlush;
    psHooks->FClose = SADFClose;

    psHooks->Error = SADError;
    psHooks->Atof = atof;
}
#endif
