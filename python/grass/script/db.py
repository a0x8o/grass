"""
Database related functions to be used in Python scripts.

Usage:

::

    from grass.script import db as grass

    grass.db_describe(table)
    ...

(C) 2008-2015 by the GRASS Development Team
This program is free software under the GNU General Public
License (>=v2). Read the file COPYING that comes with GRASS
for details.

.. sectionauthor:: Glynn Clements
.. sectionauthor:: Martin Landa <landa.martin gmail.com>
"""
<<<<<<< HEAD
=======
from __future__ import absolute_import
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8630c1908e (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 6fdaa03757 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> e54d3f3e40 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 692afe97f6 (pythonlib: Remove star imports (#1546))
=======
=======
=======
=======
=======
>>>>>>> 2e4a058ca6 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> fcbc6eaf1c (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 958298688f (pythonlib: Remove star imports (#1546))
=======
>>>>>>> db4f0c5e9e (pythonlib: Remove star imports (#1546))
=======
>>>>>>> edbe88c194 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7c9ebb33c7 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> fd6b673316 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> bf337dfc4c (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 9407a0d6c1 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> f8a1d36c40 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 38eafe025f (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 9cb1837c15 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> c5e22f8b98 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 16628047b7 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 813bf89b9d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7ee999faa1 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> a55384b51b (pythonlib: Remove star imports (#1546))
=======
>>>>>>> da2395c9c7 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2e22515ef0 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 43413f8004 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 993ab127c0 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> ff67671fa4 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 1f65836381 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 46ecaf1932 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 53f003b3c5 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 75b5e29c4a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 894fed55ec (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2e9a40703f (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 4d810f7f30 (pythonlib: Remove star imports (#1546))
>>>>>>> aaf70da5d9 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 4d810f7f30 (pythonlib: Remove star imports (#1546))
>>>>>>> ae14ae6860 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> bca36f399f (pythonlib: Remove star imports (#1546))
>>>>>>> 585ba722f9 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> aeac88cf3a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7d811718e6 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> d416b78612 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> ae24e8727d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> d869a3a87d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 0942f70280 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 250a82a9d5 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 631756bf9f (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 72c2e4860b (pythonlib: Remove star imports (#1546))
=======
>>>>>>> bdb772eadd (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 15ee9980f8 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 8844e5da9c (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 4759f473a2 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 9fe3ace091 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 24602374be (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 15e8b8ec25 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2c35594c85 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> dbedecb198 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> f0068152e1 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 1c0cb85d51 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> bca36f399f (pythonlib: Remove star imports (#1546))
>>>>>>> f6df93ab65 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 1df4f6c1a9 (pythonlib: Remove star imports (#1546))
>>>>>>> b62c64d69c (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 1df4f6c1a9 (pythonlib: Remove star imports (#1546))
>>>>>>> 64384cd976 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> bd15a01a37 (pythonlib: Remove star imports (#1546))
>>>>>>> 858dcd2c02 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> bd15a01a37 (pythonlib: Remove star imports (#1546))
>>>>>>> 32987ee457 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2ec038aafa (pythonlib: Remove star imports (#1546))
>>>>>>> 78a24c3407 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 2ec038aafa (pythonlib: Remove star imports (#1546))
>>>>>>> 0934ce9a0b (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 65eebf45c4 (pythonlib: Remove star imports (#1546))
>>>>>>> 705f9aa694 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 1653b03705 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 8a28804560 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7dc011e093 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 6a11812108 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 65eebf45c4 (pythonlib: Remove star imports (#1546))
>>>>>>> 859ce80446 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3960f36bc5 (pythonlib: Remove star imports (#1546))
>>>>>>> d08c50382a (pythonlib: Remove star imports (#1546))
=======
<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 240dcc86f4 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 3ab33fc0b6 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 628e5dfc04 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> c190252548 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
=======
>>>>>>> ae94629933 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> f008e4ec0d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> a0e50c9b34 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 8fcf52b064 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2bb9b85a2d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 1acc93c650 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 158dbc71ea (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> f9cdd7121a (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3960f36bc5 (pythonlib: Remove star imports (#1546))
>>>>>>> f6578350cf (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> c6554e4c24 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8ac6037718 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> eb96438b70 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 6c0fed7e9a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 02833e8e05 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> cbf3352a7e (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 964321810a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2f7ff18221 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2e2dc3004e (pythonlib: Remove star imports (#1546))
=======
>>>>>>> f9cdd7121a (pythonlib: Remove star imports (#1546))
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 27551073cd (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ae94629933 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 2f785ecbac (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f008e4ec0d (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 02833e8e05 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f9cdd7121a (pythonlib: Remove star imports (#1546))
>>>>>>> 9441e85caa (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a0e50c9b34 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> ba719f126c (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8fcf52b064 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 964321810a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> e2d3096606 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2bb9b85a2d (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> ba3eb01af9 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1acc93c650 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 2e2dc3004e (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> e1a7453c89 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 158dbc71ea (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> f9cdd7121a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c6554e4c24 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 8ac6037718 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> c6554e4c24 (pythonlib: Remove star imports (#1546))
>>>>>>> f6578350cf (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
>>>>>>> 3960f36bc5 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d08c50382a (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8630c1908e (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 8a28804560 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fdaa03757 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> bdc1a9eff8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e54d3f3e40 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 6a11812108 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 56010eb999 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 692afe97f6 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 56010eb999 (pythonlib: Remove star imports (#1546))
>>>>>>> 859ce80446 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 240dcc86f4 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65eebf45c4 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 705f9aa694 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 65eebf45c4 (pythonlib: Remove star imports (#1546))
>>>>>>> 0934ce9a0b (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 3ab33fc0b6 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ec038aafa (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 78a24c3407 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 2ec038aafa (pythonlib: Remove star imports (#1546))
>>>>>>> 32987ee457 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bd15a01a37 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 858dcd2c02 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> bd15a01a37 (pythonlib: Remove star imports (#1546))
>>>>>>> 64384cd976 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
>>>>>>> 1df4f6c1a9 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b62c64d69c (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2e4a058ca6 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 7d811718e6 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fcbc6eaf1c (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 0b441b6432 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 958298688f (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> ae24e8727d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 0915ba12ad (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> db4f0c5e9e (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 474e98d46c (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> edbe88c194 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 0942f70280 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fbbce42f6 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7c9ebb33c7 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 4bd0126b6c (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fd6b673316 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 631756bf9f (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> dd23d5dc15 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bf337dfc4c (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 9e2a78d963 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9407a0d6c1 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> bdb772eadd (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> e397082cd0 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8a1d36c40 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> f4b9197871 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 38eafe025f (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 8844e5da9c (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 3ced907ea6 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9cb1837c15 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 6d81b53481 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5e22f8b98 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 9fe3ace091 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 53344b046a (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 16628047b7 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> e1e8127d65 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 813bf89b9d (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 15e8b8ec25 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 0fa369e964 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7ee999faa1 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> ce79f96bcb (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55384b51b (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> dbedecb198 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> da0563df3d (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> da2395c9c7 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 81fdb5da80 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2e22515ef0 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 1c0cb85d51 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ffb921b231 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 43413f8004 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> ffb921b231 (pythonlib: Remove star imports (#1546))
>>>>>>> f6df93ab65 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 628e5dfc04 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bca36f399f (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 585ba722f9 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> bca36f399f (pythonlib: Remove star imports (#1546))
>>>>>>> ae14ae6860 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> c190252548 (pythonlib: Remove star imports (#1546))
>>>>>>> 4d810f7f30 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> aaf70da5d9 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 2c7840ea99 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 993ab127c0 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 75b5e29c4a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> f82f5fa253 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ff67671fa4 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 84a9bb8d2c (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f65836381 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 2e9a40703f (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> da1787bad3 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 46ecaf1932 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 5bb8db950a (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> eb96438b70 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 2f785ecbac (pythonlib: Remove star imports (#1546))
>>>>>>> 6c0fed7e9a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 9441e85caa (pythonlib: Remove star imports (#1546))
>>>>>>> 02833e8e05 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> ba719f126c (pythonlib: Remove star imports (#1546))
>>>>>>> cbf3352a7e (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 964321810a (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> ba3eb01af9 (pythonlib: Remove star imports (#1546))
>>>>>>> 2f7ff18221 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2e2dc3004e (pythonlib: Remove star imports (#1546))
=======
>>>>>>> c6554e4c24 (pythonlib: Remove star imports (#1546))
>>>>>>> f9cdd7121a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> f6578350cf (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
>>>>>>> 1653b03705 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 8a28804560 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> bdc1a9eff8 (pythonlib: Remove star imports (#1546))
>>>>>>> 7dc011e093 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 56010eb999 (pythonlib: Remove star imports (#1546))
>>>>>>> 6a11812108 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 65eebf45c4 (pythonlib: Remove star imports (#1546))
>>>>>>> 859ce80446 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2ec038aafa (pythonlib: Remove star imports (#1546))
>>>>>>> 0934ce9a0b (pythonlib: Remove star imports (#1546))
=======
>>>>>>> bd15a01a37 (pythonlib: Remove star imports (#1546))
>>>>>>> 32987ee457 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 64384cd976 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
>>>>>>> aeac88cf3a (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7d811718e6 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 0b441b6432 (pythonlib: Remove star imports (#1546))
>>>>>>> d416b78612 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> ae24e8727d (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 474e98d46c (pythonlib: Remove star imports (#1546))
>>>>>>> d869a3a87d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 0942f70280 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 4bd0126b6c (pythonlib: Remove star imports (#1546))
>>>>>>> 250a82a9d5 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 631756bf9f (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 9e2a78d963 (pythonlib: Remove star imports (#1546))
>>>>>>> 72c2e4860b (pythonlib: Remove star imports (#1546))
=======
>>>>>>> bdb772eadd (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> f4b9197871 (pythonlib: Remove star imports (#1546))
>>>>>>> 15ee9980f8 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 8844e5da9c (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 6d81b53481 (pythonlib: Remove star imports (#1546))
>>>>>>> 4759f473a2 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 9fe3ace091 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> e1e8127d65 (pythonlib: Remove star imports (#1546))
>>>>>>> 24602374be (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 15e8b8ec25 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> ce79f96bcb (pythonlib: Remove star imports (#1546))
>>>>>>> 2c35594c85 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> dbedecb198 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 81fdb5da80 (pythonlib: Remove star imports (#1546))
>>>>>>> f0068152e1 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> ffb921b231 (pythonlib: Remove star imports (#1546))
>>>>>>> 1c0cb85d51 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> bca36f399f (pythonlib: Remove star imports (#1546))
>>>>>>> f6df93ab65 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> ae14ae6860 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 2c7840ea99 (pythonlib: Remove star imports (#1546))
>>>>>>> 53f003b3c5 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 75b5e29c4a (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 84a9bb8d2c (pythonlib: Remove star imports (#1546))
>>>>>>> 894fed55ec (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2e9a40703f (pythonlib: Remove star imports (#1546))

import os
from .core import (
    run_command,
    parse_command,
    read_command,
    tempfile,
    fatal,
    list_strings,
)
from .utils import try_remove
from grass.exceptions import CalledModuleError


def db_describe(table, env=None, **args):
    """Return the list of columns for a database table
    (interface to `db.describe -c`). Example:

    >>> run_command("g.copy", vector="firestations,myfirestations")
    0
    >>> db_describe("myfirestations")  # doctest: +ELLIPSIS
    {'nrows': 71, 'cols': [['cat', 'INTEGER', '20'], ... 'ncols': 22}
    >>> run_command("g.remove", flags="f", type="vector", name="myfirestations")
    0

    :param str table: table name
    :param list args:
    :param env: environment

    :return: parsed module output
    """
    if "database" in args and args["database"] == "":
        args.pop("database")
    if "driver" in args and args["driver"] == "":
        args.pop("driver")
    s = read_command("db.describe", flags="c", table=table, env=env, **args)
    if not s:
        fatal(_("Unable to describe table <%s>") % table, env=env)

    cols = []
    result = {}
    for line in s.splitlines():
        f = line.split(":")
        key = f[0]
        f[1] = f[1].lstrip(" ")
        if key.startswith("Column "):
            n = int(key.split(" ")[1])
            cols.insert(n, f[1:])
        elif key in {"ncols", "nrows"}:
            result[key] = int(f[1])
        else:
            result[key] = f[1:]
    result["cols"] = cols

    return result


def db_table_exist(table, env=None, **args):
    """Check if table exists.

    If no driver or database are given, then default settings is used
    (check db_connection()).

    >>> run_command("g.copy", vector="firestations,myfirestations")
    0
    >>> db_table_exist("myfirestations")
    True
    >>> run_command("g.remove", flags="f", type="vector", name="myfirestations")
    0

    :param str table: table name
    :param args:
    :param env: environment

    :return: True for success, False otherwise
    """
    nuldev = open(os.devnull, "w+")
    ok = True
    try:
        run_command(
            "db.describe",
            flags="c",
            table=table,
            stdout=nuldev,
            stderr=nuldev,
            env=env,
            **args,
        )
    except CalledModuleError:
        ok = False
    finally:
        nuldev.close()

    return ok


def db_connection(force=False, env=None):
    """Return the current database connection parameters
    (interface to `db.connect -g`). Example:

    >>> db_connection()
    {'group': '', 'schema': '', 'driver': 'sqlite', 'database': '$GISDBASE/$LOCATION_NAME/$MAPSET/sqlite/sqlite.db'}

    :param force True to set up default DB connection if not defined
    :param env: environment

    :return: parsed output of db.connect
    """  # noqa: E501
    try:
        nuldev = open(os.devnull, "w")
        conn = parse_command("db.connect", flags="g", stderr=nuldev, env=env)
        nuldev.close()
    except CalledModuleError:
        conn = None

    if not conn and force:
        run_command("db.connect", flags="c", env=env)
        conn = parse_command("db.connect", flags="g", env=env)

    return conn


def db_select(sql=None, filename=None, table=None, env=None, **args):
    """Perform SQL select statement

    Note: one of <em>sql</em>, <em>filename</em>, or <em>table</em>
    arguments must be provided.

    Examples:

    >>> run_command("g.copy", vector="firestations,myfirestations")
    0
    >>> db_select(sql="SELECT cat,CITY FROM myfirestations WHERE cat < 4")
    (('1', 'Morrisville'), ('2', 'Morrisville'), ('3', 'Apex'))

    Simplyfied usage (it performs <tt>SELECT * FROM myfirestations</tt>.)

    >>> db_select(table="myfirestations")  # doctest: +ELLIPSIS
    (('1', '24', 'Morrisville #3', ... 'HS2A', '1.37'))
    >>> run_command("g.remove", flags="f", type="vector", name="myfirestations")
    0

    :param str sql: SQL statement to perform (or None)
    :param str filename: name of file with SQL statements (or None)
    :param str table: name of table to query (or None)
    :param str args: see *db.select* arguments
    :param env: environment
    """
    fname = tempfile(create=False, env=env)
    if sql:
        args["sql"] = sql
    elif filename:
        args["input"] = filename
    elif table:
        args["table"] = table
    else:
        fatal(
            _(
                "Programmer error: '%(sql)s', '%(filename)s', or '%(table)s' must be \
                    provided"
            )
            % {"sql": "sql", "filename": "filename", "table": "table"},
            env=env,
        )

    if "sep" not in args:
        args["sep"] = "|"

    try:
        run_command("db.select", quiet=True, flags="c", output=fname, env=env, **args)
    except CalledModuleError:
        fatal(_("Fetching data failed"), env=env)

    ofile = open(fname)
    result = [tuple(x.rstrip(os.linesep).split(args["sep"])) for x in ofile]
    ofile.close()
    try_remove(fname)

    return tuple(result)


def db_table_in_vector(table, mapset=".", env=None):
    """Return the name of vector connected to the table.
    By default it check only in the current mapset, because the same table
    name could be used also in other mapset by other vector.
    It returns None if no vectors are connected to the table.

    >>> run_command("g.copy", vector="firestations,myfirestations")
    0
    >>> db_table_in_vector("myfirestations")
    ['myfirestations@user1']
    >>> db_table_in_vector("mfirestations")
    >>> run_command("g.remove", flags="f", type="vector", name="myfirestations")
    0

    :param str table: name of table to query
    :param env: environment
    """
    from .vector import vector_db

    nuldev = open(os.devnull, "w")
    used = []
    vects = list_strings("vector", mapset=mapset, env=env)
    for vect in vects:
        for f in vector_db(vect, stderr=nuldev, env=env).values():
            if not f:
                continue
            if f["table"] == table:
                used.append(vect)
                break
    if len(used) > 0:
        return used
    return None


def db_begin_transaction(driver):
    """Begin transaction.

    :return: SQL command as string
    """
    if driver in {"sqlite", "pg"}:
        return "BEGIN"
    if driver == "mysql":
        return "START TRANSACTION"
    return ""


def db_commit_transaction(driver):
    """Commit transaction.

    :return: SQL command as string
    """
    if driver in {"sqlite", "pg", "mysql"}:
        return "COMMIT"
    return ""
