import pytest
#!/usr/bin/env python3
import add_path
from mit_ocw_data_science.lec5.test_drunk import Field,  Drunk, UsualDrunk, MasochistDrunk, Location

def test_location():
  l = Location(0, 0)
  assert 0 == l.get_x()
  assert 0 == l.get_y()
  l = l.move(1,0)
  assert 1 == l.get_x()
  assert 0 == l.get_y()
  assert 0 == l.dist_from(l)

