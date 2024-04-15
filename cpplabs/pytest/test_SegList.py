import pytest
from cpplabs import Vertex
from cpplabs import SegList


def test_addVertex():
    # Create an instance of SegList
    seg_list = SegList()

    # Add some vertices to the SegList
    seg_list.addVertex(1.0, 2.0)
    seg_list.addVertex(3.0, 4.0)
    seg_list.addVertex(Vertex(5, 6))

    # Check that the vertices were added correctly
    assert seg_list.getSpec() == "x=1,y=2,x=3,y=4,x=5,y=6"

    # Test adding a vertex using a Vertex object
    vertex = Vertex(7, 8)
    seg_list.addVertex(vertex)
    assert seg_list.getSpec() == "x=1,y=2,x=3,y=4,x=5,y=6,x=7,y=8"

def test_getSpec():
    # Check that the getSpec method returns the correct string for multiple vertices
    seg_list = SegList()
    seg_list.addVertex(1.0, 2.0)
    seg_list.addVertex(3.0, 4.0)
    assert seg_list.getSpec() == "x=1,y=2,x=3,y=4"

    # Check that the getSpec method returns the correct string for a single vertex
    seg_list = SegList()
    seg_list.addVertex(5.0, 6.0)
    assert seg_list.getSpec() == "x=5,y=6"

    # Check that the getSpec method returns an empty string for an empty SegList
    seg_list = SegList()
    assert seg_list.getSpec() == ""
    
    # Check that the getSpec method still works after adding a vertex
    seg_list.addVertex(1.0, 2.0)
    assert seg_list.getSpec() == "x=1,y=2"