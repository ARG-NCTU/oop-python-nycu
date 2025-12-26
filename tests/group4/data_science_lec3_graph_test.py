import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
import numpy as np
from src.mit_ocw_data_science.lec3.lecture3_graph import Node, Edge, Digraph, Graph

def test_node():
    n = Node('A')
    assert n.get_name() == 'A'
    assert str(n) == 'A'
    n2 = Node('B')
    assert n != n2
    n3 = Node('A')
    #assert n == n3

def test_edge():
    n1 = Node('A')
    n2 = Node('B')
    e = Edge(n1, n2)
    assert e.get_source() == n1
    assert e.get_destination() == n2
    assert str(e) == 'A->B'

def test_digraph():
    g = Digraph()
    n1 = Node('A')
    n2 = Node('B')
    g.add_node(n1)
    g.add_node(n2)
    e = Edge(n1, n2)
    g.add_edge(e)
    assert g.has_node(n1)
    assert g.has_node(n2)
    assert g.children_of(n1) == [n2]
    assert g.children_of(n2) == []
    assert g.get_node('A') == n1
    assert g.get_node('B') == n2
    assert str(g) == 'A->B'

def test_graph():
    g = Graph()
    n1 = Node('A')
    n2 = Node('B')
    g.add_node(n1)
    g.add_node(n2)
    e = Edge(n1, n2)
    g.add_edge(e)
    assert g.children_of(n1) == [n2]
    assert g.children_of(n2) == [n1]
    assert str(g) == 'A->B\nB->A'
