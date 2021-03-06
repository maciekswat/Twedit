#!/bin/sh

# echo " "
# echo " dollar-zero AKA the first argument to this .command script is: "
# echo $0
# echo " "
export PYTHON_MINOR_VERSION=7

cd "${0%/*}"


export PREFIX_CC3D=$(pwd)

current_directory=$(pwd)

cd $PREFIX_CC3D

echo "====> twedit++ working directory: $PREFIX_CC3D"

# export DYLD_LIBRARY_PATH=${PREFIX_CC3D}/lib
# export DYLD_LIBRARY_PATH=${PREFIX_CC3D}/lib/python:$DYLD_LIBRARY_PATH

# export SWIG_LIB_INSTALL_DIR=${PREFIX_CC3D}/lib/python

# export PYTHON_MODULE_PATH=${PREFIX_CC3D}/pythonSetupScripts


# export DYLD_LIBRARY_PATH=${PREFIX_CC3D}/Deps:${PREFIX_CC3D}/Deps/QtDeps:${PREFIX_CC3D}/player/vtk:${PREFIX_CC3D}/player/VTKLibs:$DYLD_LIBRARY_PATH
# echo " ====> DYLD_LIBRARY_PATH: $DYLD_LIBRARY_PATH"

# export PYTHONPATH=${PREFIX_CC3D}/player:$PYTHONPATH
# echo "====> PYTHONPATH directory: $PYTHONPATH"




# # # echo "---- ---- ---- ---- ---- ---- ---- ---- "
# # # echo " setting the PYTHONLIB_SYSTEM shell variable as used by CompuCell3D: "
export PYTHONPATH=/Users/m/miniconda/envs/pyqt5/lib/python2.7/site-packages:$PYTHONPATH
export PYTHONLIB_SYSTEM=/System/Library/Frameworks/Python.framework/Versions/2.${PYTHON_MINOR_VERSION}
ln -s /System/Library/Frameworks/Python.framework/Versions/2.${PYTHON_MINOR_VERSION}/Resources/Python.app/Contents/MacOS/Python ${PREFIX_CC3D}/Twedit++
export PYTHON_EXEC=${PREFIX_CC3D}/Twedit++

# export PYTHON_EXEC=python2.${PYTHON_MINOR_VERSION}
echo " ====> PYTHONLIB_SYSTEM: $PYTHONLIB_SYSTEM"


echo "---- ---- ---- ---- ---- ---- ---- ---- "
echo " setting the PATH shell variable as used by CompuCell3D: "
# avoid any previously user-defined DYLD_LIBRARY_PATH values:
# export PATH=${PREFIX_CC3D}/LIBRARYDEPS/sipDeps:${PYTHONLIB_26_SYSTEM}/bin:${PYTHONLIB_26_SYSTEM}:${PREFIX_CC3D}/LIBRARYDEPS:${PREFIX_CC3D}/LIBRARYDEPS/LIBRARY-PYTHON-2.5/Extras/lib/python/wx/lib:$PATH
# export PATH=${PYTHONLIB_26_SYSTEM}/bin:${PYTHONLIB_26_SYSTEM}
# # # export PATH=${PYTHONLIB_SYSTEM}/bin:$PATH
echo " ====> PATH: $PATH"
# echo "---- ---- ---- ---- ---- ---- ---- ---- "
# echo " env is here:"
# echo "---- ---- ---- ---- ---- ---- ---- ---- "
# /usr/bin/env | /usr/bin/sort



echo "---- ---- ---- ---- ---- ---- ---- ---- "
echo 'Hello World. Python --version says:'
echo "---- ---- ---- ---- ---- ---- ---- ---- "
${PYTHON_EXEC} --version



export TWEDIT_MAJOR_VERSION=0
export TWEDIT_MINOR_VERSION=9
export TWEDIT_BUILD_VERSION=0


${PYTHON_EXEC} ${PREFIX_CC3D}/twedit_plus_plus.py $*


cd ${current_directory}
