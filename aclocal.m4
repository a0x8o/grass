
AC_DEFUN([LOC_CHECK_USE],[
AC_MSG_CHECKING(whether to use $2)
AC_MSG_RESULT("$with_$1")
case "$with_$1" in
	"no")	$3=	;;
	"yes")	$3="1"	;;
	*)	AC_MSG_ERROR([*** You must answer yes or no.])	;;
esac

])

AC_DEFUN([LOC_CHECK_INC_PATH],[
AC_MSG_CHECKING(for location of $2 includes)
case "$with_$1_includes" in
y | ye | yes | n | no)
	AC_MSG_ERROR([*** You must supply a directory to --with-$1-includes.])
	;;
esac
AC_MSG_RESULT($with_$1_includes)

if test -n "$with_$1_includes" ; then
    for dir in $with_$1_includes; do
        if test -d "$dir"; then
            $3="$$3 -I$dir"
        else
            AC_MSG_ERROR([*** $2 includes directory $dir does not exist.])
        fi
    done
fi
])

AC_DEFUN([LOC_CHECK_LIB_PATH],[
AC_MSG_CHECKING(for location of $2 library)
case "$with_$1_libs" in
y | ye | yes | n | no)
	AC_MSG_ERROR([*** You must supply a directory to --with-$1-libs.])
	;;
esac
AC_MSG_RESULT($with_$1_libs)

if test -n "$with_$1_libs"; then
    for dir in $with_$1_libs; do
        if test -d "$dir"; then
            $3="$$3 -L$dir"
        else
            AC_MSG_ERROR([*** $2 library directory $dir does not exist.])
        fi
    done
fi
])

AC_DEFUN([LOC_CHECK_FRAMEWORK_PATH],[
AC_MSG_CHECKING(for location of $2 framework)
case "$with_$1_framework" in
y | ye | yes | n | no)
	AC_MSG_ERROR([*** You must supply a directory to --with-$1-framework.])
	;;
esac
AC_MSG_RESULT($with_$1_framework)

if test -n "$with_$1_framework"; then
    if test -d $with_$1_framework; then
        $3="$$3 -F$with_$1_framework"
    else
        AC_MSG_ERROR([*** $2 framework directory $dir does not exist.])
    fi
fi
])

AC_DEFUN([LOC_CHECK_SHARE_PATH],[
AC_MSG_CHECKING(for location of $2 data files)
case "$with_$1_share" in
y | ye | yes | n | no)
        AC_MSG_ERROR([*** You must supply a directory to --with-$1-share.])
        ;;
esac
AC_MSG_RESULT($with_$1_share)

if test -n "$with_$1_share" ; then
    if test -d "$with_$1_share"; then
        $3="$with_$1_share"
    else
        AC_MSG_ERROR([*** $2 data directory $dir does not exist.])
    fi
fi
])

AC_DEFUN([LOC_CHECK_LDFLAGS],[
AC_MSG_CHECKING(for $2 linking flags)
case "$with_$1_ldflags" in
y | ye | yes | n | no)
	AC_MSG_ERROR([*** You must supply a directory to --with-$1-ldflags.])
	;;
esac
AC_MSG_RESULT($with_$1_ldflags)
$3="$$3 $with_$1_ldflags"
])

AC_DEFUN([LOC_CHECK_INCLUDES],[
ac_save_cppflags="$CPPFLAGS"
CPPFLAGS="$3 $CPPFLAGS"
AC_CHECK_HEADERS($1, [], ifelse($4,[],[
    AC_MSG_ERROR([*** Unable to locate $2 includes.])
], $4))
CPPFLAGS=$ac_save_cppflags
])

dnl $1  = library
dnl $2  = header
dnl $3  = function call
dnl $4  = descriptive name
dnl $5  = LDFLAGS initialiser
dnl $6  = result variable
dnl $7  = mandatory dependencies (not added to $5)
dnl $8  = mandatory dependencies (added to $5)
dnl $9  = ACTION-IF-NOT-FOUND

define(LOC_CHECK_LINK,[
ac_save_ldflags="$LDFLAGS"
ac_save_libs="$LIBS"
AC_MSG_CHECKING(for $4 library)
LDFLAGS="$5 $LDFLAGS"
LIBS="-l$1 $7 $8"
AC_LINK_IFELSE([AC_LANG_PROGRAM([[$2]], [[$3]])],[
AC_MSG_RESULT(found)
$6="$$6 -l$1 $8"
],[
ifelse($9,[],[
    AC_MSG_ERROR([*** Unable to locate $4 library.])
],$9)
])
LIBS=${ac_save_libs}
LDFLAGS=${ac_save_ldflags}
])

dnl autoconf undefines "shift", so use "builtin([shift], ...)"

define(LOC_SHIFT1,[builtin([shift],$*)])
define(LOC_SHIFT2,[LOC_SHIFT1(LOC_SHIFT1($*))])
define(LOC_SHIFT4,[LOC_SHIFT2(LOC_SHIFT2($*))])
define(LOC_SHIFT8,[LOC_SHIFT4(LOC_SHIFT4($*))])
define(LOC_SHIFT9,[LOC_SHIFT1(LOC_SHIFT8($*))])

dnl $1  = library
dnl $2  = function
dnl $3  = descriptive name
dnl $4  = LDFLAGS initialiser
dnl $5  = result variable
dnl $6  = mandatory dependencies (not added to $5)
dnl $7  = mandatory dependencies (added to $5)
dnl $8  = ACTION-IF-NOT-FOUND
dnl $9+ = optional dependencies

define(LOC_CHECK_LIBS_0,[
AC_CHECK_LIB($1, $2, $5="$$5 -l$1 $7",[
[$8]
],$6 $7)
])

define(LOC_CHECK_LIBS_1,[
ifelse($9,[],
LOC_CHECK_LIBS_0($1,$2,,,$5,$6,$7,$8),
[
LOC_CHECK_LIBS_1($1,$2,,,$5,$6,$7,
LOC_CHECK_LIBS_1($1,$2,,,$5,$6,$7 $9,$8,LOC_SHIFT9($*)),
LOC_SHIFT9($*))
]
)
])

define(LOC_CHECK_LIBS,[
ac_save_ldflags="$LDFLAGS"
LDFLAGS="$4 $LDFLAGS"
LOC_CHECK_LIBS_1($1,$2,,,$5,$6,$7,
LDFLAGS=${ac_save_ldflags}
ifelse($8,[],[
    AC_MSG_ERROR([*** Unable to locate $3 library.])
],$8),LOC_SHIFT8($*))
LDFLAGS=${ac_save_ldflags}
])

dnl $1  = function
dnl $2  = descriptive name
dnl $3  = result variable
dnl $4  = LIBS initialiser (added to $3)
dnl $5  = LDFLAGS initialiser (not added to $3)
dnl $6  = LIBS initialiser (not added to $3)
dnl $7  = ACTION-IF-FOUND
dnl $8  = ACTION-IF-NOT-FOUND

define(LOC_CHECK_FUNC,[
ac_save_libs="$LIBS"
ac_save_ldflags="$LDFLAGS"
LIBS="$4 $6 $LIBS"
LDFLAGS="$5 $LDFLAGS"
AC_CHECK_FUNC($1,[
ifelse($7,[],[
    $3="$$3 $4"
],$7)
],[
ifelse($8,[],[
ifelse($2,[],
    [AC_MSG_ERROR([*** Unable to locate $1.])],
    [AC_MSG_ERROR([*** Unable to locate $2.])]
)
],$8)
])
LIBS=${ac_save_libs}
LDFLAGS=${ac_save_ldflags}
])

