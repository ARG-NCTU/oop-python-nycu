# oop-python-nycu-2022

This repo is used for OOP class 2023 in NYCU.

## Docker

We have a Dockerfile with minimum installations of the packages we will use.
* Nginx + Flask
* vim-python-ide
* pybind11

```
source docker_run.sh
```

## Submodule

We have a submodule using pybind11 to use C++ classes in Python.

Clone the repo with submodules
```
git clone --recursive git@github.com:ARG-NCTU/oop-python-nycu.git
```
