import add_path 
import pytest
import lec3 as lec3
import random
import copy

def test_node_and_edge():
    a = lec3.Node("A")
    b = lec3.Node("B")
    edge = lec3.Edge(a, b)
    assert a.get_name() == "A"
    assert b.get_name() == "B"
    assert edge.get_source() == a
    assert edge.get_destination() == b
    assert str(edge) == "A->B"

def test_digraph_basic():
    a, b, c = lec3.Node("A"), lec3.Node("B"), lec3.Node("C")
    g = lec3.Digraph()
    for node in [a, b, c]:
        g.add_node(node)
    g.add_edge(lec3.Edge(a, b))
    g.add_edge(lec3.Edge(b, c))
    assert g.has_node(a)
    assert g.children_of(a) == [b]
    assert g.children_of(b) == [c]
    assert g.children_of(c) == []

def test_graph_is_bidirectional():
    a, b = lec3.Node("A"), lec3.Node("B")
    g = lec3.Graph()
    g.add_node(a)
    g.add_node(b)
    g.add_edge(lec3.Edge(a, b))
    # Check bidirectional
    assert b in g.children_of(a)
    assert a in g.children_of(b)

def test_get_node_and_exceptions():
    a = lec3.Node("A")
    g = lec3.Digraph()
    g.add_node(a)
    assert g.get_node("A") == a
    with pytest.raises(NameError):
        g.get_node("Z")  # 不存在的 node name

def test_cityplanner_dfs():
    a, b, c = lec3.Node("A"), lec3.Node("B"), lec3.Node("C")
    g = lec3.Digraph()
    for node in [a, b, c]:
        g.add_node(node)
    g.add_edge(lec3.Edge(a, b))
    g.add_edge(lec3.Edge(b, c))

    planner = lec3.CityPlanner()
    path = planner.shortest_path_dfs(g, a, c)
    assert [n.get_name() for n in path] == ["A", "B", "C"]

def test_cityplanner_bfs():
    a, b, c = lec3.Node("A"), lec3.Node("B"), lec3.Node("C")
    g = lec3.Digraph()
    for node in [a, b, c]:
        g.add_node(node)
    g.add_edge(lec3.Edge(a, b))
    g.add_edge(lec3.Edge(b, c))

    planner = lec3.CityPlanner()
    path = planner.shortest_path_bfs(g, a, c)
    assert [n.get_name() for n in path] == ["A", "B", "C"]

def test_cityplanner_no_path():
    a, b, c = lec3.Node("A"), lec3.Node("B"), lec3.Node("C")
    g = lec3.Digraph()
    for node in [a, b, c]:
        g.add_node(node)
    g.add_edge(lec3.Edge(a, b))  # no path from a to c

    planner = lec3.CityPlanner()
    assert planner.shortest_path_dfs(g, a, c) is None
    assert planner.shortest_path_bfs(g, a, c) is None

def test_print_path():
    path = [lec3.Node("X"), lec3.Node("Y"), lec3.Node("Z")]
    planner = lec3.CityPlanner()
    assert planner.print_path(path) == "X->Y->Z"
