"""
Created on Thu Jun 28 17:44:14 2012

@author: pietro
"""

import ctypes
from operator import itemgetter
from pathlib import Path

import grass.lib.raster as libraster
from grass.exceptions import ImplementationError

from grass.pygrass.errors import GrassError
from grass.pygrass.utils import decode
from grass.pygrass.raster.raster_type import TYPE as RTYPE


class Category(list):
    """
    I would like to add the following functions:

    Getting the umber of cats:
    Rast_number_of_cats() <- Important for ith access

    Getting and setting the title:
    Rast_get_cats_title()
    Rast_set_cats_title()

    Do not use these functions for category access:
    Rast_get_cat()
    and the specialized types for CELL, FCELL and DCELL.
    Since these functions are working on hidden static buffer.

    Use the ith-get methods:
    Rast_get_ith_c_cat()
    Rast_get_ith_f_cat()
    Rast_get_ith_d_cat()

    This can be implemented using an iterator too. So that the category object
    provides the [] access operator to the categories, returning a tuple
    (label, min, max).
    Using this, the category object must be aware of its raster map type.

    Set categories using:
    Rast_set_c_cat()
    Rast_set_f_cat()
    Rast_set_d_cat()

    Misc:
    Rast_sort_cats()
    Rast_copy_cats() <- This should be wrapped so that categories from an
    existing Python category class are copied.

    """

    def __init__(self, name, mapset="", mtype="CELL", *args, **kargs):
        self.name = name
        self.mapset = mapset
        self.c_cats = libraster.Categories()
        libraster.Rast_init_cats("", ctypes.byref(self.c_cats))
        self._mtype = mtype
        self._gtype = None if mtype is None else RTYPE[mtype]["grass type"]
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
        super().__init__(*args, **kargs)
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
        super().__init__(*args, **kargs)
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
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
        super().__init__(*args, **kargs)
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
        super().__init__(*args, **kargs)
=======
<<<<<<< HEAD
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
        super().__init__(*args, **kargs)
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
=======
        super().__init__(*args, **kargs)
