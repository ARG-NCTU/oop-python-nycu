import pytest
import lec3_strings_algos as lec
import math

#test for approximate_root()
def test_approximate_root():
    assert abs(lec.approximate_root(27, 0.01)[1] - 3) < 0.01
    assert abs(lec.approximate_root(8, 0.001)[1] - 2) < 0.001
    assert lec.approximate_root(10000, 1e-10)[1] == -1
    print("tests passed!!")

if __name__ == "__main__":
    pytest.main([__file__])
    # Alternatively, you can run pytest from the command line:
    # pytest test_lec3-2.py


