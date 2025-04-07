from matrix2 import Matrix2

def test_addition():
    m1 = Matrix2(1, 2, 3, 4)
    m2 = Matrix2(5, 6, 7, 8)
    result = m1.add(m2)
    assert str(result) == "[6 8]\n[10 12]"

def test_subtraction():
    m1 = Matrix2(5, 6, 7, 8)
    m2 = Matrix2(1, 2, 3, 4)
    result = m1.minus(m2)
    assert str(result) == "[4 4]\n[4 4]"

def test_scalar_multiplication():
    m = Matrix2(1, 2, 3, 4)
    result = m.multiply(2)
    assert str(result) == "[2 4]\n[6 8]"

def test_matrix_multiplication():
    m1 = Matrix2(1, 2, 3, 4)
    m2 = Matrix2(2, 0, 1, 2)
    result = m1.multiply_matrix(m2)
    assert str(result) == "[4 4]\n[10 8]"

def test_determinant():
    m = Matrix2(1, 2, 3, 4)
    assert m.det() == -2

def test_trace():
    m = Matrix2(1, 2, 3, 4)
    assert m.trace() == 5

if __name__ == "__main__":
    test_addition()
    test_subtraction()
    test_scalar_multiplication()
    test_matrix_multiplication()
    test_determinant()
    test_trace()
    print("All tests passed.")