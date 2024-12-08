#   Copyright (C) 2012, Almar Klein, Ant1, Marius van Voorden
#
#   This code is subject to the (new) BSD license:
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the <organization> nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

""" Module images2gif

Provides functionality for reading and writing animated GIF images.
Use writeGif to write a series of numpy arrays or PIL images as an
animated GIF. Use readGif to read an animated gif as a series of numpy
arrays.

Note that since July 2004, all patents on the LZW compression patent have
expired. Therefore the GIF format may now be used freely.

Acknowledgements:

Many thanks to Ant1 for:

* noting the use of "palette=PIL.Image.ADAPTIVE", which significantly
  improves the results.
* the modifications to save each image with its own palette, or optionally
  the global palette (if its the same).

Many thanks to Marius van Voorden for porting the NeuQuant quantization
algorithm of Anthony Dekker to Python (See the NeuQuant class for its
license).

Many thanks to Alex Robinson for implementing the concept of subrectangles,
which (depending on image content) can give a very significant reduction in
file size.

This code is based on gifmaker (in the scripts folder of the source
distribution of PIL)


Useful links:

  * http://tronche.com/computer-graphics/gif/
  * https://en.wikipedia.org/wiki/Graphics_Interchange_Format
  * http://www.w3.org/Graphics/GIF/spec-gif89a.txt

"""
# todo: This module should be part of imageio (or at least based on)

import os

try:
    import PIL
    from PIL import Image

    pillow = True
    try:
        PIL_version = PIL.__version__  # test if user has Pillow or PIL
    except AttributeError:
        pillow = False
    from PIL.GifImagePlugin import getheader, getdata
except ImportError:
    PIL = None

try:
    import numpy as np
except ImportError:
    np = None


def get_cKDTree():
    try:
        from scipy.spatial import cKDTree
    except ImportError:
        cKDTree = None
    return cKDTree


# getheader gives a 87a header and a color palette (two elements in a list)
# getdata()[0] gives the Image Descriptor up to (including) "LZW min code size"
# getdatas()[1:] is the image data itself in chunks of 256 bytes (well
# technically the first byte says how many bytes follow, after which that
# amount (max 255) follows)


def checkImages(images):
    """checkImages(images)
    Check numpy images and correct intensity range etc.
    The same for all movie formats.

    :param images:
    """
    # Init results
    images2 = []

    for im in images:
        if PIL and isinstance(im, PIL.Image.Image):
            # We assume PIL images are alright
            images2.append(im)

        elif np and isinstance(im, np.ndarray):
            # Check and convert dtype
            if im.dtype == np.uint8:
                images2.append(im)  # Ok
            elif im.dtype in [np.float32, np.float64]:
                im = im.copy()
                im[im < 0] = 0
                im[im > 1] = 1
                im *= 255
                images2.append(im.astype(np.uint8))
            else:
                im = im.astype(np.uint8)
                images2.append(im)
            # Check size
            if im.ndim == 2:
                pass  # ok
            elif im.ndim == 3:
                if im.shape[2] not in [3, 4]:
                    raise ValueError("This array can not represent an image.")
            else:
                raise ValueError("This array can not represent an image.")
        else:
            raise ValueError("Invalid image type: " + str(type(im)))

    # Done
    return images2


def intToBin(i):
    """Integer to two bytes"""
    # divide in two parts (bytes)
    i1 = i % 256
    i2 = int(i / 256)
    # make string (little endian)
    return chr(i1) + chr(i2)


