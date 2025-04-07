import pytest
from lecture3_graph import *

class TestDigraph:
    def setup_method(self):
        self.digraph = Digraph()
        self.node1 = Node('1')
        self.node2 = Node('2')
        self.node3 = Node('3')
        self.edge1 = Edge(self.node1, self.node2)
        self.edge2 = Edge(self.node2, self.node3)

    def test_add_node(self):
        self.digraph.add_node(self.node1)
        assert self.graph.has_node(self.node1)
        assert not self.graph.has_node(self.node2)
        self.digraph.add_node(self.node2)
        assert self.graph.has_node(self.node2)
