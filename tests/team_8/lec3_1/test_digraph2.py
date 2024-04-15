import pytest
from lecture3_graph import *

class TestDigraph:
    def setup_method(self):
        self.graph = Digraph()
        self.node1 = Node('A')
        self.node2 = Node('B')
        self.node3 = Node('C')
        self.node4 = Node('D')
        self.node5 = Node('E')
        self.edge1 = Edge(self.node1, self.node2)
        self.edge2 = Edge(self.node2, self.node3)
        self.edge3 = Edge(self.node2, self.node5)
        self.edge3 = Edge(self.node3, self.node4)
        self.edge4 = Edge(self.node4, self.node5)

    def test_add_node(self):
        self.graph.add_node(self.node1)
        assert self.graph.has_node(self.node1)
        assert not self.graph.has_node(self.node2)

    @pytest.mark.xfail(raises=ValueError)
    def test_add_edge(self):
        self.graph.add_node(self.node1)
        self.graph.add_node(self.node2)
        self.graph.add_edge(self.edge1)
        assert self.node2 in self.graph.children_of(self.node1)
        self.graph.add_edge(Edge(self.node2, Node('D')))
        self.graph.add_edge(Edge(Node('E'), Node('F')))

    @pytest.mark.xfail(raises=ValueError)
    def test_children_of(self):
        self.graph.add_node(self.node1)
        self.graph.add_node(self.node2)
        self.graph.add_edge(self.edge1)
        self.graph.add_edge(self.edge2)
        assert self.graph.children_of(self.node1) == [self.node2]
        assert self.graph.children_of(self.node2) == [self.node3]

    def test_has_node(self):
        self.graph.add_node(self.node1)
        assert self.graph.has_node(self.node1)
        assert not self.graph.has_node(Node('D'))

    def test_get_node(self):
        self.graph.add_node(self.node1)
        assert self.graph.get_node('A') == self.node1

def test_build_city_graph():
    
    g = Digraph()

    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):  # Create 7 nodes
        g.add_node(Node(name))

    g.add_edge(Edge(g.get_node('Boston'), g.get_node('Providence')))
    g.add_edge(Edge(g.get_node('Boston'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('Boston')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('New York'), g.get_node('Chicago')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Denver')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Los Angeles'), g.get_node('Boston')))

    print(g)
    assert len(g.edges) == 7 # 7 edges
    assert g.get_node('Boston').get_name() == 'Boston'
    assert g.get_node('Chicago').get_name() == 'Chicago'
    assert g.get_node('Los Angeles').get_name() == 'Los Angeles'
    assert g.children_of(g.get_node('Boston')) == [g.get_node('Providence'), g.get_node('New York')]
    assert g.children_of(g.get_node('Chicago')) == [g.get_node('Denver'), g.get_node('Phoenix')]
    assert g.children_of(g.get_node('Los Angeles')) == [g.get_node('Boston')]
    assert g.children_of(g.get_node('Phoenix')) == []