AC_DEFUN([LOC_CHECK_VERSION_STRING],[
AC_MSG_CHECKING($3 version)
ac_save_cppflags="$CPPFLAGS"
CPPFLAGS="$5 $CPPFLAGS"
AC_RUN_IFELSE([AC_LANG_SOURCE([[
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
#include <stdio.h>
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
#include <stdio.h>
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
#include <stdio.h>
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
#include <stdio.h>
=======
>>>>>>> osgeo-main
=======
#include <stdio.h>
=======
>>>>>>> osgeo-main
=======
#include <stdio.h>
=======
>>>>>>> osgeo-main
=======
#include <stdio.h>
=======
>>>>>>> osgeo-main
=======
#include <stdio.h>
=======
>>>>>>> osgeo-main
=======
#include <stdio.h>
=======
>>>>>>> osgeo-main
=======
#include <stdio.h>
=======
>>>>>>> osgeo-main
=======
#include <stdio.h>
=======
>>>>>>> osgeo-main
=======
#include <stdio.h>
=======
>>>>>>> osgeo-main
=======
#include <stdio.h>
=======
>>>>>>> osgeo-main
=======
#include <stdio.h>
=======
>>>>>>> osgeo-main
=======
#include <stdio.h>
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
#include <stdio.h> 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
#include <stdio.h>
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
=======
#include <stdio.h> 
=======
#include <stdio.h>
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
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
#include <stdio.h>
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
#include <stdio.h> 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
#include <stdio.h>
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
#include <stdio.h>
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
#include <stdio.h> 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
#include <stdio.h>
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
#include <stdio.h>
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
#include <stdio.h> 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
#include <stdio.h>
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
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
#include <$1>
int main(void) {
 FILE *fp = fopen("conftestdata","w");
 fputs($2, fp);
 return 0;
}
]])],[   $4=`cat conftestdata`
    AC_MSG_RESULT($$4)],[   AC_MSG_ERROR([*** Could not determine $3 version.]) ],[   $4=$6
    AC_MSG_RESULT([unknown (cross-compiling)]) ])
CPPFLAGS=$ac_save_cppflags
])

AC_DEFUN([LOC_CHECK_SHARE],[
AC_CHECK_FILE($3/$1, [], ifelse($4,[],[
    AC_MSG_ERROR([*** Unable to locate $2 data files.])
], $4))
])

AC_DEFUN([LOC_CHECK_VERSION_INT],[
AC_MSG_CHECKING($3 version)
ac_save_cppflags="$CPPFLAGS"
CPPFLAGS="$5 $CPPFLAGS"
AC_RUN_IFELSE([AC_LANG_SOURCE([[
#include <stdio.h>
#include <$1>
int main(void) {
 FILE *fp = fopen("conftestdata","w");
 fprintf(fp, "%d", $2);
 return 0;
}
    ]])],[   $4=`cat conftestdata`
        AC_MSG_RESULT($$4)],[   AC_MSG_ERROR([*** Could not determine $3 version.]) ],[   $4=$6
        AC_MSG_RESULT([unknown (cross-compiling)]) ])
CPPFLAGS=$ac_save_cppflags
])

dnl autoconf undefines "eval", so use "builtin([eval], ...)"

AC_DEFUN([LOC_PAD],[$1[]ifelse(builtin([eval],len($1) > 23),1,[
                          ],m4_substr([                        ],len($1)))])

AC_DEFUN([LOC_ARG_WITH],[
AC_ARG_WITH($1,
LOC_PAD([  --with-$1])[support $2 functionality (default: ]ifelse([$3],,yes,[$3])[)],,
[with_]patsubst([$1], -, _)[=]ifelse([$3],,yes,[$3]))
])

AC_DEFUN([LOC_ARG_WITH_INC],[
AC_ARG_WITH($1-includes,
LOC_PAD([  --with-$1-includes=DIRS])[$2 include files are in DIRS])
])

AC_DEFUN([LOC_ARG_WITH_LIB],[
AC_ARG_WITH($1-libs,
LOC_PAD([  --with-$1-libs=DIRS])[$2 library files are in DIRS])
])

AC_DEFUN([LOC_ARG_WITH_LDFLAGS],[
AC_ARG_WITH($1-ldflags,
LOC_PAD([  --with-$1-ldflags=FLAGS])[$2 needs FLAGS when linking])
])

AC_DEFUN([LOC_ARG_WITH_SHARE],[
AC_ARG_WITH($1-share,
LOC_PAD([  --with-$1-share=DIR])[$2 data files are in DIR])
])

AC_DEFUN([LOC_ARG_WITH_FRAMEWORK],[
AC_ARG_WITH($1-framework,
LOC_PAD([  --with-$1-framework=DIR])[$2 framework is in DIR])
])

AC_DEFUN([LOC_OPTIONAL],[
AC_MSG_CHECKING(whether to build $1)
if test -n "$USE_$2" ; then
	AC_MSG_RESULT(yes)
	BUILD_$3="$4"
else
	AC_MSG_RESULT(no)
	BUILD_$3=
fi
AC_SUBST(BUILD_$3)
])

dnl checks for complete floating-point support (infinity, NaN)

define(LOC_FP_TEST,[
#include <float.h>
int main(void) {
 double one = 1.0;
 double zero = 0.0;
 if (one/zero > DBL_MAX)        /* infinity */
   if (zero/zero != zero/zero)  /* NaN */
     return 0;
 return 1;
}
])

AC_DEFUN([LOC_CHECK_FP_INF_NAN],[
AC_MSG_CHECKING([for full floating-point support]$1)
AC_RUN_IFELSE([AC_LANG_SOURCE([LOC_FP_TEST])],[   AC_MSG_RESULT(yes)
    $2],[   AC_MSG_RESULT(no)
    $3],[   AC_MSG_RESULT([unknown (cross-compiling)])
    $4
])
])

dnl check whether the compiler supports the -mieee switch

AC_DEFUN([LOC_CHECK_CC_MIEEE],[
AC_MSG_CHECKING(whether "cc -mieee" works)
ac_save_cflags=${CFLAGS}
CFLAGS="$CFLAGS -mieee"
AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[]], [[]])],[   AC_MSG_RESULT(yes)
        IEEEFLAG="-mieee"],[   AC_MSG_RESULT(no)])
CFLAGS=${ac_save_cflags}
])

AC_DEFUN([LOC_MSG],[
echo "$1"
])

AC_DEFUN([LOC_PAD_26],[m4_substr([                           ],len($1))])

AC_DEFUN([LOC_YES_NO],[if test -n "${$1}" ; then echo yes ; else echo no ; fi])

AC_DEFUN([LOC_MSG_USE],[
[echo "  $1:]LOC_PAD_26($1)`LOC_YES_NO($2)`"])

AC_DEFUN(LOC_EXEEXT,[
[case $host_os in
  *cygwin* ) CYGWIN=yes;;
esac
]

[case $host_os in
  *mingw32* ) MINGW32=yes;;
esac
]
AC_MSG_CHECKING([for executable suffix])
AC_CACHE_VAL(ac_cv_exeext,
[if test "$CYGWIN" = yes || test "$MINGW32" = yes; then
  ac_cv_exeext=.exe
else
  ac_cv_exeext=no
fi])
EXEEXT=""
test x"${ac_cv_exeext}" != xno && EXEEXT=${ac_cv_exeext}
AC_MSG_RESULT(${ac_cv_exeext})
dnl Setting ac_exeext will implicitly change the ac_link command.
ac_exeext=$EXEEXT
AC_SUBST(EXEEXT)])

#------------------------------------------------------------------------
# SC_ENABLE_SHARED --
#
#	Allows the building of shared libraries
#
# Arguments:
#	none
#
# Results:
#
#	Adds the following arguments to configure:
#		--enable-shared=yes|no
#
#	Defines the following vars:
#		STATIC_BUILD	Used for building import/export libraries
#				on Windows.
#
#	Sets the following vars:
#		SHARED_BUILD	Value of 1 or 0
#------------------------------------------------------------------------

AC_DEFUN([SC_ENABLE_SHARED], [
    AC_MSG_CHECKING([how to build libraries])
    AC_ARG_ENABLE(shared,
	[  --enable-shared         build and link with shared libraries [--enable-shared]],
	[shared_ok=$enableval], [shared_ok=yes])

    if test "${enable_shared+set}" = set; then
	enableval="$enable_shared"
	shared_ok=$enableval
    else
	shared_ok=yes
    fi

    if test "$shared_ok" = "yes" ; then
	AC_MSG_RESULT([shared])
	SHARED_BUILD=1
	GRASS_LIBRARY_TYPE='shlib'
    else
	AC_MSG_RESULT([static])
	SHARED_BUILD=0
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
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
	AC_DEFINE(STATIC_BUILD, 1, [Define to 1 for Windows static build.])
=======
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
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
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
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
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
	AC_DEFINE(STATIC_BUILD, 1, [define for Windows static build])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
	GRASS_LIBRARY_TYPE='stlib'
    fi
    AC_SUBST(GRASS_LIBRARY_TYPE)
])