class GifWriter:
    """Class that contains methods for helping write the animated GIF file."""

    def getheaderAnim(self, im):
        """Get animation header. To replace PILs getheader()[0]

        :param im:
        """
        bb = "GIF89a"
        bb += intToBin(im.size[0])
        bb += intToBin(im.size[1])
        bb += "\x87\x00\x00"
        return bb

    def getImageDescriptor(self, im, xy=None):
        """Used for the local color table properties per image.
        Otherwise global color table applies to all frames irrespective of
        whether additional colors comes in play that require a redefined
        palette. Still a maximum of 256 color per frame, obviously.

        Written by Ant1 on 2010-08-22
        Modified by Alex Robinson in Janurari 2011 to implement subrectangles.

        :param im:
        :param xy:
        """

        # Default use full image and place at upper left
        if xy is None:
            xy = (0, 0)

        # Image separator,
        bb = "\x2C"

        # Image position and size
        bb += intToBin(xy[0])  # Left position
        bb += intToBin(xy[1])  # Top position
        bb += intToBin(im.size[0])  # image width
        bb += intToBin(im.size[1])  # image height

        # packed field: local color table flag1, interlace0, sorted table0,
        # reserved00, lct size111=7=2^(7 + 1)=256.
        bb += "\x87"

        # LZW min size code now comes later, beginning of [image data] blocks
        return bb

    def getAppExt(self, loops=float("inf")):
        """Application extension. This part specifies the amount of loops.
        If loops is 0 or inf, it goes on infinitely.

        :param float loops:
        """

        if loops == 0 or loops == float("inf"):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3454fc4883 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6286b6659a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 52e6c1ff9f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4d4ee1c6cc (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 67ed37bf9b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
            loops = 2**16 - 1
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e494d37988 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9087bcf6fe (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56f3d5a1bd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b30eba7edb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1d6ad40ebe (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 740bf772d6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7b80a7eedd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> de3b023788 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
            loops = 2**16 - 1
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
            loops = 2**16 - 1
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            loops = 2**16 - 1
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
            loops = 2**16 - 1
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
            loops = 2**16 - 1
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
            loops = 2**16 - 1
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            loops = 2**16 - 1
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
            loops = 2**16 - 1
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            loops = 2**16 - 1
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
            loops = 2**16 - 1
=======
>>>>>>> osgeo-main
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            loops = 2**16 - 1
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
            loops = 2**16 - 1
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
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
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
<<<<<<< HEAD
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
<<<<<<< HEAD
            loops = 2**16 - 1
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
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
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
<<<<<<< HEAD
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e494d37988 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 56f3d5a1bd (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1d6ad40ebe (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7b80a7eedd (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3454fc4883 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
            loops = 2**16 - 1
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
            loops = 2 ** 16 - 1
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 52e6c1ff9f (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
            loops = 2**16 - 1
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
            # bb = ""
            # application extension should not be used
            # (the extension interprets zero loops
            # to mean an infinite number of loops)
            # Mmm, does not seem to work
        if True:
            bb = "\x21\xFF\x0B"  # application extension
            bb += "NETSCAPE2.0"
            bb += "\x03\x01"
            bb += intToBin(loops)
            bb += "\x00"  # end
        return bb

    def getGraphicsControlExt(self, duration=0.1, dispose=2):
        """Graphics Control Extension. A sort of header at the start of
        each image. Specifies duration and transparency.

        Dispose:

          * 0 - No disposal specified.
          * 1 - Do not dispose. The graphic is to be left in place.
          * 2 -	Restore to background color. The area used by the graphic
            must be restored to the background color.
          * 3 -	Restore to previous. The decoder is required to restore the
            area overwritten by the graphic with what was there prior to
            rendering the graphic.
          * 4-7 -To be defined.

        :param double duration:
        :param dispose:
        """

        bb = "\x21\xF9\x04"
        bb += chr((dispose & 3) << 2)  # low bit 1 == transparency,
        # 2nd bit 1 == user input , next 3 bits, the low two of which are used,
        # are dispose.
        bb += intToBin(int(duration * 100))  # in 100th of seconds
        bb += "\x00"  # no transparent color
        bb += "\x00"  # end
        return bb

    def handleSubRectangles(self, images, subRectangles):
        """Handle the sub-rectangle stuff. If the rectangles are given by the
        user, the values are checked. Otherwise the subrectangles are
        calculated automatically.

        """

        if isinstance(subRectangles, (tuple, list)):
            # xy given directly

            # Check xy
            xy = subRectangles
            if xy is None:
                xy = (0, 0)
            if hasattr(xy, "__len__"):
                if len(xy) == len(images):
                    xy = list(xy)
                else:
                    raise ValueError("len(xy) doesn't match amount of images.")
            else:
                xy = [xy for im in images]
            xy[0] = (0, 0)

        else:
            # Calculate xy using some basic image processing

            # Check Numpy
            if np is None:
                raise RuntimeError("Need Numpy to use auto-subRectangles.")

            # First make numpy arrays if required
            for i in range(len(images)):
                im = images[i]
                if isinstance(im, Image.Image):
                    tmp = im.convert()  # Make without palette
                    a = np.asarray(tmp)
                    if len(a.shape) == 0:
                        raise MemoryError(
                            "Too little memory to convert PIL image to array"
                        )
                    images[i] = a

            # Determine the sub rectangles
            images, xy = self.getSubRectangles(images)

        # Done
        return images, xy

    def getSubRectangles(self, ims):
        """getSubRectangles(ims)

        Calculate the minimal rectangles that need updating each frame.
        Returns a two-element tuple containing the cropped images and a
        list of x-y positions.

        Calculating the subrectangles takes extra time, obviously. However,
        if the image sizes were reduced, the actual writing of the GIF
        goes faster. In some cases applying this method produces a GIF faster.

        """

        # Check image count
        if len(ims) < 2:
            return ims, [(0, 0) for i in ims]

        # We need numpy
        if np is None:
            raise RuntimeError("Need Numpy to calculate sub-rectangles. ")

        # Prepare
        ims2 = [ims[0]]
        xy = [(0, 0)]

        # Iterate over images
        prev = ims[0]
        for im in ims[1:]:
            # Get difference, sum over colors
            diff = np.abs(im - prev)
            if diff.ndim == 3:
                diff = diff.sum(2)
            # Get begin and end for both dimensions
            X = np.argwhere(diff.sum(0))
            Y = np.argwhere(diff.sum(1))
            # Get rect coordinates
            if X.size and Y.size:
                x0, x1 = int(X[0]), int(X[-1] + 1)
                y0, y1 = int(Y[0]), int(Y[-1] + 1)
            else:  # No change ... make it minimal
                x0, x1 = 0, 2
                y0, y1 = 0, 2

            # Cut out and store
            im2 = im[y0:y1, x0:x1]
            prev = im
            ims2.append(im2)
            xy.append((x0, y0))

        # Done
        # print('%1.2f seconds to determine subrectangles of  %i images' %
        #    (time.time()-t0, len(ims2)))
        return ims2, xy

    def convertImagesToPIL(self, images, dither, nq=0):
        """convertImagesToPIL(images, nq=0)

        Convert images to Paletted PIL images, which can then be
        written to a single animaged GIF.

        """

        # Convert to PIL images
        images2 = []
        for im in images:
            if isinstance(im, Image.Image):
                images2.append(im)
            elif np and isinstance(im, np.ndarray):
                if im.ndim == 3 and im.shape[2] == 3:
                    im = Image.fromarray(im, "RGB")
                elif im.ndim == 3 and im.shape[2] == 4:
                    im = Image.fromarray(im[:, :, :3], "RGB")
                elif im.ndim == 2:
                    im = Image.fromarray(im, "L")
                images2.append(im)

        # Convert to paletted PIL images
        images, images2 = images2, []
        if nq >= 1:
            # NeuQuant algorithm
            for im in images:
                im = im.convert("RGBA")  # NQ assumes RGBA
                nqInstance = NeuQuant(im, int(nq))  # Learn colors from image
                if dither:
                    im = im.convert("RGB").quantize(palette=nqInstance.paletteImage())
                else:
                    # Use to quantize the image itself
                    im = nqInstance.quantize(im)
                images2.append(im)
        else:
            # Adaptive PIL algorithm
            AD = Image.ADAPTIVE
            for im in images:
                im = im.convert("P", palette=AD, dither=dither)
                images2.append(im)

        # Done
        return images2

    def writeGifToFile(self, fp, images, durations, loops, xys, disposes):
        """writeGifToFile(fp, images, durations, loops, xys, disposes)

        Given a set of images writes the bytes to the specified stream.
        Requires different handling of palette for PIL and Pillow:
        based on https://github.com/rec/echomesh/blob/master/
        code/python/external/images2gif.py

        """

        # Obtain palette for all images and count each occurrence
        palettes, occur = [], []
        for im in images:
            if not pillow:
                palette = getheader(im)[1]
            else:
                palette = getheader(im)[0][-1]
                if not palette:
                    palette = im.palette.tobytes()
            palettes.append(palette)
        for palette in palettes:
            occur.append(palettes.count(palette))

        # Select most-used palette as the global one (or first in case no max)
        globalPalette = palettes[occur.index(max(occur))]

        # Init
        frames = 0
        firstFrame = True

        for im, palette in zip(images, palettes):
            if firstFrame:
                # Write header

                # Gather info
                header = self.getheaderAnim(im)
                appext = self.getAppExt(loops)

                # Write
                fp.write(header)
                fp.write(globalPalette)
                fp.write(appext)

                # Next frame is not the first
                firstFrame = False

            if True:
                # Write palette and image data

                # Gather info
                data = getdata(im)
                imdes, data = data[0], data[1:]
                graphext = self.getGraphicsControlExt(
                    durations[frames], disposes[frames]
                )
                # Make image descriptor suitable for using 256 local color palette
                lid = self.getImageDescriptor(im, xys[frames])

                # Write local header
                if (palette != globalPalette) or (disposes[frames] != 2):
                    # Use local color palette
                    fp.write(graphext)
                    fp.write(lid)  # write suitable image descriptor
                    fp.write(palette)  # write local color table
                    fp.write("\x08")  # LZW minimum size code
                else:
                    # Use global color palette
                    fp.write(graphext)
                    fp.write(imdes)  # write suitable image descriptor

                # Write image data
                for d in data:
                    fp.write(d)

            # Prepare for next round
            frames += 1

        fp.write(";")  # end gif
        return frames


def writeGif(filename, images, duration=0.1, repeat=True, **kwargs):
    """Write an animated gif from the specified images.
    Depending on which PIL library is used, either writeGifVisvis or writeGifPillow
    is used here.

    :param str filename: the name of the file to write the image to.
    :param list images: should be a list consisting of PIL images or numpy
                        arrays. The latter should be between 0 and 255 for
                        integer types, and between 0 and 1 for float types.
    :param duration: scalar or list of scalars The duration for all frames, or
                     (if a list) for each frame.
    :param repeat: bool or integer The amount of loops. If True, loops infinitetel
    :param kwargs: additional parameters for writeGifVisvis

    """
    if pillow:
        # Pillow >= 3.4.0 has animated GIF writing
        version = [int(i) for i in PIL.__version__.split(".")]
        if version[0] > 3 or (version[0] == 3 and version[1] >= 4):
            writeGifPillow(filename, images, duration, repeat)
            return
    # otherwise use the old one
    writeGifVisvis(filename, images, duration, repeat, **kwargs)


def writeGifPillow(filename, images, duration=0.1, repeat=True):
    """Write an animated gif from the specified images.
    Uses native Pillow implementation, which is available since Pillow 3.4.0.

    :param str filename: the name of the file to write the image to.
    :param list images: should be a list consisting of PIL images or numpy
                        arrays. The latter should be between 0 and 255 for
                        integer types, and between 0 and 1 for float types.
    :param duration: scalar or list of scalars The duration for all frames, or
                     (if a list) for each frame.
    :param repeat: bool or integer The amount of loops. If True, loops infinitetel

    """
    loop = 0 if repeat else 1
    quantized = []
    for im in images:
        quantized.append(im.quantize())
    quantized[0].save(
        filename,
        save_all=True,
        append_images=quantized[1:],
        loop=loop,
        duration=duration * 1000,
    )


def writeGifVisvis(
    filename,
    images,
    duration=0.1,
    repeat=True,
    dither=False,
    nq=0,
    subRectangles=True,
    dispose=None,
):
    """Write an animated gif from the specified images.
    Uses VisVis implementation. Unfortunately it produces corrupted GIF
    with Pillow >= 3.4.0.

    :param str filename: the name of the file to write the image to.
    :param list images: should be a list consisting of PIL images or numpy
                        arrays. The latter should be between 0 and 255 for
                        integer types, and between 0 and 1 for float types.
    :param duration: scalar or list of scalars The duration for all frames, or
                     (if a list) for each frame.
    :param repeat: bool or integer The amount of loops. If True, loops infinitetely.
    :param bool dither: whether to apply dithering
    :param int nq: If nonzero, applies the NeuQuant quantization algorithm to
                   create the color palette. This algorithm is superior, but
                   slower than the standard PIL algorithm. The value of nq is
                   the quality parameter. 1 represents the best quality. 10 is
                   in general a good tradeoff between quality and speed. When
                   using this option, better results are usually obtained when
                   subRectangles is False.
    :param subRectangles: False, True, or a list of 2-element tuples
                          Whether to use sub-rectangles. If True, the minimal
                          rectangle that is required to update each frame is
                          automatically detected. This can give significant
                          reductions in file size, particularly if only a part
                          of the image changes. One can also give a list of x-y
                          coordinates if you want to do the cropping yourself.
                          The default is True.
    :param int dispose: how to dispose each frame. 1 means that each frame is
                        to be left in place. 2 means the background color
                        should be restored after each frame. 3 means the
                        decoder should restore the previous frame. If
                        subRectangles==False, the default is 2, otherwise it is 1.

    """

    # Check PIL
    if PIL is None:
        raise RuntimeError("Need PIL to write animated gif files.")

    # Check images
    images = checkImages(images)

    # Instantiate writer object
    gifWriter = GifWriter()

    # Check loops
    if repeat is False:
        loops = 1
    elif repeat is True:
        loops = 0  # zero means infinite
    else:
        loops = int(repeat)

    # Check duration
    if hasattr(duration, "__len__"):
        if len(duration) == len(images):
            duration = list(duration)
        else:
            raise ValueError("len(duration) doesn't match amount of images.")
    else:
        duration = [duration for im in images]

    # Check subrectangles
    if subRectangles:
        images, xy = gifWriter.handleSubRectangles(images, subRectangles)
        defaultDispose = 1  # Leave image in place
    else:
        # Normal mode
        xy = [(0, 0) for im in images]
        defaultDispose = 2  # Restore to background color.

    # Check dispose
    if dispose is None:
        dispose = defaultDispose
    if hasattr(dispose, "__len__"):
        if len(dispose) != len(images):
            raise ValueError("len(xy) doesn't match amount of images.")
    else:
        dispose = [dispose for im in images]

    # Make images in a format that we can write easy
    images = gifWriter.convertImagesToPIL(images, dither, nq)

    # Write
    fp = open(filename, "wb")
    try:
        gifWriter.writeGifToFile(fp, images, duration, loops, xy, dispose)
    finally:
        fp.close()


def readGif(filename, asNumpy=True):
    """Read images from an animated GIF file.  Returns a list of numpy
    arrays, or, if asNumpy is false, a list if PIL images.

    """

    # Check PIL
    if PIL is None:
        raise RuntimeError("Need PIL to read animated gif files.")

    # Check Numpy
    if np is None:
        raise RuntimeError("Need Numpy to read animated gif files.")

    # Check whether it exists
    if not os.path.isfile(filename):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        raise IOError("File not found: " + str(filename))
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
>>>>>>> 3454fc4883 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6286b6659a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 52e6c1ff9f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4d4ee1c6cc (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
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
        raise IOError("File not found: " + str(filename))
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
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
<<<<<<< HEAD
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
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
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
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
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
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
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
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> e494d37988 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9087bcf6fe (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 56f3d5a1bd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b30eba7edb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1d6ad40ebe (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 740bf772d6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7b80a7eedd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> de3b023788 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 67ed37bf9b (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
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
        raise IOError("File not found: " + str(filename))
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
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
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
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
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e494d37988 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 9087bcf6fe (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 56f3d5a1bd (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b30eba7edb (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1d6ad40ebe (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 740bf772d6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7b80a7eedd (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> de3b023788 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 67ed37bf9b (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
>>>>>>> 3454fc4883 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 6286b6659a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
>>>>>>> 52e6c1ff9f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4d4ee1c6cc (Dockerfile: fix broken lib link (#1625))
        raise OSError("File not found: " + str(filename))
=======
        raise IOError("File not found: " + str(filename))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
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
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> e494d37988 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9087bcf6fe (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 56f3d5a1bd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b30eba7edb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1d6ad40ebe (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 740bf772d6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7b80a7eedd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> de3b023788 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 67ed37bf9b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3454fc4883 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6286b6659a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 52e6c1ff9f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4d4ee1c6cc (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
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
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
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
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
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
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
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
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
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
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
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
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
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
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
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
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 9087bcf6fe (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> b30eba7edb (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 740bf772d6 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> de3b023788 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
>>>>>>> 67ed37bf9b (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6286b6659a (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4d4ee1c6cc (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
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
=======
        raise IOError("File not found: " + str(filename))
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
>>>>>>> e494d37988 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9087bcf6fe (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 56f3d5a1bd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b30eba7edb (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1d6ad40ebe (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 740bf772d6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7b80a7eedd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
>>>>>>> de3b023788 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 67ed37bf9b (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
>>>>>>> 3454fc4883 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6286b6659a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
>>>>>>> 52e6c1ff9f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4d4ee1c6cc (Dockerfile: fix broken lib link (#1625))

    # Load file using PIL
    pilIm = PIL.Image.open(filename)
    pilIm.seek(0)

    # Read all images inside
    images = []
    try:
        while True:
            # Get image as numpy array
            tmp = pilIm.convert()  # Make without palette
            a = np.asarray(tmp)
            if len(a.shape) == 0:
                raise MemoryError("Too little memory to convert PIL image to array")
            # Store, and next
            images.append(a)
            pilIm.seek(pilIm.tell() + 1)
    except EOFError:
        pass

    # Convert to normal PIL images if needed
    if not asNumpy:
        images2 = images
        images = []
        for im in images2:
            images.append(PIL.Image.fromarray(im))

    # Done
    return images


class NeuQuant:
    """NeuQuant(image, samplefac=10, colors=256)

    samplefac should be an integer number of 1 or higher, 1
    being the highest quality, but the slowest performance.
    With avalue of 10, one tenth of all pixels are used during
    training. This value seems a nice tradeof between speed
    and quality.

    colors is the amount of colors to reduce the image to. This
    should best be a power of two.

    See also:
    http://members.ozemail.com.au/~dekker/NEUQUANT.HTML

    **License of the NeuQuant Neural-Net Quantization Algorithm**

    Copyright (c) 1994 Anthony Dekker
    Ported to python by Marius van Voorden in 2010

    NEUQUANT Neural-Net quantization algorithm by Anthony Dekker, 1994.
    See "Kohonen neural networks for optimal colour quantization"
    in "network: Computation in Neural Systems" Vol. 5 (1994) pp 351-367.
    for a discussion of the algorithm.
    See also  http://members.ozemail.com.au/~dekker/NEUQUANT.HTML

    Any party obtaining a copy of these files from the author, directly or
    indirectly, is granted, free of charge, a full and unrestricted
    irrevocable, world-wide, paid up, royalty-free, nonexclusive right and
    license to deal in this software and documentation files (the "Software"),
    including without limitation the rights to use, copy, modify, merge,
    publish, distribute, sublicense, and/or sell copies of the Software, and
    to permit persons who receive copies from any such party to do so, with
    the only requirement being that this copyright notice remain intact.

    """

    NCYCLES = None  # Number of learning cycles
    NETSIZE = None  # Number of colours used
    SPECIALS = None  # Number of reserved colours used
    BGCOLOR = None  # Reserved background colour
    CUTNETSIZE = None
    MAXNETPOS = None

    INITRAD = None  # For 256 colours, radius starts at 32
    RADIUSBIASSHIFT = None
    RADIUSBIAS = None
    INITBIASRADIUS = None
    RADIUSDEC = None  # Factor of 1/30 each cycle

    ALPHABIASSHIFT = None
    INITALPHA = None  # biased by 10 bits

    GAMMA = None
    BETA = None
    BETAGAMMA = None

    network = None  # The network itself
    colormap = None  # The network itself

    netindex = None  # For network lookup - really 256

    bias = None  # Bias and freq arrays for learning
    freq = None

    pimage = None

    # Four primes near 500 - assume no image has a length so large
    # that it is divisible by all four primes
    PRIME1 = 499
    PRIME2 = 491
    PRIME3 = 487
    PRIME4 = 503
    MAXPRIME = PRIME4

    pixels = None
    samplefac = None

    a_s = None

    def setconstants(self, samplefac, colors):
        self.NCYCLES = 100  # Number of learning cycles
        self.NETSIZE = colors  # Number of colours used
        self.SPECIALS = 3  # Number of reserved colours used
        self.BGCOLOR = self.SPECIALS - 1  # Reserved background colour
        self.CUTNETSIZE = self.NETSIZE - self.SPECIALS
        self.MAXNETPOS = self.NETSIZE - 1

        self.INITRAD = self.NETSIZE / 8  # For 256 colours, radius starts at 32
        self.RADIUSBIASSHIFT = 6
        self.RADIUSBIAS = 1 << self.RADIUSBIASSHIFT
        self.INITBIASRADIUS = self.INITRAD * self.RADIUSBIAS
        self.RADIUSDEC = 30  # Factor of 1/30 each cycle

        self.ALPHABIASSHIFT = 10  # Alpha starts at 1
        self.INITALPHA = 1 << self.ALPHABIASSHIFT  # biased by 10 bits

        self.GAMMA = 1024.0
        self.BETA = 1.0 / 1024.0
        self.BETAGAMMA = self.BETA * self.GAMMA

        # The network itself
        self.network = np.empty((self.NETSIZE, 3), dtype="float64")
        # The network itself
        self.colormap = np.empty((self.NETSIZE, 4), dtype="int32")

        self.netindex = np.empty(256, dtype="int32")  # For network lookup - really 256

        # Bias and freq arrays for learning
        self.bias = np.empty(self.NETSIZE, dtype="float64")
        self.freq = np.empty(self.NETSIZE, dtype="float64")

        self.pixels = None
        self.samplefac = samplefac

        self.a_s = {}

    def __init__(self, image, samplefac=10, colors=256):
        # Check Numpy
        if np is None:
            raise RuntimeError("Need Numpy for the NeuQuant algorithm.")

        # Check image
        if image.size[0] * image.size[1] < NeuQuant.MAXPRIME:
            raise OSError("Image is too small")
        if image.mode != "RGBA":
            raise OSError("Image mode should be RGBA.")

        # Initialize
        self.setconstants(samplefac, colors)
        self.pixels = np.fromstring(image.tobytes(), np.uint32)
        self.setUpArrays()

        self.learn()
        self.fix()
        self.inxbuild()

    def writeColourMap(self, rgb, outstream):
        for i in range(self.NETSIZE):
            bb = self.colormap[i, 0]
            gg = self.colormap[i, 1]
            rr = self.colormap[i, 2]
            outstream.write(rr if rgb else bb)
            outstream.write(gg)
            outstream.write(bb if rgb else rr)
        return self.NETSIZE

    def setUpArrays(self):
        self.network[0, 0] = 0.0  # Black
        self.network[0, 1] = 0.0
        self.network[0, 2] = 0.0

        self.network[1, 0] = 255.0  # White
        self.network[1, 1] = 255.0
        self.network[1, 2] = 255.0

        # RESERVED self.BGCOLOR # Background

        for i in range(self.SPECIALS):
            self.freq[i] = 1.0 / self.NETSIZE
            self.bias[i] = 0.0

        for i in range(self.SPECIALS, self.NETSIZE):
            p = self.network[i]
            p[:] = (255.0 * (i - self.SPECIALS)) / self.CUTNETSIZE

            self.freq[i] = 1.0 / self.NETSIZE
            self.bias[i] = 0.0

    # Omitted: setPixels

    def altersingle(self, alpha, i, b, g, r):
        """Move neuron i towards biased (b, g, r) by factor alpha"""
        n = self.network[i]  # Alter hit neuron
        n[0] -= alpha * (n[0] - b)
        n[1] -= alpha * (n[1] - g)
        n[2] -= alpha * (n[2] - r)

    def geta(self, alpha, rad):
        try:
            return self.a_s[alpha, rad]
        except KeyError:
            length = rad * 2 - 1
            mid = length / 2
            q = np.array(list(range(mid - 1, -1, -1)) + list(range(-1, mid)))
            a = alpha * (rad * rad - q * q) / (rad * rad)
            a[mid] = 0
            self.a_s[alpha, rad] = a
            return a

    def alterneigh(self, alpha, rad, i, b, g, r):
        if i - rad >= self.SPECIALS - 1:
            lo = i - rad
            start = 0
        else:
            lo = self.SPECIALS - 1
            start = self.SPECIALS - 1 - (i - rad)

        if i + rad <= self.NETSIZE:
            hi = i + rad
            end = rad * 2 - 1
        else:
            hi = self.NETSIZE
            end = self.NETSIZE - (i + rad)

        a = self.geta(alpha, rad)[start:end]

        p = self.network[lo + 1 : hi]
        p -= np.transpose(np.transpose(p - np.array([b, g, r])) * a)

    # def contest(self, b, g, r):
    #    """ Search for biased BGR values
    #            Finds closest neuron (min dist) and updates self.freq
    #            finds best neuron (min dist-self.bias) and returns position
    #            for frequently chosen neurons, self.freq[i] is high and self.bias[i]
    #            is negative
    #            self.bias[i] = self.GAMMA * ((1/self.NETSIZE)-self.freq[i])"""
    #
    #    i, j = self.SPECIALS, self.NETSIZE
    #    dists = abs(self.network[i:j] - np.array([b, g, r])).sum(1)
    #    bestpos = i + np.argmin(dists)
    #    biasdists = dists - self.bias[i:j]
    #    bestbiaspos = i + np.argmin(biasdists)
    #    self.freq[i:j] -= self.BETA * self.freq[i:j]
    #    self.bias[i:j] += self.BETAGAMMA * self.freq[i:j]
    #    self.freq[bestpos] += self.BETA
    #    self.bias[bestpos] -= self.BETAGAMMA
    #    return bestbiaspos
    def contest(self, b, g, r):
        """Search for biased BGR values
        Finds closest neuron (min dist) and updates self.freq
        finds best neuron (min dist-self.bias) and returns position
        for frequently chosen neurons, self.freq[i] is high and self.bias[i]
        is negative self.bias[i] = self.GAMMA * ((1/self.NETSIZE)-self.freq[i])
        """
        i, j = self.SPECIALS, self.NETSIZE
        dists = abs(self.network[i:j] - np.array([b, g, r])).sum(1)
        bestpos = i + np.argmin(dists)
        biasdists = dists - self.bias[i:j]
        bestbiaspos = i + np.argmin(biasdists)
        self.freq[i:j] *= 1 - self.BETA
        self.bias[i:j] += self.BETAGAMMA * self.freq[i:j]
        self.freq[bestpos] += self.BETA
        self.bias[bestpos] -= self.BETAGAMMA
        return bestbiaspos

    def specialFind(self, b, g, r):
        for i in range(self.SPECIALS):
            n = self.network[i]
            if n[0] == b and n[1] == g and n[2] == r:
                return i
        return -1

    def learn(self):
        biasRadius = self.INITBIASRADIUS
        alphadec = 30 + ((self.samplefac - 1) / 3)
        lengthcount = self.pixels.size
        samplepixels = lengthcount / self.samplefac
        delta = samplepixels / self.NCYCLES
        alpha = self.INITALPHA

        i = 0
        rad = biasRadius >> self.RADIUSBIASSHIFT
        if rad <= 1:
            rad = 0

        print(
            "Beginning 1D learning: samplepixels = %1.2f  rad = %i"
            % (samplepixels, rad)
        )
        step = 0
        pos = 0
        if lengthcount % NeuQuant.PRIME1 != 0:
            step = NeuQuant.PRIME1
        elif lengthcount % NeuQuant.PRIME2 != 0:
            step = NeuQuant.PRIME2
        elif lengthcount % NeuQuant.PRIME3 != 0:
            step = NeuQuant.PRIME3
        else:
            step = NeuQuant.PRIME4

        i = 0
        printed_string = ""
        while i < samplepixels:
            if i % 100 == 99:
                tmp = "\b" * len(printed_string)
                printed_string = str((i + 1) * 100 / samplepixels) + "%\n"
                print(tmp + printed_string)
            p = self.pixels[pos]
            r = (p >> 16) & 0xFF
            g = (p >> 8) & 0xFF
            b = (p) & 0xFF

            if i == 0:  # Remember background colour
                self.network[self.BGCOLOR] = [b, g, r]

            j = self.specialFind(b, g, r)
            if j < 0:
                j = self.contest(b, g, r)

            if j >= self.SPECIALS:  # Don't learn for specials
                a = (1.0 * alpha) / self.INITALPHA
                self.altersingle(a, j, b, g, r)
                if rad > 0:
                    self.alterneigh(a, rad, j, b, g, r)

            pos = (pos + step) % lengthcount

            i += 1
            if i % delta == 0:
                alpha -= alpha / alphadec
                biasRadius -= biasRadius / self.RADIUSDEC
                rad = biasRadius >> self.RADIUSBIASSHIFT
                if rad <= 1:
                    rad = 0

        finalAlpha = (1.0 * alpha) / self.INITALPHA
        print("Finished 1D learning: final alpha = %1.2f!" % finalAlpha)

    def fix(self):
        for i in range(self.NETSIZE):
            for j in range(3):
                x = int(0.5 + self.network[i, j])
                x = max(0, x)
                x = min(255, x)
                self.colormap[i, j] = x
            self.colormap[i, 3] = i

    def inxbuild(self):
        previouscol = 0
        startpos = 0
        for i in range(self.NETSIZE):
            p = self.colormap[i]
            q = None
            smallpos = i
            smallval = p[1]  # Index on g
            # Find smallest in i..self.NETSIZE-1
            for j in range(i + 1, self.NETSIZE):
                q = self.colormap[j]
                if q[1] < smallval:  # Index on g
                    smallpos = j
                    smallval = q[1]  # Index on g

            q = self.colormap[smallpos]
            # Swap p (i) and q (smallpos) entries
            if i != smallpos:
                p[:], q[:] = q, p.copy()

            # smallval entry is now in position i
            if smallval != previouscol:
                self.netindex[previouscol] = (startpos + i) >> 1
                for j in range(previouscol + 1, smallval):
                    self.netindex[j] = i
                previouscol = smallval
                startpos = i
        self.netindex[previouscol] = (startpos + self.MAXNETPOS) >> 1
        for j in range(previouscol + 1, 256):  # Really 256
            self.netindex[j] = self.MAXNETPOS

    def paletteImage(self):
        """PIL weird interface for making a paletted image: create an image
        which already has the palette, and use that in Image.quantize. This
        function returns this palette image."""
        if self.pimage is None:
            palette = []
            for i in range(self.NETSIZE):
                palette.extend(self.colormap[i][:3])

            palette.extend([0] * (256 - self.NETSIZE) * 3)

            # a palette image to use for quant
            self.pimage = Image.new("P", (1, 1), 0)
            self.pimage.putpalette(palette)
        return self.pimage

    def quantize(self, image):
        """Use a kdtree to quickly find the closest palette colors for the
        pixels

        :param image:
        """
        if get_cKDTree():
            return self.quantize_with_scipy(image)
<<<<<<< HEAD
        print("Scipy not available, falling back to slower version.")
        return self.quantize_without_scipy(image)
=======
        else:
            print("Scipy not available, falling back to slower version.")
            return self.quantize_without_scipy(image)
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))

    def quantize_with_scipy(self, image):
        w, h = image.size
        px = np.asarray(image).copy()
        px2 = px[:, :, :3].reshape((w * h, 3))

        cKDTree = get_cKDTree()
        kdtree = cKDTree(self.colormap[:, :3], leafsize=10)
        result = kdtree.query(px2)
        colorindex = result[1]
        print("Distance: %1.2f" % (result[0].sum() / (w * h)))
        px2[:] = self.colormap[colorindex, :3]

        return Image.fromarray(px).convert("RGB").quantize(palette=self.paletteImage())

    def quantize_without_scipy(self, image):
        """ " This function can be used if no scipy is available.
        It's 7 times slower though.

        :param image:
        """
        w, h = image.size
        px = np.asarray(image).copy()
        memo = {}
        for j in range(w):
            for i in range(h):
                key = (px[i, j, 0], px[i, j, 1], px[i, j, 2])
                try:
                    val = memo[key]
                except KeyError:
                    val = self.convert(*key)
                    memo[key] = val
                px[i, j, 0], px[i, j, 1], px[i, j, 2] = val
        return Image.fromarray(px).convert("RGB").quantize(palette=self.paletteImage())

    def convert(self, *color):
        i = self.inxsearch(*color)
        return self.colormap[i, :3]

    def inxsearch(self, r, g, b):
        """Search for BGR values 0..255 and return colour index"""
        dists = self.colormap[:, :3] - np.array([r, g, b])
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
        return np.argmin((dists * dists).sum(1))
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
        return np.argmin((dists * dists).sum(1))
=======
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
        a = np.argmin((dists * dists).sum(1))
        return a
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))


if __name__ == "__main__":
    im = np.zeros((200, 200), dtype=np.uint8)
    im[10:30, :] = 100
    im[:, 80:120] = 255
    im[-50:-40, :] = 50

    images = [im * 1.0, im * 0.8, im * 0.6, im * 0.4, im * 0]
    writeGif("lala3.gif", images, duration=0.5, dither=0)
