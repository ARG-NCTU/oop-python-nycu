import pytest
import lec3_strings_algos as lec
import math

#test for cube_root()

def test_cube_root():
    assert lec.cube_root(27) == 3
    assert lec.cube_root(8) == 2
    assert lec.cube_root(125) == 5
    print("tests passed!!")

if __name__ == "__main__":
    pytest.main([__file__])
    # Alternatively, you can run pytest from the command line:
    # pytest test_lec3-1.py

