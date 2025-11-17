from lec3_for_loops_113511088 import find_perfect_cube_root, print_cube_root


def test_find_perfect_cube_root_27():
    # 27 = 3^3
    assert find_perfect_cube_root(27) == 3


def test_find_perfect_cube_root_large():
    # 8120601 = 201^3
    assert find_perfect_cube_root(8120601) == 201


def test_find_perfect_cube_root_negative():
    # -27 = (-3)^3
    assert find_perfect_cube_root(-27) == -3


def test_find_perfect_cube_root_not_perfect():
    # 28 不是 perfect cube
    assert find_perfect_cube_root(28) is None


def test_print_cube_root_perfect(capsys):
    # 測輸出格式：perfect cube
    print_cube_root(27)
    captured = capsys.readouterr()
    # out 會包含換行，所以用 strip() 去掉
    assert captured.out.strip() == "Cube root of 27 is 3"


def test_print_cube_root_not_perfect(capsys):
    # 測輸出格式：不是 perfect cube
    print_cube_root(28)
    captured = capsys.readouterr()
    assert captured.out.strip() == "28 is not a perfect cube"
