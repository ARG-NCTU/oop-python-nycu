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
    f_return,
    run_returning_function_example,
    scope_example_f,
    scope_example_g,
    scope_example_h,
    harder_scope_example,
    simple_scope_f,
    run_simple_scope_example,
    nested_scope_g,
    run_nested_scope_example,
)

# ----------------------
# combinations of print and return
# ----------------------


def test_is_even_with_return(capsys):
    res = is_even_with_return(4)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()
    assert res is True
    assert lines[-1] == "with return"

    res2 = is_even_with_return(3)
    captured = capsys.readouterr()
    lines2 = captured.out.strip().splitlines()
    assert res2 is False
    assert lines2[-1] == "with return"


def test_is_even_without_return(capsys):
    res = is_even_without_return(3)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()
    assert res is None
    assert lines[-1] == "without return"


def test_is_even_range_0_to_9():
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
# bisection cuberoot
# ----------------------


def test_bisection_cuberoot_values():
    epsilon = 0.01
    for x in [1, 10, 100, 1000, 10000]:
        approx = bisection_cuberoot_approx(x, epsilon)
        assert abs(approx**3 - x) < epsilon


def test_print_bisection_cuberoot_series_default(capsys):
    print_bisection_cuberoot_series()
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()
    assert len(lines) == 5  # 1,10,100,1000,10000

    xs = [1, 10, 100, 1000, 10000]
    for line, x in zip(lines, xs):
        parts = line.split()
        approx = float(parts[0])
        tail = " ".join(parts[1:])
        assert tail == f"is close to cube root of {x}"
        assert abs(approx**3 - x) < 0.01


# ----------------------
# functions as arguments
# ----------------------


def test_func_a(capsys):
    res = func_a()
    captured = capsys.readouterr()
    assert res is None
    assert captured.out.strip().splitlines() == ["inside func_a"]


def test_func_b(capsys):
    res = func_b(7)
    captured = capsys.readouterr()
    assert res == 7
    assert captured.out.strip().splitlines() == ["inside func_b"]


def test_func_c_calls_func_a(capsys):
    res = func_c(func_a)
    captured = capsys.readouterr()
    assert res is None
    assert captured.out.strip().splitlines() == ["inside func_c", "inside func_a"]


# ----------------------
# returning function objects
# ----------------------


def test_f_return_add():
    add_fn = f_return()
    assert callable(add_fn)
    assert add_fn(3, 4) == 7
    assert add_fn(10, -2) == 8


def test_run_returning_function_example(capsys):
    val = run_returning_function_example()
    captured = capsys.readouterr()
    assert val == 7
    assert captured.out.strip().splitlines()[-1] == "7"


# ----------------------
# scope examples
# ----------------------


def test_scope_example_f(capsys):
    scope_example_f()
    captured = capsys.readouterr()
    assert captured.out.strip().splitlines() == ["2", "5"]


def test_scope_example_g(capsys):
    scope_example_g()
    captured = capsys.readouterr()
    assert captured.out.strip().splitlines() == ["5", "6", "5"]


def test_scope_example_h(capsys):
    scope_example_h()
    captured = capsys.readouterr()
    assert captured.out.strip().splitlines() == ["5"]


# ----------------------
# harder scope example
# ----------------------


def test_harder_scope_example(capsys):
    x, z = harder_scope_example()
    captured = capsys.readouterr()
    assert captured.out.strip().splitlines() == ["in g(x): x = 4"]
    assert x == 3
    assert z == 4


# ----------------------
# complicated scope examples
# ----------------------


def test_simple_scope_f(capsys):
    z = simple_scope_f(3)
    captured = capsys.readouterr()
    assert z == 4
    assert captured.out.strip().splitlines() == ["in f(x): x = 4"]


def test_run_simple_scope_example(capsys):
    x, z = run_simple_scope_example()
    captured = capsys.readouterr()
    assert x == 3
    assert z == 4
    assert captured.out.strip().splitlines() == [
        "in f(x): x = 4",
        "in main program scope: z = 4",
        "in main program scope: x = 3",
    ]


def test_nested_scope_g(capsys):
    z = nested_scope_g(3)
    captured = capsys.readouterr()
    assert z == 4
    assert captured.out.strip().splitlines() == [
        "in g(x): x =  4",
        "in h(x): x =  5",
    ]


def test_run_nested_scope_example(capsys):
    x, z = run_nested_scope_example()
    captured = capsys.readouterr()
    assert x == 3
    assert z == 4
    assert captured.out.strip().splitlines() == [
        "in g(x): x =  4",
        "in h(x): x =  5",
        "in main program scope: x =  3",
        "in main program scope: z =  4",
    ]
