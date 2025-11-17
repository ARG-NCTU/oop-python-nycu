
##############
## EXAMPLE: a set of integers as class
##############
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
def test_intSet():
    s = intSet()
    assert str(s) == "{}"  # 初始集合應該是空的

    s.insert(3)
    s.insert(4)
    s.insert(3)  # 重複插入應該無效
    assert str(s) == "{3,4}"

    assert s.member(3) is True
    assert s.member(5) is False

    s.insert(6)
    assert str(s) == "{3,4,6}"

    s.remove(3)
    assert str(s) == "{4,6}"

    try:
        s.remove(3)  # 應該拋出 ValueError
    except ValueError as e:
        assert str(e) == "3 not found"

"""
s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
print(s)
s.member(3)
s.member(5)
s.insert(6)
print(s)
#s.remove(3)  # leads to an error
print(s)
s.remove(3)
"""
