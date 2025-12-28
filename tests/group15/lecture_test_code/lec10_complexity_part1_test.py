import pytest
import lec10_complexity_part1 as lec


@pytest.mark.parametrize(
    "L,e,expect",
    [
        ([], 1, False),                         # 空清單
        ([1], 1, True),                         # 單一元素，命中
        ([1], 2, False),                        # 單一元素，未命中
        ([1, 3, 4, 5, 9, 18, 27], 9, True),     # 中間命中
        ([1, 3, 4, 5, 9, 18, 27], 28, False),   # 不存在
        ([-3, -1, 0, 2], -1, True),             # 負數命中
    ],
)
def test_linear_search(L, e, expect):
    assert lec.linear_search(L, e) == expect


# ---------- search (假設 L 已排序遞增) ----------

@pytest.mark.parametrize(
    "L,e,expect",
    [
        ([], 1, False),                 # 空清單
        ([1], 1, True),                 # 命中
        ([1], 2, False),                # 未命中
        ([1, 3, 4, 5, 9], 4, True),     # 中間命中
        ([1, 3, 4, 5, 9], 2, False),    # 早停：遇到 3 > 2 直接 False
        ([1, 3, 4, 5, 9], 10, False),   # 大於最大值，掃到結尾
        ([-5, -2, 0, 7], -3, False),    # 負數範圍內早停
    ],
)
def test_search_sorted_increasing(L, e, expect):
    assert lec.search(L, e) == expect


def test_search_assumes_sorted_behavior():
    """
    若 L 未排序，此函式的行為不可靠（設計上假設遞增排序）。
    這裡僅確認：在未排序情況下，可能得到與線性搜尋不同的結果。
    """
    L = [3, 1, 4]  # 未排序
    # 正確答案（線性掃描）應為 True
    assert lec.linear_search(L, 1) is True
    # search 可能早停造成 False（這裡因為 3 > 1 直接回傳 False）
    assert lec.search(L, 1) is False


# ---------- isSubset ----------

def test_isSubset_basic_true():
    assert lec.isSubset([1, 5, 3], [1, 2, 3, 4, 5]) is True

def test_isSubset_basic_false():
    assert lec.isSubset([1, 6], [1, 2, 3, 4, 5]) is False

def test_isSubset_edge_cases():
    assert lec.isSubset([], []) is True                  # 空是任何集合子集合
    assert lec.isSubset([], [1, 2, 3]) is True          # 空是子集合
    assert lec.isSubset([1], []) is False               # 非空不可能是空的子集合

def test_isSubset_ignores_multiplicity():
    """
    此實作不考慮多重度（像 set 子集合）。[1,1] 對 [1] 仍會回 True。
    """
    assert lec.isSubset([1, 1], [1]) is True


# ---------- intersect ----------

def test_intersect_basic():
    assert lec.intersect([1, 2, 3], [2, 3, 4]) == [2, 3]

def test_intersect_unique_and_order_by_L1():
    """
    intersect 先收集所有相等元素到 tmp，再去重到 res。
    因此結果：
      1) 只包含唯一元素（去重）
      2) 元素順序以 L1 的出現順序為準
    """
    L1 = [3, 1, 2, 2, 1, 3]
    L2 = [2, 2, 3, 5, 1]
    # L1 中相交元素出現順序：3 -> 1 -> 2 -> (2/1/3 之後因去重不再加入)
    assert lec.intersect(L1, L2) == [3, 1, 2]

def test_intersect_no_overlap():
    assert lec.intersect([7, 8], [1, 2, 3]) == []

def test_intersect_with_negatives():
    assert lec.intersect([-2, -1, 0, 1], [-1, 1, 2]) == [-1, 1]
