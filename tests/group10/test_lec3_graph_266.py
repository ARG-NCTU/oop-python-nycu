import pytest
import practice.lec3_graph as lec3

def test_node():
    node = lec3.Node("A")
    assert node.getName() == "A"
    assert str(node) == "A"
