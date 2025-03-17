import add_path
import mit_ocw_exercises.lec8_classes as lec8
import pytest

def test_coordinate():
  coo1 = lec8.Coordinate(1,2);
  coo2 = coo1 + lec8.Coordinate(5,5);
  assert coo1.x == 1;
  assert coo1.y == 2;
  assert coo1.distance(coo2) == 5;
