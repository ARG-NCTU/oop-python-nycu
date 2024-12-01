import pytest
import random
from lec11_source_code import minkowskiDist
from lec11_source_code import stdDev
from lec11_source_code import variance

"""
Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2
"""
def test_minkowskiDist():
    assert minkowskiDist([], [], 2) == 0
    assert minkowskiDist([0, 0], [0, 0], 1) == 0
    assert minkowskiDist([0, 0], [1, 1], 1) == 2
    assert minkowskiDist([0, 0], [1, 1], 2) == pytest.approx(2**0.5, rel=1e-9)
    assert minkowskiDist([0, 0], [3, 4], 1) == 7
    assert minkowskiDist([0, 0], [3, 4], 6) == pytest.approx(4825**0.16666666666666666, rel=1e-9)
    
    assert minkowskiDist([1, 1, 1], [2, 2, 2], 1) == 3
    assert minkowskiDist([1, 1, 1], [2, 2, 2], 2) == pytest.approx(3**0.5, rel=1e-9)
    assert minkowskiDist([1, 1, 1], [2, 2, 2], 3) == pytest.approx(3**0.3333333333333333, rel=1e-9)
    
    assert minkowskiDist([1, 2], [4, 6], 1) == 7
    assert minkowskiDist([1, 2], [4, 6], 2) == pytest.approx(25**0.5, rel=1e-9)
    assert minkowskiDist([1, 2], [4, 6], 3) == pytest.approx(91**0.3333333333333333, rel=1e-9)
    
    assert minkowskiDist([1, 2, 3, 4], [4, 5, 6, 7], 1) == 12

def test_stdDev():
    assert stdDev([]) == 0
    # Normal cases
    assert stdDev([1, 2, 3, 4, 5]) == pytest.approx(1.4142135623730951, rel=1e-9)
    assert stdDev([10, 20, 30, 40, 50]) == pytest.approx(14.142135623730951, rel=1e-9)
    
    # Edge cases
    assert stdDev([0, 0, 0, 0, 0]) == 0
    assert stdDev([1]) == 0
    assert stdDev([-1, -1, -1, -1, -1]) == 0
    assert stdDev([1, 1, 1, 1, 1]) == 0
    
    # Random cases
    random.seed(0)
    for _ in range(4):
        X = [random.randint(0, 100) for _ in range(10)]
        expected_output = (sum((x - sum(X)/len(X))**2 for x in X) / len(X))**0.5
        assert stdDev(X) == pytest.approx(expected_output, rel=1e-9)

def test_variance():
    assert variance([]) == 0 
    # Normal cases
    assert variance([1, 2, 3, 4, 5]) == 2
    assert variance([10, 20, 30, 40, 50]) == 200
    
    # Edge cases
    assert variance([0, 0, 0, 0, 0]) == 0
    assert variance([1]) == 0
    assert variance([-1, -1, -1, -1, -1]) == 0
    assert variance([1, 1, 1, 1, 1]) == 0
    
    # Random cases
    random.seed(0)
    for _ in range(4):
        X = [random.randint(0, 100) for _ in range(10)]
        expected_output = sum((x - sum(X)/len(X))**2 for x in X) / len(X)
        assert variance(X) == pytest.approx(expected_output, rel=1e-9)