#--------------------------------------------------------------------
# SC_CONFIG_CFLAGS
#
#	Try to determine the proper flags to pass to the compiler
#	for building shared libraries and other such nonsense.
#
# Arguments:
#	none
#
# Results:
#
#	Defines and substitutes the following vars:
#
#       LDFLAGS -      Flags to pass to the compiler when linking object
#                       files into an executable application binary such
#                       as tclsh.
#       LD_SEARCH_FLAGS-Flags to pass to ld, such as "-R /usr/local/tcl/lib",
#                       that tell the run-time dynamic linker where to look
#                       for shared libraries such as libtcl.so.  Depends on
#                       the variable LIB_RUNTIME_DIR in the Makefile. Could
#                       be the same as CC_SEARCH_FLAGS if ${CC} is used to link.
#       CC_SEARCH_FLAGS-Flags to pass to ${CC}, such as "-Wl,-rpath,/usr/local/tcl/lib",
#                       that tell the run-time dynamic linker where to look
#                       for shared libraries such as libtcl.so.  Depends on
#                       the variable LIB_RUNTIME_DIR in the Makefile.
#       STLIB_LD -      Base command to use for combining object files
#                       into a static library.
#       SHLIB_CFLAGS -  Flags to pass to cc when compiling the components
#                       of a shared library (may request position-independent
#                       code, among other things).
#       SHLIB_LD -      Base command to use for combining object files
#                       into a shared library.
#       SHLIB_LDX -     Base command to use for combining object files
#                       into a shared C++ library.  Make sure "IS_CXX = yes"
#                       is set in the library's Makefile.
#       SHLIB_LD_FLAGS -Flags to pass when building a shared library. This
#                       differs from the SHLIB_CFLAGS as it is not used
#                       when building object files or executables.
#       SHLIB_LD_LIBS - Dependent libraries for the linker to scan when
#                       creating shared libraries.  This symbol typically
#                       goes at the end of the "ld" commands that build
#                       shared libraries. The value of the symbol is
#                       "${LIBS}" if all of the dependent libraries should
#                       be specified when creating a shared library.  If
#                       dependent libraries should not be specified (as on
#                       SunOS 4.x, where they cause the link to fail, or in
#                       general if Tcl and Tk aren't themselves shared
#                       libraries), then this symbol has an empty string
#                       as its value.
#       SHLIB_SUFFIX -  Suffix to use for the names of dynamically loadable
#                       extensions.  An empty string means we don't know how
#                       to use shared libraries on this platform.
#
#--------------------------------------------------------------------

AC_DEFUN([SC_CONFIG_CFLAGS], [
    SHLIB_CFLAGS=""
    SHLIB_LD_FLAGS=""
    SHLIB_SUFFIX=""
    SHLIB_LD=""
    SHLIB_LDX=""
    STLIB_LD='${AR} cr'
    STLIB_SUFFIX='.a'
    GRASS_TRIM_DOTS='`echo ${LIB_VER} | tr -d .`'
    GRASS_LIB_VERSIONS_OK=ok
    LDFLAGS=""
    LD_SEARCH_FLAGS=""
    LD_LIBRARY_PATH_VAR="LD_LIBRARY_PATH"

    case $host in
        *-linux-* | *-gnu* | *-kfreebsd*-gnu)
	    SHLIB_CFLAGS="-fPIC"
            SHLIB_LD_FLAGS="-Wl,-soname,\$(notdir \$[@])"
	    SHLIB_SUFFIX=".so"
	    SHLIB_LD="${CC} -shared"
            SHLIB_LDX="${CXX} -shared"
            LDFLAGS="-Wl,--export-dynamic"
            LD_SEARCH_FLAGS='-Wl,-rpath-link,${LIB_RUNTIME_DIR} -Wl,-rpath,${INST_DIR}/lib'
            LD_LIBRARY_PATH_VAR="LD_LIBRARY_PATH"
            ;;
        *-pc-cygwin)
            SHLIB_SUFFIX=".dll"
            SHLIB_LD="${CC} -shared"
            LDFLAGS="-Wl,--export-dynamic"
	    LD_LIBRARY_PATH_VAR="PATH"
	    ;;
        *-pc-mingw32 | *-w64-mingw32 | *-pc-msys)
            SHLIB_SUFFIX=".dll"
            SHLIB_LD="${CC} -shared"
            SHLIB_LDX="${CXX} -shared"
            LDFLAGS="-Wl,--export-dynamic,--enable-runtime-pseudo-reloc"
            LD_LIBRARY_PATH_VAR="PATH"
            ;;
        *-apple-darwin*)
            SHLIB_CFLAGS="-fno-common"
            SHLIB_SUFFIX=".dylib"
            SHLIB_LD="${CC} -dynamiclib -compatibility_version \${GRASS_VERSION_MAJOR}.\${GRASS_VERSION_MINOR} -current_version \${GRASS_VERSION_MAJOR}.\${GRASS_VERSION_MINOR} -install_name @rpath/lib\${LIB_NAME}\${SHLIB_SUFFIX}"
            SHLIB_LDX="${CXX} -dynamiclib -compatibility_version \${GRASS_VERSION_MAJOR}.\${GRASS_VERSION_MINOR} -current_version \${GRASS_VERSION_MAJOR}.\${GRASS_VERSION_MINOR} -install_name @rpath/lib\${LIB_NAME}\${SHLIB_SUFFIX}"
            LDFLAGS="-Wl,-rpath,${INSTDIR}/lib,-rpath,\${GISBASE}/lib"
            LD_LIBRARY_PATH_VAR="LD_RUN_PATH"
            ;;
	*-sun-solaris*)
	    # Note: If _REENTRANT isn't defined, then Solaris
	    # won't define thread-safe library routines.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	    AC_DEFINE(_REENTRANT, 1, [define _REENTRANT flag (for SunOS)])
	    AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [enable threading extensions on Solaris])
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
	    AC_DEFINE(_REENTRANT, 1, [Define to 1 for _REENTRANT flag (for SunOS).])
	    AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [Define to 1 to enable threading extensions on Solaris.])
=======
	    AC_DEFINE(_REENTRANT, 1, [define _REENTRANT flag (for SunOS)])
	    AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [enable threading extensions on Solaris])
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
	    AC_DEFINE(_REENTRANT, 1, [define _REENTRANT flag (for SunOS)])
	    AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [enable threading extensions on Solaris])
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
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
	    # Note: need the LIBS below, otherwise Tk won't find Tcl's
	    # symbols when dynamically loaded into tclsh.
            if test "$GCC" = "yes" ; then
                SHLIB_CFLAGS="-fPIC"
                SHLIB_LD="$CC -shared"
                LD_SEARCH_FLAGS='-Wl,-R,${LIB_RUNTIME_DIR}'
            else
                SHLIB_CFLAGS="-KPIC"
                SHLIB_LD="/usr/ccs/bin/ld -G -z text"
                LD_SEARCH_FLAGS='-R ${LIB_RUNTIME_DIR}'
            fi
            SHLIB_SUFFIX=".so"
            LD_LIBRARY_PATH_VAR="LD_LIBRARY_PATH"
	    ;;
	*-solaris2*)
	    # Note: Solaris is as of 2010 Oracle Solaris, not Sun Solaris
	    #       Oracle Solaris derives from Solaris 2
	    #       derives from SunOS 5
	    #       derives from UNIX System V Release 4
	    # Note: If _REENTRANT isn't defined, then Solaris
	    # won't define thread-safe library routines.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	    AC_DEFINE(_REENTRANT, 1, [define _REENTRANT flag (for SunOS)])
	    AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [enable threading extensions on Solaris])
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
	    AC_DEFINE(_REENTRANT, 1, [Define to 1 for _REENTRANT flag (for SunOS).])
	    AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [Define to 1 to enable threading extensions on Solaris.])
