import pytest
from cpplabs import VertexSimple


def test_getSpec():
    v = VertexSimple(3, 5)
    assert v.getSpec() == "x=3,y=5"

def test_setRandom():
    v = VertexSimple()
    v.setRandom(1, 10)
    spec = v.getSpec()
    x_str, y_str = spec.split(",")
    x = int(x_str.split("=")[1])
    y = int(y_str.split("=")[1])
    assert 1 <= x <= 10 and 1 <= y <= 10

def test_setRandom_minGreaterEqualMax():
    v = VertexSimple()
    v.setRandom(10, 1)
    assert v.getSpec() == "x=0,y=0"