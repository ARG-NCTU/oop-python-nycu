# Python Compiler

```
$ cd ~/oop-python-nycu
$ source docker_run.sh
# cd ~/oop-python-nycu/sample-code/
```

## Run the OCW Examples via CPython Interpreter 

```
# time python3 fib.py
# time pythoo3 fib_fast.py
```

## Run the Nuitka Example

```
nuitka3 --follow-imports fib.py
# time ./fib.bin
```

## Run the Codon Example

```
# time codon run -release fib.py
```

See https://github.com/ARG-NCTU/codon

## Run the PyPy Example

```
# time pypy3 fib.py
```
