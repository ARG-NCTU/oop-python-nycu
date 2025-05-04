import pytest
#from lecture3_graph import *

"""utils"""

class Node:
    """Represents a node in a graph."""
    def __init__(self, name):
        """Assumes name is a string."""
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Edge:
    """Represents a directed edge in a graph."""
    def __init__(self, src, dest):
        """Assumes src and dest are nodes."""
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return self.src.get_name() + '->' + self.dest.get_name()


class Digraph:
    """Edges is a dict mapping each node to a list of its children."""
    def __init__(self):
        self.edges = {}

    def add_node(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.edges

    def get_node(self, name):
        for n in self.edges:
            if n.get_name() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.get_name() + '->' + dest.get_name() + '\n'
        return result[:-1]  # Omit final newline
    
"""The end of utils"""

"""Testing"""

class TestDigraph:
    def setup_method(self):
        self.graph = Digraph() #empty graph
        self.node1 = Node('1')
        self.node2 = Node('2')
        self.node3 = Node('3')
        self.node4 = Node('4')
        self.edge1 = Edge(self.node1, self.node2)
        self.edge2 = Edge(self.node2, self.node3)
        self.edge3 = Edge(self.node3, self.node4)
        self.edge4 = Edge(self.node4, self.node1)

    def test_add_node(self):
        self.graph.add_node(self.node1)
        assert self.graph.has_node(self.node1)
        assert not self.graph.has_node(self.node2)

    @pytest.mark.xfail(raises=ValueError)
    def test_add_edge(self):
        self.graph.add_node(self.node1)
        self.graph.add_node(self.node2)
        self.graph.add_node(self.node4)
        self.graph.add_edge(self.edge4)
        self.graph.add_edge(self.edge1) # pass
        assert self.node2 in self.graph.children_of(self.node1)
        assert self.node1 in self.graph.children_of(self.node4)
        self.graph.add_edge(Edge(self.node2, self.node4))#pass
        self.graph.add_edge(Edge(Node('5'), Node('6')))#fail

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
        assert not self.graph.has_node(Node('3'))
        assert not self.graph.has_node(Node('2'))

    @pytest.mark.xfail(raises=NameError)
    def test_get_node(self):
        self.graph.add_node(self.node1)
        assert self.graph.get_node('1') == self.node1
        self.graph.get_node('2')

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
    assert len(g.edges) == 7 
    assert g.get_node('Boston').get_name() == 'Boston'

test_build_city_graph()
 