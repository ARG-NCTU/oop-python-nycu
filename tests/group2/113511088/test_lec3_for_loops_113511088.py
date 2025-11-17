from lec3_for_loops_113511088 import (
    bisection_cube_root,
    print_bisection_cube_root,
)


def test_bisection_cube_root_27():
    cube = 27
    epsilon = 0.01
    guess, num_guesses = bisection_cube_root(cube, epsilon)

    assert num_guesses > 0
    assert 0 < guess < cube
    assert abs(guess ** 3 - cube) < epsilon


def test_bisection_cube_root_large():
    cube = 8120601  # 201^3
    epsilon = 0.01
    guess, num_guesses = bisection_cube_root(cube, epsilon)

    assert num_guesses > 0
    assert 0 < guess < cube
    assert abs(guess ** 3 - cube) < epsilon


def test_bisection_cube_root_invalid():
    # 只支援 cube > 0
    import pytest

    with pytest.raises(ValueError):
        bisection_cube_root(0)
    with pytest.raises(ValueError):
        bisection_cube_root(-8)


def test_print_bisection_cube_root_27(capsys):
    cube = 27
    epsilon = 0.01
    print_bisection_cube_root(cube, epsilon)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    # 第一行只檢查開頭字串
    assert lines[0].startswith("num_guesses = ")

    # 第二行格式 + 內容
    # 例如："2.99993896484375 is close to the cube root of 27"
    parts = lines[1].split()
    guess_str = parts[0]
    tail = " ".join(parts[1:])

    assert tail == "is close to the cube root of 27"

    # 確認數值上真的接近立方根
    guess = float(guess_str)
    assert abs(guess ** 3 - cube) < epsilon
