########################################
### EXAMPLE: Buggy code to reverse a list
### Try to debug it! (fixes needed are explained below)
########################################

##def rev_list_buggy(L):
##  """
##    input: L, a list
##    Modifies L such that its elements are in reverse order
##    returns: nothing
##    """
##    for i in range(len(L)):
##        j = len(L) - i
#3        L[i] = temp
##        L[i] = L[j]
#3        L[j] = temp

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
    for i in range(len(L)//2): ##range(1) only do one time, " / " return float, " // " return lower bound
        j = len(L) - i - 1
        temp = L[i]
        L[i] = L[j]
        L[j] = temp
        
L = [1,'c',3,'a']
rev_list(L)
print(L)
#
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
    for j in range(3,n+1):  ## j go through 3 to n+1
        is_div = False
        # go through each element of primes list
        for p in primes:
            if j%p == 0:
                is_div = True
        if not is_div:
            primes.append(j)    ##append is an operation on the list
    return primes

print(primes_list(2))               
print(primes_list(15))              


######################################
# EXAMPLE: Exceptions and input
######################################
#a = int(input("Tell me one number: "))
#b = int(input("Tell me another number: "))
#print("a/b = ", a/b)
#print("a+b = ", a+b)

try:    ## try to run this code
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
except: ##if there is an error, run this code
    print("Bug in user input.")


try:    ## the code check for errors in every steps, and go to corresponding except once the error occur
    a = int(input("Tell me one number: "))  ##if error here then go to except ValueError
    b = int(input("Tell me another number: "))  ##if no error aat Valuueerror then if error here then go to except ZeroDivisionError
    print("a/b = ", a/b)
    print("a+b = ", a+b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Something went very wrong.")



######################################
# EXAMPLE: Raising your own exceptions
######################################
def get_ratios(L1, L2):             ##note that it's illeagel to use two non designated except simultaneously
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number, but it is still a float type
        except:
            raise ValueError('get_ratios called with bad arg')  #occur some non zerodivisor error, it halt the program and print the sentence
        else:   ##execute if no error
            print("success")
        finally:    ##execute no matter what
            print("executed no matter what!")
    return ratios
    
print(get_ratios([1, 4], [2, 4]))
print(get_ratios([1, 4], [2, 0]))


#######################################
## EXAMPLE: Exceptions and lists
#######################################
def get_stats(class_list):
	new_stats = []
	for person in class_list:
		new_stats.append([person[0], person[1], avg(person[1])])
	return new_stats 

# avg function: version without an exception
#def avg(grades):
#    return (sum(grades))/len(grades)
    
# avg function: version with an exception
def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('warning: no grades data type1')
        return 0.0


# avg function: version with assert
def avg(grades):
    assert len(grades) != 0, 'warning: no grades data type2'  ##檢查grades是否為空。如果是空的，就會引發一個錯誤（AssertionError），並顯示訊息 'warning: no grades data', and halt the program
    return sum(grades)/len(grades)                      

###當一個名稱相同的函式被再次定義時，後來的定義會覆蓋先前的定義。###
    
test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], 
              [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
              [['captain', 'america'], [80.0, 70.0, 96.0]],
              [['deadpool'], []]]

print("only print valid element in th list :\n", get_stats(test_grades[0 : 3]))
'''
print(get_stats(test_grades)) ##this will be erroe
'''
