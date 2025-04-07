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

def test_digraph():
    graph = lec3.Digraph()
    node1 = lec3.Node("A")
    node2 = lec3.Node("B")
    node3 = lec3.Node("C")
    
    graph.addNode(node1)
    graph.addNode(node2)
    graph.addNode(node3)
    
    assert graph.hasNode(node1) == True
    assert graph.hasNode(lec3.Node("D")) == False
    
    edge1 = lec3.Edge(node1, node2)
    edge2 = lec3.Edge(node2, node3)
    
    graph.addEdge(edge1)
    graph.addEdge(edge2)
    
    assert graph.childrenOf(node1) == [node2]
    assert graph.childrenOf(node2) == [node3]
    
    with pytest.raises(ValueError):
        graph.addEdge(edge1)  # Adding duplicate edge should raise ValueError


