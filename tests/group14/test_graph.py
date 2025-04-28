import add_path
import pytest
import mit_ocw_data_science.lec3.lecture3_graph as lec3
import random

def test_city_planner():

    cp = lec3.CityPlanner()
    g = lec3.Digraph()

    for name in ('Taipei', 'Kaohsiung', 'Taichung', 'Tainan',
                 'Hsinchu', 'Keelung', 'Yilan'):  # Create 7 nodes
        g.add_node(lec3.Node(name))

    g.add_edge(lec3.Edge(g.get_node('Taipei'), g.get_node('Kaohsiung')))
    g.add_edge(lec3.Edge(g.get_node('Taipei'), g.get_node('Taichung')))
    g.add_edge(lec3.Edge(g.get_node('Kaohsiung'), g.get_node('Taipei')))
    g.add_edge(lec3.Edge(g.get_node('Kaohsiung'), g.get_node('Taichung')))
    g.add_edge(lec3.Edge(g.get_node('Taichung'), g.get_node('Tainan')))
    g.add_edge(lec3.Edge(g.get_node('Tainan'), g.get_node('Hsinchu')))
    g.add_edge(lec3.Edge(g.get_node('Tainan'), g.get_node('Keelung')))
    g.add_edge(lec3.Edge(g.get_node('Hsinchu'), g.get_node('Keelung')))
    g.add_edge(lec3.Edge(g.get_node('Hsinchu'), g.get_node('Taichung')))
    g.add_edge(lec3.Edge(g.get_node('Yilan'), g.get_node('Taipei')))

    cp.g = g

    assert cp.g.get_node('Taipei').get_name() == 'Taipei'
    path = cp.DFS(g, g.get_node('Taipei'), g.get_node('Keelung'),
                  path=[], shortest=None)
    assert path == [g.get_node('Taipei'), g.get_node('Taichung'), g.get_node('Tainan'),g.get_node('Keelung')]
    path_2 = cp.BFS(g, g.get_node('Taipei'), g.get_node('Keelung') )
    assert path_2 == [g.get_node('Taipei'), g.get_node('Taichung'), g.get_node('Tainan'), g.get_node('Keelung')]