def rev_list_buggy(L):
    """
    input: L, a list
    Modifies L such that its elements are in reverse order
    returns: nothing
    """
    for i in range(len(L) // 2):
        L[i], L[-1-i] = L[-1-i], L[i]
    
L = [1,2,3,4]
rev_list_buggy(L)
print(L)

# =============================================================================

def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    
    print(L1)
    print(L2)
    try:
        assert len(L1) == len(L2)
    except:
        # raise ValueError("兩列表要一樣長喔") # 這樣會顯示錯誤訊息然後中斷
        print("兩列表要一樣長喔")
        return [];
    

    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        # except:
        #     raise ValueError('get_ratios called with bad arg')
        else:
            print("success")
        finally:
            print("executed no matter what!")
    return ratios
    
print(get_ratios([1, 4], [2, 4]))

print(get_ratios([1, 4], [2, 0]))

print(get_ratios([1, 4], [5, 6, 7]))

import pdb
pdb.set_trace()
# 'c' to run the code
# stop the code by typing 'q'