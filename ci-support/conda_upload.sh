#!/usr/bin/env bash
PKG_NAME=vcsaddons
USER=cdat
VERSION="2.12"
echo "Trying to upload conda"
if [ `uname` == "Linux" ]; then
    OS=linux-64
    echo "Linux OS"
    yum install -y wget git gcc
    wget --no-check https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh  -O miniconda2.sh 2> /dev/null
    bash miniconda2.sh -b -p ${HOME}/miniconda2
    export PATH="$HOME/miniconda2/bin:$PATH"
    echo $PATH
    conda config --set always_yes yes --set changeps1 no
    conda config --set anaconda_upload false --set ssl_verify false
    conda install -n root -q anaconda-client conda-build
    conda install -n root gcc future
    conda update -y -q conda
    BRANCH=${TRAVIS_BRANCH}
else
    echo "Mac OS"
    OS=osx-64
    BRANCH=${CIRCLE_BRANCH}
fi

mkdir ~/conda-bld
conda config --set anaconda_upload no
export CONDA_BLD_PATH=${HOME}/conda-bld
echo "Cloning recipes"
git clone git://github.com/UV-CDAT/conda-recipes
cd conda-recipes
python ./prep_for_build.py
conda build $PKG_NAME -c cdat/label/nightly -c conda-forge -c uvcdat --python=2.7
conda build $PKG_NAME -c cdat/label/nightly -c conda-forge -c uvcdat --python=3.6
anaconda -t $CONDA_UPLOAD_TOKEN upload -u $USER -l nightly $CONDA_BLD_PATH/$OS/$PKG_NAME-$VERSION.`date +%Y*`0.tar.bz2 --force
