
def quotient_and_remainder(x,y):
    if y == 0:
        raise ZeroDivisionError("division by zero")
    q = x // y
    r = x % y
    
    return (q, r)

