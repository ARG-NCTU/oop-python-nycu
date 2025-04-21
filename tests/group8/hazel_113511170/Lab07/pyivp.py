import tests.group8.hazel_113511170.Lab07.pyivp as pyivp    

print(pyivp.__doc__)

py_v1 = pyivp.XYPoint()
print(py_v1.get_spec(""))
py_v2 = pyivp.XYPoint(10, 15)
py_v2.shift_x(5)
print(py_v2.get_spec("")) 
py_v2.clear()
print(py_v2.get_spec("")) 
py_v2.set_vertex(y = 2, x = 1)
print(py_v2.get_vx(), py_v2.get_vy(), py_v2.get_vz())
