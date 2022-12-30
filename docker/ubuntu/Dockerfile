<<<<<<< HEAD
# syntax=docker/dockerfile:1.10@sha256:865e5dd094beca432e8c0a1d5e1c465db5f998dca4e439981029b3b81fb39ed5
=======
<<<<<<< HEAD
# syntax=docker/dockerfile:1.9@sha256:fe40cf4e92cd0c467be2cfc30657a680ae2398318afd50b0c80585784c604f28
=======
<<<<<<< HEAD
# syntax=docker/dockerfile:1.8@sha256:e87caa74dcb7d46cd820352bfea12591f3dba3ddc4285e19c7dcd13359f7cefd
=======
<<<<<<< HEAD
# syntax=docker/dockerfile:1.8@sha256:d6d396f3780b1dd56a3acbc975f57bd2fc501989b50164c41387c42d04e780d0
=======
<<<<<<< HEAD
# syntax=docker/dockerfile:1.7@sha256:a57df69d0ea827fb7266491f2813635de6f17269be881f696fbfdf2d83dda33e
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))

# Note: This file must be kept in sync in ./Dockerfile and ./docker/ubuntu/Dockerfile.
#       Changes to this file must be copied over to the other file.

ARG GUI=without

FROM ubuntu:22.04@sha256:0e5e4a57c2499249aafc3b40fcd541e9a456aab7296681a3994d631587203f97 as common_start

LABEL authors="Carmen Tawalika,Markus Neteler,Anika Weinmann,Stefan Blumentrath"
=======
FROM ubuntu:22.04

LABEL authors="Carmen Tawalika,Markus Neteler,Anika Weinmann"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
LABEL maintainer="tawalika@mundialis.de,neteler@mundialis.de,weinmann@mundialis.de"

ENV DEBIAN_FRONTEND noninteractive

<<<<<<< HEAD
=======
# define versions to be used
# https://github.com/PDAL/PDAL/releases
ARG PDAL_VERSION=2.4.3
# https://github.com/hobuinc/laz-perf/releases
ARG LAZ_PERF_VERSION=3.2.0

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
SHELL ["/bin/bash", "-c"]

WORKDIR /tmp

<<<<<<< HEAD
ARG GUI

# Todo: re-consider required dev packages for addons (~400MB in dev packages)
ARG GRASS_RUN_PACKAGES="\
    bison \
    build-essential \
    bzip2 \
=======
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential \
    bison \
    bzip2 \
    cmake \
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    curl \
    flex \
    g++ \
    gcc \
    gdal-bin \
<<<<<<< HEAD
    geos-bin \
    git \
    language-pack-en-base \
    libcairo2 \
    libcurl4-gnutls-dev \
    libfftw3-bin \
    libfftw3-dev \
    libfreetype6 \
    libgdal-dev \
    libgeos-dev \
    libgsl-dev \
    libgsl27 \
    libjpeg-turbo8 \
    libjsoncpp-dev \
    liblapacke-dev \
    libmagic-mgc \
    libmagic1 \
    libncurses5 \
    libomp-dev \
    libomp5 \
    libopenblas-base \
    libopenblas-dev \
    libopenjp2-7 \
    libpdal-base13 \
    libpdal-dev \
    libpdal-plugin-hdf \
    libpdal-plugins \
    libpdal-util13 \
    libpnglite0 \
    libpq-dev \
    libpq5 \
    libproj-dev \
    libpython3-all-dev \
    libreadline8 \
    libsqlite3-0 \
    libtiff-tools \
    libzstd1 \
    locales \
    make \
    mesa-utils \
    moreutils \
    ncurses-bin \
    netcdf-bin \
    pdal \
    proj-bin \
    proj-data \
    python-is-python3 \
    python3 \
    python3-dev \
    python3-venv \
    sqlite3 \
=======
    git \
    language-pack-en-base \
    libbz2-dev \
    libcairo2 \
    libcairo2-dev \
    libcurl4-gnutls-dev \
    libfftw3-bin \
    libfftw3-dev \
    libfreetype6-dev \
    libgdal-dev \
    libgeos-dev \
    libgsl0-dev \
    libjpeg-dev \
    libjsoncpp-dev \
    libnetcdf-dev \
    libncurses5-dev \
    libopenblas-base \
    libopenblas-dev \
    libopenjp2-7 \
    libopenjp2-7-dev \
    libpnglite-dev \
    libpq-dev \
    libproj-dev \
    libpython3-all-dev \
    libsqlite3-dev \
    libtiff-dev \
    libzstd-dev \
    locales \
    make \
    mesa-common-dev \
    moreutils \
    ncurses-bin \
    netcdf-bin \
    proj-bin \
    proj-data \
    python3 \
    python3-dateutil \
    python3-dev \
    python3-magic \
    python3-numpy \
    python3-pil \
    python3-pip \
    python3-ply \
    python3-setuptools \
    python3-venv \
    software-properties-common \
    sqlite3 \
    subversion \
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    unzip \
    vim \
    wget \
    zip \
