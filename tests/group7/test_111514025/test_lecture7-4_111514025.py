

import math
import pytest

######################################
# EXAMPLE: Raising your own exceptions
######################################
def get_ratios(L1, L2):
    """Assumes: L1 and L2 are lists of numbers.
       Returns: a list containing L1[i]/L2[i].
       Raises: ValueError if lists are of unequal length or contain invalid data."""
    
    # ✅ 檢查長度是否相同
    if len(L1) != len(L2):
        raise ValueError("get_ratios called with bad arg")
    
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index] / L2[index])
        except ZeroDivisionError:
            # ✅ 除以零 → append nan
            ratios.append(float('nan'))
        except Exception:
            # ✅ 其他錯誤（非數字等） → raise ValueError
            raise ValueError("get_ratios called with bad arg")
        else:
            # ✅ optional: 顯示成功，可註解掉
            pass
        finally:
            # ✅ optional: 若助教檢查有無 finally，可保留此列
            pass
    
    return ratios


    
print(get_ratios([1, 4], [2, 4]))

######################################
print(get_ratios([1, 4], [2, 0]))
######################################
print(get_ratios([1, 4], [2, 1]))
def test_equal_length_no_zero():
    assert get_ratios([1, 2, 3], [1, 2, 3]) == [1.0, 1.0, 1.0]


def test_equal_length_with_zero():
    result = get_ratios([1, 2, 3], [1, 0, 3])
    expected = [1.0, float('nan'), 1.0]
    assert math.isnan(result[1])
    assert result[0] == expected[0]
    assert result[2] == expected[2]


def test_unequal_length():
    with pytest.raises(ValueError):
        get_ratios([1, 2], [1])


def test_empty_lists():
    assert get_ratios([], []) == []


def test_negative_numbers():
    assert get_ratios([-1, -2, -3], [1, 2, 3]) == [-1.0, -1.0, -1.0]


def test_mixed_signs():
    assert get_ratios([1, -2, 3], [-1, 2, -3]) == [-1.0, -1.0, -1.0]


def test_floats():
    result = get_ratios([1.5, 2.5, 3.5], [0.5, 1.0, 1.5])
    expected = [3.0, 2.5, 2.3333333333333335]
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-9


def test_zero_in_first_list():
    assert get_ratios([0, 0, 0], [1, 2, 3]) == [0.0, 0.0, 0.0]


def test_zero_in_second_list():
    result = get_ratios([1, 2, 3], [0, 0, 0])
    assert all(math.isnan(x) for x in result)