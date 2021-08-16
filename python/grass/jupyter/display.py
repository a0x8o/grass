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
from pathlib import Path
=======
import shutil
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
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
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
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
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
=======
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from pathlib import Path
=======
import shutil
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
from IPython.display import Image
<<<<<<< HEAD
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
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
>>>>>>> 8081de8037 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
from pathlib import Path
from IPython.display import Image
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
import tempfile
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 0f6214829f (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
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
<<<<<<< HEAD
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
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

    def __init__(
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
        self,
        height=400,
        width=600,
        filename=None,
        env=None,
        text_size=12,
        renderer="cairo",
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
    """The grassRenderer class creates and displays GRASS maps in
    Jupyter Notebooks."""

    def __init__(
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
>>>>>>> 0f6214829f (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
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
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 8081de8037 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ea09951b82 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 51c2c65241 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> db3907dcb5 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 222c716b0d (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 56dc956a16 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> ff6453d3a3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
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
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 7310acc566 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 523219d6d4 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 7310acc566 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> b983b20647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> a7de541b7b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6ccfc6c568 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 6256f6ce93 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a17f4a3d78 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
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
>>>>>>> ff6453d3a3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> d7075af684 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 397f650647 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 51c2c65241 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> ae5deb8874 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 7ed89dabad (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 6a71499d8b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 8984405ebb (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f91c52c645 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 7475d19efc (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> ff17a4ac2b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 6abb78d81f (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 577d32036e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> be3c74c20a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> eae04b13cd (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 4f7b5aea0b (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 3627af9569 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 1dc35c6f9a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 523ee84db7 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 6d0d0f1535 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f1ae4cefc3 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 4bce14c842 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> c326142eac (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> f4219c860c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> bceba4c6e2 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
>>>>>>> 2126e07d57 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 46ba5034eb (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> ab99037454 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 2efe487a0f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> c95214f898 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 7ad845718b (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> eb42b06b22 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 980c935a7d (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a73283d12a (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> d5647b4648 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> f0a06841f5 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 094016f111 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> cb74f10c60 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 8ea2c80b24 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 13ad0bbd2d (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 97c1ae10bf (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 8e12996ca3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 302e41dba7 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> b615a40687 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> a883fdb8f6 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
<<<<<<< HEAD
>>>>>>> 8081de8037 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
=======
=======
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 9cf5faa5d3 (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
>>>>>>> 0f6214829f (r.in.pdal: info.cpp also needs PDALCPPFLAGS (#1768))
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
<<<<<<< HEAD
=======
>>>>>>> c21dcd3d37 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 9a51bf3124 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
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
>>>>>>> f3a0d5f10c (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> osgeo-main
=======
    def show(self):
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
>>>>>>> 74c5391ad5 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
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
>>>>>>> ac28540237 (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
>>>>>>> osgeo-main
=======
    def show(self):
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
>>>>>>> fe5de958ac (libraster: fix Rast_legal_bandref() (#1796))
=======
=======
    def show(self):
        """Displays a PNG image of the map (non-interactive)"""
>>>>>>> 742603b912 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4480ca2a94 (libpython: Save and load benchmark results (#1711))
        return Image(self._filename)
