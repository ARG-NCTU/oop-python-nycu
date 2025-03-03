import numpy as np
import pytest
from dbscan.dbscan import DBSCAN


class MockDataset:
    def __init__(self):
        self.data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        self.label = np.array([0, 1, 0, 1])

# Tests for DBSCAN class
def test_dbscan_initialization():
    dbscan = DBSCAN()
    assert dbscan is not None
    assert dbscan.eps == 0.5
    assert dbscan.min_samples == 5

def test_dbscan_set_dataset():
    dataset = MockDataset()
    dbscan = DBSCAN()
    dbscan.set_dataset(dataset)
    assert np.array_equal(dbscan.dataset.data, dataset.data)
    assert np.array_equal(dbscan.dataset.label, dataset.label)

def test_dbscan_fit():
    dataset = MockDataset()
    dbscan = DBSCAN()
    dbscan.fit(dataset)
    assert dbscan.cluster is not None

def test_dbscan_evaluate():
    dataset = MockDataset()
    dbscan = DBSCAN()
    dbscan.fit(dataset)
    score = dbscan.evaluate()
    assert isinstance(score, float)

def test_dbscan_visualize():
    dataset = MockDataset()
    dbscan = DBSCAN()
    dbscan.fit(dataset)
    dbscan.visualize(save=True, save_name="test_dbscan_visualize")
