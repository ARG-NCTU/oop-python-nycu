
class fib(object):

    def __init__(self,n):
        self.n=n

    def fib(n):
        if n < 0:
            print("Incorrect input")
        elif n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return Fibonacci(n-1) + Fibonacci(n-2)
