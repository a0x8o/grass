"""Test session functions in grass.jupyter"""

import subprocess
import os
import sys


# All init tests change the global environment, but we use a separate process
# only when it is necessary.
# Ideally, the functions would support env parameter and the tests
# would mostly use that.
def run_in_subprocess(file):
    """Run function in a separate process
    The function must take a Queue and put its result there.
    The result is then returned from this function.
    """
    process = subprocess.run(
        [sys.executable, os.fspath(file)], stdout=subprocess.PIPE, text=True, check=True
    )
    return process.stdout


def test_init_finish(tmp_path):
    """Check that init function works with an explicit session finish"""
    location = "test"
    script = f"""
import os
import grass.script as gs
import grass.jupyter as gj
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
gs.core._create_location_xy(r"{tmp_path}", r"{location}")
session = gj.init(r"{tmp_path / location}")
=======
gs.core._create_location_xy("{tmp_path}", "{location}")
session = gj.init("{tmp_path / location}")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
gs.core._create_location_xy("{tmp_path}", "{location}")
session = gj.init("{tmp_path / location}")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
gs.read_command("g.region", flags="p")
print(os.environ["GISRC"])
session.finish()
"""
    file = tmp_path / "script.py"
    file.write_text(script)
    session_file = run_in_subprocess(file)
    assert session_file, "Expected something from the subprocess"
    session_file = session_file.strip()
    assert "\n" not in session_file, "Expected a file name from the subprocess"
    assert not os.path.exists(session_file), f"Session file {session_file} not deleted"


def test_init_with_auto_finish(tmp_path):
    """Check that init function works with an implicit session finish"""
    location = "test"
    script = f"""
import os
import grass.script as gs
import grass.jupyter as gj
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
gs.core._create_location_xy(r"{tmp_path}", r"{location}")
session = gj.init(r"{tmp_path / location}")
=======
gs.core._create_location_xy("{tmp_path}", "{location}")
session = gj.init("{tmp_path / location}")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
gs.core._create_location_xy("{tmp_path}", "{location}")
session = gj.init("{tmp_path / location}")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
print(os.environ["GISRC"])
"""

    file = tmp_path / "script.py"
    file.write_text(script)
    session_file = run_in_subprocess(file)
    assert session_file, "Expected something from the subprocess"
    session_file = session_file.strip()
    assert "\n" not in session_file, "Expected a file name from the subprocess"
    assert not os.path.exists(session_file), f"Session file {session_file} not deleted"
