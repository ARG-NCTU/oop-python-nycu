# test_variance.py

import pytest
import numpy as np
import time
from lec11_intro_to_ML import variance

# Test variance function correctness
def test_variance_correctness():
    assert variance([1, 2, 3, 4, 5]) == 2.0
    assert variance([1, 1, 1, 1, 1]) == 0.0
    assert variance([1, 2, 3]) == pytest.approx(0.6667, rel=1e-3)
    assert variance([1]) == 0.0
    with pytest.raises(ValueError, match="The input list is empty"):
        variance([])

# Test variance function performance
def test_variance_performance():
    large_input = np.random.rand(1000000).tolist()
    start_time = time.time()
    variance(large_input)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time for large input: {execution_time} seconds")
    assert execution_time < 1.0  # Division by zero is not allowed

# Run tests
if __name__ == "__main__":
    pytest.main()