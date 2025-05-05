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
    return L
        
L = [1,2,3,4]
x = L[:]
rev_list(L)
print(L)
print(x)
x.reverse()
print(x)

##primes

def primes_list(n):
    list_of_primes = []

    for i in range(1, n + 1):
        x = find_primes(i)
        if x != False:
            list_of_primes.append(x)

    return list_of_primes   


def find_primes(x):
    check = 0
    if x <= 1 :
        return False
    for i in range(2,x+1):
        #print(i)
        if x % i == 0 and i != x:
            return False
        else :
            check = 1
        #print(check)
    if check == 1:
        return x

#primes_list(10)
print(primes_list(100))

#######################################
## EXAMPLE: Exceptions and lists
#######################################
def calculate_stat(test_grades):
    new_list = []
    rank = []
    for student in test_grades:
        new_list.append([student[0],average(student[1])])
 
    for i in new_list:
        if i[1] != False:
            rank.append(i[1])

    new_rank = sorted(rank , reverse= True)
    return new_list, new_rank[0]

def average(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('warning: no grades data')
        return False


test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], 
              [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
              [['captain', 'america'], [80.0, 70.0, 96.0]],
              [['deadpool'], []],
              [["Edward", "Lee"], [100, 99 , 98 , 94]]
              ]

#calculate_stat(test_grades)
print(calculate_stat(test_grades))

print("hello")
