import pytest
from lecture3_graph import *


def test_city_planner():
    """
    This test function creates an instance of CityPlanner and a directed graph (Digraph).
    It then adds nodes representing cities to the graph and connects them with edges.
    The graph is then assigned to the CityPlanner instance for further operations.
    """

    cp = CityPlanner()  # Create an instance of CityPlanner
    g = Digraph()  # Create a directed graph

    # Add nodes representing cities to the graph
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):  # Create 7 nodes
        g.add_node(Node(name))

    # Connect the cities with edges
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

    cp.g = g  # Assign the graph to the CityPlanner instance

    # Assertions
    assert len(g.edges) == 7, "The graph should have 7 nodes."
    #assert len(g.edges) == 10, "The graph should have 10 edges."
    #assert g.get_node('Boston').get_edges() == [g.get_node('Providence'), g.get_node('New York')], "Boston should be connected to Providence and New York."
    #assert cp.g == g, "The graph should be correctly assigned to the CityPlanner instance."
    assert cp.g.get_node('Boston').get_name() == 'Boston'
    assert cp.g.get_node('Chicago').get_name() == 'Chicago'
    cp.get_shortest_path('Chicago', 'Boston')

