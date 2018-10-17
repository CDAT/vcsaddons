export CFLAGS="-Wall -g -m64 -pipe -O2  -fPIC"
export CXXLAGS="${CFLAGS}"
export CPPFLAGS="-I${PREFIX}/include"
export LDFLAGS="-L${PREFIX}/lib"
if [[ `uname` == "Linux" ]]; then
    export LDSHARED="-shared -pthread"
else
    export LDSHARED="-bundle -undefined dynamic_lookup"
fi
env LDSHARED="${CC} ${LDSHARED}" python setup.py install