=======
	    AC_DEFINE(_REENTRANT, 1, [define _REENTRANT flag (for SunOS)])
	    AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [enable threading extensions on Solaris])
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
	    AC_DEFINE(_REENTRANT, 1, [define _REENTRANT flag (for SunOS)])
	    AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [enable threading extensions on Solaris])
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
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
	    # Note: need the LIBS below, otherwise Tk won't find Tcl's
	    # symbols when dynamically loaded into tclsh.
            if test "$GCC" = "yes" ; then
                SHLIB_CFLAGS="-fPIC"
                SHLIB_LD="$CC -shared"
                LD_SEARCH_FLAGS='-Wl,-R,${LIB_RUNTIME_DIR}'
            else
                SHLIB_CFLAGS="-KPIC"
                SHLIB_LD="/usr/ccs/bin/ld -G -z text"
                LD_SEARCH_FLAGS='-R ${LIB_RUNTIME_DIR}'
            fi
            SHLIB_SUFFIX=".so"
            LD_LIBRARY_PATH_VAR="LD_LIBRARY_PATH"
	    ;;
	*-freebsd*)
	    # NOTE: only FreeBSD 4+ is supported
	    # FreeBSD 3.* and greater have ELF.
	    SHLIB_CFLAGS="-fPIC"
	    #SHLIB_LD="ld -Bshareable -x"
	    SHLIB_LD="${CC} -shared"
            SHLIB_LDX="${CXX} -shared"
            SHLIB_LD_FLAGS="-Wl,-soname,\$(notdir \$[@])"
	    SHLIB_SUFFIX=".so"
	    LDFLAGS="-Wl,--export-dynamic"
	    #LD_SEARCH_FLAGS='-rpath ${LIB_RUNTIME_DIR}'
	    LD_SEARCH_FLAGS='-Wl,-rpath-link,${LIB_RUNTIME_DIR} -Wl,-rpath,${INST_DIR}/lib'
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
	    # TODO: add optional pthread support with any combination of:
	    # CFLAGS="$CFLAGS -pthread"
	    # LDFLAGS="$LDFLAGS -lpthread"
	    # AC_DEFINE(_REENTRANT, 1, [define _REENTRANT flag (for SunOS)])
	    # AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [enable threading extensions on Solaris])
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
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
	    # TODO: add optional pthread support with any combination of:
	    # CFLAGS="$CFLAGS -pthread"
	    # LDFLAGS="$LDFLAGS -lpthread"
	    # AC_DEFINE(_REENTRANT, 1, [Define to 1 for _REENTRANT flag (for SunOS).])
	    # AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [Define to 1 to enable threading extensions on Solaris.])
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
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
	    # TODO: add optional pthread support with any combination of: 
=======
	    # TODO: add optional pthread support with any combination of:
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
	    # TODO: add optional pthread support with any combination of: 
=======
	    # TODO: add optional pthread support with any combination of:
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
=======
<<<<<<< HEAD
>>>>>>> main
=======
	    # TODO: add optional pthread support with any combination of: 
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
	    # TODO: add optional pthread support with any combination of: 
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
	    # TODO: add optional pthread support with any combination of: 
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
	    # CFLAGS="$CFLAGS -pthread"
	    # LDFLAGS="$LDFLAGS -lpthread"
	    # AC_DEFINE(_REENTRANT, 1, [define _REENTRANT flag (for SunOS)])
	    # AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [enable threading extensions on Solaris])
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
	    ;;
	*-netbsd*)
	    # NetBSD has ELF.
	    SHLIB_CFLAGS="-fPIC"
	    SHLIB_LD="${CC} -shared"
            SHLIB_LDX="${CXX} -shared"
	    SHLIB_LD_LIBS="${LIBS}"
	    LDFLAGS='-Wl,-rpath,${LIB_RUNTIME_DIR} -export-dynamic'
	    SHLIB_LD_FLAGS='-Wl,-rpath,${LIB_RUNTIME_DIR} -export-dynamic'
	    LD_SEARCH_FLAGS='-Wl,-rpath,${INST_DIR}/lib -L${LIB_RUNTIME_DIR}'
	    # some older NetBSD versions do not handle version numbers with dots.
	    #STLIB_SUFFIX='${GRASS_TRIM_DOTS}.a'
	    #SHLIB_SUFFIX='${GRASS_TRIM_DOTS}.so'
	    #GRASS_LIB_VERSIONS_OK=nodots
	    # NetBSD 6 does handle version numbers with dots.
	    STLIB_SUFFIX=".a"
	    SHLIB_SUFFIX=".so"
	    # TODO: add optional pthread support with any combination of:
	    # CFLAGS="$CFLAGS -pthread"
	    # LDFLAGS="$LDFLAGS -lpthread"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	    # AC_DEFINE(_REENTRANT, 1, [define _REENTRANT flag (for SunOS)])
	    # AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [enable threading extensions on Solaris])
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
	    # AC_DEFINE(_REENTRANT, 1, [Define to 1 for _REENTRANT flag (for SunOS).])
	    # AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [Define to 1 to enable threading extensions on Solaris.])
=======
	    # AC_DEFINE(_REENTRANT, 1, [define _REENTRANT flag (for SunOS)])
	    # AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [enable threading extensions on Solaris])
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
	    # AC_DEFINE(_REENTRANT, 1, [define _REENTRANT flag (for SunOS)])
	    # AC_DEFINE(_POSIX_PTHREAD_SEMANTICS, 1, [enable threading extensions on Solaris])
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
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
	    ;;
	*aix*)
		# NOTE: do we need to support aix < 6 ?
	    LIBS="$LIBS -lc"
	    SHLIB_CFLAGS=""
	    LDFLAGS=""
        if test "$GCC" = "yes" ; then
            SHLIB_CFLAGS="-fPIC"
            SHLIB_LD="$CC -shared"
            LD_SEARCH_FLAGS='-Wl,-bsvr4,-R,${LIB_RUNTIME_DIR}'
        else
        	# assume xlc
            SHLIB_CFLAGS="-qmkshrobj"
            SHLIB_LD="$CC -shared"
            LD_SEARCH_FLAGS='-Wl,-bsvr4,-R,${LIB_RUNTIME_DIR}'
        fi
	    SHLIB_SUFFIX=".so"
	    LD_LIBRARY_PATH_VAR="LIBPATH"
	    GRASS_NEEDS_EXP_FILE=1
	    GRASS_EXPORT_FILE_SUFFIX='${LIB_VER}.exp'
	    ;;
        *)
            AC_MSG_ERROR([***Unknown platform: $host***])
            ;;
    esac

    AC_SUBST(LDFLAGS)
    AC_SUBST(LD_SEARCH_FLAGS)
    AC_SUBST(LD_LIBRARY_PATH_VAR)

    AC_SUBST(SHLIB_LD)
    AC_SUBST(SHLIB_LDX)
    AC_SUBST(SHLIB_LD_FLAGS)
    AC_SUBST(SHLIB_CFLAGS)
    AC_SUBST(SHLIB_SUFFIX)

    AC_SUBST(STLIB_LD)
    AC_SUBST(STLIB_SUFFIX)
])

dnl -------------------- OpenMP -----------------------------------------------
dnl OpenMP code borrowed and modified from Autoconf 2.69 (AC_OPENMP)
dnl to enable Clang detection
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
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

# _LOC_LANG_OPENMP
# ---------------
# Expands to some language dependent source code for testing the presence of
# OpenMP.
AC_DEFUN([_LOC_LANG_OPENMP],
[AC_LANG_SOURCE([_AC_LANG_DISPATCH([$0], _AC_LANG, $@)])])

# _LOC_LANG_OPENMP(C)
# ------------------
m4_define([_LOC_LANG_OPENMP(C)],
[
#ifndef _OPENMP
 choke me
#endif
#include <omp.h>
int main () { return omp_get_num_threads (); }
])

# _LOC_LANG_OPENMP(C++)
# --------------------
m4_copy([_LOC_LANG_OPENMP(C)], [_LOC_LANG_OPENMP(C++)])

