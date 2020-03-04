#!/bin/sh
Version=9.1
GDB=gdb-$Version
wget https://ftp.gnu.org/gnu/gdb/$GDB.tar.gz
tar -zxvf $GDB.tar.gz
cd $GDB
mkdir build
cd build
../configure  --with-python --prefix=/usr  --target=arm-none-eabi
make -j8