import pytest
import practice.lec3_graph as lec3

def test_node():
    node = lec3.Node("A")
    assert node.getName() == "A"
    assert str(node) == "A"

def test_edge():
    node1 = lec3.Node("A")
    node2 = lec3.Node("B")
    edge = lec3.Edge(node1, node2)
    assert edge.getSource() == node1
    assert edge.getDestination() == node2
    assert str(edge) == "A->B"