# _LOC_LANG_OPENMP(Fortran 77)
# ---------------------------
m4_define([_LOC_LANG_OPENMP(Fortran 77)],
[
      program main
      implicit none
!$    integer tid
      tid = 42
      call omp_set_num_threads(2)
      end
])

# _LOC_LANG_OPENMP(Fortran)
# ------------------------
m4_copy([_LOC_LANG_OPENMP(Fortran 77)], [_LOC_LANG_OPENMP(Fortran)])

# LOC_OPENMP
# ---------
# Check which options need to be passed to the C compiler to support OpenMP.
# Set the OPENMP_CFLAGS / OPENMP_CXXFLAGS / OPENMP_FFLAGS variable to these
# options.
# The options are necessary at compile time (so the #pragmas are understood)
# and at link time (so the appropriate library is linked with).
# This macro takes care to not produce redundant options if $CC $CFLAGS already
# supports OpenMP. It also is careful to not pass options to compilers that
# misinterpret them; for example, most compilers accept "-openmp" and create
# an output file called 'penmp' rather than activating OpenMP support.
AC_DEFUN([LOC_OPENMP],
[
  OPENMP_[]_AC_LANG_PREFIX[]FLAGS=
  AC_ARG_ENABLE([openmp],
    [AS_HELP_STRING([--disable-openmp], [do not use OpenMP])])
  if test "$enable_openmp" != no; then
    AC_CACHE_CHECK([for $[]_AC_CC[] option to support OpenMP],
      [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp],
      [AC_LINK_IFELSE([_LOC_LANG_OPENMP],
	 [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp='none needed'],
	 [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp='unsupported'
	  dnl Try these flags:
	  dnl   GCC >= 4.2           -fopenmp
	  dnl   SunPRO C             -xopenmp
	  dnl   Intel C              -openmp
	  dnl   SGI C, PGI C         -mp
	  dnl   Tru64 Compaq C       -omp
	  dnl   IBM C (AIX, Linux)   -qsmp=omp
          dnl   Cray CCE             -homp
          dnl   NEC SX               -Popenmp
          dnl   Lahey Fortran (Linux)  --openmp
          dnl   Clang (Apple)        -Xclang -fopenmp
	  dnl If in this loop a compiler is passed an option that it doesn't
	  dnl understand or that it misinterprets, the AC_LINK_IFELSE test
	  dnl will fail (since we know that it failed without the option),
	  dnl therefore the loop will continue searching for an option, and
	  dnl no output file called 'penmp' or 'mp' is created.
	  for ac_option in -fopenmp -xopenmp -openmp -mp -omp -qsmp=omp -homp \
                           -Popenmp --openmp '-Xclang -fopenmp'; do
	    ac_save_[]_AC_LANG_PREFIX[]FLAGS=$[]_AC_LANG_PREFIX[]FLAGS
	    _AC_LANG_PREFIX[]FLAGS="$[]_AC_LANG_PREFIX[]FLAGS $ac_option"
	    AC_LINK_IFELSE([_LOC_LANG_OPENMP],
	      [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp=$ac_option])
	    _AC_LANG_PREFIX[]FLAGS=$ac_save_[]_AC_LANG_PREFIX[]FLAGS
	    if test "$ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp" != unsupported; then
	      break
	    fi
	  done])])
    case $ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp in #(
      "none needed" | unsupported)
	;; #(
      *)
	OPENMP_[]_AC_LANG_PREFIX[]FLAGS=$ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp ;;
    esac
  fi
  AC_SUBST([OPENMP_]_AC_LANG_PREFIX[FLAGS])
])

dnl -------------------- / OpenMP ---------------------------------------------

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main

# _LOC_LANG_OPENMP
# ---------------
# Expands to some language dependent source code for testing the presence of
# OpenMP.
AC_DEFUN([_LOC_LANG_OPENMP],
[AC_LANG_SOURCE([_AC_LANG_DISPATCH([$0], _AC_LANG, $@)])])

# _LOC_LANG_OPENMP(C)
# ------------------
m4_define([_LOC_LANG_OPENMP(C)],
[
#ifndef _OPENMP
 choke me
#endif
#include <omp.h>
int main () { return omp_get_num_threads (); }
])

# _LOC_LANG_OPENMP(C++)
# --------------------
m4_copy([_LOC_LANG_OPENMP(C)], [_LOC_LANG_OPENMP(C++)])

# _LOC_LANG_OPENMP(Fortran 77)
# ---------------------------
m4_define([_LOC_LANG_OPENMP(Fortran 77)],
[
      program main
      implicit none
!$    integer tid
      tid = 42
      call omp_set_num_threads(2)
      end
])

# _LOC_LANG_OPENMP(Fortran)
# ------------------------
m4_copy([_LOC_LANG_OPENMP(Fortran 77)], [_LOC_LANG_OPENMP(Fortran)])

# LOC_OPENMP
# ---------
# Check which options need to be passed to the C compiler to support OpenMP.
# Set the OPENMP_CFLAGS / OPENMP_CXXFLAGS / OPENMP_FFLAGS variable to these
# options.
# The options are necessary at compile time (so the #pragmas are understood)
# and at link time (so the appropriate library is linked with).
# This macro takes care to not produce redundant options if $CC $CFLAGS already
# supports OpenMP. It also is careful to not pass options to compilers that
# misinterpret them; for example, most compilers accept "-openmp" and create
# an output file called 'penmp' rather than activating OpenMP support.
AC_DEFUN([LOC_OPENMP],
[
  OPENMP_[]_AC_LANG_PREFIX[]FLAGS=
  AC_ARG_ENABLE([openmp],
    [AS_HELP_STRING([--disable-openmp], [do not use OpenMP])])
  if test "$enable_openmp" != no; then
    AC_CACHE_CHECK([for $[]_AC_CC[] option to support OpenMP],
      [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp],
      [AC_LINK_IFELSE([_LOC_LANG_OPENMP],
	 [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp='none needed'],
	 [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp='unsupported'
	  dnl Try these flags:
	  dnl   GCC >= 4.2           -fopenmp
	  dnl   SunPRO C             -xopenmp
	  dnl   Intel C              -openmp
	  dnl   SGI C, PGI C         -mp
	  dnl   Tru64 Compaq C       -omp
	  dnl   IBM C (AIX, Linux)   -qsmp=omp
          dnl   Cray CCE             -homp
          dnl   NEC SX               -Popenmp
          dnl   Lahey Fortran (Linux)  --openmp
          dnl   Clang (Apple)        -Xclang -fopenmp
	  dnl If in this loop a compiler is passed an option that it doesn't
	  dnl understand or that it misinterprets, the AC_LINK_IFELSE test
	  dnl will fail (since we know that it failed without the option),
	  dnl therefore the loop will continue searching for an option, and
	  dnl no output file called 'penmp' or 'mp' is created.
	  for ac_option in -fopenmp -xopenmp -openmp -mp -omp -qsmp=omp -homp \
                           -Popenmp --openmp '-Xclang -fopenmp'; do
	    ac_save_[]_AC_LANG_PREFIX[]FLAGS=$[]_AC_LANG_PREFIX[]FLAGS
	    _AC_LANG_PREFIX[]FLAGS="$[]_AC_LANG_PREFIX[]FLAGS $ac_option"
	    AC_LINK_IFELSE([_LOC_LANG_OPENMP],
	      [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp=$ac_option])
	    _AC_LANG_PREFIX[]FLAGS=$ac_save_[]_AC_LANG_PREFIX[]FLAGS
	    if test "$ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp" != unsupported; then
	      break
	    fi
	  done])])
    case $ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp in #(
      "none needed" | unsupported)
	;; #(
      *)
	OPENMP_[]_AC_LANG_PREFIX[]FLAGS=$ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp ;;
    esac
  fi
  AC_SUBST([OPENMP_]_AC_LANG_PREFIX[FLAGS])
])

dnl -------------------- / OpenMP ---------------------------------------------

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))

# _LOC_LANG_OPENMP
# ---------------
# Expands to some language dependent source code for testing the presence of
# OpenMP.
AC_DEFUN([_LOC_LANG_OPENMP],
[AC_LANG_SOURCE([_AC_LANG_DISPATCH([$0], _AC_LANG, $@)])])

