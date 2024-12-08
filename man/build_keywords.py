#!/usr/bin/env python3

"""
Generates keywords.html file for core and optionally for addons modules.

Usage:

Generate core modules keywords HTML page

python man/build_keywords.py <path_to_core_modules_html_man_files>

Generate core modules and optionally inject addons keywords HTML page

python man/build_keywords.py <dir_path_to_core_modules_html_man_files>
    <dir_path_to_addons_modules_html_man_files>

@author Luca Delucchi
@author Tomas Zigo <tomas.zigo slovanet.sk> - inject addons modules keywords
"""

import os
import sys
import glob

blacklist = [
    "Display",
    "Database",
    "General",
    "Imagery",
    "Misc",
    "Postscript",
    "Raster",
    "Raster3D",
    "Temporal",
    "Vector",
]

<<<<<<< HEAD
addons_path = None
if len(sys.argv) >= 2:
    addons_path = sys.argv[1]
=======
path = sys.argv[1]
addons_path = None
if len(sys.argv) >= 3:
    addons_path = sys.argv[2]
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

year = os.getenv("VERSION_DATE")


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
def get_module_man_file_path(man_dir, module, addons_man_files):
    """Get module manual HTML file path
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
def get_module_man_file_path(man_dir, module, addons_man_files):
    """Get module manual HTML file path
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
htmlfiles = glob.glob(os.path.join(path, "*.html"))
if addons_path:
    addons_man_files = glob.glob(os.path.join(addons_path, "*.html"))
    htmlfiles.extend(addons_man_files)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

    :param str module: module manual HTML file name e.g. v.surf.rst.html
    :param addons_man_files: list of HTML manual files

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

def get_module_man_html_file_path(module):
    """Get module manual HTML file path

    :param str module: module manual HTML file name e.g. v.surf.rst.html

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    :return str module_path: core/addon module manual HTML file path
    """
    if addons_path and module in ",".join(addons_man_files):
        module_path = os.path.join(addons_path, module)
        module_path = module_path.replace(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
            os.path.commonpath([man_dir, module_path]),
            ".",
        )
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
            os.path.commonpath([path, module_path]),
            ".",
        )
    else:
        module_path = f"./{module}"
    return module_path


for html_file in htmlfiles:
    fname = os.path.basename(html_file)
    with open(html_file) as f:
        lines = f.readlines()
    # TODO maybe move to Python re (regex)
    # remove empty lines
    lines = [x for x in lines if x != "\n"]
    try:
        index_keys = lines.index("<h2>KEYWORDS</h2>\n") + 1
        index_desc = lines.index("<h2>NAME</h2>\n") + 1
    except:
        continue
    try:
        keys = lines[index_keys].split(",")
    except:
        continue
    for key in keys:
        key = key.strip()
        try:
            key = key.split(">")[1].split("<")[0]
        except:
            pass
        if not key:
<<<<<<< HEAD
<<<<<<< HEAD
            sys.exit("Empty keyword from file %s line: %s" % (fname, lines[index_keys]))
=======
            exit("Empty keyword from file %s line: %s" % (fname, lines[index_keys]))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
            sys.exit("Empty keyword from file %s line: %s" % (fname, lines[index_keys]))
>>>>>>> 66dd6d1baa (style: Fixes sys-exit-alias (PLR1722) (#3951))
        if key not in keywords.keys():
            keywords[key] = []
            keywords[key].append(fname)
        elif fname not in keywords[key]:
            keywords[key].append(fname)

for black in blacklist:
    try:
        del keywords[black]
    except:
        try:
            del keywords[black.lower()]
        except:
            continue

for key in sorted(keywords.keys()):
    # this list it is useful to create the TOC using only the first
    # character for keyword
    firstchar = key[0].lower()
    if firstchar not in char_list.keys():
        char_list[str(firstchar)] = key
    elif firstchar in char_list.keys():
        if key.lower() < char_list[str(firstchar)].lower():
            char_list[str(firstchar.lower())] = key

keywordsfile = open(os.path.join(path, "keywords.html"), "w")
keywordsfile.write(
    header1_tmpl.substitute(
<<<<<<< HEAD
<<<<<<< HEAD
        title="GRASS GIS %s Reference Manual: Keywords index" % grass_version
=======
        title="GRASS GIS %s Reference " "Manual: Keywords index" % grass_version
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
        title="GRASS GIS %s Reference Manual: Keywords index" % grass_version
>>>>>>> d10220bba4 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))
    )
)
keywordsfile.write(headerkeywords_tmpl)
keywordsfile.write("<dl>")

sortedKeys = sorted(keywords.keys(), key=lambda s: s.lower())

