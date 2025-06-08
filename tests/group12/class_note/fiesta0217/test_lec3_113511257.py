#import add_path
#import mit_ocw_data_science.lec3.lecture3_graph as lec3
import pytest

class Testnode_and_edge:
    def test_node(self):
        node = lec3.Node('Node1')
        assert node.get_name() == 'Node1'
        assert str(node) == 'Node1'

    def test_edge(self):
        node1 = lec3.Node('Node1')
        node2 = lec3.Node('Node2')
        edge = lec3.Edge(node1, node2)
        assert edge.get_source() == node1         
        assert edge.get_destination() == node2    
        assert str(edge) == 'Node1->Node2'        

class Testdigraph:
    def test_digraph(self):
        g = lec3.Digraph()
        node1 = lec3.Node('Node1')
        node2 = lec3.Node('Node2')
        g.add_node(node1)
        g.add_node(node2)
        assert g.get_node('Node1') == node1
        assert g.get_node('Node2') == node2

    def test_add_edge(self):
        g = lec3.Digraph()
        node1 = lec3.Node('Node1')
        node2 = lec3.Node('Node2')
        g.add_node(node1)
        g.add_node(node2)
        edge = lec3.Edge(node1, node2)
        g.add_edge(edge)
        assert node2 in g.children_of(node1)       
