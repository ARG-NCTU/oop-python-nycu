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
        
L = [10,20,30,40]
rev_list(L)
print(L)


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
		break
        if not is_div:
            primes.append(j)
    return primes

print(primes_list(2) )               
print(primes_list(15)  ) 
print(primes_list(97)  )             


try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
except:
    print("Bug in user input.")


try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
    print("a+b = ", a+b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Something went very wrong.")


def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
        else:
            print("success")
        finally:
            print("executed no matter what!")
    return ratios
    
print(get_ratios([1, 4], [2, 4]))


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
        print('warning: no grades data')
        return 0.0


# avg function: version with assert
def avg(grades):
    assert len(grades) != 0, 'warning: no grades data'
    return sum(grades)/len(grades)

    
test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], 
              [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
              [['captain', 'america'], [80.0, 70.0, 96.0]],
              [['deadpool'], []]]

print(get_stats(test_grades))
