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

class TestDigraph:
    def setup_method(self):
        self.graph = lec3.Digraph()
        self.node1 = lec3.Node('1')
        self.node2 = lec3.Node('2')
        self.node3 = lec3.Node('3')
        self.edge1 = lec3.Edge(self.node1, self.node2)
        self.edge2 = lec3.Edge(self.node2, self.node3)

    def test_add_node(self):
        self.graph.addNode(self.node1)
        assert self.graph.hasNode(self.node1)
        assert not self.graph.hasNode(self.node2)

    @pytest.mark.xfail(raises=ValueError)
    def test_add_edge(self):
        self.graph.addNode(self.node1)
        self.graph.addNode(self.node2)
        self.graph.addEdge(self.edge1)
        assert self.node2 in self.graph.childrenOf(self.node1)
        self.graph.addEdge(lec3.Edge(self.node2, lec3.Node('4')))
        self.graph.addEdge(lec3.Edge(lec3.Node('5'), lec3.Node('6')))

    def test_add_edge_without_xfail(self):
        self.graph.addNode(self.node1)
        self.graph.addNode(self.node2)
        self.graph.addEdge(self.edge1)
        assert self.node2 in self.graph.childrenOf(self.node1)
        with pytest.raises(ValueError):
            self.graph.addEdge(lec3.Edge(self.node2, lec3.Node('4')))
            self.graph.addEdge(lec3.Edge(lec3.Node('5'), lec3.Node('6')))
    
    @pytest.mark.xfail(raises=ValueError)
    def test_children_of(self):
        self.graph.addNode(self.node1)
        self.graph.addNode(self.node2)
        self.graph.addEdge(self.edge1)
        self.graph.addEdge(self.edge2)
        assert self.graph.childrenOf(self.node1) == [self.node2]
        assert self.graph.childrenOf(self.node2) == [self.node3]

    def test_children_of_without_xfail(self):
        self.graph.addNode(self.node1)
        self.graph.addNode(self.node2)
        self.graph.addEdge(self.edge1)
        with pytest.raises(ValueError):
            self.graph.addEdge(self.edge2)
    
    def test_has_node(self):
        self.graph.addNode(self.node1)
        assert self.graph.hasNode(self.node1)
        assert not self.graph.hasNode(lec3.Node('4'))

    def test_get_node(self):
        self.graph.addNode(self.node1)
        assert self.graph.getNode('1') == self.node1
    
def test_build_city_graph():
    g = lec3.Digraph()

    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):  # Create 7 nodes
        g.addNode(lec3.Node(name))

    g.addEdge(lec3.Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(lec3.Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(lec3.Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(lec3.Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(lec3.Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(lec3.Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(lec3.Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(lec3.Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(lec3.Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(lec3.Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    assert g.hasNode(g.getNode('Boston'))
    assert g.hasNode(g.getNode('Providence'))
    assert g.hasNode(g.getNode('New York'))
    assert g.hasNode(g.getNode('Chicago'))
    assert g.hasNode(g.getNode('Denver'))
    assert g.hasNode(g.getNode('Phoenix'))
    assert g.hasNode(g.getNode('Los Angeles'))