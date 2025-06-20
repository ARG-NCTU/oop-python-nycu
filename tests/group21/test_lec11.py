import pytest
import matplotlib.pylab as pylab
import lec11

def test_variance():
    assert lec11.variance([1, 2, 3, 4]) == pytest.approx(1.25)
    assert lec11.variance([5, 5, 5, 5]) == 0

def test_stdDev():
    assert lec11.stdDev([1, 2, 3, 4]) == pytest.approx(1.1180, rel=1e-3)
    assert lec11.stdDev([5, 5, 5]) == 0

def test_minkowskiDist():
    assert lec11.minkowskiDist([1, 2], [4, 6], 1) == 7
    assert lec11.minkowskiDist([1, 2], [4, 6], 2) == pytest.approx(5.0)
    assert lec11.minkowskiDist([0, 0], [0, 0], 2) == 0

def test_animal_distance():
    a = lec11.Animal("A", [1, 2])
    b = lec11.Animal("B", [4, 6])
    assert a.distance(b) == pytest.approx(5.0)
    
def test_animal_attributes():
    features = [1, 0, 1, 1]
    a = lec11.Animal("TestAnimal", features)
    assert a.getName() == "TestAnimal"
    assert (a.getFeatures() == pylab.array(features)).all()

