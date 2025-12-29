import pytest
import random
import io
import sys
from add_path import add_path
add_path()
# 假設 lec4_module.py 包含您提供的程式碼
from lec4_module import roll_die, same_date, birthday_prob, run_sim, run_birthday_experiments

# ----------------------------- 輔助函數測試 -----------------------------

def test_roll_die_range():
    """測試 roll_die 的輸出是否在 [1, 6] 範圍內"""
    for _ in range(100):
        result = roll_die()
        # 確保結果是一個整數
        assert isinstance(result, int)
        # 確保結果在 1 到 6 之間 (包含邊界)
        assert 1 <= result <= 6

# ----------------------------- 生日問題核心邏輯測試 -----------------------------

def test_same_date_specific_seed():
    """
    測試 same_date 函數在固定 seed 下，結果是否符合預期。
    我們只檢查它的返回值類型，並在確定 seed 下檢查一次結果。
    """
    random.seed(0)  # 固定一個 seed
    # 測試一個預期會返回 True 的情況 (需要足夠的人數)
    # 由於 seed 固定，這裡的 True 必須是可重現的
    assert same_date(num_people=25, num_same=2) is True, "seed=0, 25人, 2人同生日應為 True"

    random.seed(0)
    # 測試一個預期會返回 False 的情況
    assert same_date(num_people=5, num_same=3) is False, "seed=0, 5人, 3人同生日應為 False"

def test_same_date_edge_cases():
    """測試邊界情況"""
    # 測試只有一個人
    assert same_date(num_people=1, num_same=2) is False
    # 測試 num_same=1 (必定為 True)
    assert same_date(num_people=10, num_same=1) is True

# ----------------------------- 模擬結果的穩定性測試 -----------------------------

def test_run_sim_output_format(capsys):
    """測試 run_sim 函數的輸出格式和實際機率是否正確計算"""
    random.seed(1)
    
    # 執行一次模擬
    run_sim("1111", 10000, "測試四個 1")
    
    # 捕獲 print 輸出
    captured = capsys.readouterr()
    output = captured.out

    # 驗證 Actual probability (1/6^4 = 1/1296 ≈ 0.00077160)
    expected_actual_prob = round(1 / (6 ** 4), 8)
    assert f"Actual probability = {expected_actual_prob}" in output

    # 驗證輸出是否包含估計機率
    assert "Estimated probability" in output
    
def test_birthday_prob_stability():
    """
    測試 birthday_prob 函數在固定 seed 下，輸出是否穩定且接近已知範圍。
    """
    random.seed(10)
    # 執行一次模擬
    prob1 = birthday_prob(num_people=23, num_same=2, num_trials=20000)
    
    random.seed(10)
    # 再次執行，確保結果可重現 (由於 seed 相同，結果應該完全一致)
    prob2 = birthday_prob(num_people=23, num_same=2, num_trials=20000)
    
    # 在相同的 seed 和 trial 數下，結果必須相同
    assert prob1 == prob2
    
    # 根據生日問題理論，23 人的機率大約是 0.507。
    # 測試結果必須在合理的範圍內 (例如 0.48 到 0.53 之間)
    assert 0.48 <= prob1 <= 0.53


def test_birthday_prob_return_type():
    """Ensure birthday_prob returns a float in [0, 1]."""
    random.seed(42)
    p = birthday_prob(num_people=23, num_same=2, num_trials=1000)
    assert isinstance(p, float)
    assert 0.0 <= p <= 1.0
