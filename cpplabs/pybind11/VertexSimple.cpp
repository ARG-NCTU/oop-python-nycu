#include "../lib_geometry/VertexSimple.h"

#include <pybind11/stl.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

void init_VertexSimple(py::module &m) {
    
    py::class_<VertexSimple>(m, "VertexSimple")
    .def(py::init())
    .def("setRandom", &VertexSimple::setRandom)
    .def("getSpec", &VertexSimple::getSpec);
}
