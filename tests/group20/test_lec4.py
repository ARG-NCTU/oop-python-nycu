import pytest
from lec4_functions_scope import (
    is_even, check_even_with_message, print_even_status,
    approximate_cube_root, execute_function, create_adder,
    modify_local_variable, read_global_variable,
    nested_scope_example, complex_scope
)

def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True
    assert is_even(-2) is True

def test_check_even_with_message(capsys):
    assert check_even_with_message(4) is True
    captured = capsys.readouterr()
    assert "Checking if 4 is even" in captured.out
    assert check_even_with_message(3) is False
    captured = capsys.readouterr()
    assert "Checking if 3 is even" in captured.out

def test_print_even_status(capsys):
    assert print_even_status(5) is None
    captured = capsys.readouterr()
    assert "Processing 5 for evenness" in captured.out
    assert print_even_status(2) is None
    captured = capsys.readouterr()
    assert "Processing 2 for evenness" in captured.out

def test_approximate_cube_root():
    result = approximate_cube_root(27, epsilon=0.01)
    assert result["success"] is True
    assert abs(result["guess"] ** 3 - 27) < 0.01
    assert result["iterations"] > 0
    result = approximate_cube_root(0, epsilon=0.01)
    assert result["success"] is False
    assert result["guess"] is None
    result = approximate_cube_root(0.125, epsilon=0.001)
    assert result["success"] is True
    assert abs(result["guess"] ** 3 - 0.125) < 0.001

def test_execute_function(capsys):
    def sample_func():
        print("Sample function")
        return 42
    result = execute_function(sample_func)
    assert result == 42
    captured = capsys.readouterr()
    assert "Executing function sample_func" in captured.out
    assert "Sample function" in captured.out

def test_create_adder():
    adder = create_adder()
    assert adder(3, 4) == 7
    assert adder(0, 0) == 0
    assert adder(-1, 2) == 1

def test_modify_local_variable(capsys):
    result = modify_local_variable(5)
    assert result == 6  # 1 + 5
    captured = capsys.readouterr()
    assert "Local x: 6" in captured.out
    result = modify_local_variable(0)
    assert result == 1
    captured = capsys.readouterr()
    assert "Local x: 1" in captured.out

def test_read_global_variable(capsys):
    assert read_global_variable(10) is None
    captured = capsys.readouterr()
    assert "Global x: 5" in captured.out
    assert "Global x + 1: 6" in captured.out

def test_nested_scope_example(capsys):
    result = nested_scope_example(3)
    assert result == 4  # 3 + 1
    captured = capsys.readouterr()
    assert "In outer function: x = 4" in captured.out
    assert "In inner_function: x = abc" in captured.out

def test_complex_scope(capsys):
    result = complex_scope(3)
    assert result["outer"] == 4  # 3 + 1
    assert result["inner"] == 5  # 4 + 1
    captured = capsys.readouterr()
    assert "In outer function: x = 4" in captured.out
    assert "In inner_modify: x = 5" in captured.out
