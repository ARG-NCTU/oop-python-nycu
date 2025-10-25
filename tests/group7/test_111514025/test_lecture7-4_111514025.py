



######################################
# EXAMPLE: Raising your own exceptions
######################################
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

######################################
print(get_ratios([1, 4], [2, 0]))
######################################
print(get_ratios([1, 4], [2]))


#print(get_stats(test_grades))
def test_get_ratios():
    assert get_ratios([1, 2, 3], [1, 2, 3]) == [1.0, 1.0, 1.0]
    assert get_ratios([1, 2, 3], [1, 0, 3]) == [1.0, float('nan'), 1.0]
    try:
        get_ratios([1, 2], [1])
    except ValueError as e:
        assert str(e) == 'get_ratios called with bad arg'