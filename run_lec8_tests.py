import sys
import os

# Add directory to path to find components
current_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.join(current_dir, 'tests', 'group11')
sys.path.append(target_dir)

try:
    from lec8_classes import Fraction
    print("Import success")

    f1 = Fraction(1, 4)
    f2 = Fraction(3, 4)

    # Test add
    f3 = f1 + f2
    f3_red = f3.reduce()
    assert f3_red.num == 1 and f3_red.denom == 1, f"Add failed: {f3}"
    print("Add passed")

    # Test sub
    f4 = f2 - f1
    f4_red = f4.reduce()
    assert f4_red.num == 1 and f4_red.denom == 2, f"Sub failed: {f4}"
    print("Sub passed")

    # Test mul
    f5 = f1 * f2
    assert f5.num == 3 and f5.denom == 16, f"Mul failed: {f5}"
    print("Mul passed")

    # Test div
    f6 = f1 / f2 # 1/4 / 3/4 = 1/3 ?? No, 1/4 * 4/3 = 4/12
    f6_red = f6.reduce()
    assert f6_red.num == 1 and f6_red.denom == 3, f"Div failed: {f6} -> {f6_red}"
    print("Div passed")

    # Test eq
    assert Fraction(1, 2) == Fraction(2, 4), "Eq failed"
    print("Eq passed")

    print("ALL LEC 8 TESTS PASSED")

except Exception as e:
    print(f"FAILED: {e}")
    import traceback
    traceback.print_exc()