<<<<<<< HEAD
    zlib1g \
    "
ENV GRASS_RUN_PACKAGES=${GRASS_RUN_PACKAGES}

# Define build packages
ARG GRASS_BUILD_PACKAGES="\
    cmake \
    libbz2-dev \
    libcairo2-dev \
    libfreetype6-dev \
    libjpeg-dev \
    libncurses5-dev \
    libnetcdf-dev \
    libopenjp2-7-dev \
    libpnglite-dev \
    libreadline-dev \
    libsqlite3-dev \
    libtiff-dev \
    libzstd-dev \
    mesa-common-dev \
    zlib1g-dev \
    "
ENV GRASS_BUILD_PACKAGES=${GRASS_BUILD_PACKAGES}

ARG GRASS_CONFIG="\
  --enable-largefile \
  --with-blas \
  --with-bzlib \
  --with-cairo --with-cairo-ldflags=-lfontconfig \
  --with-cxx \
  --with-fftw \
  --with-freetype --with-freetype-includes=/usr/include/freetype2/ \
  --with-gdal=/usr/bin/gdal-config \
  --with-geos \
  --with-lapack \
  --with-netcdf \
  --with-odbc \
  --with-openmp \
  --with-pdal \
  --with-postgres --with-postgres-includes=/usr/include/postgresql \
  --with-proj-share=/usr/share/proj \
  --with-readline \
  --with-sqlite \
  --with-zstd \
  --without-mysql \
  "

ARG GRASS_PYTHON_PACKAGES="\
    Pillow \
    matplotlib \
    numpy \
    pip \
    ply \
    psycopg2 \
    python-dateutil \
    python-magic \
    setuptools \
  "
ENV GRASS_PYTHON_PACKAGES=${GRASS_PYTHON_PACKAGES}


FROM common_start as grass_without_gui

ARG GRASS_CONFIG="${GRASS_CONFIG} --without-opengl"
ENV GRASS_CONFIG=${GRASS_CONFIG}

FROM common_start as grass_with_gui

ARG GRASS_RUN_PACKAGES="${GRASS_RUN_PACKAGES} \
  adwaita-icon-theme-full \
  freeglut3 \
  gettext \
  libglu1-mesa \
  libgstreamer-plugins-base1.0 \
  libgtk-3-0 \
  libjpeg8 \
  libnotify4 \
  libpng16-16 \
  librsvg2-common \
  libsdl2-2.0-0 \
  libsm6 \
  libtiff5 \
  libwebkit2gtk-4.0 \
  libxtst6 \
"
# librsvg2-common \
# (fix error (wxgui.py:7782): Gtk-WARNING **: 19:53:09.774:
# Could not load a pixbuf from /org/gtk/libgtk/theme/Adwaita/assets/check-symbolic.svg.
# This may indicate that pixbuf loaders or the mime database could not be found.)

ARG GRASS_BUILD_PACKAGES="${GRASS_BUILD_PACKAGES} \
  adwaita-icon-theme-full \
  freeglut3-dev \
  libgl1-mesa-dev \
  libglu1-mesa-dev \
  libgstreamer-plugins-base1.0-dev \
  libgtk-3-dev \
  libjpeg-dev \
  libnotify-dev \
  libpng-dev \
  libsdl2-dev \
  libsm-dev \
  libtiff-dev \
  libwebkit2gtk-4.0-dev \
  libxtst-dev \
"

ARG GRASS_CONFIG="${GRASS_CONFIG} \
  --with-nls \
  --with-opengl \
  --with-readline \
  --with-x \
  "
ARG GRASS_PYTHON_PACKAGES="${GRASS_PYTHON_PACKAGES} wxPython"
# If you do not use any Gnome Accessibility features, to suppress warning
# WARNING **: Couldn't connect to accessibility bus:
# execute programs with
ENV NO_AT_BRIDGE=1


