from test_lec_movingModule_testing_code_111514025 import *
import pytest
import random



def test_walking():
    """Test the walking functionality"""
    assert sim_walks(1000, 10, UsualDrunk) != [14.2, 41.8, 27.3, 10.3, 56.5, 34.5, 28.6, 5.1, 27.8, 24.4]
    assert sim_walks(1000, 10, MasochistDrunk) != [53.9, 34.2, 10.8, 49.5, 41.5, 61.5, 48.8, 46.7, 81.7, 49.7]


    

if __name__ == "__main__":
    # pytest.main()
    # Run the test
    sim_walk1 = sim_walks(1000, 10, UsualDrunk)
    print(sim_walk1)
    sim_walk2 = sim_walks(1000, 10, MasochistDrunk)
    print(sim_walk2)
    





    
