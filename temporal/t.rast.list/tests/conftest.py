"""Fixture for t.rast.list test"""

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import os
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0c13ccda1f (style(temporal): Sort and group imports (#3959))
=======
import os
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
from datetime import datetime
from types import SimpleNamespace

import pytest

import grass.script as gs


@pytest.fixture(scope="module")
def space_time_raster_dataset(tmp_path_factory):
    """Start a session and create a raster time series

    Returns object with attributes about the dataset.
    """
    tmp_path = tmp_path_factory.mktemp("raster_time_series")
    location = "test"
    gs.core._create_location_xy(tmp_path, location)  # pylint: disable=protected-access
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
    with gs.setup.init(tmp_path / location, env=os.environ.copy()) as session:
        gs.run_command(
            "g.region",
            s=0,
            n=80,
            w=0,
            e=120,
            b=0,
            t=50,
            res=10,
            res3=10,
            env=session.env,
        )
        names = [f"precipitation_{i}" for i in range(1, 7)]
        max_values = [550, 450, 320, 510, 300, 650]
        for name, value in zip(names, max_values):
            gs.mapcalc(f"{name} = rand(0, {value})", seed=1, env=session.env)
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
    with gs.setup.init(tmp_path / location):
        gs.run_command("g.region", s=0, n=80, w=0, e=120, b=0, t=50, res=10, res3=10)
        names = [f"precipitation_{i}" for i in range(1, 7)]
        max_values = [550, 450, 320, 510, 300, 650]
        for name, value in zip(names, max_values):
            gs.mapcalc(f"{name} = rand(0, {value})", seed=1)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
        dataset_name = "precipitation"
        gs.run_command(
            "t.create",
            type="strds",
            temporaltype="absolute",
            output=dataset_name,
            title="Precipitation",
            description="Random series generated for tests",
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            env=session.env,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            env=session.env,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
        )
        dataset_file = tmp_path / "names.txt"
        dataset_file.write_text("\n".join(names))
        gs.run_command(
            "t.register",
            type="raster",
            flags="i",
            input=dataset_name,
            file=dataset_file,
            start="2001-01-01",
            increment="1 month",
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            env=session.env,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            env=session.env,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
        )
        times = [datetime(2001, i, 1) for i in range(1, len(names) + 1)]
        full_names = [f"{name}@PERMANENT" for name in names]
        yield SimpleNamespace(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            session=session,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            session=session,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
            name=dataset_name,
            raster_names=names,
            full_raster_names=full_names,
            start_times=times,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            env=session,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            env=session,
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
        )
