import pytest

from lec4_functions_113511088 import (
    f,
    g,
    run_f_example,
    run_g_example,
)


def test_f_basic_behavior(capsys):
    # 直接測 f(3)：印一行 + 回傳 4
    z = f(3)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert z == 4
    assert lines == ["in f(x): x = 4"]


def test_run_f_example_full_flow(capsys):
    # 對應：
    # x = 3
    # z = f(x)
    # print('in main program scope: z =', z)
    # print('in main program scope: x =', x)
    x, z = run_f_example()
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert x == 3
    assert z == 4
    assert lines == [
        "in f(x): x = 4",
        "in main program scope: z = 4",
        "in main program scope: x = 3",
    ]


def test_g_basic_behavior(capsys):
    # 直接測 g(3)：印兩行 + 回傳 4
    z = g(3)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert z == 4
    # 注意空格：原本是 print('in g(x): x = ', x) 等寫法
    assert lines == [
        "in g(x): x =  4",
        "in h(x): x =  5",
    ]


def test_run_g_example_full_flow(capsys):
    # 對應：
    # x = 3
    # z = g(x)
    # print('in main program scope: x = ', x)
    # print('in main program scope: z = ', z)
    x, z = run_g_example()
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert x == 3
    assert z == 4
    assert lines == [
        "in g(x): x =  4",
        "in h(x): x =  5",
        "in main program scope: x =  3",
        "in main program scope: z =  4",
    ]
