import pytest
import random
import time
from lec5_module import (
    Location, Field, Drunk, UsualDrunk, MasochistDrunk, 
    walk, sim_walks, sim_drunk, StyleIterator
)

# Fixtures for reusability
@pytest.fixture
def field():
    return Field()

@pytest.fixture
def usual_drunk():
    return UsualDrunk()

@pytest.fixture
def masochist_drunk():
    return MasochistDrunk()

@pytest.fixture
def origin():
    return Location(0, 0)

# Test StyleIterator
def test_style_iterator():
    styles = ['b-', 'r--', 'g:']
    iterator = StyleIterator(styles)
    assert iterator.next_style() == 'b-'
    assert iterator.next_style() == 'r--'
    assert iterator.next_style() == 'g:'
    assert iterator.next_style() == 'b-'  # Test cycling
    # Test empty styles list
    with pytest.raises(IndexError):
        empty_iterator = StyleIterator([])
        empty_iterator.next_style()

# Test sim_drunk
def test_sim_drunk():
    random.seed(0)
    walk_lengths = [10, 100]
    num_trials = 10
    means = sim_drunk(num_trials, UsualDrunk, walk_lengths)
    assert len(means) == len(walk_lengths)
    assert all(isinstance(m, float) for m in means)
    assert all(m >= 0 for m in means)
    # Check approximate mean for 100 steps
    assert means[1] == pytest.approx(10, abs=2)

# Test Drunk __str__
def test_drunk_str():
    d = Drunk("Bob")
    assert str(d) == "Bob"
    d = Drunk()
    assert str(d) == "Anonymous"

# Test Location invalid inputs
def test_location_invalid_input():
    with pytest.raises(TypeError):
        Location("invalid", 0)
    with pytest.raises(TypeError):
        Location(0, None)
    loc = Location(0, 0)
    with pytest.raises(TypeError):
        loc.move("invalid", 1)
    with pytest.raises(TypeError):
        loc.move(1, None)

# Test Location with extreme coordinates
def test_location_extreme_coordinates():
    loc1 = Location(1e308, 1e308)
    loc2 = Location(0, 0)
    with pytest.raises(OverflowError):
        loc1.dist_from(loc2)  # Should handle overflow gracefully
    loc3 = Location(1e308, 0)
    assert loc3.get_x() == 1e308
    assert loc3.get_y() == 0

# Test Field with multiple drunks
def test_field_multiple_drunks(field):
    d1 = Drunk("Bob")
    d2 = Drunk("Alice")
    loc1 = Location(0, 0)
    loc2 = Location(1, 1)
    field.add_drunk(d1, loc1)
    field.add_drunk(d2, loc2)
    assert field.get_loc(d1) == loc1
    assert field.get_loc(d2) == loc2
    # Move both drunks
    d1.take_step = lambda: (1, 0)
    d2.take_step = lambda: (0, 1)
    field.move_drunk(d1)
    field.move_drunk(d2)
    assert field.get_loc(d1).get_x() == 1
    assert field.get_loc(d2).get_y() == 2

# Test walk with invalid steps
def test_walk_invalid_steps(field, usual_drunk, origin):
    field.add_drunk(usual_drunk, origin)
    with pytest.raises(ValueError):
        walk(field, usual_drunk, -1)

# Test sim_walks with invalid trials
def test_sim_walks_invalid_trials():
    with pytest.raises(ValueError):
        sim_walks(10, 0, UsualDrunk)
    with pytest.raises(ValueError):
        sim_walks(10, -1, UsualDrunk)

# Test UsualDrunk step distribution
def test_usual_drunk_step_distribution(usual_drunk):
    random.seed(0)
    steps = [usual_drunk.take_step() for _ in range(10000)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    counts = [steps.count(d) for d in directions]
    assert all(2300 < c < 2700 for c in counts)  # Each direction ~25%

# Test MasochistDrunk step distribution
def test_masochist_drunk_step_distribution(masochist_drunk):
    random.seed(0)
    steps = [masochist_drunk.take_step() for _ in range(10000)]
    directions = [(0.0, 1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)]
    counts = [steps.count(d) for d in directions]
    assert all(2300 < c < 2700 for c in counts)  # Each direction ~25%

# Test sim_walks mean distance
def test_sim_walks_mean_distance():
    random.seed(0)
    distances = sim_walks(100, 100, UsualDrunk)
    mean = sum(distances) / len(distances)
    assert 8 < mean < 12  # Expected mean ~ sqrt(100)

# Test sim_walks large trials
def test_sim_walks_large_trials():
    random.seed(0)
    distances = sim_walks(100, 100, UsualDrunk)
    assert len(distances) == 100
    assert all(isinstance(d, float) for d in distances)
    assert all(d >= 0 for d in distances)

# Test comparison of drunks
def test_compare_drunks(field, usual_drunk, masochist_drunk, origin):
    random.seed(0)
    field.add_drunk(usual_drunk, origin)
    field.add_drunk(masochist_drunk, origin)
    usual_distances = sim_walks(100, 10, UsualDrunk)
    masochist_distances = sim_walks(100, 10, MasochistDrunk)
    usual_mean = sum(usual_distances) / len(usual_distances)
    masochist_mean = sum(masochist_distances) / len(masochist_distances)
    assert masochist_mean > usual_mean  # MasochistDrunk has larger steps

# Test walk performance
def test_walk_performance(field, usual_drunk, origin):
    field.add_drunk(usual_drunk, origin)
    start_time = time.time()
    walk(field, usual_drunk, 100000)
    elapsed = time.time() - start_time
    assert elapsed < 1  # Ensure reasonable performance