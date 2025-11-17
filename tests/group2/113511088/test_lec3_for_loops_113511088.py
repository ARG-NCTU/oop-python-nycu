from lec3_for_loops_113511088 import cheer_word


def test_cheer_basic_mit(capsys):
    # 測試範例：MIT，times=2
    cheer_word("MIT", 2)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert lines == [
        "Give me an M! M",
        "Give me an I! I",
        "Give me a  T! T",
        "What does that spell?",
        "MIT !!!",
        "MIT !!!",
    ]


def test_cheer_times_count(capsys):
    # 確認 times 真的會控制重複次數
    cheer_word("hi", 3)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    # 最後三行應該都是 "hi !!!"
    assert lines[-3:] == ["hi !!!", "hi !!!", "hi !!!"]


def test_cheer_zero_times(capsys):
    # times = 0 時，只要有前面的口號 & What does that spell?，但沒有 "word !!!"
    cheer_word("OK", 0)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    # 前面兩行是字母 O, K 的口號
    assert lines[0] == "Give me an O! O"   # O 在 AN_LETTERS 裡
    assert lines[1] == "Give me a  K! K"   # K 不在 AN_LETTERS 裡
    assert lines[2] == "What does that spell?"
    # 沒有多的 "OK !!!"
    assert len(lines) == 3
