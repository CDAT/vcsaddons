if [[ `uname` == "Linux" ]]; then
    export LDSHARED="${LDSHARED} -shared -pthread"
else
    export LDSHARED="${LDSHARED} -bundle -undefined dynamic_lookup"
fi
export LDSHARED="${CC} ${LDSHARED}"
LDSHARED=$LDSHARED $PYTHON -m pip install . --no-deps -vv
