from lec3_for_loops_113511088 import (
    guess_and_check_cube_root,
    print_guess_and_check_result,
)


def test_guess_and_check_cube_root_27():
    # 27 = 3^3
    assert guess_and_check_cube_root(27) == 3


def test_guess_and_check_cube_root_large():
    # 8120601 = 201^3
    assert guess_and_check_cube_root(8120601) == 201


def test_guess_and_check_cube_root_negative():
    # -27 = (-3)^3
    assert guess_and_check_cube_root(-27) == -3


def test_guess_and_check_cube_root_not_perfect():
    # 28 不是 perfect cube，應該回傳 None
    assert guess_and_check_cube_root(28) is None


def test_print_guess_and_check_perfect(capsys):
    # 測試輸出格式（perfect cube）
    print_guess_and_check_result(27)
    captured = capsys.readouterr()
    # 去除換行與前後空白
    assert captured.out.strip() == "Cube root of 27 is 3"


def test_print_guess_and_check_not_perfect(capsys):
    # 測試輸出格式（不是 perfect cube）
    print_guess_and_check_result(28)
    captured = capsys.readouterr()
    assert captured.out.strip() == "28 is not a perfect cube"