FROM grass_${GUI}_gui as grass_gis
# Add ubuntugis unstable and fetch packages
RUN apt-get update \
    && apt-get install  -y --no-install-recommends --no-install-suggests \
    software-properties-common \
    gpg \
    gpg-agent \
    && LC_ALL=C.UTF-8 add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable \
    && apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    $GRASS_RUN_PACKAGES \
    && apt-get remove -y gpg gpg-agent \
    && apt-get autoremove -y \
    && apt-get clean all \
    && rm -rf /var/lib/apt/lists/*

RUN echo LANG="en_US.UTF-8" > /etc/default/locale \
    && echo en_US.UTF-8 UTF-8 >> /etc/locale.gen \
    && locale-gen

## fetch vertical datums for PDAL and store into PROJ dir
WORKDIR /src

# # Get datum grids
# # Currently using https://proj.org/en/9.3/usage/network.html#how-to-enable-network-capabilities
# FROM ubuntu:22.04 as datum_grids

# # See: https://github.com/OSGeo/PROJ-data
# RUN apt-get update \
#     && apt-get install  -y --no-install-recommends --no-install-suggests \
#     wget \
#     && apt-get clean all \
#     && rm -rf /var/lib/apt/lists/*

# WORKDIR /tmp
# RUN wget --no-check-certificate -r -l inf -A tif https://cdn.proj.org/

# Start build stage
FROM grass_gis as build

# Add build packages
RUN apt-get update \
    && apt-get install  -y --no-install-recommends --no-install-suggests \
    $GRASS_BUILD_PACKAGES \
    && apt-get clean all \
    && rm -rf /var/lib/apt/lists/*

# Add pip and Python packages
RUN (echo "Install Python" \
    && wget https://bootstrap.pypa.io/pip/get-pip.py \
    # && apt-get install -y python3-ensurepip \
    && python get-pip.py \
    # && python3 -m ensurepip --upgrade \
    && rm -r get-pip.py \
    && mkdir -p /src/site-packages \
    && cd /src \
    && python -m pip install --no-cache-dir -t /src/site-packages --upgrade \
    $GRASS_PYTHON_PACKAGES \
    && rm -r /root/.cache \
    && rm -rf /tmp/pip-* \
    )

# copy grass gis source
COPY . /src/grass_build/

WORKDIR /src/grass_build

=======
    zlib1g-dev

RUN echo LANG="en_US.UTF-8" > /etc/default/locale
RUN echo en_US.UTF-8 UTF-8 >> /etc/locale.gen && locale-gen

## install laz-perf (missing from https://packages.ubuntu.com/)
RUN apt-get install cmake
WORKDIR /src
RUN wget -q https://github.com/hobu/laz-perf/archive/${LAZ_PERF_VERSION}.tar.gz -O laz-perf-${LAZ_PERF_VERSION}.tar.gz && \
    tar -zxf laz-perf-${LAZ_PERF_VERSION}.tar.gz && \
    cd laz-perf-${LAZ_PERF_VERSION} && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install

## fetch vertical datums for PDAL and store into PROJ dir
WORKDIR /src
RUN mkdir vdatum && \
    cd vdatum && \
    wget -q http://download.osgeo.org/proj/vdatum/usa_geoid2012.zip && unzip -j -u usa_geoid2012.zip -d /usr/share/proj; \
    wget -q http://download.osgeo.org/proj/vdatum/usa_geoid2009.zip && unzip -j -u usa_geoid2009.zip -d /usr/share/proj; \
    wget -q http://download.osgeo.org/proj/vdatum/usa_geoid2003.zip && unzip -j -u usa_geoid2003.zip -d /usr/share/proj; \
    wget -q http://download.osgeo.org/proj/vdatum/usa_geoid1999.zip && unzip -j -u usa_geoid1999.zip -d /usr/share/proj; \
    wget -q http://download.osgeo.org/proj/vdatum/vertcon/vertconc.gtx && mv vertconc.gtx /usr/share/proj; \
    wget -q http://download.osgeo.org/proj/vdatum/vertcon/vertcone.gtx && mv vertcone.gtx /usr/share/proj; \
    wget -q http://download.osgeo.org/proj/vdatum/vertcon/vertconw.gtx && mv vertconw.gtx /usr/share/proj; \
    wget -q http://download.osgeo.org/proj/vdatum/egm96_15/egm96_15.gtx && mv egm96_15.gtx /usr/share/proj; \
    wget -q http://download.osgeo.org/proj/vdatum/egm08_25/egm08_25.gtx && mv egm08_25.gtx /usr/share/proj; \
    cd .. && \
    rm -rf vdatum

## install pdal
ENV NUMTHREADS=4
WORKDIR /src
RUN wget -q \
 https://github.com/PDAL/PDAL/releases/download/${PDAL_VERSION}/PDAL-${PDAL_VERSION}-src.tar.gz && \
    tar xfz PDAL-${PDAL_VERSION}-src.tar.gz && \
    cd /src/PDAL-${PDAL_VERSION}-src && \
    mkdir build && \
    cd build && \
    cmake .. \
      -G "Unix Makefiles" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_C_COMPILER=gcc \
      -DCMAKE_CXX_COMPILER=g++ \
      -DCMAKE_MAKE_PROGRAM=make \
      -DBUILD_PLUGIN_PYTHON=ON \
      -DBUILD_PLUGIN_CPD=OFF \
      -DBUILD_PLUGIN_GREYHOUND=ON \
      -DBUILD_PLUGIN_HEXBIN=ON \
      -DHEXER_INCLUDE_DIR=/usr/include/ \
      -DBUILD_PLUGIN_NITF=OFF \
      -DBUILD_PLUGIN_ICEBRIDGE=ON \
      -DBUILD_PLUGIN_PGPOINTCLOUD=ON \
      -DBUILD_PGPOINTCLOUD_TESTS=OFF \
      -DBUILD_PLUGIN_SQLITE=ON \
      -DWITH_LASZIP=ON \
      -DWITH_LAZPERF=ON \
      -DWITH_TESTS=ON && \
    make -j $NUMTHREADS && \
    make install

# copy grass gis source
WORKDIR /src
COPY . /src/grass_build/
WORKDIR /src/grass_build

# Cleanup potentially leftover GISRC file with wrong path to "demolocation"
RUN rm -f /src/grass_build/dist.*/demolocation/.grassrc*

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
# Set environmental variables for GRASS GIS compilation, without debug symbols
# Set gcc/g++ environmental variables for GRASS GIS compilation, without debug symbols
ENV MYCFLAGS "-O2 -std=gnu99 -m64"
ENV MYLDFLAGS "-s"
# CXX stuff:
<<<<<<< HEAD
ENV LD_LIBRARY_PATH "/usr/local/lib"
=======
<<<<<<< HEAD
#ENV LD_LIBRARY_PATH "/usr/local/lib"
=======
ENV LD_LIBRARY_PATH "/usr/local/lib"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
ENV LDFLAGS "$MYLDFLAGS"
ENV CFLAGS "$MYCFLAGS"
ENV CXXFLAGS "$MYCXXFLAGS"

