import pytest
import random

class Drunk:
    def __init__(self, name=None):
        """Assumes name is a str"""
        self.name = name

    def __str__(self):
        if self is not None:
            return self.name
        return 'Anonymous'

class UsualDrunk(Drunk):
    def take_step(self):
        step_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(step_choices)

class MasochistDrunk(Drunk):
    def take_step(self):
        step_choices = [(0.0, 1.1), (0.0, -0.9),
                        (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)
    

def test_usual_drunk():
    # Test taking a step
    d = UsualDrunk()
    for i in range(10):
        step = d.take_step()
        assert step in [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    
def test_masochist_drunk():
    # Test taking a step
    d = MasochistDrunk()
    for i in range(10):
        step = d.take_step()
        assert step in [(0.0, 1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)]
    
    
    
test_usual_drunk()
test_masochist_drunk()