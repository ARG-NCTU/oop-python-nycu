#include "../lib_geometry/SegList.h"

#include <pybind11/stl.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

void init_SegList(py::module &m) {
    
    py::class_<SegList>(m, "SegList")
    .def(py::init())
    .def("addVertex", 
            static_cast<void (SegList::*)(double, double)>(&SegList::addVertex),
            "add vertex with x, y")
    .def("addVertex", 
            static_cast<void (SegList::*)(Vertex)>(&SegList::addVertex),
            "add vertex with a vertex")
    //.def("setRandom", &SegList::setRandom)
    .def("getSpec", &SegList::getSpec);
}
