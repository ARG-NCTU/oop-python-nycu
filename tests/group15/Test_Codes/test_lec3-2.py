import pytest
import lec3_strings_algos as lec
import math

#test for approximate_root()
def approximate_root_tests():
    assert abs(lec.approximate_root(27, 0.01)[1] - 3) < 0.01
    assert abs(lec.approximate_root(8, 0.001)[1] - 2) < 0.001
    assert lec.approximate_root(10000, 1e-10)[1] == -1
    print("tests passed!!")

approximate_root_tests()

