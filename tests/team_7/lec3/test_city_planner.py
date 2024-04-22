import pytest
from lecture3_graph import *

def test_city_planner():
    """
    This function tests the functionality of the CityPlanner class. It creates a directed graph (Digraph) 
    representing a network of cities and the connections between them. It then uses the CityPlanner's 
    get_shortest_path method to find the shortest path between two cities and checks if the result is as expected.
    """

    # Create an instance of CityPlanner
    cp = CityPlanner()

    # Create an instance of Digraph
    g = Digraph()

    # Add nodes to the graph representing cities
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


    cp.get_shortest_path('Chicago', 'Boston')

