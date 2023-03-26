class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

class Square:
    def __init__(self):
        self.topLeft = Point()
        self.side = 0.0

class Rectangle:
    def __init__(self):
        self.topLeft = Point()
        self.height = 0.0
        self.width = 0.0

class Circle:
    def __init__(self):
        self.center = Point()
        self.radius = 0.0

class Geometry:
    PI = 3.141592653589793

    def area(self, shape):
        if isinstance(shape, Square):
            s = shape
            return s.side * s.side
        elif isinstance(shape, Rectangle):
            r = shape
            return r.height * r.width
        elif isinstance(shape, Circle):
            c = shape
            return self.PI * c.radius * c.radius
        raise NoSuchShapeException()

def main():
    # Create some shapes
    square = Square()
    square.side = 5.0

    rectangle = Rectangle()
    rectangle.width = 10.0
    rectangle.height = 5.0

    circle = Circle()
    circle.radius = 3.0

    # Calculate the areas of the shapes
    geometry = Geometry()
    square_area = geometry.area(square)
    rectangle_area = geometry.area(rectangle)
    circle_area = geometry.area(circle)

    # Print the results
    print(f"Square area: {square_area}")
    print(f"Rectangle area: {rectangle_area}")
    print(f"Circle area: {circle_area}")

if __name__ == '__main__':
    main()
