def eval_quadratic(a, b, c, x):
    """Returns a*x*x + b*x + c"""
    return a*x*x + b*x + c

def clip(lo, x, hi):
    """Returns lo if x < lo, hi if x > hi, else x"""
    return max(lo, min(x, hi))
