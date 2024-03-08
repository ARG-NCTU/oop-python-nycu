class Point:
    """Represents a point in 2-D space."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Create a point at the origin
origin = Point()

# Create a point at (3, 4)
point = Point()
point.x = 3
point.y = 4

