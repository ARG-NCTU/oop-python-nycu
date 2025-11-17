import pytest

from lec4_functions_113511088 import (
    is_even_with_return,
    is_even_without_return,
    is_even,
    print_even_or_not_upto,
)


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

    # 不應該有回傳值
    assert result is None
    # 會印出 without return
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

    # 第一行標題
    assert lines[0] == "All numbers between 0 and 6: even or not"

    # 後面 6 行是 0~5 的奇偶
    expected = [
        "0 even",
        "1 odd",
        "2 even",
        "3 odd",
        "4 even",
        "5 odd",
    ]
    assert lines[1:] == expected
