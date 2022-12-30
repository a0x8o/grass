"""Test t.rast.list output formats"""

import csv
import datetime
import io
import json

import pytest

<<<<<<< HEAD
<<<<<<< HEAD
import grass.script as gs

yaml = pytest.importorskip("yaml", reason="PyYAML package not available")


@pytest.mark.needs_solo_run
def test_defaults(space_time_raster_dataset):
    """Check that the module runs with default parameters"""
    gs.run_command(
        "t.rast.list",
        input=space_time_raster_dataset.name,
        env=space_time_raster_dataset.session.env,
    )


@pytest.mark.needs_solo_run
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
try:
    import yaml
except ImportError:
    yaml = None

import grass.script as gs


def test_defaults(space_time_raster_dataset):
    """Check that the module runs with default parameters"""
    gs.run_command("t.rast.list", input=space_time_raster_dataset.name)


<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
def test_line(space_time_raster_dataset):
    """Line format can be parsed and contains full names by default"""
    names = (
        gs.read_command(
<<<<<<< HEAD
<<<<<<< HEAD
            "t.rast.list",
            input=space_time_raster_dataset.name,
            format="line",
            env=space_time_raster_dataset.session.env,
=======
            "t.rast.list", input=space_time_raster_dataset.name, format="line"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            "t.rast.list", input=space_time_raster_dataset.name, format="line"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        )
        .strip()
        .split(",")
    )
    assert names == space_time_raster_dataset.full_raster_names


<<<<<<< HEAD
<<<<<<< HEAD
@pytest.mark.needs_solo_run
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
def test_json(space_time_raster_dataset):
    """Check JSON can be parsed and contains the right values"""
    result = json.loads(
        gs.read_command(
<<<<<<< HEAD
<<<<<<< HEAD
            "t.rast.list",
            input=space_time_raster_dataset.name,
            format="json",
            env=space_time_raster_dataset.session.env,
=======
            "t.rast.list", input=space_time_raster_dataset.name, format="json"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            "t.rast.list", input=space_time_raster_dataset.name, format="json"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        )
    )
    assert "data" in result
    assert "metadata" in result
    for item in result["data"]:
        for name in result["metadata"]["column_names"]:
            assert item[name], "All values should be set with the default columns"
    names = [item["name"] for item in result["data"]]
    assert names == space_time_raster_dataset.raster_names


<<<<<<< HEAD
<<<<<<< HEAD
@pytest.mark.needs_solo_run
=======
@pytest.mark.skipif(yaml is None, reason="PyYAML package not available")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
@pytest.mark.skipif(yaml is None, reason="PyYAML package not available")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
def test_yaml(space_time_raster_dataset):
    """Check JSON can be parsed and contains the right values"""
    result = yaml.safe_load(
        gs.read_command(
<<<<<<< HEAD
<<<<<<< HEAD
            "t.rast.list",
            input=space_time_raster_dataset.name,
            format="yaml",
            env=space_time_raster_dataset.session.env,
=======
            "t.rast.list", input=space_time_raster_dataset.name, format="yaml"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            "t.rast.list", input=space_time_raster_dataset.name, format="yaml"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        )
    )
    assert "data" in result
    assert "metadata" in result
    for item in result["data"]:
        for name in result["metadata"]["column_names"]:
            assert item[name], "All values should be set with the default columns"
        assert isinstance(item["start_time"], datetime.datetime)
    names = [item["name"] for item in result["data"]]
    assert names == space_time_raster_dataset.raster_names
    times = [item["start_time"] for item in result["data"]]
    assert times == space_time_raster_dataset.start_times


