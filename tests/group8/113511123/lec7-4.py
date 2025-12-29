import pytest
import math

# --- 被測試的函式 (SUT: System Under Test) ---
def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) # nan = Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
        else:
            # 測試時通常不建議保留 print，除非為了除錯，這裡保留是為了符合原題意
            print("success")
        finally:
            print("executed no matter what!")
    return ratios

# --- 測試案例 (Test Cases) ---

# 1. 快樂路徑 (Happy Path)：最一般的正常情況
def test_equal_length_no_zero():
    assert get_ratios([1, 2, 3], [1, 2, 3]) == [1.0, 1.0, 1.0]

# 2. 異常處理測試：除以零的情況
# 重點：NaN (Not a Number) 不能直接用 == 比較，必須用 math.isnan()
def test_equal_length_with_zero():
    result = get_ratios([2, 2, 3], [1, 0, 3])
    expected_val_0 = 2.0
    expected_val_2 = 1.0
    
    assert result[0] == expected_val_0
    assert math.isnan(result[1])  # 檢查是否正確產生了 nan
    assert result[2] == expected_val_2

# 3. 異常處理測試：捕捉 ValueError
# 這是用來測試原程式碼中 `except:` 區塊是否正確 raise 出錯誤
def test_unequal_length():
    with pytest.raises(ValueError):
        get_ratios([1, 2], [1])

# 4. 邊界測試 (Edge Case)：空列表
def test_empty_lists():
    assert get_ratios([], []) == []

# 5. 數學邏輯測試：負數
def test_negative_numbers():
    assert get_ratios([-1, -2, -3], [1, 2, 3]) == [-1.0, -1.0, -1.0]

def test_mixed_signs():
    assert get_ratios([1, -2, 3], [-1, 2, -3]) == [-1.0, -1.0, -1.0]

# 6. 浮點數精度測試
# 重點：浮點數運算會有微小誤差，不能直接用 ==，要用 abs(a-b) < 誤差值
def test_floats():
    result = get_ratios([1.5, 2.5, 3.5], [0.5, 1.0, 1.5])
    expected = [3.0, 2.5, 2.3333333333333335]
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-9

# 7. 更多零的邊界測試
def test_zero_in_first_list():
    assert get_ratios([0, 0, 0], [1, 2, 3]) == [0.0, 0.0, 0.0]

def test_zero_in_second_list():
    result = get_ratios([1, 2, 3], [0, 0, 0])
    assert all(math.isnan(x) for x in result)