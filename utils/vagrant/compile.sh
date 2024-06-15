#!/bin/bash

### inspired by https://github.com/OSGeo/gdal/blob/master/gdal/scripts/vagrant/gdal.sh

# abort install if any errors occur and enable tracing
set -o errexit
set -o xtrace

NUMTHREADS=2
if [[ -f /sys/devices/system/cpu/online ]]; then
	# Calculates 1.5 times physical threads
	NUMTHREADS=$(( ( $(cut -f 2 -d '-' /sys/devices/system/cpu/online) + 1 ) * 15 / 10  ))
fi
#NUMTHREADS=1 # disable MP
export NUMTHREADS

cd /vagrant

if [ ! -f "include/Make/Platform.make" ] ; then
    ./configure \
        --bindir=/usr/bin \
<<<<<<< HEAD
        --enable-largefile \
=======
        --srcdir=/vagrant \
        --prefix=/usr/lib \
>>>>>>> 4b6fca67b9 (packaging: Update Vagrantfile to Ubuntu 24.04 (#3836))
        --enable-shared \
        --prefix=/usr/lib \
        --srcdir=/vagrant \
        --with-blas \
        --with-bzlib \
        --with-cairo \
        --with-cxx \
        --with-freetype \
        --with-freetype-includes=/usr/include/freetype2 \
        --with-gdal \
        --with-geos \
<<<<<<< HEAD
        --with-lapack \
        --with-mysql \
        --with-mysql-includes=`mysql_config --include | sed -e 's/-I//'` \
        --with-netcdf \
=======
        --with-freetype \
        --with-readline \
>>>>>>> 4b6fca67b9 (packaging: Update Vagrantfile to Ubuntu 24.04 (#3836))
        --with-nls \
        --with-odbc \
        --with-postgres \
        --with-postgres-includes=`pg_config --includedir` \
        --with-proj-share=/usr/share/proj \
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        --with-pthread \
        --with-readline \
        --with-sqlite \
        --with-x \
        --without-pdal
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        --with-python \
        --with-cairo \
        --with-liblas
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        --with-cairo \
        --with-pthread \
        --with-bzlib \
        --without-pdal
>>>>>>> 4b6fca67b9 (packaging: Update Vagrantfile to Ubuntu 24.04 (#3836))
fi

make -j $NUMTHREADS

sudo make install
sudo ldconfig

exit 0
