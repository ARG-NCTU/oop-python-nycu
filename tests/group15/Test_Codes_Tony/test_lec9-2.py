import lec9_inheritance as lec
from lec9_inheritance import Rabbit
import pytest

def test_rabbit():
    print("rabbit test!!")
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r3 = Rabbit(5)
    assert r1.get_age() == 3
    print("r7:", r1)
    r4 = r1+r2 
    print("r10 parent1:", r4.get_parent1())
    print("r10 parent2:", r4.get_parent2())
    r5 = r4+r3
    print("r11:", r5)
    print("r4 and r5 have same parents?", r5 == r4)


if __name__ == "__main__":
    pytest.main([__file__])
    # Alternatively, you can run pytest from the command line:
    # pytest test_lec9-2.py


