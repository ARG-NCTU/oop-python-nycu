import pytest
import add_path
import random
from mit_ocw_data_science.lec12.cluster import *
import numpy as np

def test_euclidean_dist():
    assert euclidean_dist([0,0], [3,4]) == 5.0
    assert euclidean_dist([1,2,3], [4,5,6]) == 5.196152422706632
    assert euclidean_dist([1,1], [4,5]) == 5.0
    assert euclidean_dist([2,3,4], [5,6,7]) == 5.196152422706632

def test_Point():
    point = Point('test_point', [1,2,3])
    assert point.name == 'test_point'
    assert point.coords == [1,2,3]
    assert point.dimension() == 3
    assert point.getCoords() == [1,2,3]
    assert point.getName() == 'test_point'
    assert point.distance(Point('other_point', [4,5,6])) == 5.196152422706632
    assert str(point) == 'test_point:[1, 2, 3]'

def test_Group():
    p1 = Point('Alice', [30,1,1])
    p2 = Point('Bob', [25,0,1])
    p3 = Point('Charlie', [20,0,1])
    p4 = Point('Diana', [35,1,0])
    p5 = Point('Eve', [40,1,0])
    p6 = Point('Frank', [45,0,1])
    group1 = Group([p1, p2, p3, p4])
    group2 = Group([p5, p6])
    assert p1 in list(group1.members())
    assert p2 in list(group1.members())
    assert p3 in list(group1.members())
    assert p4 in list(group1.members())
    assert p5 in list(group2.members())
    assert p6 in list(group2.members())

    np.testing.assert_almost_equal(group1.getCentroid().coords, [27.5, 0.5, 0.75], decimal=2)
    np.testing.assert_almost_equal(group1.variability(), 250.0, decimal=1)

    np.testing.assert_almost_equal(group2.getCentroid().coords, [42.5, 1, 0.5], decimal=2)
    np.testing.assert_almost_equal(group2.variability(), 12.5, decimal=1)

    assert dissimilarity([group1, group2]) == 262.5