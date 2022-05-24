import random

class VertexSimple():
    def __init__(self, x = 0, y = 0):
        self._mx = x
        self._my = y
    def setRandom(self,min,max):
        self._mx = random.randint(min,max)
        self._my = random.randint(min,max)
    def getSpec(self):
        print(f'x={self._mx},y={self._my}')
    @property
    def X(self):
        return self._mx
    @property
    def Y(self):
        return self._my
    @X.setter
    def X(self,x):
        self._mx = x
    @Y.setter
    def Y(self,y):
        self._my = y

vertex = VertexSimple(5,5)
print(vertex.X, vertex.Y)
vertex.X = 10
vertex.Y = 10
vertex.getSpec()