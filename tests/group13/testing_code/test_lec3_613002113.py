import pytest
import graph_structures as gs

def test_vertex():
    vertex = gs.Vertex("A")
    assert vertex.getName() == "A"
    assert str(vertex) == "A"

def test_connection():
    vertex1 = gs.Vertex("A")
    vertex2 = gs.Vertex("B")
    connection = gs.Connection(vertex1, vertex2)
    assert connection.getSource() == vertex1
    assert connection.getDestination() == vertex2
    assert str(connection) == "A->B"

