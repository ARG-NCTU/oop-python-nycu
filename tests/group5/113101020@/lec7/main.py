# main.py

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


def primes_list(n):
    """
    input: n an integer > 1
    returns: list of all the primes up to and including n
    """
    if n < 2:
        return []
    primes = [2]
    for j in range(3, n+1):
        is_div = False
        for p in primes:
            if j % p == 0:
                is_div = True
                break
        if not is_div:
            primes.append(j)
    return primes


def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('get_ratios called with bad arg')
        else:
            print("success")
        finally:
            print("executed no matter what!")
    return ratios


def avg(grades):
    assert len(grades) != 0, 'warning: no grades data'
    return sum(grades) / len(grades)


def get_stats(class_list):
    new_stats = []
    for person in class_list:
        new_stats.append([person[0], person[1], avg(person[1])])
    return new_stats
