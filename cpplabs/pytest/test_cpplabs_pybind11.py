import cpplabs

print(cpplabs.__doc__)

print("== Test package and local function. ==")
result = cpplabs.python_test_plus(1, 2)
print("Python result x plus y is: ", result)
assert result == 3

print("== Test VertexSimple ==")
py_vertex_simple = cpplabs.VertexSimple()
py_vertex_simple.setRandom(0, 10)
print(py_vertex_simple.getSpec())

print("== Test Vertex ==")
py_vertex = cpplabs.Vertex()
print(py_vertex.getSpec())
py_v2 = cpplabs.Vertex(5, 10)
print(py_v2.getSpec())
py_v3 = cpplabs.Vertex()
py_v3.setRandom(10, 20)
print(py_v3.getSpec())
py_v4 = cpplabs.Vertex()
py_v4.setRandom(10, 20, 20, 30)
print(py_v4.getSpec())
py_v5 = cpplabs.Vertex()
py_v5.setXY(10, 20)
print("getX: {}, getY: {}".format(py_v5.getX(), py_v5.getY()))

print("== Test SegList ==")
py_seglist = cpplabs.SegList()
py_seglist.addVertex(3.0, 5.0)
py_seglist.addVertex(6.0, 9.0)
py_seglist.addVertex(py_v2)
py_seglist.addVertex(py_v3)
py_seglist.addVertex(py_v4)
py_seglist.addVertex(py_v5)
print(py_seglist.getSpec())

