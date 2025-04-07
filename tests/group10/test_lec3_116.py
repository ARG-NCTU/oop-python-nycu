import add_path
import pytest
import mit_ocw_data_science.lec3.lecture3_graph as lec3

def test_node():
    """Test the Node class"""
    node = lec3.Node("TestNode")
    assert node.get_name() == "TestNode"
    assert str(node) == "TestNode"