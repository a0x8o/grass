# MODULE:    grass.jupyter.display
#
# AUTHOR(S): Caitlin Haedrich <caitlin DOT haedrich AT gmail>
#
# PURPOSE:   This module contains functions for non-interactive display
#            in Jupyter Notebooks
#
# COPYRIGHT: (C) 2021 Caitlin Haedrich, and by the GRASS Development Team
#
#           This program is free software under the GNU General Public
#           License (>=v2). Read the file COPYING that comes with GRASS
#           for details.

import os
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
import shutil
=======
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
=======
import shutil
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
<<<<<<< HEAD
import shutil
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
<<<<<<< HEAD
import shutil
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
import shutil
=======
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
=======
import shutil
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
<<<<<<< HEAD
import shutil
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
<<<<<<< HEAD
import shutil
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
import shutil
=======
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
=======
import shutil
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
<<<<<<< HEAD
import shutil
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
<<<<<<< HEAD
import shutil
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
import shutil
=======
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
=======
import shutil
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
<<<<<<< HEAD
import shutil
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
<<<<<<< HEAD
import shutil
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
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
import shutil
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
>>>>>>> osgeo-main
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b88da686d1 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a7de541b7b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6256f6ce93 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c3b9f9f4e9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fcb86551a0 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f70ee0fc63 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 92eec250e9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
import tempfile
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 91e809e6a4 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
<<<<<<< HEAD
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
>>>>>>> main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 07c04c0cb0 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
=======
=======
import shutil
>>>>>>> 686e3354a5 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
<<<<<<< HEAD
>>>>>>> b88da686d1 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
=======
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a7de541b7b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
from IPython.display import Image
=======
>>>>>>> 29f5805aab (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 7310acc566 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> ab87aab656 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> a7de541b7b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> d039fa87a3 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 6256f6ce93 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> 92d8fccb2c (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
<<<<<<< HEAD
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 226b9e4eb9 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> c3b9f9f4e9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ff6453d3a3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 44e0a36ee9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> fb5abcdf0c (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 397f650647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4cf4cf1886 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
<<<<<<< HEAD
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 6a8cff7429 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
<<<<<<< HEAD
>>>>>>> 44e0a36ee9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 3598b08521 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 222c716b0d (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51c2c65241 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> d961091ec4 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 6a71499d8b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 03ae449941 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> ff17a4ac2b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 842bc8bfeb (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> eae04b13cd (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 4aa2f06bc9 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 523ee84db7 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 8293003471 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> c326142eac (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 3aba158581 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 46ba5034eb (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 3fbae0cad4 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 7ad845718b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 9d2cb9263f (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> d5647b4648 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> b09d5a689a (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 8ea2c80b24 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
>>>>>>> cce0034b83 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
<<<<<<< HEAD
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 67ba91ffa3 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> b4c4edd395 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
<<<<<<< HEAD
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 302e41dba7 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 07c04c0cb0 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8081de8037 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> ba259679a9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
>>>>>>> ba259679a9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
>>>>>>> ed2459abf0 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
<<<<<<< HEAD
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> f862c48c9b (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 6e99641a20 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 0f6214829f (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
from pathlib import Path
from IPython.display import Image
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
import tempfile
>>>>>>> ba259679a9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 57eb0fc74c (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
from pathlib import Path
from IPython.display import Image
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
=======
=======
import shutil
>>>>>>> 686e3354a5 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
=======
from IPython.display import Image
=======
>>>>>>> 29f5805aab (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 4669177a24 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> ab87aab656 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> fcb86551a0 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> d039fa87a3 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> f70ee0fc63 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
from pathlib import Path
from IPython.display import Image
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
=======
import tempfile
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 92eec250e9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 1ccb4d037b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 44e0a36ee9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> fb5abcdf0c (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 92d8fccb2c (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
from pathlib import Path
from IPython.display import Image
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
=======
import tempfile
<<<<<<< HEAD
>>>>>>> 44e0a36ee9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> fd36f2255e (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> e85f15e95c (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> c148a03408 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> d961091ec4 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 4cf4cf1886 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 03ae449941 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 06650bd8ff (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 842bc8bfeb (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> a094b1adaf (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 4aa2f06bc9 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 93d436eafe (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 8293003471 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> e54c387168 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 3aba158581 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> df9f44f8e2 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 3fbae0cad4 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 3cac4bf9e0 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 9d2cb9263f (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 9f55b90413 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> b09d5a689a (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 2938aba0bf (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
from pathlib import Path
from IPython.display import Image
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
=======
import tempfile
<<<<<<< HEAD
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 9fff8a6023 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
import tempfile
>>>>>>> osgeo-main
=======
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 07c04c0cb0 (libraster: fix Rast_legal_bandref() (#1796))
import tempfile
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a649be6646 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
from pathlib import Path
from IPython.display import Image
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
=======
import tempfile
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> cce0034b83 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
from pathlib import Path
from IPython.display import Image
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
>>>>>>> 5faab49e7e (libpython: Save and load benchmark results (#1711))
=======
=======
import tempfile
>>>>>>> ba259679a9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> ed2459abf0 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
import grass.script as gs


class GrassRenderer:
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
<<<<<<< HEAD
>>>>>>> main
=======
>>>>>>> b88da686d1 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5faab49e7e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 91e809e6a4 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
    """GrassRenderer creates and displays GRASS maps in
    Jupyter Notebooks.

    Elements are added to the display by calling GRASS display modules.

    Basic usage::
    >>> m = GrassRenderer()
    >>> m.run("d.rast", map="elevation")
    >>> m.run("d.legend", raster="elevation")
    >>> m.show()

    GRASS display modules can also be called by using the name of module
    as a class method and replacing "." with "_" in the name.

    Shortcut usage::
    >>> m = GrassRenderer()
    >>> m.d_rast(map="elevation")
    >>> m.d_legend(raster="elevation")
    >>> m.show()
    """
<<<<<<< HEAD
<<<<<<< HEAD
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""
>>>>>>> osgeo-main
=======
>>>>>>> b88da686d1 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
>>>>>>> 91e809e6a4 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))

    def __init__(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 4669177a24 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self,
        height=400,
        width=600,
        filename=None,
        env=None,
        text_size=12,
        renderer="cairo",
<<<<<<< HEAD
<<<<<<< HEAD
    ):
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
        """Initiates an instance of the GrassRenderer class."""
=======
>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======
>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======
>>>>>>> osgeo-main

        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> osgeo-main
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> osgeo-main
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> osgeo-main

        # Copy Environment
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""

    def __init__(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self,
        height=400,
        width=600,
        filename=None,
        env=None,
        text_size=12,
        renderer="cairo",
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4669177a24 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
=======
        """Initiates an instance of the GrassRenderer class."""
=======

>>>>>>> osgeo-main
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
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
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
<<<<<<< HEAD
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
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
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):

        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """

<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
        # Copy Environment
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 7310acc566 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""

    def __init__(
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
<<<<<<< HEAD
=======
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 44e0a36ee9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> ba259679a9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self,
        height=400,
        width=600,
        filename=None,
        env=None,
        text_size=12,
        renderer="cairo",
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
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> a7de541b7b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 6256f6ce93 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> c3b9f9f4e9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> ff6453d3a3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 397f650647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
<<<<<<< HEAD
>>>>>>> 44e0a36ee9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 44e0a36ee9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 3598b08521 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> osgeo-main
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 222c716b0d (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 51c2c65241 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 6a71499d8b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> ff17a4ac2b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> eae04b13cd (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
<<<<<<< HEAD
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 523ee84db7 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> c326142eac (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 46ba5034eb (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 7ad845718b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> d5647b4648 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 8ea2c80b24 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 302e41dba7 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> osgeo-main
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 8081de8037 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 0f6214829f (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> ba259679a9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> ba259679a9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 57eb0fc74c (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
    ):
        """Initiates an instance of the GrassRenderer class."""

>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):

        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """

<<<<<<< HEAD
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
        # Copy Environment
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 4669177a24 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""

    def __init__(
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
<<<<<<< HEAD
=======
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 44e0a36ee9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> ba259679a9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self,
        height=400,
        width=600,
        filename=None,
        env=None,
        text_size=12,
        renderer="cairo",
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
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> fcb86551a0 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> f70ee0fc63 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 92eec250e9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 1ccb4d037b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 92d8fccb2c (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
<<<<<<< HEAD
>>>>>>> 44e0a36ee9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 44e0a36ee9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> fd36f2255e (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> osgeo-main
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> e85f15e95c (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> c148a03408 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 4cf4cf1886 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 06650bd8ff (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> a094b1adaf (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
<<<<<<< HEAD
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 93d436eafe (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> e54c387168 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> df9f44f8e2 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 3cac4bf9e0 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 9f55b90413 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 2938aba0bf (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 9fff8a6023 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> osgeo-main
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> a649be6646 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> cce0034b83 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
        self, env=None, width=600, height=400, filename="map.png", text_size=12
=======
>>>>>>> ba259679a9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    ):
<<<<<<< HEAD
        """Initiates an instance of the GrassRenderer class."""
=======

<<<<<<< HEAD
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 5faab49e7e (libpython: Save and load benchmark results (#1711))
=======
=======
        """Creates an instance of the GrassRenderer class.

        :param int height: height of map in pixels
        :param int width: width of map in pixels
        :param str filename: filename or path to save a PNG of map
        :param str env: environment
        :param int text_size: default text size, overwritten by most display modules
        :param renderer: GRASS renderer driver (options: cairo, png, ps, html)
        """
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))

        # Copy Environment
>>>>>>> ba259679a9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> ed2459abf0 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        if env:
            self._env = env.copy()
        else:
            self._env = os.environ.copy()
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7310acc566 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a7de541b7b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6256f6ce93 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c3b9f9f4e9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 397f650647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3598b08521 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
=======
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6a71499d8b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ff17a4ac2b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> eae04b13cd (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 523ee84db7 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c326142eac (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 46ba5034eb (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7ad845718b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d5647b4648 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8ea2c80b24 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 302e41dba7 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0f6214829f (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 57eb0fc74c (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> cce0034b83 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 5faab49e7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ed2459abf0 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 8081de8037 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a649be6646 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4cf4cf1886 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 06650bd8ff (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a094b1adaf (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 93d436eafe (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> e54c387168 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> df9f44f8e2 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3cac4bf9e0 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 9f55b90413 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2938aba0bf (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 9fff8a6023 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 51c2c65241 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> c148a03408 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 222c716b0d (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> e85f15e95c (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 92d8fccb2c (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fd36f2255e (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> ff6453d3a3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4669177a24 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fcb86551a0 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f70ee0fc63 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 92eec250e9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 1ccb4d037b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        # Environment Settings
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
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
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

=======

=======
        # Environment Settings
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"
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
>>>>>>> 6c2ecbcdd0 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 1a0e9d8383 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 6a3d5d8229 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 844932ae5d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> f6d796fd40 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> c59f93bc6e (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 52352c0e7e (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> fa18e11eae (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 41d412ce2a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> d7a05702af (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 98f7fb42ae (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 45bfaad52a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 868ff9591d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> c1037a4f82 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 7a7db5d2e7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 7a5d2a81ff (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

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

=======
        # Environment Settings
<<<<<<< HEAD
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======

=======
        # Environment Settings
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======

=======
        # Environment Settings
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
=======
>>>>>>> 1ccb4d037b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 7310acc566 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======

=======
        # Environment Settings
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
=======

=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"
<<<<<<< HEAD

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> ff6453d3a3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======

=======
        # Environment Settings
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 44e0a36ee9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
=======

=======
        # Environment Settings
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======

=======
        # Environment Settings
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a649be6646 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
        # Environment Settings
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> d4beced40f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 6b58199776 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 057ade7c94 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 602a59f3d1 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 9322f81244 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 1de6bbf813 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 71e71e7e89 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 6547fb8a44 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> c462857ee4 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        # Environment Settings
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 094ff59126 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> ba259679a9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> c8b938ae61 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======

=======
        # Environment Settings
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4669177a24 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======

=======
        # Environment Settings
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
=======
=======

=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 1ccb4d037b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======

=======
        # Environment Settings
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 44e0a36ee9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
=======
=======

=======
        # Environment Settings
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
=======
=======

=======
        # Environment Settings
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> d4beced40f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 6b58199776 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 057ade7c94 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 602a59f3d1 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 9322f81244 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 1de6bbf813 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 71e71e7e89 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 6547fb8a44 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> c462857ee4 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        # Environment Settings
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
        self._env["GRASS_RENDER_TRANSPARENT"] = "TRUE"

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> 094ff59126 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
=======

=======
        # Environment Settings
>>>>>>> ba259679a9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_WIDTH"] = str(width)
        self._env["GRASS_RENDER_HEIGHT"] = str(height)
<<<<<<< HEAD
        self._env["GRASS_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = "cairo"
        self._env["GRASS_RENDER_FILE"] = str(filename)
=======
        self._env["GRASS_RENDER_TEXT_SIZE"] = str(text_size)
        self._env["GRASS_RENDER_IMMEDIATE"] = renderer
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self._env["GRASS_RENDER_FILE_READ"] = "TRUE"
=======
>>>>>>> c8b938ae61 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))

        # Create PNG file for map
        # If not user-supplied, we will write it to a map.png in a
        # temporary directory that we can delete later. We need
        # this temporary directory for the legend anyways so we'll
        # make it now
        self._tmpdir = tempfile.TemporaryDirectory()

        if filename:
            self._filename = filename
        else:
            self._filename = os.path.join(self._tmpdir.name, "map.png")
        # Set environment var for file
        self._env["GRASS_RENDER_FILE"] = self._filename

        # Create Temporary Legend File
        self._legend_file = os.path.join(self._tmpdir.name, "legend.txt")
        self._env["GRASS_LEGEND_FILE"] = str(self._legend_file)

<<<<<<< HEAD
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
>>>>>>> 5faab49e7e (libpython: Save and load benchmark results (#1711))
        self._filename = filename

        self.run("d.erase")

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
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
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5faab49e7e (libpython: Save and load benchmark results (#1711))
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7310acc566 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a7de541b7b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6256f6ce93 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c3b9f9f4e9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ff6453d3a3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 397f650647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
>>>>>>> 44e0a36ee9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 3598b08521 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 222c716b0d (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51c2c65241 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a71499d8b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ff17a4ac2b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eae04b13cd (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 523ee84db7 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c326142eac (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 46ba5034eb (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7ad845718b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d5647b4648 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8ea2c80b24 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 302e41dba7 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> a649be6646 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8081de8037 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0f6214829f (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ba259679a9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 57eb0fc74c (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 4669177a24 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> fcb86551a0 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> f70ee0fc63 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 92eec250e9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 1ccb4d037b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 92d8fccb2c (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
>>>>>>> 44e0a36ee9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> fd36f2255e (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> ddb6db9b59 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> e85f15e95c (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> c148a03408 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 4cf4cf1886 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 06650bd8ff (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a094b1adaf (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 93d436eafe (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> e54c387168 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> df9f44f8e2 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 3cac4bf9e0 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 9f55b90413 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 2938aba0bf (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 9fff8a6023 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a649be6646 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> cce0034b83 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
>>>>>>> 5faab49e7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ba259679a9 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> ed2459abf0 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
    def run(self, module, **kwargs):
        """Run modules from "d." GRASS library"""
        # Check module is from display library then run
        if module[0] == "d":
            gs.run_command(module, env=self._env, **kwargs)
        else:
            raise ValueError("Module must begin with letter 'd'.")

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
<<<<<<< HEAD
>>>>>>> main
=======
>>>>>>> b88da686d1 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5faab49e7e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 91e809e6a4 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
    def __getattr__(self, name):
        """Parse attribute to GRASS display module. Attribute should be in
        the form 'd_module_name'. For example, 'd.rast' is called with 'd_rast'.
        """

        # Check to make sure format is correct
        if not name.startswith("d_"):
            raise AttributeError(_("Module must begin with 'd_'"))
        # Reformat string
        grass_module = name.replace("_", ".")
        # Assert module exists
        if not shutil.which(grass_module):
            raise AttributeError(_("Cannot find GRASS module {}").format(grass_module))

        def wrapper(**kwargs):
            # Run module
            self.run(grass_module, **kwargs)

        return wrapper

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 91e809e6a4 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
    def show(self):
        """Displays a PNG image of the map"""
        from IPython.display import Image

=======
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
>>>>>>> b88da686d1 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
    def show(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

<<<<<<< HEAD
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
=======
<<<<<<< HEAD
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
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
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 07c04c0cb0 (libraster: fix Rast_legal_bandref() (#1796))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
        """Displays a PNG image of the map (non-interactive)"""
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
        """Displays a PNG image of the map"""
>>>>>>> 686e3354a5 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
<<<<<<< HEAD
>>>>>>> b88da686d1 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 2f4b0e227d (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 29f5805aab (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4a4e8d0c8b (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> ab87aab656 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e764f6bfd (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> d039fa87a3 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f3a0d5f10c (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
    def show(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 4c2a8e0e3c (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebd8d6c4e0 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40f77bd087 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> fb5abcdf0c (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 91ac389e42 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> osgeo-main
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 6711551a1e (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 160d954222 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 3774f705e0 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b7b02b03b (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b6874bbce2 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> d961091ec4 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 56b7fca044 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 03ae449941 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6d9bf88380 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 842bc8bfeb (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 74c5391ad5 (libraster: fix Rast_legal_bandref() (#1796))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 4aa2f06bc9 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7bbc719494 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 8293003471 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7ac11e20d9 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 3aba158581 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cf5e5490a0 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 3fbae0cad4 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 37ee2a4a9a (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 9d2cb9263f (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dddf6714ad (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> b09d5a689a (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ac28540237 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
    def show(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 07c04c0cb0 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> d2d2e6504a (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe5de958ac (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> b4c4edd395 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ff1b448832 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 70b350b826 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 6e99641a20 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 5e8964d94a (libraster: fix Rast_legal_bandref() (#1796))
=======
    def show(self):
        """Displays a PNG image of the map (non-interactive)"""
>>>>>>> 173e44f2dc (libpython: Save and load benchmark results (#1711))
=======
=======
        """Displays a PNG image of the map (non-interactive)"""
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> fbe1fc358a (libpython: Save and load benchmark results (#1711))
=======
=======
        """Displays a PNG image of the map"""
>>>>>>> 686e3354a5 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
<<<<<<< HEAD
>>>>>>> 91e809e6a4 (jupyter: Add `__getattr__` shortcut for calling GRASS display modules (#1723))
=======
=======
>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> a80c8300ee (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 319ab246f0 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 29f5805aab (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 08e876fd03 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a112feb47 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> ab87aab656 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 8b7b13b370 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 7439490972 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> d039fa87a3 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> ff391007a5 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> e9fa08af5b (libraster: fix Rast_legal_bandref() (#1796))
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9cac1201a9 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 4c2a8e0e3c (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> e9fa08af5b (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6dbb418f88 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ab44c2131 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 226b9e4eb9 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 0d0bc8bfd9 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> fb5abcdf0c (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 61f09a8772 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> osgeo-main
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8a286c75d5 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 2ee8fe98e4 (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 6711551a1e (libraster: fix Rast_legal_bandref() (#1796))
<<<<<<< HEAD
>>>>>>> 932668ca58 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> dcc1810d30 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 3774f705e0 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 05aac187c6 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> a29c4a1571 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 877945a9e8 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 6a8cff7429 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 23a05fbab6 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> d961091ec4 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 9b9adf03ac (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 8051b01c88 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 03ae449941 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> d3bc1c59f9 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 969385adae (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 842bc8bfeb (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 4f68eb61a1 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d86c47b865 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 4aa2f06bc9 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 09c79f2b3e (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f226a36d82 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 8293003471 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 52da6d28d3 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 102ca719c3 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 3aba158581 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 39e2c8a7ff (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2e1fe7db7 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 3fbae0cad4 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> b0b193d204 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 39aa99710a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 9d2cb9263f (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> b131e1fa40 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6178b77bf1 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> b09d5a689a (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> df220f8b18 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> 9ace3ebc2a (libraster: fix Rast_legal_bandref() (#1796))
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1c3c7a612a (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 07c04c0cb0 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> d2d2e6504a (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 9ace3ebc2a (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 6c56216d2e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> b4c4edd395 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 67ba91ffa3 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
<<<<<<< HEAD
        """Displays a PNG image of the map (non-interactive)"""
<<<<<<< HEAD
>>>>>>> 4e0c4a2cca (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 5faab49e7e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        """Displays a PNG image of the map"""
        from IPython.display import Image

>>>>>>> 920471e340 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> 6e99641a20 (libraster: fix Rast_legal_bandref() (#1796))
>>>>>>> f862c48c9b (libraster: fix Rast_legal_bandref() (#1796))
        return Image(self._filename)
