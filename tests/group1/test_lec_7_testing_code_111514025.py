import pytest, math

# -------------------------------
# 1. Reverse a list in-place
# -------------------------------
def rev_list(L):
    """
    Reverses the list L in place.
    """
    for i in range(len(L) // 2):
        L[i], L[-1 - i] = L[-1 - i], L[i]

# 測試 reverse function
L = [1, 2, 3, 4]
rev_list(L)
print("Reversed List:", L)


# -------------------------------
# 2. Get element-wise ratios of two lists
# -------------------------------
def get_ratios(L1, L2):
    """
    Returns a list of L1[i] / L2[i] for each i.
    If L2[i] == 0, puts NaN.
    If lengths differ, prints error and returns empty list.
    """
    print("L1:", L1)
    print("L2:", L2)

    if len(L1) != len(L2):
        print("兩列表要一樣長喔")
        return []

    ratios = []
    for i in range(len(L1)):
        try:
            ratio = L1[i] / L2[i]
            ratios.append(ratio)
        except ZeroDivisionError:
            ratios.append(float('nan'))
        else:
            print("success")
        finally:
            print("executed no matter what!")

    return ratios

# -------------------------------
# Pytest Test Cases
# -------------------------------

@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3], [3, 2, 1]),
    ([1], [1]),
    ([], []),
    ([10, 20, 30, 40], [40, 30, 20, 10])
])
def test_rev_list(input_list, expected):
    rev_list(input_list)
    assert input_list == expected


@pytest.mark.parametrize("L1, L2, expected", [
    ([1, 2], [1, 2], [1.0, 1.0]),
    ([1, 4], [2, 0], [0.5, float('nan')]),
    ([10, 20, 30], [2, 5, 6], [5.0, 4.0, 5.0]),
    ([1, 2], [1], []),  # length mismatch returns empty
])
def test_get_ratios(L1, L2, expected):
    result = get_ratios(L1, L2)
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        if math.isnan(e):
            assert math.isnan(r)
        else:
            assert r == pytest.approx(e)
# -------------------------------
# 測試 get_ratios function
# -------------------------------
if __name__ == "__main__":
    print("Result 1:", get_ratios([1, 4], [2, 4]))      # 正常
    print("Result 2:", get_ratios([1, 4], [2, 0]))      # 除以 0
    print("Result 3:", get_ratios([1, 4], [5, 6, 7]))    # 長度不同
