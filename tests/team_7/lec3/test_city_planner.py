from lecture3_graph import CityPlanner
from lecture3_graph import Digraph

def test_city_planner():
    """
    This function tests the functionality of the CityPlanner class.
    It creates an instance of CityPlanner and a directed graph (Digraph).
    It then adds several nodes, each representing a city, to the graph.
    """
    cp = CityPlanner()  # Create an instance of CityPlanner
    g = Digraph()  # Create an instance of Digraph

    # Add nodes to the graph
    # Each node represents a city
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):
        g.add_node(Node(name))  # Add a node with the city name to the graph
    # Add edges to the graph
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

    # Test the name retrieval of a node
    assert cp.g.get_node('Boston').get_name() == 'Boston'

    # Test the shortest path functionality
    shortest_path = cp.get_shortest_path('Chicago', 'Boston')
    expected_path = ['Chicago', 'New York', 'Boston']
    assert shortest_path == expected_path

