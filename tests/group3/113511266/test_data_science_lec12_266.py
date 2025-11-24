import add_path
import numpy as np

import mit_ocw_data_science.lec12.cluster as data_lec12 


def test_minkowski_dist():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    assert data_lec12.minkowski_dist(a, b, 2) == 5.196152422706632
    c = np.array([1, 2, 3, 4])
    d = np.array([4, 5, 6, 7])
    assert data_lec12.minkowski_dist(c, d, 3) == 4.762203155904598
    e = np.array([0, 0])
    f = np.array([3, 4])
    assert data_lec12.minkowski_dist(e, f, 1) == 7.0

def test_example():
    ex = data_lec12.Example("Tim", [1, 5, 9, 48], "eating")
    assert ex.getName() == "Tim"
    assert ex.getFeatures() == [1, 5, 9, 48]
    assert ex.getLabel() == "eating"
    assert ex.dimensionality() == 4
    assert str(ex) == "Tim:[1, 5, 9, 48]:eating"


def test_cluster():
    ex0 = data_lec12.Example("Tim", [1, 5, 9, 48], "eating")
    ex1 = data_lec12.Example("Bob", [21, 75, 49, 8], "sleeping")
    cluster = data_lec12.Cluster([ex0, ex1])
    assert cluster.examples == [ex0, ex1]
    assert cluster.centroid.getName() == "centroid"
    assert cluster.centroid.dimensionality() == 4
    assert cluster.centroid.getLabel() is None
    assert cluster.getCentroid() == cluster.centroid
    assert cluster.variability() == 4250.0
    assert list(cluster.members()) == [ex0, ex1]
    assert str(cluster) == "Cluster with centroid [11. 40. 29. 28.] contains:\n  Bob, Tim"
    assert cluster.update([ex0, ex1]) == 0.0

def test_dissimilarity():
    ex0 = data_lec12.Example("Tim", [1, 5, 9, 48], "eating")
    ex1 = data_lec12.Example("Bob", [21, 75, 49, 8], "sleeping")
    cluster = data_lec12.Cluster([ex0, ex1])
    assert data_lec12.dissimilarity([cluster]) == 4250.0

