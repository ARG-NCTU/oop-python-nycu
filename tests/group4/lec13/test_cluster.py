import pytest
import add_path
import random
from mit_ocw_data_science.lec12.cluster import *
import numpy as np

def test_minkowski_dist():
    assert minkowski_dist([0,0], [3,4], 2) == 5.0
    assert minkowski_dist([1,2,3], [4,5,6], 1) == 9.0
    
def test_Example():
    example = Example('test', [1,2,3], 'test')
    assert example.name == 'test'
    assert example.features == [1,2,3]
    assert example.label == 'test'
    assert example.dimensionality() == 3
    assert example.getFeatures() == [1,2,3]
    assert example.getLabel() == 'test'
    assert example.getName() == 'test'
    assert example.distance(Example('test', [4,5,6], 'test')) == 5.196152422706632
    assert str(example) == 'test:[1, 2, 3]:test'
    
def test_Cluster():
    #[age, tale, gender], gender: 1:male, 0:female
    e1 = Example('LBJ', [39,0,1], 'human')
    e2 = Example('Tiffany', [19,0,0], 'human')
    e3 = Example('John', [9,0,1], 'human')
    e4 = Example('Howard', [26,0,1], 'human')
    e5 = Example('Bunny', [4,1,1], 'rabbit')
    e6 = Example('Coco', [8,1,0], 'rabbit')
    cluster1 = Cluster([e1, e2, e3, e4])
    cluster2 = Cluster([e5, e6])
    assert e1 in list(cluster1.members())
    assert e2 in list(cluster1.members())
    assert e3 in list(cluster1.members())
    assert e4 in list(cluster1.members())
    assert e5 in list(cluster2.members())
    assert e6 in list(cluster2.members())

    np.testing.assert_almost_equal(cluster1.getCentroid().features, [23.25, 0, 0.75], decimal=2)
    np.testing.assert_almost_equal(cluster1.variability(), 477.5, decimal=1)

    np.testing.assert_almost_equal(cluster2.getCentroid().features, [6, 1, 0.5], decimal=2)
    np.testing.assert_almost_equal(cluster2.variability(), 8.5, decimal=1)

    assert dissimilarity([cluster1, cluster2]) == 486.0

