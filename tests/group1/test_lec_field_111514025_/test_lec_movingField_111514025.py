from test_lec_movingModule_testing_code_111514025 import *
import pytest
import random



def test_Field():
    """Test the Field class"""
    field = Field()
    drunk = UsualDrunk("John")
    loc = Location(0, 0)
    field.add_drunk(drunk, loc)
    assert field.get_loc(drunk) == loc
    field.move_drunk(drunk)
    assert field.get_loc(drunk) != loc
    with pytest.raises(ValueError):
        field.add_drunk(drunk, loc)
    with pytest.raises(ValueError):
        field.move_drunk(Drunk("Jane"))
    with pytest.raises(ValueError):
        field.get_loc(Drunk("Jane"))
    field.move_drunk(drunk)
    

if __name__ == "__main__":
    # pytest.main()
    # Run the test

    field = Field()
    drunk = UsualDrunk("Brian")
    loc = Location(0, 0)
    field.add_drunk(drunk, loc)
    field.move_drunk(drunk)
    print(f"Field: {field}, Drunk: {drunk}, Location: {loc}")
    


    
