import add_path
import mit_ocw_exercises.lec4_functions as lec4_functions

# is_even_with_return
def test_is_even_with_return_even():
    assert lec4_functions.is_even_with_return(4) is True

def test_is_even_with_return_odd():
    assert lec4_functions.is_even_with_return(5) is False

# is_even_without_return (no return value)
def test_is_even_without_return(capsys):
    lec4_functions.is_even_without_return(4)
    out, _ = capsys.readouterr()
    assert "without return" in out

# is_even
def test_is_even_even():
    assert lec4_functions.is_even(2) is True

def test_is_even_odd():
    assert lec4_functions.is_even(3) is False

# bisection_cuberoot_approx
def test_bisection_cuberoot_approx():
    result = lec4_functions.bisection_cuberoot_approx(27, 0.01)
    assert abs(result - 3) < 0.01

# func_a, func_b, func_c
def test_func_a(capsys):
    lec4_functions.func_a()
    out, _ = capsys.readouterr()
    assert "inside func_a" in out

def test_func_b():
    assert lec4_functions.func_b(10) == 10

def test_func_c(capsys):
    def dummy():
        print("dummy")
    lec4_functions.func_c(dummy)
    out, _ = capsys.readouterr()
    assert "inside func_c" in out

# f (function object version)
def test_f_function_object():
    func = lec4_functions.f()
    assert func(2, 3) == 5

# f (scope version)
def test_f_scope(capsys):
    lec4_functions.f(10)
    out, _ = capsys.readouterr()
    assert "2" in out  # x is incremented from 1 to 2

def test_g_scope(capsys):
    global_x = 5
    lec4_functions.x = global_x  # set module-level x
    lec4_functions.g(10)
    out, _ = capsys.readouterr()
    assert "in g(x): x =  11" in out
    assert "in h(x): x =  12" in out

# h (scope version, does nothing)
def test_h_scope():
    assert lec4_functions.h(10) is None

# g (hader scope example)
def test_g_hader_scope(capsys):
    result = lec4_functions.g(2)
    out, _ = capsys.readouterr()
    assert "in g(x): x =" in out
    assert isinstance(result, int)

# f (complicated scope)
def test_f_complicated_scope(capsys):
    result = lec4_functions.f(2)
    out, _ = capsys.readouterr()
    assert "in f(x): x =" in out
    assert isinstance(result, int)

# g (complicated scope)
def test_g_complicated_scope(capsys):
    result = lec4_functions.g(2)
    out, _ = capsys.readouterr()
    assert "in g(x): x =" in out
    assert isinstance(result, int)
