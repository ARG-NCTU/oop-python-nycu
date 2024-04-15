import pytest
from lecture3_graph import *


def test_city_planner():

    cp = CityPlanner()
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
    
    cp.g = g

    assert cp.g.get_node('Boston').get_name() == 'Boston'
    assert cp.g.get_node('Providence').get_name() == 'Providence'
    assert cp.g.get_node('New York').get_name() == 'New York'
    assert cp.g.get_node('Chicago').get_name() == 'Chicago'
    assert cp.g.get_node('Denver').get_name() == 'Denver'
    assert cp.g.get_node('Phoenix').get_name() == 'Phoenix'
    assert cp.g.get_node('Los Angeles').get_name() == 'Los Angeles'


    cp.get_shortest_path('Chicago', 'Boston')
    assert cp.get_shortest_path('Chicago', 'Boston') == 'Chicago -> New York -> Boston'
    assert cp.get_shortest_path('Boston', 'Phoenix') == 'Boston -> New York -> Chicago -> Phoenix'
    assert cp.get_shortest_path('Boston', 'Boston') == 'Boston'
    assert cp.get_shortest_path('Boston', 'Los Angeles') == 'Boston -> Los Angeles'
    assert cp.get_shortest_path('Los Angeles', 'Boston') == 'Los Angeles -> Boston'
    assert cp.get_shortest_path('Los Angeles', 'Los Angeles') == 'Los Angeles'
    assert cp.get_shortest_path('Los Angeles', 'New York') == 'Los Angeles -> Boston -> New York'
    assert cp.get_shortest_path('New York', 'Los Angeles') == 'New York -> Boston -> Los Angeles'
    assert cp.get_shortest_path('New York', 'Boston') == 'New York -> Boston'
    assert cp.get_shortest_path('New York', 'New York') == 'New York'

