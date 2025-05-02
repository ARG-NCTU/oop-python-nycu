class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"<{str(self.x)} , {str(self.y)}>"
    def __add__(self,other):
        return Coordinate(self.x + other.x , self.y + other.y)
    def __sub__(self,other):
        return Coordinate(self.x - other.x , self.y - other.y)
    def __mul__(self,other):
        return Coordinate(self.x * other.x , self.y * other.y)
    def __truediv__(self,other):
        return Coordinate(self.x / other.x , self.y / other.y)
    def __float__(self):
        return (self.x + self.y)**0.5
    def distance(self,other):
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return(x_diff**2 + y_diff**2)**0.5
    def vector(self,other):
        return f"<{self.x - other.x},{self.y - other.y}>"
    
try:
    a = Coordinate(3, 4)
    b = Coordinate(-3, -4)
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    print(c)
    print(d)
    print(e)
    print(f)
    print(float(a))
    print(a.distance(b))
    print(Coordinate.distance(a,b))
    print(a.vector(b))
    print(Coordinate.vector(b,a))
except ZeroDivisionError:
    print("分母為0")