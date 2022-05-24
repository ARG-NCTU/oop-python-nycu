import random
from multipledispatch import dispatch

class VertexSimple():
    def __init__(self, x = 0, y = 0):
        self._mx = x
        self._my = y
    @dispatch(int,int)
    def setRandom(self,min,max):
        self._mx = random.randint(min,max)
        self._my = random.randint(min,max)

    @dispatch(int,int,int,int)  
    def setRandom(self,xmin,xmax,ymin,ymax):
        self._mx = random.randint(xmin,xmax)
        self._my = random.randint(ymin,ymax)

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

vertex = VertexSimple
vertex.X = 10
vertex.Y = 10
print(f'x={vertex.X}y={vertex.Y}')
vertex.setRandom(0,100)
vertex.getSpec()