# _LOC_LANG_OPENMP(C)
# ------------------
m4_define([_LOC_LANG_OPENMP(C)],
[
#ifndef _OPENMP
 choke me
#endif
#include <omp.h>
int main () { return omp_get_num_threads (); }
])

# _LOC_LANG_OPENMP(C++)
# --------------------
m4_copy([_LOC_LANG_OPENMP(C)], [_LOC_LANG_OPENMP(C++)])

# _LOC_LANG_OPENMP(Fortran 77)
# ---------------------------
m4_define([_LOC_LANG_OPENMP(Fortran 77)],
[
      program main
      implicit none
!$    integer tid
      tid = 42
      call omp_set_num_threads(2)
      end
])

# _LOC_LANG_OPENMP(Fortran)
# ------------------------
m4_copy([_LOC_LANG_OPENMP(Fortran 77)], [_LOC_LANG_OPENMP(Fortran)])

# LOC_OPENMP
# ---------
# Check which options need to be passed to the C compiler to support OpenMP.
# Set the OPENMP_CFLAGS / OPENMP_CXXFLAGS / OPENMP_FFLAGS variable to these
# options.
# The options are necessary at compile time (so the #pragmas are understood)
# and at link time (so the appropriate library is linked with).
# This macro takes care to not produce redundant options if $CC $CFLAGS already
# supports OpenMP. It also is careful to not pass options to compilers that
# misinterpret them; for example, most compilers accept "-openmp" and create
# an output file called 'penmp' rather than activating OpenMP support.
AC_DEFUN([LOC_OPENMP],
[
  OPENMP_[]_AC_LANG_PREFIX[]FLAGS=
  AC_ARG_ENABLE([openmp],
    [AS_HELP_STRING([--disable-openmp], [do not use OpenMP])])
  if test "$enable_openmp" != no; then
    AC_CACHE_CHECK([for $[]_AC_CC[] option to support OpenMP],
      [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp],
      [AC_LINK_IFELSE([_LOC_LANG_OPENMP],
	 [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp='none needed'],
	 [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp='unsupported'
	  dnl Try these flags:
	  dnl   GCC >= 4.2           -fopenmp
	  dnl   SunPRO C             -xopenmp
	  dnl   Intel C              -openmp
	  dnl   SGI C, PGI C         -mp
	  dnl   Tru64 Compaq C       -omp
	  dnl   IBM C (AIX, Linux)   -qsmp=omp
          dnl   Cray CCE             -homp
          dnl   NEC SX               -Popenmp
          dnl   Lahey Fortran (Linux)  --openmp
          dnl   Clang (Apple)        -Xclang -fopenmp
	  dnl If in this loop a compiler is passed an option that it doesn't
	  dnl understand or that it misinterprets, the AC_LINK_IFELSE test
	  dnl will fail (since we know that it failed without the option),
	  dnl therefore the loop will continue searching for an option, and
	  dnl no output file called 'penmp' or 'mp' is created.
	  for ac_option in -fopenmp -xopenmp -openmp -mp -omp -qsmp=omp -homp \
                           -Popenmp --openmp '-Xclang -fopenmp'; do
	    ac_save_[]_AC_LANG_PREFIX[]FLAGS=$[]_AC_LANG_PREFIX[]FLAGS
	    _AC_LANG_PREFIX[]FLAGS="$[]_AC_LANG_PREFIX[]FLAGS $ac_option"
	    AC_LINK_IFELSE([_LOC_LANG_OPENMP],
	      [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp=$ac_option])
	    _AC_LANG_PREFIX[]FLAGS=$ac_save_[]_AC_LANG_PREFIX[]FLAGS
	    if test "$ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp" != unsupported; then
	      break
	    fi
	  done])])
    case $ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp in #(
      "none needed" | unsupported)
	;; #(
      *)
	OPENMP_[]_AC_LANG_PREFIX[]FLAGS=$ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp ;;
    esac
  fi
  AC_SUBST([OPENMP_]_AC_LANG_PREFIX[FLAGS])
])

dnl -------------------- / OpenMP ---------------------------------------------

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))

# _LOC_LANG_OPENMP
# ---------------
# Expands to some language dependent source code for testing the presence of
# OpenMP.
AC_DEFUN([_LOC_LANG_OPENMP],
[AC_LANG_SOURCE([_AC_LANG_DISPATCH([$0], _AC_LANG, $@)])])

# _LOC_LANG_OPENMP(C)
# ------------------
m4_define([_LOC_LANG_OPENMP(C)],
[
#ifndef _OPENMP
 choke me
#endif
#include <omp.h>
int main () { return omp_get_num_threads (); }
])

# _LOC_LANG_OPENMP(C++)
# --------------------
m4_copy([_LOC_LANG_OPENMP(C)], [_LOC_LANG_OPENMP(C++)])

# _LOC_LANG_OPENMP(Fortran 77)
# ---------------------------
m4_define([_LOC_LANG_OPENMP(Fortran 77)],
[
      program main
      implicit none
!$    integer tid
      tid = 42
      call omp_set_num_threads(2)
      end
])

# _LOC_LANG_OPENMP(Fortran)
# ------------------------
m4_copy([_LOC_LANG_OPENMP(Fortran 77)], [_LOC_LANG_OPENMP(Fortran)])

# LOC_OPENMP
# ---------
# Check which options need to be passed to the C compiler to support OpenMP.
# Set the OPENMP_CFLAGS / OPENMP_CXXFLAGS / OPENMP_FFLAGS variable to these
# options.
# The options are necessary at compile time (so the #pragmas are understood)
# and at link time (so the appropriate library is linked with).
# This macro takes care to not produce redundant options if $CC $CFLAGS already
# supports OpenMP. It also is careful to not pass options to compilers that
# misinterpret them; for example, most compilers accept "-openmp" and create
# an output file called 'penmp' rather than activating OpenMP support.
AC_DEFUN([LOC_OPENMP],
[
  OPENMP_[]_AC_LANG_PREFIX[]FLAGS=
  AC_ARG_ENABLE([openmp],
    [AS_HELP_STRING([--disable-openmp], [do not use OpenMP])])
  if test "$enable_openmp" != no; then
    AC_CACHE_CHECK([for $[]_AC_CC[] option to support OpenMP],
      [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp],
      [AC_LINK_IFELSE([_LOC_LANG_OPENMP],
	 [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp='none needed'],
	 [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp='unsupported'
	  dnl Try these flags:
	  dnl   GCC >= 4.2           -fopenmp
	  dnl   SunPRO C             -xopenmp
	  dnl   Intel C              -openmp
	  dnl   SGI C, PGI C         -mp
	  dnl   Tru64 Compaq C       -omp
	  dnl   IBM C (AIX, Linux)   -qsmp=omp
          dnl   Cray CCE             -homp
          dnl   NEC SX               -Popenmp
          dnl   Lahey Fortran (Linux)  --openmp
          dnl   Clang (Apple)        -Xclang -fopenmp
	  dnl If in this loop a compiler is passed an option that it doesn't
	  dnl understand or that it misinterprets, the AC_LINK_IFELSE test
	  dnl will fail (since we know that it failed without the option),
	  dnl therefore the loop will continue searching for an option, and
	  dnl no output file called 'penmp' or 'mp' is created.
	  for ac_option in -fopenmp -xopenmp -openmp -mp -omp -qsmp=omp -homp \
                           -Popenmp --openmp '-Xclang -fopenmp'; do
	    ac_save_[]_AC_LANG_PREFIX[]FLAGS=$[]_AC_LANG_PREFIX[]FLAGS
	    _AC_LANG_PREFIX[]FLAGS="$[]_AC_LANG_PREFIX[]FLAGS $ac_option"
	    AC_LINK_IFELSE([_LOC_LANG_OPENMP],
	      [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp=$ac_option])
	    _AC_LANG_PREFIX[]FLAGS=$ac_save_[]_AC_LANG_PREFIX[]FLAGS
	    if test "$ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp" != unsupported; then
	      break
	    fi
	  done])])
    case $ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp in #(
      "none needed" | unsupported)
	;; #(
      *)
	OPENMP_[]_AC_LANG_PREFIX[]FLAGS=$ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp ;;
    esac
  fi
  AC_SUBST([OPENMP_]_AC_LANG_PREFIX[FLAGS])
])

