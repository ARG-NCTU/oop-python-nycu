# utils.py
import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def normalize(self):
        length = math.sqrt(self.x**2 + self.y**2)
        if length != 0:
            return Vector2(self.x / length, self.y / length)
        return Vector2(0, 0) 
