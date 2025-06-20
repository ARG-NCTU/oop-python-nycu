import pytest
import lec3_strings_algos as lec
import math

def test_vertex():
    vertex = gs.Vertex("A")
    assert vertex.getName() == "A"
    assert str(vertex) == "A"

def test_connection():
    vertex1 = gs.Vertex("A")
    vertex2 = gs.Vertex("B")
    connection = gs.Connection(vertex1, vertex2)
    assert connection.getSource() == vertex1
    assert connection.getDestination() == vertex2
    assert str(connection) == "A->B"

class TestDirectedGraph:
    def setup_method(self):
        self.directed_graph = gs.DirectedGraph()
        self.vertex1 = gs.Vertex('1')
        self.vertex2 = gs.Vertex('2')
        self.vertex3 = gs.Vertex('3')
        self.connection1 = gs.Connection(self.vertex1, self.vertex2)
        self.connection2 = gs.Connection(self.vertex2, self.vertex3)

    def test_insert_vertex(self):
        self.directed_graph.addVertex(self.vertex1)
        assert self.directed_graph.hasVertex(self.vertex1)
        assert not self.directed_graph.hasVertex(self.vertex2)

    @pytest.mark.xfail(raises=ValueError)
    def test_insert_connection(self):
        self.directed_graph.addVertex(self.vertex1)
        self.directed_graph.addVertex(self.vertex2)
        self.directed_graph.addConnection(self.connection1)
        assert self.vertex2 in self.directed_graph.childrenOf(self.vertex1)
        self.directed_graph.addConnection(gs.Connection(self.vertex2, gs.Vertex('4')))
        self.directed_graph.addConnection(gs.Connection(gs.Vertex('5'), gs.Vertex('6')))

    def test_insert_connection_without_xfail(self):
        self.directed_graph.addVertex(self.vertex1)
        self.directed_graph.addVertex(self.vertex2)
        self.directed_graph.addConnection(self.connection1)
        assert self.vertex2 in self.directed_graph.childrenOf(self.vertex1)
        with pytest.raises(ValueError):
            self.directed_graph.addConnection(gs.Connection(self.vertex2, gs.Vertex('4')))
            self.directed_graph.addConnection(gs.Connection(gs.Vertex('5'), gs.Vertex('6')))
    
    @pytest.mark.xfail(raises=ValueError)
    def test_get_children_of(self):
        self.directed_graph.addVertex(self.vertex1)
        self.directed_graph.addVertex(self.vertex2)
        self.directed_graph.addConnection(self.connection1)
        self.directed_graph.addConnection(self.connection2)
        assert self.directed_graph.childrenOf(self.vertex1) == [self.vertex2]
        assert self.directed_graph.childrenOf(self.vertex2) == [self.vertex3]

    def test_get_children_of_without_xfail(self):
        self.directed_graph.addVertex(self.vertex1)
        self.directed_graph.addVertex(self.vertex2)
        self.directed_graph.addConnection(self.connection1)
        with pytest.raises(ValueError):
            self.directed_graph.addConnection(self.connection2)
    
    def test_check_vertex_exists(self):
        self.directed_graph.addVertex(self.vertex1)
        assert self.directed_graph.hasVertex(self.vertex1)
        assert not self.directed_graph.hasVertex(gs.Vertex('4'))

    def test_retrieve_vertex(self):
        self.directed_graph.addVertex(self.vertex1)
        assert self.directed_graph.getVertex('1') == self.vertex1
    
def test_construct_location_graph():
    network = gs.DirectedGraph()
    for location in ('Boston', 'Providence', 'New York', 'Chicago',
                     'Denver', 'Phoenix', 'Los Angeles'):
        network.addVertex(gs.Vertex(location))
    network.addConnection(gs.Connection(network.getVertex('Boston'), network.getVertex('Providence')))
    network.addConnection(gs.Connection(network.getVertex('Boston'), network.getVertex('New York')))
    network.addConnection(gs.Connection(network.getVertex('Providence'), network.getVertex('Boston')))
    network.addConnection(gs.Connection(network.getVertex('Providence'), network.getVertex('New York')))
    network.addConnection(gs.Connection(network.getVertex('New York'), network.getVertex('Chicago')))
    network.addConnection(gs.Connection(network.getVertex('Chicago'), network.getVertex('Denver')))
    network.addConnection(gs.Connection(network.getVertex('Chicago'), network.getVertex('Phoenix')))
    network.addConnection(gs.Connection(network.getVertex('Denver'), network.getVertex('Phoenix')))
    network.addConnection(gs.Connection(network.getVertex('Denver'), network.getVertex('New York')))
    network.addConnection(gs.Connection(network.getVertex('Los Angeles'), network.getVertex('Boston')))
    assert network.hasVertex(network.getVertex('Boston'))
    assert network.hasVertex(network.getVertex('Providence'))
    assert network.hasVertex(network.getVertex('New York'))
    assert network.hasVertex(network.getVertex('Chicago'))
    assert network.hasVertex(network.getVertex('Denver'))
    assert network.hasVertex(network.getVertex('Phoenix'))
    assert network.hasVertex(network.getVertex('Los Angeles'))