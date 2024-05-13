def test_drunk_init():
    # Test Drunk object initialization with a name
    d = Drunk("John")
    assert str(d) == "John"

def test_location_init():
    # Test Location object initialization
    loc = Location(3, 4)
    assert loc.x == 3
    assert loc.y == 4

def test_location_move():
    # Test Location move method
    loc = Location(3, 4)
    new_loc = loc.move(1, -1)
    assert new_loc.x == 4
    assert new_loc.y == 3

def test_location_distance():
    # Test Location distance calculation
    loc1 = Location(0, 0)
    loc2 = Location(3, 4)
    assert loc1.dist_from(loc2) == 5.0

def test_field_add_drunk():
    # Test Field add_drunk method
    f = Field()
    d = UsualDrunk("Bob")
    loc = Location(0, 0)
    f.add_drunk(d, loc)
    assert f.drunks[d] == loc

# Add more test cases as needed...


