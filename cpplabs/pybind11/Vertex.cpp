#include "../lib_geometry/Vertex.h"

#include <pybind11/stl.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

void init_Vertex(py::module &m) {
    
    py::class_<Vertex>(m, "Vertex")
    .def(py::init())
    .def(py::init<int, int>())
    .def("setXY", &Vertex::setXY)
    .def("getX", &Vertex::getX)
    .def("getY", &Vertex::getY)
    .def("setRandom", 
            static_cast<void (Vertex::*)(int, int)>(&Vertex::setRandom), 
            "set max/min")
    .def("setRandom", 
            static_cast<void (Vertex::*)(int, int, int, int)>(&Vertex::setRandom), 
            "set x, y max/min")
    .def("getSpec", &Vertex::getSpec);
}
