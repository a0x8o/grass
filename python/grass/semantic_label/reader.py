import os
import sys
import json
import glob
import re
from collections import OrderedDict

import grass.script as gs

# Semantic label can have any form. Explanatory metadata can be stored
# separately. It is suggested to follow some standard e.g. remote
# sensing band names should be STAC common names, see
# https://stacspec.org/
# https://github.com/radiantearth/stac-spec/blob/master/extensions/eo/README.md#band-object


class SemanticLabelReaderError(Exception):
    pass


class SemanticLabelReader:
    """Semantic label reader"""

    def __init__(self):
        self._json_files = glob.glob(
            os.path.join(os.environ["GISBASE"], "etc", "i.band.library", "*.json")
        )
        if not self._json_files:
            raise SemanticLabelReaderError("No semantic label definitions found")

        self._read_config()

    def _read_config(self):
        """Read configuration"""
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb7ff0932b (style: Fixes unnecessary-collection-call (C408) for empty collections (#3945))
        self.config = {}
=======
        self.config = dict()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
        self.config = dict()
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        self.config = {}
>>>>>>> 962f525ded (style: Fixes unnecessary-collection-call (C408) for empty collections (#3945))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
        self.config = dict()
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb7ff0932b (style: Fixes unnecessary-collection-call (C408) for empty collections (#3945))
        for json_file in self._json_files:
            try:
                with open(json_file) as fd:
                    config = json.load(fd, object_pairs_hook=OrderedDict)
            except json.decoder.JSONDecodeError as e:
                raise SemanticLabelReaderError(
                    "Unable to parse '{}': {}".format(json_file, e)
                )

            # check if configuration is valid
            self._check_config(config)

            self.config[os.path.basename(json_file)] = config

    @staticmethod
    def _check_config(config):
        """Check if config is valid

        :todo: check shortcut uniqueness

        :param dict config: configuration to be validated
        """
        for items in config.values():
            for item in ("shortcut", "bands"):
                if item not in items.keys():
                    raise SemanticLabelReaderError(
                        "Invalid band definition: <{}> is missing".format(item)
                    )
            if len(items["bands"]) < 1:
                raise SemanticLabelReaderError(
                    "Invalid band definition: no bands defined"
                )

    @staticmethod
    def _print_label_extended(label, item):
        """Print label specific metadata

        :param str label: label identifier
        :param str item: items to be printed out
        """

        def print_kv(k, v, indent):
            if isinstance(v, OrderedDict):
                print("{}{}:".format(" " * indent * 2, k))
                for ki, vi in v.items():
                    print_kv(ki, vi, indent * 2)
            else:
                print("{}{}: {}".format(" " * indent * 2, k, v))

        indent = 4
        print("{}label: {}".format(" " * indent, label))
        for k, v in item[label].items():
            print_kv(k, v, indent)

    def _print_label(self, semantic_label=None, tag=None):
        sys.stdout.write(semantic_label)
        if tag:
            sys.stdout.write(" {}".format(tag))
        sys.stdout.write(os.linesep)

    def print_info(self, shortcut=None, band=None, semantic_label=None, extended=False):
        """Prints semantic label information to stdout.

        Can be filtered by semantic label identifier.

        :param str shortcut: shortcut to filter (eg. S2) or None
        :param str band: band (eg. 1) or None
        :param str semantic_label: semantic_label filter (eg. S2_8A) or None
        :param bool extended: print also extended metadata
        """
        if semantic_label:
            try:
                shortcut, band = semantic_label.split("_")
            except ValueError:
                shortcut = semantic_label
                band = None
        found = False
        for root in self.config.values():
            for item in root.values():
                try:
                    if shortcut and re.match(shortcut, item["shortcut"]) is None:
                        continue
                except re.error as e:
                    raise SemanticLabelReaderError("Invalid pattern: {}".format(e))

                found = True
                if band and band not in item["bands"]:
                    raise SemanticLabelReaderError(
                        "Band <{}> not found in <{}>".format(band, shortcut)
                    )

                # print generic information
                if extended:
                    for subitem in item.keys():
                        if subitem == "bands":
                            # bands item is processed bellow
                            continue
                        print("{}: {}".format(subitem, item[subitem]))

                    # print detailed band information
                    if band:
                        self._print_label_extended(band, item["bands"])
                    else:
                        for iband in item["bands"]:
                            self._print_label_extended(iband, item["bands"])
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
                else:  # noqa: PLR5501
=======
                else:
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
                else:
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
                else:
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
                    # basic information only
                    if band:
                        self._print_label(
                            semantic_label=item["shortcut"],
                            tag=item["bands"][band].get("tag"),
                        )
                    else:
                        for iband in item["bands"]:
                            self._print_label(
                                semantic_label=item["shortcut"],
                                tag=item["bands"][iband].get("tag"),
                            )

        # print warning when defined shortcut not found
        if not found:
            gs.warning(
                "Metadata for semantic label <{}> not found".format(semantic_label)
            )

    def find_file(self, semantic_label):
        """Find file by semantic label.

        Match is case-insensitive.

        :param str semantic_label: semantic label identifier to search for (eg. S2_1)

        :return str: file basename if found or None
        """
        try:
            shortcut, band = semantic_label.split("_")
        except ValueError:
            # raise SemanticLabelReaderError("Invalid band identifier <{}>".format(
            #    semantic_label
            # ))
            shortcut = None

        for filename, config in self.config.items():
            for root in config.keys():
                if (
                    shortcut
                    and config[root]["shortcut"].upper() == shortcut.upper()
                    and band.upper()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
                    in (x.upper() for x in config[root]["bands"].keys())
=======
                    in map(lambda x: x.upper(), config[root]["bands"].keys())
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
                    in map(lambda x: x.upper(), config[root]["bands"].keys())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
                    in map(lambda x: x.upper(), config[root]["bands"].keys())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
                ):
                    return filename

        return None

    def get_bands(self):
        """Get list of band identifiers.

        :return list: list of valid band identifiers
        """
        bands = []
        for root in self.config.values():
            for item in root.values():
                for band in item["bands"]:
                    bands.append("{}_{}".format(item["shortcut"], band))
        return bands
