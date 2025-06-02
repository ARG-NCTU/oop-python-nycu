from test_lec_movingModule_testing_code_111514025 import *
import pytest
import random



def test_location():
    """Test the Field class"""
    pass
    # Test the Location class
    loc = Location(0, 0)
    assert loc.get_x() == 0
    assert loc.get_y() == 0
    loc2 = loc.move(1, 1)
    assert loc2.get_x() == 1
    assert loc2.get_y() == 1
    assert loc.dist_from(loc2) == 1.4142135623730951
    assert loc2.dist_from(loc) == 1.4142135623730951
    assert loc2.dist_from(loc2) == 0
    assert loc.dist_from(loc) == 0
    
    

if __name__ == "__main__":
    # pytest.main()
    # Run the test

    loc = Location(0, 0)
    loc2 = loc.move(1, 1)
    print(f"Location: {loc}, Location2: {loc2}")
    print(f"Distance from {loc} to {loc2}: {loc.dist_from(loc2)}")
    print(f"Distance from {loc2} to {loc}: {loc2.dist_from(loc)}")



    
