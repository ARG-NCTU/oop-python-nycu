import add_path
import mit_ocw_data_science.lec3.lecture3_graph as lec3
import pytest

class TestDigraph:
    def setup_method(self):
        self.graph = lec3.Digraph()
        self.node1 = lec3.Node('1')
        self.node2 = lec3.Node('2')
        self.node3 = lec3.Node('3')
        self.node4 = lec3.Node('4')
        self.node5 = lec3.Node('5')
        self.edge1 = lec3.Edge(self.node1, self.node2)
        self.edge2 = lec3.Edge(self.node2, self.node3)
        self.edge3 = lec3.Edge(self.node3, self.node4)
        self.edge4 = lec3.Edge(self.node4, self.node5)

    def test_add_node(self):
        self.graph.add_node(self.node1)
        assert self.graph.has_node(self.node1)
        assert not self.graph.has_node(self.node2)
        self.graph.add_node(self.node2)
        assert self.graph.has_node(self.node2)
        self.graph.add_node(self.node3)
        assert self.graph.has_node(self.node3)

    def test_add_edge(self):
        self.graph.add_node(self.node1)
        self.graph.add_node(self.node2)
        self.graph.add_edge(self.edge1)
        assert self.node2 in self.graph.children_of(self.node1)
        self.graph.add_node(self.node3)
        self.graph.add_edge(self.edge2)
        assert self.node3 in self.graph.children_of(self.node2)
        assert self.node1 not in self.graph.children_of(self.node2)

    def test_add_node(self):
        self.graph.add_node(self.node2)
        assert self.graph.has_node(self.node2)
        assert not self.graph.has_node(self.node3)
        self.graph.add_node(self.node3)
        assert self.graph.has_node(self.node3)

    def test_get_node(self):
        self.graph.add_node(self.node1)
        assert self.graph.get_node('1') == self.node1
        self.graph.add_node(self.node2)
        assert self.graph.get_node('2') == self.node2
        self.graph.add_node(self.node3)
        assert self.graph.get_node('3') == self.node3

    def test_add_edge(self):
        self.graph.add_node(self.node1)
        self.graph.add_node(self.node2)
        self.graph.add_edge(self.edge1)
        assert self.node2 in self.graph.children_of(self.node1)
        self.graph.add_node(self.node3)
        self.graph.add_edge(self.edge2)
        assert self.node3 in self.graph.children_of(self.node2)
        assert self.node1 not in self.graph.children_of(self.node2)
