# test_lec11_complexity_part2.py
import pytest
import itertools as it
import lec11_complexity_part2 as lec


# -------------------------
# bisect_search1
# -------------------------

@pytest.mark.parametrize(
    "L,e,expect",
    [
        ([5], 5, True),
        ([5], 4, False),
        ([1, 3, 5, 7, 9], 1, True),     # 最小值
        ([1, 3, 5, 7, 9], 9, True),     # 最大值
        ([1, 3, 5, 7, 9], 6, False),    # 不存在
        ([1, 1, 1, 2, 2, 3], 2, True),  # 重複值
        ([0, 2, 4, 6, 8], -1, False),   # 比最小還小
        ([0, 2, 4, 6, 8], 10, False),   # 比最大還大
    ]
)
def test_bisect_search1_basic(L, e, expect):
    assert lec.bisect_search1(L[:], e) == expect


def test_bisect_search1_empty_behavior():
    """
    原始實作在函式開頭就使用 L[0] 與 L[-1] 進行輸出，
    因此若 L 為空，會觸發 IndexError（而非回傳 False）。
    這裡用測試文件化目前行為。
    """
    with pytest.raises(IndexError):
        lec.bisect_search1([], 42)


# -------------------------
# bisect_search2
# -------------------------

@pytest.mark.parametrize(
    "L,e,expect",
    [
        ([], 1, False),                 # 空清單 => False
        ([5], 5, True),
        ([5], 4, False),
        ([1, 3, 5, 7, 9], 7, True),
        ([1, 3, 5, 7, 9], 6, False),
        ([-5, -2, 0, 7], -5, True),
        ([-5, -2, 0, 7], 8, False),
        ([1, 1, 1, 2, 2, 3], 2, True),
    ]
)
def test_bisect_search2_basic(L, e, expect):
    assert lec.bisect_search2(L[:], e) == expect


def test_bisect_search2_verbose_output(capsys):
    lec.bisect_search2([1, 3, 5], 3)
    out = capsys.readouterr().out
    assert "low:" in out and "high:" in out  # 有列印範圍資訊


def test_bisect_requires_sorted_behavior():
    """
    若輸入未排序，二分搜尋的結果不可靠。
    用線性搜尋的正確性對照，確認未排序時可能會失敗。
    """
    L = [4, 1, 3, 2]  # 未排序
    # 正確答案：存在 1
    assert 1 in L
    # bisect_search2 在未排序時可能回傳 False（這裡很可能 False）
    result = lec.bisect_search2(L, 1)
    # 不強制規定必須錯，但至少不是可靠的 True
    assert result in (False, True)
    # 用註解提醒此行為
    # 若你將清單排序，bisect_search2 才有保證：
    assert lec.bisect_search2(sorted(L), 1) is True


# -------------------------
# genSubsets
# -------------------------

def _as_set_of_frozensets(list_of_lists):
    """將 [[...], [...]] 轉成 {frozenset(...), ...}，方便比較不計順序"""
    return {frozenset(x) for x in list_of_lists}

@pytest.mark.parametrize("src", [
    [], [1], [1, 2], [1, 2, 3],
])
def test_genSubsets_size_and_contents(src):
    """
    驗證：
    1) 子集合數量為 2^n
    2) 所有子集合都存在（不計順序）
    3) 無重複
    """
    subsets = lec.genSubsets(src[:])
    # 1) 大小為 2^n
    assert len(subsets) == 2 ** len(src)

    # 2) 內容正確（與 itertools.chain/combinations 建立的 power set 比對）
    expected = []
    for r in range(len(src) + 1):
        for comb in it.combinations(src, r):
            expected.append(list(comb))
    assert _as_set_of_frozensets(subsets) == _as_set_of_frozensets(expected)

    # 3) 無重複（集合大小不變）
    assert len(_as_set_of_frozensets(subsets)) == len(subsets)


def test_genSubsets_example_order_is_not_required():
    """
    不強制要求回傳順序；只要集合內容正確即可。
    測一個有 4 個元素的例子，重點放在內容與數量。
    """
    src = [1, 2, 3, 4]
    subsets = lec.genSubsets(src)
    assert len(subsets) == 16
    # 檢查幾個特定子集合是否存在
    want = [
        [], [1], [4], [1, 4], [2, 3], [1, 2, 3, 4]
    ]
    aset = _as_set_of_frozensets(subsets)
    for w in want:
        assert frozenset(w) in aset
