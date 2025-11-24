from functions_scope_113511070 import bisection_cuberoot_approx

def test_cube_root_27():
    approx = bisection_cuberoot_approx(27, 0.01)
    assert abs(approx - 3) < 0.1
