import random
import math
import pytest
from lec4_module import roll_die, run_sim, same_date, birthday_prob

# ---------- fixtures ----------
@pytest.fixture(autouse=True)
def fixed_seed():
    random.seed(42)

# ---------- roll_die ----------
def test_roll_die_range_and_freq():
    results = [roll_die() for _ in range(6000)]
    # 範圍
    assert all(1 <= r <= 6 for r in results)
    # 粗略頻率檢查（期望各 ~1000 次）
    for pips in range(1, 7):
        assert results.count(pips) == pytest.approx(1000, rel=0.2)

# ---------- run_sim ----------
def test_run_sim_output_and_value(capsys):
    goal = '111'
    est = run_sim(goal, 10_000, goal)   # 改過原始碼就能回傳
    captured = capsys.readouterr().out
    assert 'Actual probability of' in captured
    assert 'Estimated Probability of' in captured
    # 理論機率 1/216 ≈ 0.00462963
    assert est == pytest.approx(1/216, rel=0.2)

# ---------- same_date ----------
@pytest.mark.parametrize(
    'num_people, num_same, expected',
    [(2, 2, False),     # 不可能撞日
     (366, 2, True)]    # 鴿籠原理必撞
)
def test_same_date_edge(num_people, num_same, expected):
    assert same_date(num_people, num_same) is expected

# ---------- birthday_prob ----------
@pytest.mark.parametrize('n', [10, 20, 40, 100])
def test_birthday_prob_matches_theory(n):
    est = birthday_prob(n, 2, 20_000)
    # 理論計算
    numerator = math.factorial(366)
    denom = (366 ** n) * math.factorial(366 - n)
    theoretical = 1 - numerator / denom
    assert est == pytest.approx(theoretical, abs=0.05)
