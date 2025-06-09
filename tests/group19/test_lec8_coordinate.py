import pytest

class Coordinate(object):
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def distance(self, other):
        """ Returns the euclidean distance between two points """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    
def Coordinate_test():
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    assert c1.x == 3 and c1.y == 4  # Check x and y values
    assert c2.x == 0 and c2.y == 0  # Check x and y values
    assert c1.distance(c2) == 5.0  # Check distance calculation
    assert str(c1) == "<3,4>"  # Check string representation
    assert str(c2) == "<0,0>"  # Check string representation of c2
    assert c1.distance(c1) == 0.0  # Distance to itself should be 0
    assert c2.distance(c2) == 0.0  # Distance to itself should be 0
    assert c1.distance(Coordinate(6, 8)) == 5.0  # Check distance to another point
    assert c2.distance(Coordinate(3, 4)) == 5.0  # Check distance from origin to c1
    assert c1.distance(Coordinate(0, 0)) == 5.0  # Distance from c1 to origin
    assert c2.distance(Coordinate(6, 8)) == 10.0  # Distance from origin to another point
    assert c1.distance(Coordinate(3, 4)) == 0.0  # Distance to itself should be 0