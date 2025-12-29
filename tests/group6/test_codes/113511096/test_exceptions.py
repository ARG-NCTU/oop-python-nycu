def safe_divide(a_str, b_str):
    """Logic pulled from your example to make it testable."""
    try:
        a = int(a_str)
        b = int(b_str)
        return a / b
    except ValueError:
        return "Could not convert to a number."
    except ZeroDivisionError:
        return "Can't divide by zero"
    except:
        return "Something went very wrong."

# --- Pytest Functions ---

def test_value_error():
    # Tests that string input triggers the ValueError message
    result = safe_divide("hello", "5")
    assert result == "Could not convert to a number."

def test_zero_division():
    # Tests that dividing by zero triggers the ZeroDivisionError message
    result = safe_divide("10", "0")
    assert result == "Can't divide by zero"

def test_valid_division():
    # Tests a normal successful division
    result = safe_divide("10", "2")
    assert result == 5.0

def test_exceptions_manual_check():
    """Your original test structure for ValueError"""
    try:
        int("hello")
    except ValueError:
        assert True  # Correctly caught
        return
    assert False # Should not reach here