=======
<<<<<<< HEAD
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
=======
        super().__init__(*args, **kargs)
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
        super(Category, self).__init__(*args, **kargs)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))

    def _get_mtype(self):
        return self._mtype

    def _set_mtype(self, mtype):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 001cfcbd00 (style: Fixes literal-membership (PLR6201) for other code (#3954))
        if mtype.upper() not in {"CELL", "FCELL", "DCELL"}:
            raise ValueError(_("Raster type: {0} not supported").format(mtype))
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
        if mtype.upper() not in ("CELL", "FCELL", "DCELL"):
=======
        if mtype.upper() not in {"CELL", "FCELL", "DCELL"}:
>>>>>>> 75456afff2 (style: Fixes literal-membership (PLR6201) for other code (#3954))
<<<<<<< HEAD
=======
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
        if mtype.upper() not in {"CELL", "FCELL", "DCELL"}:
            raise ValueError(_("Raster type: {0} not supported").format(mtype))
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
        if mtype.upper() not in ("CELL", "FCELL", "DCELL"):
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 001cfcbd00 (style: Fixes literal-membership (PLR6201) for other code (#3954))
            raise ValueError(_("Raster type: {0} not supported".format(mtype)))
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
        self._mtype = mtype
        self._gtype = RTYPE[self.mtype]["grass type"]

    mtype = property(
        fget=_get_mtype, fset=_set_mtype, doc="Set or obtain raster data type"
    )

    def _get_title(self):
        return libraster.Rast_get_cats_title(ctypes.byref(self.c_cats))

    def _set_title(self, newtitle):
        return libraster.Rast_set_cats_title(newtitle, ctypes.byref(self.c_cats))

    title = property(fget=_get_title, fset=_set_title, doc="Set or obtain raster title")

    def __str__(self):
        return self.__repr__()

    def __list__(self):
        cats = []
        for cat in self.__iter__():
            cats.append(cat)
        return cats

    def __dict__(self):
        diz = {}
        for cat in self.__iter__():
            label, min_cat, max_cat = cat
            diz[min_cat, max_cat] = label
        return diz

    def __repr__(self):
        cats = []
        for cat in self.__iter__():
            cats.append(repr(cat))
        return "[{0}]".format(",\n ".join(cats))

    def _chk_index(self, index):
        if type(index) == str:
            try:
                index = self.labels().index(index)
            except ValueError:
                raise KeyError(index)
        return index

    def _chk_value(self, value):
        if type(value) == tuple:
            length = len(value)
            if length == 2:
                label, min_cat = value
                value = (label, min_cat, None)
            elif length < 2 or length > 3:
                raise TypeError("Tuple with a length that is not supported.")
        else:
            raise TypeError("Only Tuple are supported.")
        return value

    def __getitem__(self, index):
        return super().__getitem__(self._chk_index(index))

    def __setitem__(self, index, value):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        return super(Category, self).__setitem__(
            self._chk_index(index), self._chk_value(value)
        )
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
        return super(Category, self).__setitem__(
            self._chk_index(index), self._chk_value(value)
        )
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
        return super(Category, self).__setitem__(
            self._chk_index(index), self._chk_value(value)
        )
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
        return super(Category, self).__setitem__(
            self._chk_index(index), self._chk_value(value)
        )
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
=======
        return super(Category, self).__setitem__(
            self._chk_index(index), self._chk_value(value)
        )
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
=======
=======
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
        return super().__setitem__(self._chk_index(index), self._chk_value(value))
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
        return super(Category, self).__setitem__(
            self._chk_index(index), self._chk_value(value)
        )
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
        return super(Category, self).__setitem__(
            self._chk_index(index), self._chk_value(value)
        )
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))

    def _get_c_cat(self, index):
        """Returns i-th description and i-th data range from the list of
        category descriptions with corresponding data ranges. end points of
        data interval.

        Rast_get_ith_cat(const struct Categories * 	pcats,
                         int 	i,
                         void * 	rast1,
                         void * 	rast2,
                         RASTER_MAP_TYPE 	data_type
                         )
        """
        min_cat = ctypes.pointer(RTYPE[self.mtype]["grass def"]())
        max_cat = ctypes.pointer(RTYPE[self.mtype]["grass def"]())
        lab = decode(
            libraster.Rast_get_ith_cat(
                ctypes.byref(self.c_cats),
                index,
                ctypes.cast(min_cat, ctypes.c_void_p),
                ctypes.cast(max_cat, ctypes.c_void_p),
                self._gtype,
            )
        )
        # Manage C function Errors
        if lab == "":
            raise GrassError(_("Error executing: Rast_get_ith_cat"))
        if max_cat.contents.value == min_cat.contents.value:
            max_cat = None
        else:
            max_cat = max_cat.contents.value
        return lab, min_cat.contents.value, max_cat

    def _set_c_cat(self, label, min_cat, max_cat=None):
        """Adds the label for range min through max in category structure cats.

        int Rast_set_cat(const void * 	rast1,
                         const void * 	rast2,
                         const char * 	label,
                         struct Categories * 	pcats,
                         RASTER_MAP_TYPE 	data_type
                         )
        """
        max_cat = min_cat if max_cat is None else max_cat
        min_cat = ctypes.pointer(RTYPE[self.mtype]["grass def"](min_cat))
        max_cat = ctypes.pointer(RTYPE[self.mtype]["grass def"](max_cat))
        err = libraster.Rast_set_cat(
            ctypes.cast(min_cat, ctypes.c_void_p),
            ctypes.cast(max_cat, ctypes.c_void_p),
            label,
            ctypes.byref(self.c_cats),
            self._gtype,
        )
        # Manage C function Errors
        if err == 1:
            return None
        if err == 0:
            raise GrassError(_("Null value detected"))
        if err == -1:
            raise GrassError(_("Error executing: Rast_set_cat"))

    def __del__(self):
        libraster.Rast_free_cats(ctypes.byref(self.c_cats))

    def get_cat(self, index):
        return self[index]

    def set_cat(self, index, value):
        if index is None:
            self.append(value)
        elif index < (len(self)):
            self[index] = value
        else:
            raise TypeError("Index outside range.")

    def reset(self):
        for i in range(len(self) - 1, -1, -1):
            del self[i]
        libraster.Rast_init_cats("", ctypes.byref(self.c_cats))

    def _read_cats(self):
        """Copy from the C struct to the list"""
        for i in range(self.c_cats.ncats):
            self.append(self._get_c_cat(i))

    def _write_cats(self):
        """Copy from the list data to the C struct"""
        # reset only the C struct
        libraster.Rast_init_cats("", ctypes.byref(self.c_cats))
        # write to the c struct
        for cat in iter(self):
            label, min_cat, max_cat = cat
            if max_cat is None:
                max_cat = min_cat
            self._set_c_cat(label, min_cat, max_cat)

    def read(self):
        """Read categories from a raster map

        The category file for raster map name in mapset is read into the
        cats structure. If there is an error reading the category file,
        a diagnostic message is printed.

        int Rast_read_cats(const char * 	name,
                           const char * 	mapset,
                           struct Categories * 	pcats
                           )
        """
        self.reset()
        err = libraster.Rast_read_cats(
            self.name, self.mapset, ctypes.byref(self.c_cats)
        )
        if err == -1:
            raise GrassError("Can not read the categories.")
        # copy from C struct to list
        self._read_cats()

    def write(self):
        """Writes the category file for the raster map name in the current
           mapset from the cats structure.

        void Rast_write_cats(const char * 	name,
                             struct Categories * 	cats
                             )
        """
        # copy from list to C struct
        self._write_cats()
        # write to the map
        libraster.Rast_write_cats(self.name, ctypes.byref(self.c_cats))

    def copy(self, category):
        """Copy from another Category class

        :param category: Category class to be copied
        :type category: Category object
        """
        libraster.Rast_copy_cats(
            ctypes.byref(self.c_cats), ctypes.byref(category.c_cats)  # to
        )  # from
        self._read_cats()

    def ncats(self):
        return len(self)

    def set_cats_fmt(self, fmt, m1, a1, m2, a2):
        """Not implemented yet.
        void Rast_set_cats_fmt()
        """
        # TODO: add
        raise ImplementationError("set_cats_fmt() is not implemented yet.")

    def read_rules(self, filename, sep=":"):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
        """Copy categories from a rules file, default separator is ':', the
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
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
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
<<<<<<< HEAD
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
<<<<<<< HEAD
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
        """Copy categories from a rules file, default separetor is ':', the
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
        columns must be: min and/or max and label. ::

            1:forest
            2:road
            3:urban

            0.:0.5:forest
            0.5:1.0:road
            1.0:1.5:urban

        :param str filename: the name of file with categories rules
        :param str sep: the separator used to divide values and category

        """
        self.reset()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
        with open(filename) as f:
            for row in f:
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
        with open(filename) as f:
            for row in f:
=======
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
        with open(filename, "r") as f:
            for row in f.readlines():
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
                cat = row.strip().split(sep)
                if len(cat) == 2:
                    label, min_cat = cat
                    max_cat = None
                elif len(cat) == 3:
                    label, min_cat, max_cat = cat
                else:
                    raise TypeError("Row length is greater than 3")
                self.append((label, min_cat, max_cat))

    def write_rules(self, filename, sep=":"):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
        """Copy categories from a rules file, default separator is ':', the
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
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
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
<<<<<<< HEAD
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
<<<<<<< HEAD
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
=======
        """Copy categories from a rules file, default separator is ':', the
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
        """Copy categories from a rules file, default separetor is ':', the
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
        columns must be: min and/or max and label. ::

            1:forest
            2:road
            3:urban

            0.:0.5:forest
            0.5:1.0:road
            1.0:1.5:urban

        :param str filename: the name of file with categories rules
        :param str sep: the separator used to divide values and category
        """
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
        cats = []
        for cat in iter(self):
            if cat[-1] is None:
                cat = cat[:-1]
            cats.append(sep.join([str(i) for i in cat]))
        Path(filename).write_text("\n".join(cats))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
        with open(filename, "w") as f:
            cats = []
            for cat in self.__iter__():
                if cat[-1] is None:
                    cat = cat[:-1]
                cats.append(sep.join([str(i) for i in cat]))
            f.write("\n".join(cats))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))

    def sort(self):
        libraster.Rast_sort_cats(ctypes.byref(self.c_cats))

    def labels(self):
        return list(map(itemgetter(0), self))
