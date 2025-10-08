import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.mit_ocw_exercises.lec8_classes import Coordinate,Fraction,intSet
import add_path


# test_Coordinate()
# test if (x,y) is correct
# test if distance is correct
# test if str is correct
def test_Coordinate():
    C1 = Coordinate(9,4)
    C2 = Coordinate(5,3)
    assert C1.x == 9 and C1.y == 4
    assert C2.x == 5 and C2.y == 3
    assert C1.distance(C2) == ((9-5)**2+(4-3)**2)**0.5  # (4^2 + 1^2) ** 0.5 = 4.123105625617661
    assert str(C1) == "<9,4>"
    assert str(C2) == "<5,3>"

#test_fraction()
#test add, sub, str, float, inverse is correct

def test_Fraction():
    A = Fraction(9,4)
    B = Fraction(5,3)
    C = A + B
    D = A - B
    E = A.inverse()
    F = B.inverse()
    G = C.inverse()
    H = D.inverse()

    assert C.num == 47 and C.denom == 12
    assert D.num == 7 and D.denom == 12
    assert str(A) == "9/4"
    assert str(B) == "5/3"
    assert str(C) == "47/12"
    assert str(D) == "7/12"
    assert float(A) == 2.25
    assert float(B) == 5/3
    assert float(C) == 47/12
    assert float(D) == 7/12

    assert E.num == 4 and E.denom == 9
    assert F.num == 3 and F.denom == 5
    assert G.num == 12 and G.denom == 47
    assert H.num == 12 and H.denom == 7
    assert str(E) == "4/9"
    assert str(F) == "3/5"
    assert str(G) == "12/47"
    assert str(H) == "12/7"
    assert float(E) == 4/9
    assert float(F) == 3/5
    assert float(G) == 12/47
    assert float(H) == 12/7

#test_intSet()
# test insert, remove, str is correct
def test_intSet():
    S = intSet()
    assert str(S) == "{}"
    S.insert(3)
    assert str(S) == "{3}"
    S.insert(4)
    S.insert(6)
    assert str(S) == "{3,4,6}"
    S.insert(3)
    assert str(S) == "{3,4,6}"
    S.remove(3)
    assert str(S) == "{4,6}"
    try:
        S.remove(3)
        assert False
    except ValueError as e:
        assert str(e) == "3 not found"


