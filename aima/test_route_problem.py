import matplotlib.pyplot as plt
import random
import heapq
import math
import sys
from collections import defaultdict, deque, Counter
from itertools import combinations
import pytest
import sys
sys.path.append('../utils')
from search import * 

def get_romania():

    romania = Map(
    {('O', 'Z'):  71, ('O', 'S'): 151, ('A', 'Z'): 75, ('A', 'S'): 140, ('A', 'T'): 118,
     ('L', 'T'): 111, ('L', 'M'):  70, ('D', 'M'): 75, ('C', 'D'): 120, ('C', 'R'): 146,
     ('C', 'P'): 138, ('R', 'S'):  80, ('F', 'S'): 99, ('B', 'F'): 211, ('B', 'P'): 101,
     ('B', 'G'):  90, ('B', 'U'):  85, ('H', 'U'): 98, ('E', 'H'):  86, ('U', 'V'): 142,
     ('I', 'V'):  92, ('I', 'N'):  87, ('P', 'R'): 97},
    {'A': ( 76, 497), 'B': (400, 327), 'C': (246, 285), 'D': (160, 296), 'E': (558, 294),
     'F': (285, 460), 'G': (368, 257), 'H': (548, 355), 'I': (488, 535), 'L': (162, 379),
     'M': (160, 343), 'N': (407, 561), 'O': (117, 580), 'P': (311, 372), 'R': (227, 412),
     'S': (187, 463), 'T': ( 83, 414), 'U': (471, 363), 'V': (535, 473), 'Z': (92, 539)})

    return romania

def test_map():

    romania = get_romania()

    assert str(romania.neighbors['A']) == "['Z', 'S', 'T']"
    assert romania.distances['A', 'Z'] == 75
    assert sldistance(romania.locations['A'], romania.locations['B']) == \
        pytest.approx(366, abs=0.5)

def test_route_problem():

    romania = get_romania()

    r0 = RouteProblem('A', 'A', map=romania)
    r1 = RouteProblem('A', 'B', map=romania)
    r2 = RouteProblem('N', 'L', map=romania)
    r3 = RouteProblem('E', 'T', map=romania)
    r4 = RouteProblem('O', 'M', map=romania)

    assert r1.initial == 'A'
    assert r1.goal == 'B'
    assert str(r1.actions('A')) == "['Z', 'S', 'T']"
    assert r1.result('A', 'S') == 'S'
    assert r1.result('A', 'B') == 'A'
    assert r1.action_cost('A', 'S', 'S') == 140

def test_expand():

    romania = get_romania()
    r1 = RouteProblem('A', 'B', map=romania)

    node_a = Node('A')
    print(expand(r1, node_a))
    for c_node in expand(r1, node_a):
        print(f"child node: {c_node}, parent node:{c_node.parent}")

def test_search():

    romania = get_romania()
    r1 = RouteProblem('A', 'B', map=romania)

    assert str(path_states(breadth_first_search(r1))) == "['A', 'S', 'F', 'B']"
    assert str(path_states(depth_first_recursive_search(r1))) == \
        "['A', 'Z', 'O', 'S', 'R', 'C', 'P', 'B']"
    assert str(path_states(uniform_cost_search(r1))) == "['A', 'S', 'F', 'B']"
    assert str(path_states(astar_search(r1))) == "['A', 'S', 'F', 'B']"