<<<<<<< HEAD
<<<<<<< HEAD
@pytest.mark.needs_solo_run
@pytest.mark.parametrize(
    ("separator", "delimiter"), [(None, ","), (",", ","), (";", ";"), ("tab", "\t")]
=======
@pytest.mark.parametrize(
    "separator,delimiter", [(None, ","), (",", ","), (";", ";"), ("tab", "\t")]
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
@pytest.mark.parametrize(
    "separator,delimiter", [(None, ","), (",", ","), (";", ";"), ("tab", "\t")]
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
)
def test_csv(space_time_raster_dataset, separator, delimiter):
    """Check CSV can be parsed with different separators"""
    columns = ["name", "start_time"]
    text = gs.read_command(
        "t.rast.list",
        input=space_time_raster_dataset.name,
        columns=columns,
        format="csv",
        separator=separator,
<<<<<<< HEAD
<<<<<<< HEAD
        env=space_time_raster_dataset.session.env,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    )
    io_string = io.StringIO(text)
    reader = csv.DictReader(
        io_string,
        delimiter=delimiter,
        quotechar='"',
        doublequote=True,
        lineterminator="\n",
        strict=True,
    )
    data = list(reader)
    assert len(data) == len(space_time_raster_dataset.raster_names)
    for row in data:
        assert len(row) == len(columns)


<<<<<<< HEAD
<<<<<<< HEAD
@pytest.mark.needs_solo_run
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
def test_columns_list(space_time_raster_dataset):
    """Check CSV can be parsed with different separators"""
    # All relevant columns from the interface.
    columns = [
        "id",
        "name",
        "semantic_label",
        "creator",
        "mapset",
        "temporal_type",
        "creation_time",
        "start_time",
        "end_time",
        "north",
        "south",
        "west",
        "east",
        "nsres",
        "ewres",
        "cols",
        "rows",
        "number_of_cells",
        "min",
        "max",
    ]
    result = json.loads(
        gs.read_command(
            "t.rast.list",
            input=space_time_raster_dataset.name,
            method="list",
            columns=columns,
            format="json",
<<<<<<< HEAD
<<<<<<< HEAD
            env=space_time_raster_dataset.session.env,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        )
    )
    data = result["data"]
    assert len(data) == len(space_time_raster_dataset.raster_names)
    for row in data:
        assert len(row) == len(columns)


<<<<<<< HEAD
<<<<<<< HEAD
@pytest.mark.needs_solo_run
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
def test_columns_delta_gran(space_time_raster_dataset):
    """Check CSV can be parsed with different separators"""
    # All relevant columns from the interface.
    columns = [
        "id",
        "name",
        "mapset",
        "start_time",
        "end_time",
        "interval_length",
        "distance_from_begin",
    ]
    result = json.loads(
        gs.read_command(
            "t.rast.list",
            input=space_time_raster_dataset.name,
            method="gran",
            columns=columns,
            format="json",
<<<<<<< HEAD
<<<<<<< HEAD
            env=space_time_raster_dataset.session.env,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        )
    )
    data = result["data"]
    assert len(data) == len(space_time_raster_dataset.raster_names)
    for row in data:
        assert len(row) == len(columns)


<<<<<<< HEAD
<<<<<<< HEAD
@pytest.mark.needs_solo_run
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
def test_json_empty_result(space_time_raster_dataset):
    """Check JSON is generated for no returned values"""
    result = json.loads(
        gs.read_command(
            "t.rast.list",
            input=space_time_raster_dataset.name,
            format="json",
            where="FALSE",
<<<<<<< HEAD
<<<<<<< HEAD
            env=space_time_raster_dataset.session.env,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        )
    )
    assert "data" in result
    assert "metadata" in result
    assert len(result["data"]) == 0


<<<<<<< HEAD
<<<<<<< HEAD
@pytest.mark.needs_solo_run
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
@pytest.mark.parametrize("output_format", ["plain", "line"])
def test_plain_empty_result(space_time_raster_dataset, output_format):
    """Check module fails with non-zero return code for empty result"""
    return_code = gs.run_command(
        "t.rast.list",
        input=space_time_raster_dataset.name,
        format=output_format,
        where="FALSE",
        errors="status",
<<<<<<< HEAD
<<<<<<< HEAD
        env=space_time_raster_dataset.session.env,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    )
    assert return_code != 0


<<<<<<< HEAD
<<<<<<< HEAD
@pytest.mark.needs_solo_run
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
@pytest.mark.parametrize("output_format", ["csv", "plain"])
def test_no_header_accepted(space_time_raster_dataset, output_format):
    """Check that the no column names flag is accepted"""
    gs.run_command(
<<<<<<< HEAD
<<<<<<< HEAD
        "t.rast.list",
        input=space_time_raster_dataset.name,
        format=output_format,
        env=space_time_raster_dataset.session.env,
    )


@pytest.mark.needs_solo_run
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        "t.rast.list", input=space_time_raster_dataset.name, format=output_format
    )


<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
@pytest.mark.parametrize("output_format", ["json", "yaml"])
def test_no_header_rejected(space_time_raster_dataset, output_format):
    """Check that the no column names flag is rejected

    Given how the format dependencies are handled, this will run even
    when YAML support is missing.
    """
    return_code = gs.run_command(
        "t.rast.list",
        input=space_time_raster_dataset.name,
        format=output_format,
        flags="u",
        errors="status",
<<<<<<< HEAD
<<<<<<< HEAD
        env=space_time_raster_dataset.session.env,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    )
    assert return_code != 0


<<<<<<< HEAD
<<<<<<< HEAD
@pytest.mark.needs_solo_run
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
@pytest.mark.parametrize("method", ["delta", "deltagaps", "gran"])
def test_other_methods_json(space_time_raster_dataset, method):
    """Test methods other than list"""
    result = json.loads(
        gs.read_command(
            "t.rast.list",
            input=space_time_raster_dataset.name,
            format="json",
            method=method,
<<<<<<< HEAD
<<<<<<< HEAD
            env=space_time_raster_dataset.session.env,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        )
    )
    assert "data" in result
    assert "metadata" in result
    for item in result["data"]:
        assert item["interval_length"] >= 0
        assert item["distance_from_begin"] >= 0
    names = [item["name"] for item in result["data"]]
    assert names == space_time_raster_dataset.raster_names


<<<<<<< HEAD
<<<<<<< HEAD
@pytest.mark.needs_solo_run
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
def test_gran_json(space_time_raster_dataset):
    """Test granularity method"""
    result = json.loads(
        gs.read_command(
            "t.rast.list",
            input=space_time_raster_dataset.name,
            format="json",
            method="gran",
            gran="15 days",
<<<<<<< HEAD
<<<<<<< HEAD
            env=space_time_raster_dataset.session.env,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        )
    )
    assert "data" in result
    assert "metadata" in result
    for item in result["data"]:
        assert item["interval_length"] >= 0
        assert item["distance_from_begin"] >= 0
        assert (
            item["name"] in space_time_raster_dataset.raster_names
            or item["name"] is None
        )
    assert len(result["data"]) > len(
        space_time_raster_dataset.raster_names
    ), "There should be more entries because of finer granularity"
