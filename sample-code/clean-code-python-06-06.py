class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self):
        self.topLeft = Point()
        self.side = 0.0

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self):
        self.topLeft = Point()
        self.height = 0.0
        self.width = 0.0

    def area(self):
        return self.height * self.width

class Circle(Shape):
    def __init__(self):
        self.center = Point()
        self.radius = 0.0
        self.PI = 3.141592653589793

    def area(self):
        return self.PI * self.radius * self.radius

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
    square_area = square.area()
    rectangle_area = rectangle.area()
    circle_area = circle.area()

    # Print the results
    print(f"Square area: {square_area}")
    print(f"Rectangle area: {rectangle_area}")
    print(f"Circle area: {circle_area}")

if __name__ == '__main__':
    main()

