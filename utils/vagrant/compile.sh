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
<<<<<<< HEAD
        --enable-largefile \
=======
        --srcdir=/vagrant \
        --prefix=/usr/lib \
>>>>>>> 4b6fca67b9 (packaging: Update Vagrantfile to Ubuntu 24.04 (#3836))
=======
        --enable-largefile \
>>>>>>> 88cfd0573d (style: Sort package lists, configure options, and other various sortable files (#4563))
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
<<<<<<< HEAD
=======
>>>>>>> 88cfd0573d (style: Sort package lists, configure options, and other various sortable files (#4563))
        --with-lapack \
        --with-mysql \
        --with-mysql-includes=`mysql_config --include | sed -e 's/-I//'` \
        --with-netcdf \
<<<<<<< HEAD
=======
        --with-freetype \
        --with-readline \
>>>>>>> 4b6fca67b9 (packaging: Update Vagrantfile to Ubuntu 24.04 (#3836))
=======
>>>>>>> 88cfd0573d (style: Sort package lists, configure options, and other various sortable files (#4563))
        --with-nls \
        --with-odbc \
        --with-postgres \
        --with-postgres-includes=`pg_config --includedir` \
        --with-proj-share=/usr/share/proj \
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
        --with-pthread \
        --with-readline \
        --with-sqlite \
        --with-x \
        --without-pdal
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
        --with-python \
        --with-cairo \
        --with-liblas
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
        --with-cairo \
=======
>>>>>>> 88cfd0573d (style: Sort package lists, configure options, and other various sortable files (#4563))
        --with-pthread \
        --with-readline \
        --with-sqlite \
        --with-x \
        --without-pdal
>>>>>>> 4b6fca67b9 (packaging: Update Vagrantfile to Ubuntu 24.04 (#3836))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
fi

make -j $NUMTHREADS

sudo make install
sudo ldconfig

exit 0
