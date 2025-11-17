from lec3_for_loops_113511088 import (
    approximate_cube_root,
    print_approximate_cube_root,
)


def test_approximate_cube_root_27():
    # 27，epsilon=0.1, increment=0.01
    guess, num_guesses, success = approximate_cube_root(27, 0.1, 0.01)

    assert success is True
    assert num_guesses == 300            # 跟原程式一致
    assert abs(guess**3 - 27) < 0.1      # 在誤差範圍內


def test_approximate_cube_root_large():
    # 8120601 = 201^3
    guess, num_guesses, success = approximate_cube_root(8120601, 0.1, 0.01)

    assert success is True
    assert num_guesses == 20100          # 每次加 0.01，走到 ~201
    assert abs(guess**3 - 8120601) < 0.1


def test_approximate_cube_root_fail():
    # 10000 用這組 epsilon / increment 會失敗
    guess, num_guesses, success = approximate_cube_root(10000, 0.1, 0.01)

    assert success is False
    assert num_guesses == 1000000        # 原程式會嘗試一百萬次
    assert abs(guess**3 - 10000) >= 0.1


def test_print_approximate_cube_root_success(capsys):
    # 測試印出成功的版本（cube = 27）
    print_approximate_cube_root(27, 0.1, 0.01)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    # 這些字串要和原 script 輸出一樣
    assert lines[0] == "num_guesses = 300"
    assert lines[1] == "2.99999999999998 is close to the cube root of 27"


def test_print_approximate_cube_root_fail(capsys):
    # 測試印出失敗的版本（cube = 10000）
    print_approximate_cube_root(10000, 0.1, 0.01)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert lines[0] == "num_guesses = 1000000"
    assert lines[1] == "Failed on cube root of 10000 with these parameters."