# Configure compile and install GRASS GIS
ENV NUMTHREADS=4
RUN make distclean || echo "nothing to clean"
<<<<<<< HEAD
RUN ./configure $GRASS_CONFIG \
    && make -j $NUMTHREADS \
    && make install && ldconfig \
    &&  cp /usr/local/grass85/gui/wxpython/xml/module_items.xml module_items.xml; \
    rm -rf /usr/local/grass85/demolocation; \
    rm -rf /usr/local/grass85/fonts; \
    rm -rf /usr/local/grass85/gui; \
    rm -rf /usr/local/grass85/share; \
    mkdir -p /usr/local/grass85/gui/wxpython/xml/; \
    mv module_items.xml /usr/local/grass85/gui/wxpython/xml/module_items.xml;

# Build the GDAL-GRASS plugin
RUN git clone https://github.com/OSGeo/gdal-grass \
    && cd "gdal-grass" \
    && ./configure \
      --with-gdal=/usr/bin/gdal-config \
      --with-grass=/usr/local/grass85 \
    && make -j $NUMTHREADS \
    && make install -j $NUMTHREADS \
    && cd /src \
    && rm -rf "gdal-grass"

# Leave build stage
FROM grass_gis as grass_gis_final

# GRASS GIS specific
# allow work with MAPSETs that are not owned by current user
ENV GRASS_SKIP_MAPSET_OWNER_CHECK=1 \
    SHELL="/bin/bash" \
    # https://proj.org/usage/environmentvars.html#envvar-PROJ_NETWORK
    PROJ_NETWORK=ON \
    LC_ALL="en_US.UTF-8" \
    PYTHONPATH="/usr/local/grass/etc/python/:${PYTHONPATH}" \
    LD_LIBRARY_PATH="/usr/local/grass/lib:$LD_LIBRARY_PATH" \
    GDAL_DRIVER_PATH="/usr/lib/gdalplugins"

