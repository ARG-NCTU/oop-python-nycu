from setuptools import setup, Extension
import pybind11
ext_modules = [
    Extension(
        "example",
        ["example.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
    ),
]

setup(
    name="example",
    ext_modules=ext_modules,
)
