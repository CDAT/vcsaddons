if [[ `uname` == "Linux" ]]; then
    export LDSHARED="${LDSHARED} -shared -pthread"
else
    export LDSHARED="${LDSHARED} -bundle -undefined dynamic_lookup"
fi
python setup.py install
