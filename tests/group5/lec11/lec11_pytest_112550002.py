import pytest
import random
from lec11_source_code import minkowskidist
from lec11_source_code import stdDev
from lec11_source_code import variance

"""
Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2
"""
def test_minkowskidist():
    assert minkowskidist([], [], 2) == 0
    assert minkowskidist([0, 0], [0, 0], 1) == 0
    assert minkowskidist([0, 0], [1, 1], 1) == 2
    assert minkowskidist([0, 0], [1, 1], 2) == pytest.approx(2**0.5, rel=1e-9)
    assert minkowskidist([0, 0], [3, 4], 1) == 7
    assert minkowskidist([0, 0], [3, 4], 6) == pytest.approx(4825**0.16666666666666666, rel=1e-9)

    assert minkowskidist([1, 2, 3], [4, 5, 6], 1) == 9
    assert minkowskidist([1, 2, 3], [4, 5, 6], 2) == pytest.approx(27**0.5, rel=1e-9)
    assert minkowskidist([1, 2, 3], [4, 5, 6], 3) == pytest.approx(27**0.3333333333333333, rel=1e-9)
    assert minkowskidist([1, 2, 3], [4, 5, 6], 4) == pytest.approx(189**0.25, rel=1e-9)
    
    assert minkowskidist([1, 1, 1], [2, 2, 2], 1) == 3
    assert minkowskidist([1, 1, 1], [2, 2, 2], 2) == pytest.approx(3**0.5, rel=1e-9)
    assert minkowskidist([1, 1, 1], [2, 2, 2], 3) == pytest.approx(3**0.3333333333333333, rel=1e-9)
    
    assert minkowskidist([1, 2], [4, 6], 1) == 7
    assert minkowskidist([1, 2], [4, 6], 2) == pytest.approx(25**0.5, rel=1e-9)
    assert minkowskidist([1, 2], [4, 6], 3) == pytest.approx(91**0.3333333333333333, rel=1e-9)
    
    assert minkowskidist([1, 2, 3, 4], [4, 5, 6, 7], 1) == 12
    assert minkowskidist([1, 2, 3, 4], [4, 5, 6, 7], 2) == pytest.approx(48**0.5, rel=1e-9)
    assert minkowskidist([1, 2, 3, 4], [4, 5, 6, 7], 3) == pytest.approx(216**0.3333333333333333, rel=1e-9)

def test_stdDev():
    assert stdDev([]) == 0
    # Normal cases
    assert stdDev([1, 2, 3, 4, 5]) == pytest.approx(1.5811388300841898, rel=1e-9)
    assert stdDev([10, 20, 30, 40, 50]) == pytest.approx(15.811388300841896, rel=1e-9)
    
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
    assert variance([1, 2, 3, 4, 5]) == 2.5
    assert variance([10, 20, 30, 40, 50]) == 250
    
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