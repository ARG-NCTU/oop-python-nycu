import add_path
import numpy as np
from src.mit_ocw_data_science.lec12.cluster import *


def test_minkowski_dist():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    assert minkowski_dist(a, b, 2) == 5.196152422706632
    c = np.array([1, 2, 3, 4])
    d = np.array([4, 5, 6, 7])
    assert minkowski_dist(c, d, 3) == 4.762203155904598
    e = np.array([0, 0])
    f = np.array([3, 4])
    assert minkowski_dist(e, f, 1) == 7.0

def test_example():
    ex = Example("Tim", [1, 5, 9, 48], "eating")
    assert ex.getName() == "Tim"
    assert ex.getFeatures() == [1, 5, 9, 48]
    assert ex.getLabel() == "eating"
    assert ex.dimensionality() == 4
    assert str(ex) == "Tim:[1, 5, 9, 48]:eating"




