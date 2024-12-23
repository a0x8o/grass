# Docker GRASS GIS (Ubuntu Linux)

Dockerfile with an [Ubuntu Linux](https://ubuntu.com/) image with
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b59427ac06 (docker: Use only native Python API, set only necessary variables (#3819))
[GRASS GIS](https://grass.osgeo.org/), [PDAL](https://pdal.io) support.
=======
[GRASS GIS](https://grass.osgeo.org/), [PDAL](https://pdal.io) support and
[grass-session](https://github.com/zarch/grass-session/).
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
[GRASS GIS](https://grass.osgeo.org/), [PDAL](https://pdal.io) support and
[grass-session](https://github.com/zarch/grass-session/).
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
[GRASS GIS](https://grass.osgeo.org/), [PDAL](https://pdal.io) support.
>>>>>>> dd2e07572c (docker: Use only native Python API, set only necessary variables (#3819))
=======
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
[GRASS GIS](https://grass.osgeo.org/), [PDAL](https://pdal.io) support.
>>>>>>> dd2e07572c (docker: Use only native Python API, set only necessary variables (#3819))
>>>>>>> b59427ac06 (docker: Use only native Python API, set only necessary variables (#3819))

Download size of this image is of approximately 2.6 GB.

Clone this repository and change directory:

```bash
git clone https://github.com/OSGeo/grass.git
cd grass
```

## Ubuntu stable

__Build the docker with__:

```bash
docker build \
         --file docker/ubuntu_wxgui/Dockerfile \
         --tag grass-py3-pdal:stable-ubuntu .
```

View the images available using `sudo docker images` and open a bash terminal
with:

```bash
$ docker run -it grass-py3-pdal:stable-ubuntu /bin/bash
bash-5.0#
```

__To build a stable version__:

change to the releasebranch or tag you want to build:

```bash
git checkout remotes/origin/releasebranch_8_2
```

and build and enter with:

```bash
$ docker build \
         -f docker/ubuntu_wxgui/Dockerfile \
         -t grass-py3-pdal:stable-ubuntu .

$ docker run -it grass-py3-pdal:stable-ubuntu /bin/bash
bash-5.0#
```

## Ubuntu latest

__Build the docker with__:

```bash
$ docker build \
         --file docker/ubuntu_wxgui/Dockerfile_ubuntu_wxgui_latest_pdal \
         --tag grass-py3-pdal:latest-ubuntu .
```

View the images available using `sudo docker images` and open a bash terminal
with:

```bash
$ docker run -it grass-py3-pdal:latest-ubuntu /bin/bash
bash-5.0#
```

__To build a latest version__:

change to the releasebranch or tag you want to build:

```bash
git checkout remotes/origin/releasebranch_8_2
```

and build and enter with:

```bash
$ docker build \
         -f docker/ubuntu_wxgui/Dockerfile_ubuntu_wxgui_latest_pdal \
         -t grass-py3-pdal:latest-ubuntu .

$ docker run -it grass-py3-pdal:latest-ubuntu /bin/bash
bash-5.0#
```
