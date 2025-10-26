
#
########################################
### EXAMPLE: Buggy code to get a list of primes
### Try to debug it! (fixes needed are explained below)
########################################
##def primes_list_buggy(n):
##    """
##    input: n an integer > 1
##    returns: list of all the primes up to and including n
##    """
##    # initialize primes list
##    if i == 2:
##        primes.append(2)
##    # go through each elem of primes list
##    for i in range(len(primes)):
##        # go through each of 2...n
##        for j in range(len(n)):
##            # check if not divisible by elem of list
##            if i%j != 0:
##                primes.append(i)
#
#
## FIXES: --------------------------
## = invalid syntax, variable i unknown, variable primes unknown
## can't apply 'len' to an int
## division by zero -> iterate through elems not indices
##                  -> iterate from 2 not 0
## forgot to return 
## primes is empty list for n > 2
## n = 3 goes through loop once -> range to n+1 not n
## infinite loop -> append j not i
##               -> list is getting modified as iterating over it!
##               -> switch loops around
## n = 4 adds 4 -> need way to stop going once found a divisible num
##              -> use a flag
## --------------------------
def primes_list(n):
    """
    input: n an integer > 1
    returns: list of all the primes up to and including n
    """
    # initialize primes list
    primes = [2]
    # go through each of 3...n
    for j in range(3,n+1):
        is_div = False
        # go through each elem of primes list
        for p in primes:
            if j%p == 0:
                is_div = True
        if not is_div:
            primes.append(j)
    return primes

print(primes_list(2) )               
print(primes_list(15)  )              


def test_primes_list():
    assert primes_list(2) == [2]
    assert primes_list(3) == [2, 3]
    assert primes_list(10) == [2, 3, 5, 7]
    assert primes_list(20) == [2, 3, 5, 7, 11, 13, 17, 19]