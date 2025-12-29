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
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

# --- Pytest Functions ---

def test_Coordinate_basic():
    """ Tests basic initialization and string representation """
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    assert c1.x == 3 and c1.y == 4
    assert c2.x == 0 and c2.y == 0
    assert str(c1) == "<3,4>"

def test_Coordinate_distance():
    """ Tests the distance calculation between two points """
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    # (3^2 + 4^2) ** 0.5 = 5.0
    assert c1.distance(c2) == 5.0
    
    c3 = Coordinate(4, 2)
    c4 = Coordinate(7, 6)
    # sqrt((7-4)^2 + (6-2)^2) = sqrt(3^2 + 4^2) = 5.0
    assert c3.distance(c4) == 5.0

def test_Coordinate_symmetry():
    """ Tests that distance from A to B is the same as B to A """
    c = Coordinate(4, 3)
    origin = Coordinate(0, 0)
    assert c.distance(origin) == origin.distance(c)