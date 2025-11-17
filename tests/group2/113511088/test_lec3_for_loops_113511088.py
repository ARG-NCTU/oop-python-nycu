import pytest

from lec3_for_loops_113511088 import (
    print_i_or_u_by_index,
    print_i_or_u_by_char,
    cheer_word,
    perfect_cube_root,
    guess_and_check_cube_root,
    approximate_cube_root,
    print_approximate_cube_root,
    bisection_cube_root,
    print_bisection_cube_root,
    is_palindrome,
)


# ----------------------
# for loops over strings
# ----------------------


def test_print_i_or_u_by_index(capsys):
    # s 裡只有一個 u
    print_i_or_u_by_index("bus")
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert lines == ["There is an i or u"]


def test_print_i_or_u_by_char(capsys):
    # s 裡有 i 和 u 各一個
    print_i_or_u_by_char("quiz")
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert lines == [
        "There is an i or u",
        "There is an i or u",
    ]


# ----------------------
# while / for cheer_word
# ----------------------


def test_cheer_word_mit(capsys):
    cheer_word("MIT", 2)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    # AN_LETTERS 裡有 M 跟 I，沒有 T
    assert lines == [
        "Give me an M! M",
        "Give me an I! I",
        "Give me a  T! T",
        "What does that spell?",
        "MIT !!!",
        "MIT !!!",
    ]


# ----------------------
# perfect cube
# ----------------------


def test_perfect_cube_root_basic():
    assert perfect_cube_root(27) == 3
    assert perfect_cube_root(64) == 4
    # 不是 perfect cube
    assert perfect_cube_root(28) is None
    # 負數直接回傳 None（我們的設計）
    assert perfect_cube_root(-8) is None


# ----------------------
# guess and check cube root
# ----------------------


def test_guess_and_check_cube_root_perfect():
    assert guess_and_check_cube_root(27) == 3
    assert guess_and_check_cube_root(8120601) == 201  # 201^3


def test_guess_and_check_cube_root_negative():
    assert guess_and_check_cube_root(-27) == -3


def test_guess_and_check_cube_root_not_perfect():
    assert guess_and_check_cube_root(28) is None


# ----------------------
# approximate cube root
# ----------------------


def test_approximate_cube_root_27():
    cube = 27
    epsilon = 0.1
    increment = 0.01

    guess, num_guesses, success = approximate_cube_root(cube, epsilon, increment)

    assert success is True
    assert num_guesses > 0
    # 誤差要在 epsilon 範圍內
    assert abs(guess**3 - cube) < epsilon


def test_approximate_cube_root_fail_case():
    # 這是原範例會 fail 的典型例子（會跑很多圈）
    cube = 10000
    epsilon = 0.1
    increment = 0.01

    guess, num_guesses, success = approximate_cube_root(cube, epsilon, increment)

    assert success is False
    # 至少有做很多次猜測（不檢查精確次數，避免太死）
    assert num_guesses > 10000
    assert abs(guess**3 - cube) >= epsilon


def test_print_approximate_cube_root_success(capsys):
    cube = 27
    epsilon = 0.1
    increment = 0.01

    print_approximate_cube_root(cube, epsilon, increment)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    # 第 1 行：num_guesses = xxx
    assert lines[0].startswith("num_guesses = ")
    # 第 2 行：<guess> is close to the cube root of 27
    parts = lines[1].split()
    guess_str = parts[0]
    tail = " ".join(parts[1:])
    assert tail == "is close to the cube root of 27"

    guess = float(guess_str)
    assert abs(guess**3 - cube) < epsilon


def test_print_approximate_cube_root_fail(capsys):
    cube = 10000
    epsilon = 0.1
    increment = 0.01

    print_approximate_cube_root(cube, epsilon, increment)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert lines[0].startswith("num_guesses = ")
    assert lines[1] == "Failed on cube root of 10000 with these parameters."


# ----------------------
# bisection cube root
# ----------------------


def test_bisection_cube_root_27():
    cube = 27
    epsilon = 0.01

    guess, num_guesses = bisection_cube_root(cube, epsilon)

    assert num_guesses > 0
    assert 0 < guess < cube
    assert abs(guess**3 - cube) < epsilon


def test_bisection_cube_root_large():
    cube = 8120601  # 201^3
    epsilon = 0.01

    guess, num_guesses = bisection_cube_root(cube, epsilon)

    assert num_guesses > 0
    assert 0 < guess < cube
    assert abs(guess**3 - cube) < epsilon


def test_bisection_cube_root_invalid():
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

    # 第 1 行：num_guesses = xxx
    assert lines[0].startswith("num_guesses = ")

    # 第 2 行：<guess> is close to the cube root of 27
    parts = lines[1].split()
    guess_str = parts[0]
    tail = " ".join(parts[1:])
    assert tail == "is close to the cube root of 27"

    guess = float(guess_str)
    assert abs(guess**3 - cube) < epsilon


# ----------------------
# palindrome
# ----------------------


def test_is_palindrome_basic():
    assert is_palindrome("Level") is True      # 忽略大小寫
    assert is_palindrome("racecar") is True
    assert is_palindrome("Python") is False
    assert is_palindrome("Abba") is True