for key in sortedKeys:
<<<<<<< HEAD
<<<<<<< HEAD
    keyword_line = '<dt><b><a name="%s" class="urlblack">%s</a></b></dt><dd>' % (
=======
    keyword_line = '<dt><b><a name="%s" class="urlblack">%s</a></b></dt>' "<dd>" % (
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
    keyword_line = '<dt><b><a name="%s" class="urlblack">%s</a></b></dt><dd>' % (
>>>>>>> 2dd437519f (style: Manual fixes for single-line-implicit-string-concatenation violations (ISC001) (#3944))
        key,
        key,
    )
    for value in sorted(keywords[key]):
        keyword_line += (
            f' <a href="{get_module_man_html_file_path(value)}">'
            f'{value.replace(".html", "")}</a>,'
        )
    keyword_line = keyword_line.rstrip(",")
    keyword_line += "</dd>\n"
    keywordsfile.write(keyword_line)
keywordsfile.write("</dl>\n")
# create toc
toc = '<div class="toc">\n<h4 class="toc">Table of contents</h4><p class="toc">'
test_length = 0
all_keys = len(char_list.keys())
for k in sorted(char_list.keys()):
    test_length += 1
    #    toc += '<li><a href="#%s" class="toc">%s</a></li>' % (char_list[k], k)
    if test_length % 4 == 0 and not test_length == all_keys:
        toc += '\n<a href="#%s" class="toc">%s</a>, ' % (char_list[k], k)
    elif test_length % 4 == 0 and test_length == all_keys:
        toc += '\n<a href="#%s" class="toc">%s</a>' % (char_list[k], k)
    elif test_length == all_keys:
        toc += '<a href="#%s" class="toc">%s</a>' % (char_list[k], k)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    else:
        module_path = f"./{module}"
    return module_path


def build_keywords(ext):
    if ext == "html":
        from build_html import header1_tmpl, headerkeywords_tmpl, man_dir
    else:
        from build_md import (
            header1_tmpl,
            headerkeywords_tmpl,
            man_dir,
        )

    keywords = {}

    files = glob.glob(os.path.join(man_dir, f"*.{ext}"))
    # TODO: add markdown support
    if addons_path:
        addons_man_files = glob.glob(os.path.join(addons_path, f"*.{ext}"))
        files.extend(addons_man_files)
    else:
        addons_man_files = []

    char_list = {}

    for in_file in files:
        fname = os.path.basename(in_file)
        with open(in_file) as f:
            lines = f.readlines()

        if ext == "html":
            # TODO maybe move to Python re (regex)
            try:
                index_keys = lines.index("<h2>KEYWORDS</h2>\n") + 1
            except Exception:
                continue
            try:
                keys = []
                for k in lines[index_keys].split(","):
                    keys.append(k.strip().split(">")[1].split("<")[0])
            except Exception:
                continue
        else:
            keys = []
            for line in lines:
                if "keywords:" in line:
                    keys = [x.strip() for x in line.split(":", 1)[1].strip().split(",")]
                    break

        for key in keys:
            if key not in keywords.keys():
                keywords[key] = []
                keywords[key].append(fname)
            elif fname not in keywords[key]:
                keywords[key].append(fname)

    for black in blacklist:
        try:
            del keywords[black]
        except Exception:
            try:
                del keywords[black.lower()]
            except Exception:
                continue

    for key in sorted(keywords.keys()):
        # this list it is useful to create the TOC using only the first
        # character for keyword
        firstchar = key[0].lower()
        if firstchar not in char_list.keys():
            char_list[str(firstchar)] = key
        elif firstchar in char_list.keys():
            if key.lower() < char_list[str(firstchar)].lower():
                char_list[str(firstchar.lower())] = key

    with open(os.path.join(man_dir, f"keywords.{ext}"), "w") as keywordsfile:
        keywordsfile.write(
            header1_tmpl.substitute(
                title=f"GRASS GIS {grass_version} Reference Manual - Keywords index"
            )
        )
        keywordsfile.write(headerkeywords_tmpl)
        if ext == "html":
            keywordsfile.write("<dl>")
        sortedKeys = sorted(keywords.keys(), key=lambda s: s.lower())

        for key in sortedKeys:
            if ext == "html":
                keyword_line = '<dt><b><a name="{key}" class="urlblack">{key}</a></b></dt><dd>'.format(  # noqa: E501
                    key=key
                )
            else:
                keyword_line = f"### **{key}**\n"
            for value in sorted(keywords[key]):
                man_file_path = get_module_man_file_path(
                    man_dir, value, addons_man_files
                )
                if ext == "html":
                    keyword_line += f' <a href="{man_file_path}">{value.replace(f".{ext}", "")}</a>,'  # noqa: E501
                else:
                    keyword_line += f' [{value.rsplit(".", 1)[0]}]({man_file_path}),'
            keyword_line = keyword_line.rstrip(",")
            if ext == "html":
                keyword_line += "</dd>"
            keyword_line += "\n"
            keywordsfile.write(keyword_line)
        if ext == "html":
            keywordsfile.write("</dl>\n")
        if ext == "html":
            # create toc
            toc = '<div class="toc">\n<h4 class="toc">Table of contents</h4><p class="toc">'  # noqa: E501
            test_length = 0
            all_keys = len(char_list.keys())
            for k in sorted(char_list.keys()):
                test_length += 1
                # toc += '<li><a href="#%s" class="toc">%s</a></li>' % (char_list[k], k)
                if test_length % 4 == 0 and test_length != all_keys:
                    toc += '\n<a href="#%s" class="toc">%s</a>, ' % (char_list[k], k)
                elif test_length % 4 == 0 and test_length == all_keys:
                    toc += '\n<a href="#%s" class="toc">%s</a>' % (char_list[k], k)
                elif test_length == all_keys:
                    toc += '<a href="#%s" class="toc">%s</a>' % (char_list[k], k)
                else:
                    toc += '<a href="#%s" class="toc">%s</a>, ' % (char_list[k], k)
            toc += "</p></div>\n"
            keywordsfile.write(toc)

        write_footer(keywordsfile, f"index.{ext}", year, template=ext)


if __name__ == "__main__":
    from build import (
        grass_version,
        write_footer,
    )

    build_keywords("html")

    build_keywords("md")
