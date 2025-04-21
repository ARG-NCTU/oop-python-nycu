#########################
## EXAMPLE: combinations of print and return
#########################
def even_odd( i ):

    if i % 2 ==0:
        print( i, "is even")
        return True
    else:
        print( i, "is odd")
        return False
    
even_odd(-1)


#########################
## EXAMPLE: applying functions to repeat same task many times
#########################

def bisection_cuberoot_approx(x, epsilon):

    if x>0 :
        low = 0
        high = x
    else:
        low = x
        high = 0

    guess = (high + low)/2
    count = 0
    while abs(guess**3 - x) >= epsilon :
        #print(guess)
        count +=1
        if guess**3 <x :
            low = guess
        else:
            high = guess

        guess = (high + low)/2


    return guess
        
x = -27
while abs(x) <= 10000:
    #print(x)
    approx = bisection_cuberoot_approx(x, 0.01)
    print(approx, "is close to cube root of", x)
    x *= 10

#########################
## EXAMPLE: returning function objects
#########################
import numpy as np

def just_return(n):
    def add(a, b):
        return a + b

    def minus(a, b):
        return a - b
    
    if n == 1:
        return add
    else:
        return minus
    
n = np.random.choice([1, 2])
num_input = just_return(n)(10,5)
print(num_input)

#########################
## EXAMPLE: shows accessing variables outside scope
#########################
import numpy as np
def pass_or_not(total):#直到pass為止
    test_time = 0
    check = 0
    while check == 0:
        test_time += 1
        average = total / 10
        print("average score is ", average)

        if average >= 60:
            print("pass")
            check = 1
            #print("test time is ", test_time)
            return check
        else:
            print("not pass")
            seed = np.random.choice(range(1, 100000))
            total = generate_score(seed)
            check = 0
        

def generate_score(seed):
    np.random.seed(seed)
    score = []
    for _ in range(10):
        score.append(np.random.randint(0, 100))
    #score = np.array(score)
    #print(score)
    #print(np.sum(score)/10)
    return np.sum(score)

seed = np.random.choice(range(1, 100000))
total = generate_score(seed)
pass_or_not(total)

#########################
## EXAMPLE: Return book
#########################
import numpy as np

def return_book(return_rate = 0.8,seed=0):
    np.random.seed(seed)
    x = np.random.uniform(0,1)
    print(x)
    print(return_rate)
    if x > return_rate :
        print("not return")
        return 0
    else:
        print("returned")
        return 1

return_book()
