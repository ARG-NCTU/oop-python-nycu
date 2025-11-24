import add_path
import numpy as np

from mit_ocw_data_science.lec11.lec11_module import *

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

