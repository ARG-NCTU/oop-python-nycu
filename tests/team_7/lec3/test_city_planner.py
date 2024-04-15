import pytest
from lecture3_graph import *

# This test case is for the CityPlanner class.
def test_city_planner():

    # Create an instance of CityPlanner
    cp = CityPlanner()
    # Create an instance of Digraph
    g = Digraph()

    # Add nodes to the graph for each city
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):  # Create 7 nodes
        g.add_node(Node(name))

    # Add edges between the nodes (cities)
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

    # Assign the graph to the CityPlanner instance
    cp.g = g

    # Assert that the node 'Boston' is correctly added to the graph
    assert cp.g.get_node('Boston').get_name() == 'Boston'

    # Test the get_shortest_path method of the CityPlanner class
    cp.get_shortest_path('Chicago', 'Boston')