# Copy GRASS GIS from build image
COPY --link --from=build /usr/local/bin/* /usr/local/bin/
COPY --link --from=build /usr/local/grass85 /usr/local/grass85/
COPY --link --from=build /src/site-packages /usr/lib/python3.10/
COPY --link --from=build /usr/lib/gdalplugins /usr/lib/gdalplugins
# COPY --link --from=datum_grids /tmp/cdn.proj.org/*.tif /usr/share/proj/

# Create generic GRASS GIS lib name regardless of version number
RUN ln -sf /usr/local/grass85 /usr/local/grass

# show GRASS GIS, PROJ, GDAL etc versions
RUN grass --tmp-project EPSG:4326 --exec g.version -rge && \
    pdal --version && \
    python --version

WORKDIR /scripts

# enable GRASS GIS Python session support
## grass --config python-path
ENV PYTHONPATH "/usr/local/grass/etc/python:${PYTHONPATH}"
# enable GRASS GIS ctypes imports
## grass --config path
ENV LD_LIBRARY_PATH "/usr/local/grass/lib:$LD_LIBRARY_PATH"

WORKDIR /tmp
COPY docker/testdata/simple.laz .
WORKDIR /scripts
COPY docker/testdata/test_grass_session.py .
## run GRASS GIS python session and scan the test LAZ file
RUN python /scripts/test_grass_session.py
RUN rm -rf /tmp/grasstest_epsg_25832
# test LAZ file
RUN grass --tmp-project EPSG:25832 --exec r.in.pdal input="/tmp/simple.laz" output="count_1" method="n" resolution=1 -g
WORKDIR /grassdb
VOLUME /grassdb

<<<<<<< HEAD
CMD ["$GRASSBIN", "--version"]
=======
CMD ["bash", "-c", "$GRASSBIN", "--version"]
=======
RUN /src/grass_build/configure \
  --with-cxx \
  --enable-largefile \
  --with-proj-share=/usr/share/proj \
  --with-gdal=/usr/bin/gdal-config \
  --with-geos \
  --with-sqlite \
  --with-cairo --with-cairo-ldflags=-lfontconfig \
  --with-freetype --with-freetype-includes="/usr/include/freetype2/" \
  --with-fftw \
  --with-postgres --with-postgres-includes="/usr/include/postgresql" \
  --with-netcdf \
  --with-zstd \
  --with-bzlib \
  --with-pdal \
  --without-mysql \
  --without-odbc \
  --without-openmp \
  --without-opengl \
    && make -j $NUMTHREADS \
    && make install && ldconfig

# Unset environmental variables to avoid later compilation issues
ENV INTEL ""
ENV MYCFLAGS ""
ENV MYLDFLAGS ""
ENV MYCXXFLAGS ""
ENV LD_LIBRARY_PATH ""
ENV LDFLAGS ""
ENV CFLAGS ""
ENV CXXFLAGS ""

# set SHELL var to avoid /bin/sh fallback in interactive GRASS GIS sessions
ENV SHELL /bin/bash
ENV LC_ALL "en_US.UTF-8"
ENV GRASS_SKIP_MAPSET_OWNER_CHECK 1

# Create generic GRASS GIS lib name regardless of version number
RUN ln -sf /usr/local/grass83 /usr/local/grass

# show GRASS GIS, PROJ, GDAL etc versions
RUN grass --tmp-location EPSG:4326 --exec g.version -rge && \
    pdal --version && \
    python3 --version

# Reduce the image size
RUN apt-get autoremove -y
RUN apt-get clean -y
RUN rm -r /src/grass_build/.git

WORKDIR /scripts

# install external GRASS GIS session Python API
RUN pip3 install grass-session

# install GRASS GIS extensions
RUN grass --tmp-location EPSG:4326 --exec g.extension extension=r.in.pdal

# add GRASS GIS envs for python usage
ENV GISBASE "/usr/local/grass/"
ENV GRASSBIN "/usr/local/bin/grass"
ENV PYTHONPATH "${PYTHONPATH}:$GISBASE/etc/python/"
ENV LD_LIBRARY_PATH "$LD_LIBRARY_PATH:$GISBASE/lib"

WORKDIR /tmp
COPY docker/testdata/simple.laz .
WORKDIR /scripts
COPY docker/testdata/test_grass_session.py .
## just scan the LAZ file
# Not yet ready for GRASS GIS 8:
#RUN /usr/bin/python3 /scripts/test_grass_session.py
RUN grass --tmp-location EPSG:25832 --exec r.in.pdal input="/tmp/simple.laz" output="count_1" method="n" resolution=1 -s

WORKDIR /grassdb
VOLUME /grassdb
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
