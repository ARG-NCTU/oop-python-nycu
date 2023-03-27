import pytest
from random import seed
from cpplabs import Vertex

def test_vertex_constructor():
    v = Vertex()
    assert v.getX() == 0
    assert v.getY() == 0

    v = Vertex(3, 4)
    assert v.getX() == 3
    assert v.getY() == 4

def test_vertex_setters():
    v = Vertex()
    v.setXY(1, 2)
    assert v.getX() == 1
    assert v.getY() == 2

    seed(12345)
    v.setRandom(1, 10)
    assert v.getX() >= 1 and v.getX() <= 10
    assert v.getY() >= 1 and v.getY() <= 10

    seed(12345)
    v.setRandom(1, 5, 6, 10)
    assert v.getX() >= 1 and v.getX() <= 5
    assert v.getY() >= 6 and v.getY() <= 10

def test_vertex_getSpec():
    v = Vertex(3, 4)
    assert v.getSpec() == "x=3,y=4"

    v.setXY(5, 6)
    assert v.getSpec() == "x=5,y=6"

    seed(12345)
    v.setRandom(1, 5, 6, 10)
    assert v.getSpec() == "x=3,y=9"