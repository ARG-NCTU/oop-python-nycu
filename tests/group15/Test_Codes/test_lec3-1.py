import pytest
import lec3_strings_algos as lec
import math

#test for cube_root()

def cube_root_test():
    assert lec.cube_root(27) == 3
    assert lec.cube_root(8) == 2
    assert lec.cube_root(0) == 0
    print("tests passed!!")

cube_root_test()
lec.while_to_for()

