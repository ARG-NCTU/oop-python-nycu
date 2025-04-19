from lec3_112704050 import (analyze_string_1, analyze_string_2, password_feedback, find_perfect_cube_1, find_perfect_cube_2, approximate_cube_root, bisection_cube_root)
import pytest

def test_analyze_string_1():
    result = analyze_string_1("input")
    assert any("There is i or u" in s for s in result)
    assert len(result) == len("input")

def test_analyze_string_2():
    result = analyze_string_2("hello")
    assert any("There is i or o" in s for s in result)
    assert len(result) == len("hello")

def test_password_feedback_correct():
    result = password_feedback("hahaisme", 2)
    assert "Password correct!!!" in result[0]
    assert result[-1] == "You got it !!!"

def test_password_feedback_partial():
    result = password_feedback("haha", 2)
    assert "Password almost correct" in result[0]
    assert result[-1] == "I don't know??"

def test_password_feedback_incorrect():
    result = password_feedback("fail", 2)
    assert "Come on, try again" in result[0]
    assert result[-1] == "Bye!!!"

def test_find_perfect_cube_1_success():
    result = find_perfect_cube_1(27)
    assert result["success"] is True
    assert result["guess"] == 3

def test_find_perfect_cube_1_fail():
    result = find_perfect_cube_1(30)
    assert result["success"] is False

def test_find_perfect_cube_2_success():
    result = find_perfect_cube_2(64)
    assert result["found"] is True
    assert result["guess"] == 4

def test_find_perfect_cube_2_fail():
    result = find_perfect_cube_2(20)
    assert result["found"] is False

def test_approximate_cube_root_success():
    result = approximate_cube_root(8, epsilon1=0.01, increment=0.001)
    assert result["success"] is True
    assert abs(result["guess"]**3 - 8) < 0.01

def test_approximate_cube_root_fail():
    result = approximate_cube_root(9, epsilon1=1e-10, increment=1.0)
    assert result["success"] is False

def test_bisection_cube_root_success():
    result = bisection_cube_root(27, epsilon2=0.001)
    assert result["success"] is True
    assert abs(result["guess"]**3 - 27) < 0.001

def test_bisection_cube_root_fail():
    result = bisection_cube_root(30, epsilon2=1e-12)
    assert result["success"] is True  # Still expected to converge, just very slowly