import pytest

from lec4_functions_113511088 import (
    is_even_with_return,
    is_even_without_return,
    is_even,
    print_even_or_not_upto,
    bisection_cuberoot_approx,
    print_bisection_cuberoot_series,
    func_a,
    func_b,
    func_c,
)

# ----------------------
# combinations of print and return
# ----------------------


def test_is_even_with_return_true_and_false(capsys):
    # 測試偶數
    result = is_even_with_return(4)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()
    assert result is True
    assert lines[-1] == "with return"

    # 測試奇數
    result = is_even_with_return(3)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()
    assert result is False
    assert lines[-1] == "with return"


def test_is_even_without_return_only_print(capsys):
    result = is_even_without_return(3)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert result is None
    assert lines[-1] == "without return"


def test_is_even_on_range_0_to_9():
    expected_even = {0, 2, 4, 6, 8}
    for i in range(10):
        if i in expected_even:
            assert is_even(i) is True
        else:
            assert is_even(i) is False


def test_print_even_or_not_upto_6(capsys):
    print_even_or_not_upto(6)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert lines[0] == "All numbers between 0 and 6: even or not"
    expected = [
        "0 even",
        "1 odd",
        "2 even",
        "3 odd",
        "4 even",
        "5 odd",
    ]
    assert lines[1:] == expected


# ----------------------
# applying functions many times: bisection_cuberoot_approx
# ----------------------


def test_bisection_cuberoot_approx_values():
    epsilon = 0.01
    for x in [1, 10, 100, 1000, 10000]:
        approx = bisection_cuberoot_approx(x, epsilon)
        assert abs(approx ** 3 - x) < epsilon


def test_print_bisection_cuberoot_series_default(capsys):
    print_bisection_cuberoot_series()
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    # 5 行：1, 10, 100, 1000, 10000
    assert len(lines) == 5

    xs = [1, 10, 100, 1000, 10000]
    epsilon = 0.01
    for line, x in zip(lines, xs):
        parts = line.split()
        approx_str = parts[0]
        tail = " ".join(parts[1:])
        assert tail == f"is close to cube root of {x}"

        approx = float(approx_str)
        assert abs(approx ** 3 - x) < epsilon


# ----------------------
# functions as arguments
# ----------------------


def test_func_a(capsys):
    result = func_a()
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert result is None
    assert lines == ["inside func_a"]


def test_func_b(capsys):
    result = func_b(7)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert result == 7
    assert lines == ["inside func_b"]


def test_func_c_calls_func_a(capsys):
    result = func_c(func_a)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    # 呼叫順序：先 inside func_c，再 inside func_a
    assert result is None
    assert lines == ["inside func_c", "inside func_a"]
