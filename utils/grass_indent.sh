#!/bin/sh

# Indent source code according to GRASS GIS submitting rules

# Should be in sync with:
#     https://trac.osgeo.org/grass/wiki/Submitting/C
#     https://grasswiki.osgeo.org/wiki/Development#Explanation_of_C_indentation_rules

# Dependencies:
#     indent

# Changes and their reasons:
#    -ts8 -ut -> --no-tabs
#        Do not use 8 space wide tabs when indent level is 4

# TODO: replace short flags by long ones to improve readability

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
case "$(uname)" in
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
case "$(uname)" in
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
case "$(uname)" in
=======
<<<<<<< HEAD
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
case "$(uname)" in
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
case "$(uname)" in
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
case "$(uname)" in
=======
<<<<<<< HEAD
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
case "$(uname)" in
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
case "$(uname)" in
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> main
=======
case "$(uname)" in
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
case "$(uname)" in
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
case "$(uname)" in
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
case "$(uname)" in
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
case "$(uname)" in
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
case "$(uname)" in
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
case "$(uname)" in
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
case "$(uname)" in 
=======
case "$(uname)" in
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
case "$(uname)" in 
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
case "$(uname)" in
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
case "$(uname)" in 
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
case "$(uname)" in
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
case "$(uname)" in 
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
case "$(uname)" in
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
 Darwin | *BSD*)
  INDENT=$(which gindent)
  ;;
 *)
  INDENT=$(which indent)
  ;;
esac

if [ -z "$INDENT" ]; then
 echo "Failed to find the 'indent' (or 'gindent' on BSD platforms) command."
 exit 1
fi

if [ $# -lt 1 ] ; then
 echo "No files specified (give file name(s) as parameter)"
 exit 1
else
 ${INDENT} -npro -bad -bap -bbb -br -bli0 -bls -cli0 -ncs -fc1 -hnl -i4 \
      -nbbo -nbc -nbfda -nbfde -ncdb -ncdw -nce -nfca -npcs -nprs \
      -npsl -nsc -nsob -saf -sai -saw -sbi0 -ss --no-tabs "$@"

 # fix broken gettext macros:
 grep -l '\<_$' "$@" | \
  while read file ; do sed -i -e '/[( \t]_$/{;N;s/\n[ \t]*//;}' "$file" ; done

 # restore original file with timestamp if indent did not change anything
 for file in "$@" ; do
  cmp "$file"~ "$file" > /dev/null && mv -f "$file"~ "$file"
 done
fi
