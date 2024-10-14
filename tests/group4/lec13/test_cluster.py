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
    
    