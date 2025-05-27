# test_dua_cheer.py
import runpy
import pytest

def run_cheer(word, times, capsys, monkeypatch):
    """
    執行 dua_cheer.py 並回傳輸出結果的字串。
    """
    inputs = [word, str(times)]
    monkeypatch.setattr('builtins.input', lambda prompt='': inputs.pop(0))
    # 重新執行腳本
    runpy.run_path('dua_cheer.py', run_name='__main__')
    out = capsys.readouterr().out
    return out

@pytest.mark.parametrize("word, times, expected_lines", [
    # 測試單一元音字母
    ("a", 1, [
        "Give me an a! a",
        "What does that spell?",
        "a !!!"
    ]),
    # 測試單一子音字母
    ("b", 2, [
        "Give me a b! b",
        "What does that spell?",
        "b !!!",
        "b !!!"
    ]),
    # 測試多字母字串
    ("Ab", 3, [
        "Give me an A! A",  # A 在 an_letters 內
        "Give me a b! b",
        "What does that spell?",
        "Ab !!!",
        "Ab !!!",
        "Ab !!!",
    ]),
    # 測試大小寫混合
    ("XyZ", 1, [
        "Give me an X! X",  # X 在 an_letters 內
        "Give me a y! y",
        "Give me a Z! Z",
        "What does that spell?",
        "XyZ !!!",
    ]),
])
def test_cheer_outputs(word, times, expected_lines, capsys, monkeypatch):
    out = run_cheer(word, times, capsys, monkeypatch)
    # 檢查每一行是否出現在輸出中，且順序正確
    lines = [line for line in out.splitlines() if line.strip()]
    for idx, expected in enumerate(expected_lines):
        assert lines[idx] == expected

def test_invalid_enthusiasm(monkeypatch, capsys):
    # 測試 enthusiasm level 非整數會拋出 ValueError
    monkeypatch.setattr('builtins.input', lambda prompt='': "hello")  # 第一次輸入字串
    # 第二次輸入也非整數
    monkeypatch.setattr('builtins.input', lambda prompt='': "not_an_int")
    with pytest.raises(ValueError):
        runpy.run_path('dua_cheer.py', run_name='__main__')