dnl -------------------- / OpenMP ---------------------------------------------


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
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> main
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
dnl -------------------- OpenMP -----------------------------------------------
dnl OpenMP code borrowed and modified from Autoconf 2.71 (AC_OPENMP)
dnl to enable Clang detection

# _LOC_LANG_OPENMP
# ---------------
# Expands to some language dependent source code for testing the presence of
# OpenMP.
AC_DEFUN([_LOC_LANG_OPENMP],
[AC_LANG_SOURCE([_AC_LANG_DISPATCH([$0], _AC_LANG, $@)])])

# _LOC_LANG_OPENMP(C)
# ------------------
m4_define([_LOC_LANG_OPENMP(C)],
[
#ifndef _OPENMP
#error "OpenMP not supported"
#endif
#include <omp.h>
int main (void) { return omp_get_num_threads (); }
])

# _LOC_LANG_OPENMP(C++)
# --------------------
m4_copy([_LOC_LANG_OPENMP(C)], [_LOC_LANG_OPENMP(C++)])

# _LOC_LANG_OPENMP(Fortran 77)
# ---------------------------
m4_define([_LOC_LANG_OPENMP(Fortran 77)],
[
      program main
      implicit none
!$    integer tid
      tid = 42
      call omp_set_num_threads(2)
      end
])

# _LOC_LANG_OPENMP(Fortran)
# ------------------------
m4_copy([_LOC_LANG_OPENMP(Fortran 77)], [_LOC_LANG_OPENMP(Fortran)])

# LOC_OPENMP
# ---------
# Check which options need to be passed to the C compiler to support OpenMP.
# Set the OPENMP_CFLAGS / OPENMP_CXXFLAGS / OPENMP_FFLAGS variable to these
# options.
# The options are necessary at compile time (so the #pragmas are understood)
# and at link time (so the appropriate library is linked with).
# This macro takes care to not produce redundant options if $CC $CFLAGS already
# supports OpenMP.
#
# For each candidate option, we do a compile test first, then a link test;
# if the compile test succeeds but the link test fails, that means we have
# found the correct option but it doesn't work because the libraries are
# broken.  (This can happen, for instance, with SunPRO C and a bad combination
# of operating system patches.)
#
# Several of the options in our candidate list can be misinterpreted by
# compilers that don't use them to activate OpenMP support; for example,
# many compilers understand "-openmp" to mean "write output to a file
# named 'penmp'" rather than "enable OpenMP".  We can't completely avoid
# the possibility of clobbering files named 'penmp' or 'mp' in configure's
# working directory; therefore, this macro will bomb out if any such file
# already exists when it's invoked.
AC_DEFUN([LOC_OPENMP],
[AC_REQUIRE([_LOC_OPENMP_SAFE_WD])]dnl
[AC_ARG_ENABLE([openmp],
   [AS_HELP_STRING([--disable-openmp], [do not use OpenMP])])]dnl
[
  OPENMP_[]_AC_LANG_PREFIX[]FLAGS=
  if test "$enable_openmp" != no; then
    AC_CACHE_CHECK([for $[]_AC_CC[] option to support OpenMP],
      [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp],
      [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp='not found'
      dnl Try these flags:
      dnl   (on by default)      ''
      dnl   GCC >= 4.2           -fopenmp
      dnl   SunPRO C             -xopenmp
      dnl   Intel C              -openmp
      dnl   SGI C, PGI C         -mp
      dnl   Tru64 Compaq C       -omp
      dnl   IBM XL C (AIX, Linux) -qsmp=omp
      dnl   Cray CCE             -homp
      dnl   NEC SX               -Popenmp
      dnl   Lahey Fortran (Linux)  --openmp
      dnl   Clang (Apple)        -Xclang -fopenmp
      for ac_option in '' -fopenmp -xopenmp -openmp -mp -omp -qsmp=omp -homp \
                       -Popenmp --openmp '-Xclang -fopenmp'; do

        ac_save_[]_AC_LANG_PREFIX[]FLAGS=$[]_AC_LANG_PREFIX[]FLAGS
        _AC_LANG_PREFIX[]FLAGS="$[]_AC_LANG_PREFIX[]FLAGS $ac_option"
        AC_COMPILE_IFELSE([_LOC_LANG_OPENMP],
          [AC_LINK_IFELSE([_LOC_LANG_OPENMP],
            [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp=$ac_option],
            [ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp='unsupported'])])
        _AC_LANG_PREFIX[]FLAGS=$ac_save_[]_AC_LANG_PREFIX[]FLAGS

        if test "$ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp" != 'not found'; then
          break
        fi
      done
      if test "$ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp" = 'not found'; then
        ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp='unsupported'
      elif test "$ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp" = ''; then
        ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp='none needed'
      fi
      dnl _AC_OPENMP_SAFE_WD checked that these files did not exist before we
      dnl started probing for OpenMP support, so if they exist now, they were
      dnl created by the probe loop and it's safe to delete them.
      rm -f penmp mp])
    if test "$ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp" != 'unsupported' && \
       test "$ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp" != 'none needed'; then
      OPENMP_[]_AC_LANG_PREFIX[]FLAGS="$ac_cv_prog_[]_AC_LANG_ABBREV[]_openmp"
    fi
  fi
  AC_SUBST([OPENMP_]_AC_LANG_PREFIX[FLAGS])
])

# _AC_OPENMP_SAFE_WD
# ------------------
# AC_REQUIREd by AC_OPENMP.  Checks both at autoconf time and at
# configure time for files that AC_OPENMP clobbers.
AC_DEFUN([_LOC_OPENMP_SAFE_WD],
[m4_syscmd([test ! -e penmp && test ! -e mp])]dnl
[m4_if(sysval, [0], [], [m4_fatal(m4_normalize(
  [LOC_OPENMP clobbers files named 'mp' and 'penmp'.
   To use LOC_OPENMP you must not have either of these files
   at the top level of your source tree.]))])]dnl
[if test -e penmp || test -e mp; then
  AC_MSG_ERROR(m4_normalize(
    [AC@&t@_OPENMP clobbers files named 'mp' and 'penmp'.
     Aborting configure because one of these files already exists.]))
fi])

dnl -------------------- / OpenMP ---------------------------------------------


=======
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
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
dnl XXXX Begin Stolen from cdrtools-2.01
dnl XXXX by Joerg Schilling <schilling fokus fraunhofer de> et al. XXXXXXXXX

dnl XXXXXXXXX Begin Stolen (but modified) from GNU tar XXXXXXXXXXXXXXXXXXXXX
dnl Changes:

dnl One line has been changed to:    [ac_save_CC="${CC-cc}" to default to "'cc"

dnl AC_SYS_LARGEFILE_MACRO_VALUE test moved from AC_FUNC_FSEEKO into AC_SYS_LARGEFILE
dnl Do not call AC_FUNC_FSEEKO because it does not check whether fseeko() is
dnl available on non Large File mode. There are additional tests for fseeko()/ftello()
dnl inside the AC_HAVE_LARGEFILES test.

dnl largefile_cc_opt definition added

#serial 18

dnl By default, many hosts won't let programs access large files;
dnl one must use special compiler options to get large-file access to work.
dnl For more details about this brain damage please see:
dnl http://www.sas.com/standards/large.file/x_open.20Mar96.html

dnl Written by Paul Eggert <eggert@twinsun.com>.

dnl Internal subroutine of AC_SYS_LARGEFILE.
dnl AC_SYS_LARGEFILE_TEST_INCLUDES
AC_DEFUN([AC_SYS_LARGEFILE_TEST_INCLUDES],
  [[#include <sys/types.h>
    /* Check that off_t can represent 2**63 - 1 correctly.
       We can't simply "#define LARGE_OFF_T 9223372036854775807",
       since some C++ compilers masquerading as C compilers
       incorrectly reject 9223372036854775807.  */
#   define LARGE_OFF_T (((off_t) 1 << 62) - 1 + ((off_t) 1 << 62))
    int off_t_is_large[(LARGE_OFF_T % 2147483629 == 721
			&& LARGE_OFF_T % 2147483647 == 1)
		       ? 1 : -1];
  ]])

dnl Internal subroutine of AC_SYS_LARGEFILE.
dnl AC_SYS_LARGEFILE_MACRO_VALUE(C-MACRO, VALUE, CACHE-VAR, COMMENT, INCLUDES, FUNCTION-BODY)
AC_DEFUN([AC_SYS_LARGEFILE_MACRO_VALUE],
  [AC_CACHE_CHECK([for $1 value needed for large files], $3,
     [$3=no
      AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[$5]], [[$6]])],[],[AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[#define $1 $2
$5
	   ]], [[$6]])],[$3=$2],[])])])
   if test "[$]$3" != no; then
     AC_DEFINE_UNQUOTED([$1], [$]$3, [$4])

   if test "$LFS_CFLAGS" ; then
     LFS_CFLAGS="$LFS_CFLAGS -D$1=[$]$3"
   else
     LFS_CFLAGS="-D$1=[$]$3"
   fi

   fi])

