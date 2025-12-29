import pytest

class intSet(object):
    """
    An intSet is a set of integers
    The value is represented by a list of ints, self.vals
    Each int in the set occurs in self.vals exactly once
    """
    def __init__(self):
        """ Create an empty set of integers """
        self.vals = []

    def insert(self, e):
        """ Assumes e is an integer and inserts e into self """
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """ Assumes e is an integer
        Returns True if e is in self, and False otherwise """
        return e in self.vals

    def remove(self, e):
        """ Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self """
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """ Returns a string representation of self """
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

# --- Pytest Functions ---

def test_intSet_basic_operations():
    s = intSet()
    # Test initial empty set
    assert str(s) == "{}"

    # Test insertion and duplication prevention
    s.insert(3)
    s.insert(4)
    s.insert(4) 
    assert str(s) == "{3,4}"

    # Test membership
    assert s.member(4) is True
    assert s.member(54) is False

def test_intSet_removal():
    s = intSet()
    s.insert(3)
    s.insert(4)
    s.insert(6)
    
    # Test successful removal
    s.remove(3)
    assert str(s) == "{4,6}"

    # Test removal of non-existent element using pytest.raises
    with pytest.raises(ValueError, match="3 not found"):
        s.remove(3)