/*!
   \file lib/manage/sighold.c

   \brief Manage Library - Hold signals

   (C) 2001-2011 by the GRASS Development Team

   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.

   \author Original author CERL
 */

#include <signal.h>
#include <grass/config.h>

/*!
   \brief Hold signals

   \param hold

   \return 0
 */
int M__hold_signals(int hold)
{
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
>>>>>>> osgeo-main
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
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
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
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
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
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
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
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
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
=======
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
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
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
=======
    void (*sig)(int) = hold ? SIG_IGN : SIG_DFL;
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
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
    void (*sig)() = hold ? SIG_IGN : SIG_DFL;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))

    signal(SIGINT, sig);

#ifndef __MINGW32__
    signal(SIGQUIT, sig);
#endif

#ifdef SIGTSTP
    signal(SIGTSTP, sig);
#endif

    return 0;
}
