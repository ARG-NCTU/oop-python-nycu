########################################
### EXAMPLE: Buggy code to reverse a list
### Try to debug it! (fixes needed are explained below)
########################################
##def rev_list_buggy(L):
##    """
##    input: L, a list
##    Modifies L such that its elements are in reverse order
##    returns: nothing
##    """
##    for i in range(len(L)):
##        j = len(L) - i
##        L[i] = temp
##        L[i] = L[j]
##        L[j] = L[i]
#
## FIXES: --------------------------
## temp unknown
## list index out of range -> sub 1 to j
## get same list back -> iterate only over half
## --------------------------
def rev_list(L):
    """
    input: L, a list
    Modifies L such that its elements are in reverse order
    returns: nothing
    """
    for i in range(len(L)//2):
        j = len(L) - i - 1
        temp = L[i]
        L[i] = L[j]
        L[j] = temp
        
L = [4,324,45,6]
rev_list(L)
print(L)

def test_rev_list():
    L = [5457, 245, 3545, 47, 54]
    rev_list(L)
    assert L == [54, 47, 3545, 245, 5457]
    
    L = ['p', 'b', 's']
    rev_list(L)
    assert L == ['s', 'b', 'p']
    
    L = []
    rev_list(L)
    assert L == []