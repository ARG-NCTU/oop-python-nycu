import random
import pytest
from lecture3_graph import *

def test():
    # Create nodes
    n1 = Node("A")
    n2 = Node("B")
    n3 = Node("C")
    n4 = Node("D")
    n5 = Node("E")
    
    # Create edges
    e1 = Edge(n1, n2)
    e2 = Edge(n2, n3)
    e3 = Edge(n3, n4)
    e4 = Edge(n4, n5)
    e5 = Edge(n1, n3)
    e6 = Edge(n2, n4)
    e7 = Edge(n2, n5)
    
    # Create graph
    g = Digraph()
    g.add_node(n1)
    g.add_node(n2)
    g.add_node(n3)
    g.add_node(n4)
    g.add_node(n5)
    g.add_edge(e1)
    g.add_edge(e2)
    g.add_edge(e3)
    g.add_edge(e4)
    g.add_edge(e5)
# This line of code adds an edge to the graph 'g'. The edge is represented by the variable 'e6'.
g.add_edge(e6)
    g.add_edge(e7)
    
    # Test shortest path
    planner = CityPlanner()
    planner.g = g
    planner.get_shortest_path("A", "E")

test()
