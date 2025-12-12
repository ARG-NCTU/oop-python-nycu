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

    C3 = Coordinate(-1,-1)
    C4 = Coordinate(2,3)
    assert C3.x == -1 and C3.y == -1
    assert C4.x == 2 and C4.y == 3
    assert C3.distance(C4) == ((-1-2)**2+(-1-3)**2)**0.5  # (3^2 + 4^2) ** 0.5 = 5.0
    assert str(C3) == "<-1,-1>"
    assert str(C4) == "<2,3>"

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

    I = Fraction(-1,2)
    J = Fraction(3,-4)
    K = I + J
    L = I - J
    M = I.inverse()
    N = J.inverse()

    O = Fraction(0,5)
    P = Fraction(-3,-1)

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

    assert K.num == 10 and K.denom == -8
    assert L.num == -2 and L.denom == -8
    assert str(I) == "-1/2"
    assert str(J) == "3/-4"
    assert str(K) == "10/-8"
    assert str(L) == "-2/-8"
    assert float(I) == -0.5
    assert float(J) == -0.75
    assert float(K) == -1.25
    assert float(L) == 0.25

    assert M.num == 2 and M.denom == -1
    assert N.num == -4 and N.denom == 3
    assert str(M) == "2/-1"
    assert str(N) == "-4/3"
    assert float(M) == -2.0
    assert float(N) == -4/3

    assert str(O) == "0/5"
    assert float(O) == 0.0
    assert str(P) == "-3/-1"
    assert float(P) == 3.0


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
    S.insert(-2)
    assert str(S) == "{-2,4,6}"
    assert S.member(4) == True
    assert S.member(5) == False
    try:
        S.remove(-2)
        assert str(S) == "{4,6}"
    except ValueError as e:
        assert False


