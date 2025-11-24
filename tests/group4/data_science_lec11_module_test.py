import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
import numpy as np
from src.mit_ocw_data_science.lec11.lec11_module import variance, stdDev, minkowskiDist, Animal

def test_variance():
    data0 = [1, 2, 3, 4, 5]
    assert variance(data0) == 2.0
    data1 = [2, 4, 4, 4, 5, 5, 7, 9]
    assert variance(data1) == 4.0
    data2 = [10]
    assert variance(data2) == 0.0

def test_stdDev():
    data0 = [1, 2, 3, 4, 5]
    assert stdDev(data0) == 1.4142135623730951
    data1 = [2, 4, 4, 4, 5, 5, 7, 9]
    assert stdDev(data1) == 2.0
    data2 = [10]
    assert stdDev(data2) == 0.0

def test_minkowskiDist():
    a1 = np.array([1, 2, 3])
    b1 = np.array([4, 5, 6])
    assert minkowskiDist(a1, b1, p=2) == 5.196152422706632
    a2 = np.array([1, 2, 3, 4])
    b2 = np.array([4, 5, 6, 7])
    assert minkowskiDist(a2, b2, p=3) == 4.762203155904598
    a3 = np.array([0, 0])
    b3 = np.array([3, 4])
    assert minkowskiDist(a3, b3, p=1) == 7.0

def test_Animal():
    animal0 = Animal("Dog", [10, 20, 30])
    assert animal0.getName() == "Dog"
    assert np.array_equal(animal0.getFeatures(), np.array([10, 20, 30]))
    animal1 = Animal("Cat", [1, 2, 3])
    assert animal1.getName() == "Cat"
    assert np.array_equal(animal1.getFeatures(), np.array([1, 2, 3]))
    assert animal0.distance(animal1) == 33.67491648096547