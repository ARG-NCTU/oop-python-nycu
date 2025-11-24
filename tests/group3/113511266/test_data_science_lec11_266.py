import add_path
import numpy as np
import pytest
import mit_ocw_data_science.lec11.lec11_module as data_lec11

def test_variance():
    data0 = [1, 2, 3, 4, 5]
    assert data_lec11.variance(data0) == 2.0
    data1 = [2, 4, 4, 4, 5, 5, 7, 9]
    assert data_lec11.variance(data1) == 4.0
    data2 = [10]
    assert data_lec11.variance(data2) == 0.0

def test_stdDev():
    data0 = [1, 2, 3, 4, 5]
    assert data_lec11.stdDev(data0) == 1.4142135623730951
    data1 = [2, 4, 4, 4, 5, 5, 7, 9]
    assert data_lec11.stdDev(data1) == 2.0
    data2 = [10]
    assert data_lec11.stdDev(data2) == 0.0

def test_minkowskiDist():
    a1 = np.array([1, 2, 3])
    b1 = np.array([4, 5, 6])
    assert data_lec11.minkowskiDist(a1, b1, p=2) == 5.196152422706632
    a2 = np.array([1, 2, 3, 4])
    b2 = np.array([4, 5, 6, 7])
    assert data_lec11.minkowskiDist(a2, b2, p=3) == 4.762203155904598
    a3 = np.array([0, 0])
    b3 = np.array([3, 4])
    assert data_lec11.minkowskiDist(a3, b3, p=1) == 7.0

def test_Animal():
    animal0 = data_lec11.Animal("Dog", [10, 20, 30])
    assert animal0.getName() == "Dog"
    assert np.array_equal(animal0.getFeatures(), np.array([10, 20, 30]))
    animal1 = data_lec11.Animal("Cat", [1, 2, 3])
    assert animal1.getName() == "Cat"
    assert np.array_equal(animal1.getFeatures(), np.array([1, 2, 3]))
    assert animal0.distance(animal1) == 33.67491648096547

