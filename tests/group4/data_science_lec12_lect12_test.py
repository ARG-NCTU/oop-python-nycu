import os
import sys
import numpy as np

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(TEST_DIR, "../.."))
LEC12_DIR = os.path.join(REPO_ROOT, "src", "mit_ocw_data_science", "lec12")

sys.path.insert(0, REPO_ROOT)
sys.path.insert(0, LEC12_DIR)

_ORIG_CWD = os.getcwd()
os.chdir(LEC12_DIR)

import cluster as cluster_mod
from src.mit_ocw_data_science.lec12.lect12 import scaleAttrs, getData, kmeans, trykmeans, printClustering

Example = cluster_mod.Example

def teardown_module(module):
    os.chdir(_ORIG_CWD)

def test_scaleAttrs():
    data = [10, 20, 30, 40, 50]
    scaled = scaleAttrs(data)
    assert abs(np.mean(scaled)) < 1e-6
    assert abs(np.std(scaled) - 1) < 1e-6

def test_getData():
    data = getData(toScale=True)
    assert len(data) > 184
    assert all(isinstance(p, Example) for p in data)
    first_patient = data[0]
    assert first_patient.getName() == "P0"
    assert len(first_patient.getFeatures()) == 4
    assert first_patient.getLabel() in [0, 1]


def test_kmeans():
    data = getData(toScale=True)
    clusters = kmeans(data, k=3, verbose=False)
    assert len(clusters) == 3
    for c in clusters:
        assert isinstance(c, cluster_mod.Cluster)
        assert list(c.members())  # non-empty

def test_trykmeans_and_printClustering():
    data = getData(toScale=True)
    clusters = trykmeans(data, numClusters=3, numTrials=2, verbose=False)
    assert len(clusters) == 3
    output = printClustering(clusters)
    assert isinstance(output, np.ndarray)
    assert len(output) == 3