import pytest
#!/usr/bin/env python3
import add_path
from mit_ocw_data_science.lec5.lec5_module import Field,  Drunk, UsualDrunk, MasochistDrunk, Location

def test_location():
  l = Location(0, 0)
  assert 0 == l.get_x()
  assert 0 == l.get_y()
  l = l.move(1,0)
  assert 1 == l.get_x()
  assert 0 == l.get_y()
  assert 0 == l.dist_from(l)

def test_field():
  f = Field()
  d1 = Drunk('Sam')
  loc1 = Location(0, 0)
  f.add_drunk(d1, loc1)
  assert f.get_loc(d1) == loc1

