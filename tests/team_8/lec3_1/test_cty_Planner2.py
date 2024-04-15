import pytest
from lecture3_graph import *

def test_city_planner():

    planner = CityPlanner()
    gra = Digraph()

    #crate 6 nodes
    for name in ("A", "B", "C", "D", "E", "F"):
        gra.add_node(Node(name))
    #add edges
    gra.add_edge(Edge(gra.get_node("A"), gra.get_node("B")))
    gra.add_edge(Edge(gra.get_node("A"), gra.get_node("C")))
    gra.add_edge(Edge(gra.get_node("B"), gra.get_node("D")))
    gra.add_edge(Edge(gra.get_node("D"), gra.get_node("E")))
    gra.add_edge(Edge(gra.get_node("E"), gra.get_node("F")))
    gra.add_edge(Edge(gra.get_node("F"), gra.get_node("D")))

    planner.g = gra
    assert planner.g.get_node("A").get_name() == "A"
    assert planner.g.get_node("B").get_name() == "B"
    
    planner.get_shortest_path("A", "F")
