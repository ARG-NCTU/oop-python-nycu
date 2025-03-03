# Python Compiler

```
$ cd ~/oop-python-nycu
$ source docker_run.sh
# cd ~/oop-python-nycu/sample-code/
```

The Python Compilers have been installed in docker.

Ask ChatGPT for more info.

## Run the OCW Examples via CPython Interpreter 

```
# time python3 fib.py
# time pythoo3 fib_fast.py
```

The Fib example is provided in MIT [OCW](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/resources/lecture2/)

## Run the Nuitka Example

If performance and the ability to generate standalone executables or shared libraries are more important, Nuitka may be a better choice.

```
# nuitka3 --follow-imports fib.py
# time ./fib.bin
```

## Run the Codon Example

Better support parallelism and multithreading via OpenMP and LLVM IR (Low-level, platform-independent, and typed assembly-like language)

```
# time codon run -release fib.py
```

See https://github.com/ARG-NCTU/codon

More [detail](https://thenewstack.io/mit-created-compiler-speeds-up-python-code/)

## Run the PyPy Example

If compatibility with a wide range of Python code and advanced tooling are important, PyPy may be a better choice.

```
# time pypy3 fib.py
```
