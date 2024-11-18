# test_cluster.py
import pytest
import pylab
import numpy as np
from cluster import minkowskiDist, Example, Cluster, dissimilarity

def test_minkowskiDist_normal():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    p = 2
    assert minkowskiDist(v1, v2, p) == pytest.approx(5.196, 0.001)

def test_minkowskiDist_edge():
    v1 = []
    v2 = []
    p = 2
    assert minkowskiDist(v1, v2, p) == 0


def test_minkowskiDist_extreme():
    v1 = [i for i in range(1000)]
    v2 = [i + 1 for i in range(1000)]
    p = 2
    assert minkowskiDist(v1, v2, p) == pytest.approx(31.6228, 0.01)

def test_Example_normal():
    name = "example"
    features = [1.0, 2.0, 3.0]
    label = "label"
    example = Example(name, features, label)
    assert example.name == name
    assert example.getFeatures() == features
    assert example.getLabel() == label
    assert example.dimensionality() == len(features)

def test_Example_extreme():
    name = "example"
    features = [i * 0.1 for i in range(1000)]
    label = "label"
    example = Example(name, features, label)
    assert example.name == name
    assert example.getFeatures() == features
    assert example.getLabel() == label
    assert example.dimensionality() == len(features)

def test_Cluster_basic():
    examples = [
        Example("A", [1.0, 2.0]),
        Example("B", [2.0, 3.0]),
        Example("C", [3.0, 4.0])
    ]
    cluster = Cluster(examples)
    assert cluster.getCentroid().getFeatures() == pytest.approx([2.0, 3.0], 0.001)
    assert cluster.variability() > 0

'''
initial_centroid 和 new_centroid 是數組，因此在進行比較時
應改為使用 numpy.array_equal 或 numpy.allclose 來確保數組元素的逐一比較
'''
def test_Cluster_update():
    example1 = Example("A", [1.0, 2.0])
    example2 = Example("B", [2.0, 3.0])
    example3 = Example("C", [3.0, 4.0])
    cluster = Cluster([example1, example2])
    
    initial_centroid = cluster.getCentroid().getFeatures()
    change = cluster.update([example1, example2, example3])
    new_centroid = cluster.getCentroid().getFeatures()
    
    assert change > 0, "Centroid should have moved after adding a new example"
    assert not np.allclose(initial_centroid, new_centroid), "Centroid should change after update"

def test_dissimilarity():
    examples1 = [Example("A", [1.0, 2.0]), Example("B", [2.0, 3.0])]
    examples2 = [Example("C", [4.0, 5.0]), Example("D", [5.0, 6.0])]
    cluster1 = Cluster(examples1)
    cluster2 = Cluster(examples2)
    total_dissimilarity = dissimilarity([cluster1, cluster2])
    
    assert total_dissimilarity > 0, "Total dissimilarity should be positive"