AC_DEFUN([AC_SYS_LARGEFILE],
  [AC_ARG_ENABLE(largefile,
     [  --disable-largefile     omit support for large files (LFS)])
   LFS_CFLAGS=
   if test "$enable_largefile" != no; then
     ac_save_cflags=$CFLAGS
     if test "`which getconf 2>&5`" ; then
       LFS_CFLAGS=`getconf LFS_CFLAGS 2>&5`
       CFLAGS="$LFS_CFLAGS $ac_save_cflags"
     fi

     AC_CACHE_CHECK([for special C compiler options needed for large files],
       ac_cv_sys_largefile_CC,
       [ac_cv_sys_largefile_CC=no
        largefile_cc_opt=""
        if test "$GCC" != yes; then
	  # IRIX 6.2 and later do not support large files by default,
	  # so use the C compiler's -n32 option if that helps.
	  AC_COMPILE_IFELSE([AC_LANG_PROGRAM([AC_SYS_LARGEFILE_TEST_INCLUDES], [[]])],[],[ac_save_CC="${CC-cc}"
	     CC="$CC -n32"
	     AC_COMPILE_IFELSE([AC_LANG_PROGRAM([AC_SYS_LARGEFILE_TEST_INCLUDES], [[]])],[ac_cv_sys_largefile_CC=' -n32'],[])
	     CC="$ac_save_CC"])
        fi])
     if test "$ac_cv_sys_largefile_CC" != no; then
       CC="$CC$ac_cv_sys_largefile_CC"
       largefile_cc_opt="$ac_cv_sys_largefile_CC"

       if test "$LFS_CFLAGS" ; then
         LFS_CFLAGS="$LFS_CFLAGS $ac_cv_sys_largefile_CC"
       else
         LFS_CFLAGS="$ac_cv_sys_largefile_CC"
         CFLAGS="$LFS_CFLAGS $ac_save_cflags"
       fi
     fi

     AC_SYS_LARGEFILE_MACRO_VALUE(_FILE_OFFSET_BITS, 64,
       ac_cv_sys_file_offset_bits,
       [Number of bits in a file offset, on hosts where this is settable.],
       AC_SYS_LARGEFILE_TEST_INCLUDES)
     AC_SYS_LARGEFILE_MACRO_VALUE(_LARGE_FILES, 1,
       ac_cv_sys_large_files,
       [Define for large files, on AIX-style hosts.],
       AC_SYS_LARGEFILE_TEST_INCLUDES)
     AC_SYS_LARGEFILE_MACRO_VALUE(_LARGEFILE_SOURCE, 1,
       ac_cv_sys_largefile_source,
       [Define to make fseeko visible on some hosts (e.g. glibc 2.2).],
       [#include <stdio.h>], [return !fseeko;])

     CFLAGS=$ac_save_cflags
   fi
  ])


AC_DEFUN([AC_FUNC_FSEEKO],
  [AC_SYS_LARGEFILE_MACRO_VALUE(_LARGEFILE_SOURCE, 1,
     ac_cv_sys_largefile_source,
     [Define to make fseeko visible on some hosts (e.g. glibc 2.2).],
     [#include <stdio.h>], [return !fseeko;])
   # We used to try defining _XOPEN_SOURCE=500 too, to work around a bug
   # in glibc 2.1.3, but that breaks too many other things.
   # If you want fseeko and ftello with glibc, upgrade to a fixed glibc.

   AC_CACHE_CHECK([for fseeko], ac_cv_func_fseeko,
     [ac_cv_func_fseeko=no
      AC_LINK_IFELSE([AC_LANG_PROGRAM([[#include <stdio.h>]], [[return fseeko && fseeko (stdin, 0, 0);]])],[ac_cv_func_fseeko=yes],[])])
   if test $ac_cv_func_fseeko != no; then
     AC_DEFINE(HAVE_FSEEKO, 1,
       [Define if fseeko (and presumably ftello) exists and is declared.])
   fi])


dnl XXXXXXXXXXXXXXXXXX End Stolen (but modified) from GNU tar XXXXXXXXXXXXXX

AC_DEFUN([AC_HAVE_LARGEFILES],
[AC_CACHE_CHECK([if system supports Large Files at all], ac_cv_largefiles,
     	[AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[#include <stdio.h>
#include <sys/types.h>]], [[
/*
 * Check that off_t can represent 2**63 - 1 correctly.
 * We can't simply "#define LARGE_OFF_T 9223372036854775807",
 * since some C++ compilers masquerading as C compilers
 * incorrectly reject 9223372036854775807.
 *
 * For MinGW, off64_t should be used and __MSVCRT_VERSION__ >= 0x0601
 * (msvcrt.dll version 6.10 or higher) is needed for _fstat64 and _stat64.
 */
#ifdef __MINGW32__
#   define LARGE_OFF_T (((off64_t) 1 << 62) - 1 + ((off64_t) 1 << 62))
#else
#   define LARGE_OFF_T (((off_t) 1 << 62) - 1 + ((off_t) 1 << 62))
#endif
    int off_t_is_large[(LARGE_OFF_T % 2147483629 == 721
			&& LARGE_OFF_T % 2147483647 == 1)
		       ? 1 : -1];
#ifdef __MINGW32__
return !fseeko64;
return !ftello64;
#else
return !fseeko;
return !ftello;
#endif]])],[ac_cv_largefiles=yes],[ac_cv_largefiles=no])])
	if test $ac_cv_largefiles = yes; then
		AC_DEFINE(HAVE_LARGEFILES, 1, [define if we have LFS])
	  USE_LARGEFILES=1
	else
	  USE_LARGEFILES=
	  LFS_CFLAGS=
	fi
	AC_SUBST(USE_LARGEFILES)
	AC_SUBST(LFS_CFLAGS)
	])

dnl Checks for whether fseeko() is available in non large file mode
dnl and whether there is a prototype for fseeko()
dnl Defines HAVE_FSEEKO on success.
AC_DEFUN([AC_SMALL_FSEEKO],
[AC_CACHE_CHECK([for fseeko()], ac_cv_func_fseeko,
                [AC_LINK_IFELSE([AC_LANG_PROGRAM([[#include <stdio.h>]], [[return !fseeko;]])],[ac_cv_func_fseeko=yes],[ac_cv_func_fseeko=no])])
if test $ac_cv_func_fseeko = yes; then
  AC_DEFINE(HAVE_FSEEKO, 1, [define if fseeko() exists])
fi])

dnl Checks for whether ftello() is available in non large file mode
dnl and whether there is a prototype for ftello()
dnl Defines HAVE_FTELLO on success.
AC_DEFUN([AC_SMALL_FTELLO],
[AC_CACHE_CHECK([for ftello()], ac_cv_func_ftello,
                [AC_LINK_IFELSE([AC_LANG_PROGRAM([[#include <stdio.h>]], [[return !ftello;]])],[ac_cv_func_ftello=yes],[ac_cv_func_ftello=no])])
if test $ac_cv_func_ftello = yes; then
  AC_DEFINE(HAVE_FTELLO, 1, [define if ftello() exists])
fi])

dnl XXXXXXXXXXX End Stolen from cdrtools-2.01 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
