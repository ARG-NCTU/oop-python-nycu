from test_lec_movingModule_testing_code_111514025 import *
import pytest
import random



def test_UsualDrunk():
    """Test the UsualDrunk class"""
    drunk = UsualDrunk("John")
    assert isinstance(drunk, Drunk)
    assert drunk.name == "John"
    assert str(drunk) == "John"
    assert drunk.take_step() in [(0, 1), (0, -1), (1, 0), (-1, 0)]
    assert drunk.take_step() != (0, 0)
    assert drunk.take_step() != (1, 1)
    assert drunk.take_step() != (-1, -1)
    assert drunk.take_step() != (1, -1)
    assert drunk.take_step() != (-1, 1)

if __name__ == "__main__":
    # pytest.main()
    # Run the test

    drunk = UsualDrunk("Brian")
    drunk.__str__()
    step = drunk.take_step()
    print(f"Drunk: {drunk}, Step: {step}")
    # Test the UsualDrunk class


    
