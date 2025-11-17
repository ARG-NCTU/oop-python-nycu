import pytest

from lec4_functions_113511088 import g, harder_scope_example


def test_g_prints_and_returns(capsys):
    # 呼叫 g(3) 應該：
    #   1. 印出 "in g(x): x = 4"
    #   2. 回傳 4
    z = g(3)
    captured = capsys.readouterr()
    assert captured.out.strip() == "in g(x): x = 4"
    assert z == 4


def test_harder_scope_example_outer_x_unchanged():
    # harder_scope_example() 內部做：
    #   x = 3
    #   z = g(x)
    # 期望：
    #   回傳的 x 還是 3
    #   z 變成 4
    x, z = harder_scope_example()
    assert x == 3
    assert z == 4
