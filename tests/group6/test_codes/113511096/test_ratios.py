import math
import pytest

def get_ratios(L1, L2):
    """Assumes: L1 and L2 are lists of numbers.
       Returns: a list containing L1[i]/L2[i].
       Raises: ValueError if lists are of unequal length or contain invalid data."""
    
    # Check if lengths are the same
    if len(L1) != len(L2):
        raise ValueError("get_ratios called with bad arg")
    
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index] / L2[index])
        except ZeroDivisionError:
            # Division by zero -> append nan
            ratios.append(float('nan'))
        except Exception:
            # Other errors (non-numeric, etc.) -> raise ValueError
            raise ValueError("get_ratios called with bad arg")
    
    return ratios

# --- Pytest Functions ---

def test_equal_length_no_zero():
    assert get_ratios([1, 2, 3], [1, 2, 3]) == [1.0, 1.0, 1.0]

def test_equal_length_with_zero():
    result = get_ratios([2, 2, 3], [1, 0, 3])
    # Cannot compare NaN with ==, must use math.isnan
    assert math.isnan(result[1])
    assert result[0] == 2.0
    assert result[2] == 1.0

def test_unequal_length():
    # Correct way to test for an expected exception
    with pytest.raises(ValueError, match="get_ratios called with bad arg"):
        get_ratios([1, 2], [1])

def test_invalid_data():
    # Tests that non-numbers trigger ValueError
    with pytest.raises(ValueError):
        get_ratios([1, "a"], [1, 2])

def test_empty_lists():
    assert get_ratios([], []) == []

def test_floats():
    result = get_ratios([1.5, 2.5], [0.5, 1.0])
    # Using approx for floating point comparisons is best practice in pytest
    assert result == pytest.approx([3.0, 2.5])