import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
lec12_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/mit_ocw_data_science/lec12"))
sys.path.insert(0, lec12_dir)

import add_path
import numpy as np
from src.mit_ocw_data_science.lec12.lect12 import scaleAttrs, getData, kmeans, trykmeans, printClustering, testClustering ,Patient
from src.mit_ocw_data_science.lec12.cluster import minkowski_dist, Example, Cluster, dissimilarity


import random


