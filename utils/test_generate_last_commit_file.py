#!/usr/bin/env python3

"""
Script for testing an core_modules_with_last_commit.json file contains
all core modules with their last commit. Used by GitHub "Additional Checks"
action workflow.

Python lib dependencies:

pytest
pytest-depends

Usage:

pytest utils/test_generate_last_commit_file.py

@author Tomas Zigo <tomas.zigo slovanet.sk>
"""

import os
import json
import subprocess

import pytest

from .generate_last_commit_file import COMMIT_DATE_FORMAT


@pytest.fixture
def json_file():
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    return "core_modules_with_last_commit.json"
=======
    file_name = "core_modules_with_last_commit.json"
    return file_name
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
    file_name = "core_modules_with_last_commit.json"
    return file_name
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))


@pytest.fixture
def read_json_file(json_file):
    with open(json_file) as f:
        return json.load(f)


def test_json_file_exists(json_file):
    assert os.path.exists(json_file) is True


@pytest.mark.depends(on=["test_json_file_exists"])
def test_json_file_is_not_empty(read_json_file):
    assert len(read_json_file) > 0


@pytest.mark.depends(on=["test_json_file_is_not_empty"])
@pytest.mark.parametrize(
    "core_module_path",
    [
        os.path.join("vector", "v.surf.rst"),
        os.path.join("raster", "r.info"),
    ],
)
def test_core_modules_in_json_file(read_json_file, core_module_path):
    core_module = os.path.basename(core_module_path)
    assert core_module in read_json_file


@pytest.mark.depends(
    on=[
        "test_json_file_is_not_empty",
        "test_core_modules_in_json_file",
    ]
)
@pytest.mark.parametrize(
    "core_module_path",
    [
        os.path.join("vector", "v.surf.rst"),
        os.path.join("raster", "r.info"),
    ],
)
def test_compare_json_file_data(read_json_file, core_module_path):
    # Get Git commit and commit date from local Git
    process_result = subprocess.run(
        [
            "git",
            "log",
            "-1",
            f"--format=%H,{COMMIT_DATE_FORMAT}",
            core_module_path,
        ],
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
>>>>>>> 8eb2fcbb41 (style: Fix replace-stdout-stderr (UP022) (#4000))
        capture_output=True,
=======
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
        capture_output=True,
>>>>>>> b90fc735fa (style: Fix replace-stdout-stderr (UP022) (#4000))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        capture_output=True,
>>>>>>> b90fc735fa (style: Fix replace-stdout-stderr (UP022) (#4000))
>>>>>>> 8eb2fcbb41 (style: Fix replace-stdout-stderr (UP022) (#4000))
        check=True,
    )  # --format=%H,COMMIT_DATE_FORMAT commit hash,author date
    commit, date = process_result.stdout.decode().strip().split(",")
    core_module = os.path.basename(core_module_path)
    # Compare commit and commit date
    assert read_json_file[core_module]["commit"] == commit
    assert read_json_file[core_module]["date"] == date
