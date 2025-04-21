# tests/group4/113511103/test_lec8_exception_scope.py

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Cannot divide by zero"
    else:
        return result

def safe_int_conversion(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        return None

# 測試區段

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) == "Cannot divide by zero"

def test_safe_int_conversion():
    assert safe_int_conversion("123") == 123
    assert safe_int_conversion("abc") is None
    assert safe_int_conversion(None) is None
