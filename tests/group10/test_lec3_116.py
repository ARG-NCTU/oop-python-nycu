import add_path
import pytest
from mit_ocw_data_science.lec3.lecture3_graph import Node, Edge, Digraph, CityPlanner

def test_city_planner():
    cp = CityPlanner()  # Create a CityPlanner instance
    g = Digraph()  # Create a Digraph instance

    # Create 6 nodes with generic names
    for name in ('Node1', 'Node2', 'Node3', 'Node4', 'Node5', 'Node6'):
        g.add_node(Node(name))

    # Add edges between the nodes
    g.add_edge(Edge(g.get_node('Node1'), g.get_node('Node2')))
    g.add_edge(Edge(g.get_node('Node1'), g.get_node('Node3')))
    g.add_edge(Edge(g.get_node('Node2'), g.get_node('Node1')))
    g.add_edge(Edge(g.get_node('Node2'), g.get_node('Node3')))
    g.add_edge(Edge(g.get_node('Node3'), g.get_node('Node4')))
    g.add_edge(Edge(g.get_node('Node4'), g.get_node('Node5')))
    g.add_edge(Edge(g.get_node('Node4'), g.get_node('Node6')))
    g.add_edge(Edge(g.get_node('Node5'), g.get_node('Node6')))
    g.add_edge(Edge(g.get_node('Node6'), g.get_node('Node1')))

    cp.g = g  # Set the graph to the CityPlanner instance

    # Test that the 'Node1' exists and has the correct name
    assert cp.g.get_node('Node1').get_name() == 'Node1'

    