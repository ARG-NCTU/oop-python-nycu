#include <iostream>
#include <pybind11/pybind11.h>

namespace py = pybind11;

void init_VertexSimple(py::module &);
void init_Vertex(py::module &);
void init_SegList(py::module &);

namespace ivp {

int cpp_test_plus(int x, int y){
    int result = x + y;
    std::cout << "C++ result x plus y is: " << result << '\n';
    return result;
}

PYBIND11_MODULE(cpplabs, m) {
    // Optional docstring
    m.doc() = "pybind11 for cpp labs";
 
    m.def("python_test_plus", &cpp_test_plus, "plus x and y");
    
    init_VertexSimple(m);
    init_Vertex(m);
    init_SegList(m);
}
}
