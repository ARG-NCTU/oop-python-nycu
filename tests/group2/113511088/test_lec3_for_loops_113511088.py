from lec3_for_loops_113511088 import (
    print_i_or_u_by_index,
    print_i_or_u_by_char,
)


def test_print_i_or_u_by_index(capsys):
    # "quiz" 裡面有 u 跟 i，剛好兩個要被印出來
    print_i_or_u_by_index("quiz")
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert lines == [
        "There is an i or u",
        "There is an i or u",
    ]


def test_print_i_or_u_by_char(capsys):
    # 一樣用 "quiz" 測試第二個 for 迴圈版本
    print_i_or_u_by_char("quiz")
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert lines == [
        "There is an i or u",
        "There is an i or u",
    ]


def test_no_i_or_u(capsys):
    # 如果字串裡面沒有 i 或 u，應該完全不會印任何東西
    print_i_or_u_by_index("abc")
    captured = capsys.readouterr()
    assert captured.out == ""

    print_i_or_u_by_char("xyz")
    captured = capsys.readouterr()
    assert captured.out == ""
