"""Test environment and GIS environment functions"""

import multiprocessing

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
import pytest

import grass.script as gs

xfail_mp_spawn = pytest.mark.xfail(
    multiprocessing.get_start_method() == "spawn",
    reason="Multiprocessing using 'spawn' start method requires pickable functions",
    raises=AttributeError,
    strict=True,
)

=======
import grass.script as gs

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
import grass.script as gs

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

def run_in_subprocess(function):
    """Run function in a separate process

    The function must take a Queue and put its result there.
    The result is then returned from this function.
    """
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=function, args=(queue,))
    process.start()
    result = queue.get()
    process.join()
    return result


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
@xfail_mp_spawn
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
@xfail_mp_spawn
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
def test_reading_respects_change_of_session(tmp_path):
    """Check new session file path is retrieved and the file is read"""

    # The switching must happen in one process to test that the reading functions
    # are not using the cached values. However, the test itself needs to be
    # process-separated otherwise other tests will be influenced by the loaded
    # libraries and initialized data structures.

    def switch_through_locations(queue):
        """Switches through a list of locations"""
        # Just to be sure we don't influence other tests.
        # pylint: disable=import-outside-toplevel
        import grass.pygrass.utils as pygrass_utils
        import grass.lib.gis as libgis

        names = []
        for location_name in ["test1", "test2", "abc"]:
            # pylint: disable=protected-access
            gs.core._create_location_xy(tmp_path, location_name)
            with gs.setup.init(tmp_path / location_name):
                libgis.G__read_gisrc_path()
                libgis.G__read_gisrc_env()
                names.append((pygrass_utils.getenv("LOCATION_NAME"), location_name))
        queue.put(names)

    names = run_in_subprocess(switch_through_locations)

    for getenv_name, expected_name in names:
        assert getenv_name == expected_name, f"All recorded names: {names}"
