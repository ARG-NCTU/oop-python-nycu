# lyrics_to_frequencies 函式與測試
def lyrics_to_frequencies(lyrics):
    freq = {}
    for word in lyrics:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def test_lyrics_to_frequencies():
    # 基本詞頻測試
    lyrics = ["you", "say", "yes", "I", "say", "no", "you", "say", "stop"]
    freq = lyrics_to_frequencies(lyrics)
    assert freq["say"] == 3
    assert freq["you"] == 2
    assert freq["stop"] == 1

    # 空歌詞列表
    assert lyrics_to_frequencies([]) == {}

    # 單一詞
    assert lyrics_to_frequencies(["hello"]) == {"hello": 1}

    # 重複相同詞
    assert lyrics_to_frequencies(["a", "a", "a"]) == {"a": 3}


# ✅ 高品質實作與測試：河內塔 towers 函式與測試
def towers(n, fr, to, spare, moves=None):
    if moves is None:
        moves = []
    if n == 1:
        moves.append((fr, to))
    else:
        towers(n-1, fr, spare, to, moves)
        towers(1, fr, to, spare, moves)
        towers(n-1, spare, to, fr, moves)
    return moves

def test_towers_moves():
    # 3 盤測試：應該有 7 步
    result = towers(3, 'A', 'C', 'B')
    assert len(result) == 7
    assert result == [
        ('A', 'C'),
        ('A', 'B'),
        ('C', 'B'),
        ('A', 'C'),
        ('B', 'A'),
        ('B', 'C'),
        ('A', 'C')
    ]

    # 1 盤測試
    assert towers(1, 'X', 'Y', 'Z') == [('X', 'Y')]

    # 2 盤測試
    assert towers(2, 'L', 'R', 'M') == [('L','M'),('L','R'),('M','R')]
