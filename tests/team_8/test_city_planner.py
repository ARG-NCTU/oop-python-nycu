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
    assert not cp.g.get_node('Denver').get_name() == 'Chicago'
    assert cp.g.get_node('Denver').get_name() == 'Denver'
    assert cp.g.get_node('Phoenix').get_name() == 'Phoenix'

    cp.get_shortest_path('Chicago', 'Boston')

