if [[ `uname` == "Linux" ]]; then
    export LDSHARED="${LDSHARED} -shared -pthread"
else
    export LDSHARED="${LDSHARED} -bundle -undefined dynamic_lookup"
fi
env LDSHARED="${CC} ${LDSHARED}" python setup.py install
