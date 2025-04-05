def fib (n):

    if n == 0 or n ==1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fast_fib (n, memo = {}):
    if n == 0 or n ==1 :
        return 1     
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fast_fib(n-1, memo) + fast_fib(n-2, memo)
        return memo[n]
    
def main ():
    for i in range(36):
        print("fib(" + str(i) + ") =" + str(fib(i)))
    for i in range(36):
        print("fib(" + str(i) + ") =" + str(fast_fib(i)))

if __name__ == "__main__":
    main()