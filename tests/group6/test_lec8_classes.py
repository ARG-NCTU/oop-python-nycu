import add_path
import mit_ocw_exercises.lec8_classes as lec8
import pytest

def test_coordinate():
  coo1 = lec8.Coordinate(3,4);
  o = lec8.Coordinate(0,0)
  assert coo1.x == 3;
  assert coo1.y == 4;
  assert str(coo1) == "<3,4>";
  assert coo1.distance(coo2) == 5;

def test_fraction():
  frac1 = lec8.Fraction(1, 4);
  frac2 = lec8.Fraction(3, 4);
  result = frac1 + frac2;
  assert result.num == 16 and result.denom == 16;
  result = frac2 - frac1;
  assert result.num == 8 and result.denom == 16;
  assert float(frac1) == 0.25;
  assert float(frac2) == 0.75;
  inverse_frac1 = frac1.inverse();
  assert inverse_frac1.num == 4 and inverse_frac1.denom == 1;
  
