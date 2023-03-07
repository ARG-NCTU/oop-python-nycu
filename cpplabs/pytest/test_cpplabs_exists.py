import importlib

def test_cpplabs_exists():
    try:
        assert importlib.util.find_spec("cpplabs") is not None
    except ImportError:
        assert False, "cpplabs package not found"