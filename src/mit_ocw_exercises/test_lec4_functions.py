# src/mit_ocw_exercises/test_lec4_functions.py
# 測試對象：src/mit_ocw_exercises/lec4_functions.py
# 目標：不依賴第三方套件、無 I/O、可在課堂環境直接跑

import math
import pytest

from .lec4_functions import (
    iter_power,
    recur_power,
    gcd_iter,
    gcd_recur,
    is_in,
    apply_to_each,
    eval_poly,
    bisection_cuberoot_approx,
    is_even,         # 可選，但我們也一併測
)

# ---------- power ----------

@pytest.mark.parametrize(
    "base,exp,expected",
    [
        (2, 0, 1.0),
        (2, 1, 2.0),
        (2, 10, 1024.0),
        (5, 3, 125.0),
        (0.5, 2, 0.25),
        (1.1, 4, 1.1**4),
    ],
)
def test_iter_power_basic(base, exp, expected):
    assert math.isclose(iter_power(base, exp), expected, rel_tol=1e-12, abs_tol=1e-12)


@pytest.mark.parametrize(
    "base,exp",
    [
        (2, 0),
        (2, 10),
        (3.14, 5),
        (0.5, 8),
    ],
)
def test_recur_power_matches_iter(base, exp):
    assert math.isclose(recur_power(base, exp), iter_power(base, exp), rel_tol=1e-12, abs_tol=1e-12)


@pytest.mark.parametrize("base", [2, 3.3, 0.5])
@pytest.mark.parametrize("exp", [-1, -2, -7])
def test_power_negative_exp_raises(base, exp):
    with pytest.raises(ValueError):
        iter_power(base, exp)
    with pytest.raises(ValueError):
        recur_power(base, exp)


# ---------- gcd ----------

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),     # 慣例上 gcd(0,0)=0
        (0, 5, 5),
        (12, 0, 12),
        (12, 18, 6),
        (18, 12, 6),
        (54, 24, 6),
        (101, 103, 1),
        (-24, 18, 6),
        (24, -18, 6),
        (-24, -18, 6),
    ],
)
def test_gcd_values(a, b, expected):
    assert gcd_iter(a, b) == expected
    assert gcd_recur(a, b) == expected


def test_gcd_basic_properties():
    # 對稱性與同一性
    for a, b in [(15, 10), (10, 15), (27, 9), (7, 7), (0, 9), (9, 0)]:
        assert gcd_iter(a, b) == gcd_iter(b, a)
        assert gcd_recur(a, b) == gcd_recur(b, a)
        # 與 iter 一致
        assert gcd_iter(a, b) == gcd_recur(a, b)


# ---------- is_in (binary-search style on sorted string) ----------

def test_is_in_basic_true_false():
    s = "aabbccddeeffgg"
    assert is_in("a", s) is True
    assert is_in("g", s) is True
    assert is_in("z", s) is False
    assert is_in("A", s) is False  # 大小寫不同


def test_is_in_edges_empty_and_singleton():
    assert is_in("x", "") is False
    assert is_in("", "") is False  # 只接受單一字元，空字元一律 False
    assert is_in("a", "a") is True
    assert is_in("b", "a") is False


# ---------- apply_to_each ----------

def test_apply_to_each_square_and_abs():
    data = [-2, -1, 0, 3]
    out1 = apply_to_each(data, lambda x: x * x)
    assert out1 == [4, 1, 0, 9]
    out2 = apply_to_each(data, abs)
    assert out2 == [2, 1, 0, 3]
    # 原始 list 不應被修改（我們定義成回傳新清單）
    assert data == [-2, -1, 0, 3]


# ---------- eval_poly (Horner) ----------

@pytest.mark.parametrize(
    "coeffs,x,expected",
    [
        ([0], 10, 0.0),
        ([5], -3, 5.0),                      # 常數多項式
        ([1, 2], 3, 1 + 2*3),                # 1 + 2x
        ([2, 0, 3], 2, 2 + 0*2 + 3*(2**2)),  # 2 + 3x^2
        ([1, -3, 2], 5, 1 - 3*5 + 2*(5**2)), # 1 - 3x + 2x^2
    ],
)
def test_eval_poly_values(coeffs, x, expected):
    assert math.isclose(eval_poly(coeffs, x), expected, rel_tol=1e-12, abs_tol=1e-12)


def test_eval_poly_zero_x_and_high_degree():
    # (x^5 - 3x^3 + 2x) 在 x=0
    coeffs = [0, 2, 0, -3, 0, 1]  # a0..a5
    assert eval_poly(coeffs, 0) == 0.0
    # 在 x=1
    assert eval_poly(coeffs, 1) == (0 + 2 + 0 - 3 + 0 + 1)  # =0


# ---------- bisection_cuberoot_approx ----------

@pytest.mark.parametrize(
    "x,eps,target",
    [
        (0, 1e-6, 0.0),
        (1, 1e-6, 1.0),
        (8, 1e-6, 2.0),
        (27, 1e-6, 3.0),
        (1e6, 1e-6, 100.0),
    ],
)
def test_bisection_cuberoot_accuracy(x, eps, target):
    got = bisection_cuberoot_approx(x, eps)
    assert abs(got - target) <= max(eps, 1e-6)
    # 立方回代也應該接近
    assert abs(got**3 - x) < max(10*eps, 1e-6)


@pytest.mark.parametrize("x", [-1, -8, -27])
def test_bisection_negative_raises(x):
    with pytest.raises(ValueError):
        bisection_cuberoot_approx(x, 1e-3)


# ---------- is_even ----------

@pytest.mark.parametrize(
    "n,expected",
    [
        (0, True),
        (1, False),
        (2, True),
        (101, False),
        (-2, True),
        (-3, False),
    ],
)
def test_is_even(n, expected):
    assert is_even(n) is expected

