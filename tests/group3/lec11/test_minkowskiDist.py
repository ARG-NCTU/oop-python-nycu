import pytest
from lec11_intro_to_ML import minkowskiDist

def test_minkowskiDist():
    assert minkowskiDist([0, 0], [0, 0], 1) == 0
    assert minkowskiDist([0, 0], [0, 0], 2) == 0
    assert minkowskiDist([0, 0], [0, 0], 3) == 0
    assert minkowskiDist([0, 0], [1, 1], 1) == 2
    assert minkowskiDist([0, 0], [1, 1], 2) == 2**0.5
    assert minkowskiDist([0, 0], [1, 1], 3) == 2**0.3333333333333333
    assert minkowskiDist([0, 0], [3, 4], 1) == 7
    assert minkowskiDist([0, 0], [3, 4], 2) == 5
    assert minkowskiDist([0, 0], [3, 4], 3) == 91**0.3333333333333333
    assert minkowskiDist([0, 0], [3, 4], 4) == 337**0.25
    assert minkowskiDist([0, 0], [3, 4], 5) == 1267**0.2
    assert minkowskiDist([0, 0], [3, 4], 6) == 4825**0.16666666666666666
if __name__ == "__main__":
    pytest.main()