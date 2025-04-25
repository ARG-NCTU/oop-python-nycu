import pytest
from lecture3_graph import *
from city_planner import * 

# Fixture 定義城市圖，供多個測試重用
@pytest.fixture
def city_graph():
    g = Digraph()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):
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
    return g

# 測試 lecture3_graph.py 的額外功能
def test_shortest_path_dfs(city_graph):
    sp = shortestPath(city_graph, city_graph.get_node('Chicago'), city_graph.get_node('Boston'))
    assert printPath(sp) == 'Chicago->Denver->New York->Boston'
    sp = shortestPath(city_graph, city_graph.get_node('Boston'), city_graph.get_node('Phoenix'))
    assert sp is None  # No path exists

def test_shortest_path_bfs(city_graph):
    sp = BFS(city_graph, city_graph.get_node('Chicago'), city_graph.get_node('Phoenix'), False)
    assert printPath(sp) == 'Chicago->Phoenix'
    sp = BFS(city_graph, city_graph.get_node('Boston'), city_graph.get_node('Phoenix'), False)
    assert sp is None  # No path exists

def test_empty_graph():
    g = Digraph()
    sp = shortestPath(g, Node('A'), Node('B'))
    assert sp is None  # Empty graph, no path

def test_single_node():
    g = Digraph()
    n = Node('A')
    g.add_node(n)
    sp = shortestPath(g, n, n)
    assert len(sp) == 1 and sp[0] == n

def test_graph_undirected():
    g = Graph()
    n1, n2 = Node('A'), Node('B')
    g.add_node(n1)
    g.add_node(n2)
    g.add_edge(Edge(n1, n2))
    assert n2 in g.children_of(n1)
    assert n1 in g.children_of(n2)  # Undirected edge

def test_print_path():
    path = [Node('A'), Node('B'), Node('C')]
    assert printPath(path) == 'A->B->C'
    assert printPath([Node('X')]) == 'X'

# 測試 CityPlanner 的額外功能
def test_city_planner_shortest_path_dfs(city_graph):
    cp = CityPlanner()
    cp.g = city_graph
    sp = cp.shortest_path_dfs(city_graph, city_graph.get_node('Chicago'), 
                             city_graph.get_node('Boston'))
    assert cp.print_path(sp) == 'Chicago->Denver->New York->Boston'
    sp = cp.shortest_path_dfs(city_graph, city_graph.get_node('Boston'), 
                             city_graph.get_node('Phoenix'))
    assert sp is None

def test_city_planner_shortest_path_bfs(city_graph):
    cp = CityPlanner()
    cp.g = city_graph
    sp = cp.shortest_path_bfs(city_graph, city_graph.get_node('Chicago'), 
                             city_graph.get_node('Phoenix'))
    assert cp.print_path(sp) == 'Chicago->Phoenix'
    sp = cp.shortest_path_bfs(city_graph, city_graph.get_node('Boston'), 
                             city_graph.get_node('Phoenix'))
    assert sp is None

def test_city_planner_get_shortest_path(capsys, city_graph):
    cp = CityPlanner()
    cp.g = city_graph
    cp.get_shortest_path('Chicago', 'Boston')
    captured = capsys.readouterr()
    assert 'Chicago->Denver->New York->Boston' in captured.out
    cp.get_shortest_path('Boston', 'Phoenix')
    captured = capsys.readouterr()
    assert 'There is no path from Boston to Phoenix' in captured.out

def test_city_planner_empty_graph():
    cp = CityPlanner()
    cp.g = Digraph()
    sp = cp.shortest_path_dfs(cp.g, Node('A'), Node('B'))
    assert sp is None

def test_city_planner_print_path():
    cp = CityPlanner()
    path = [Node('A'), Node('B'), Node('C')]
    assert cp.print_path(path) == 'A->B->C'
    assert cp.print_path([Node('X')]) == 'X'