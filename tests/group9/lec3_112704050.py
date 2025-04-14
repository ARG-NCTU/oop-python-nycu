def analyze_string_1(s):
    results1 = []
    for index in range(len(s)):
        if s[index] == 'i' or s[index] == 'u':
            results1.append(f"time {index}: There is i or u")
        else:
            results1.append(f"time {index}: There is no i or u")
    return results1

def analyze_string_2(demo):
    results2 = []
    for char in range(len(demo)):
        if demo[char] == 'i' or demo[char] == 'o':
            results2.append(f"time {char}: There is i or o")
        else:
            results2.append(f"time {char}: There is no i or o")
    return results2

####################
## EXAMPLE: while loops and strings
## CHALLENGE: rewrite while loop with a for loop
####################
def password_feedback(pw, times):
    password = "hahaisme"
    output = []
    i = 0
    n = 0
    if pw == password:
        n = 0 #correct
        while i < len(pw):        
            output.append("Password correct!!!")
            i += 1
    elif pw in password:  
        n = 1 #almost correct
        while i < len(pw):        
            output.append("Password almost correct")
            i += 1
    else:
        n = 2 #incorrect
        while i < len(pw):        
            output.append("Come on, try again")
            i += 1
    output.append("What does that call?")
    for _ in range(times):
        if n == 0:
            output.append("You got it !!!")
        elif n == 1:
            output.append("I don't know??")
        else:
            output.append("Bye!!!")
    return output
####################
## EXAMPLE: perfect cube 
####################
def find_perfect_cube_1(cube1):
    for count1 ,guess1 in enumerate(range(cube1+1), start=1):
        if guess1**3 == cube1:
            return {"success": True, "cube": cube1, "guess": guess1, "tries": count1}
    return {"success": False, "cube": cube1, "tries": count1}
        

####################
## EXAMPLE: guess and check cube root 
####################
def find_perfect_cube_2(cube2):
    count2 = 1
    for guess2 in range(cube2+1):
        if guess2**3 == cube2:
            return {"found": True,"cube": cube2,"guess": guess2,"tries": count2}
    return {"found": False,"cube": cube2,"tries": cube2 + 1}


####################
## EXAMPLE: approximate cube root 
####################
def approximate_cube_root(cube3, epsilon1, increment):
    guess3 = 0.0
    num_guesses3 = 1
    while abs(guess3**3 - cube3) >= epsilon1 and guess3 <= cube3:
        guess3 += increment
        num_guesses3 += 1
    if abs(guess3**3 - cube3) < epsilon1:
        return {"cube": cube3,"guess": guess3,"guesses time": num_guesses3 - 1,"success": True}
    else:   
        return {"cube": cube3,"guess": guess3,"guesses time": num_guesses3 - 1,"success": False}
     

####################
## EXAMPLE: bisection cube root (only positive cubes!)
####################
def bisection_cube_root(cube4 ,epsilon2):
    num_guesses4 = 0
    low = 0
    if cube4 < 1:
        high = 1
    else:
        high = cube4
    guess4 = (high + low)/2.0
    while (abs(guess4**3 - cube4) >= epsilon2) & (num_guesses4 <10000):
        #print("guess= ",guess)
        if guess4**3 < cube4:
            # look only in upper half search space
            low = guess4
            #print('low =', low)
        else:
            # look only in lower half search space
            high = guess4
            #print("high = ", high)
        # next guess is halfway in search space
        guess4 = (high + low)/2.0
        num_guesses4 += 1
        #print("num_guesses =", num_guesses)
    #print('num_guesses =', num_guesses)
    #print(guess," is close to the cube root of", cube)
    return {"guess": guess4, "success": abs(guess4**3 - cube4) < epsilon2,"tries": num_guesses4}

if __name__ == "__main__":
    print("########這是主程式碼############")

    print("=== Testing analyze_string_1 ===")
    print(analyze_string_1("input"))

    print("\n=== Testing analyze_string_2 ===")
    print(analyze_string_2("hello world"))

    print("\n=== Testing password_feedback ===")
    print(password_feedback("haha", 3))

    print("\n=== Testing find_perfect_cube_1 ===")
    print(find_perfect_cube_1(64))

    print("\n=== Testing find_perfect_cube_2 ===")
    print(find_perfect_cube_2(125))

    print("\n=== Testing approximate_cube_root ===")
    print(approximate_cube_root(27, epsilon1=0.01, increment=0.001))

    print("\n=== Testing bisection_cube_root ===")
    print(bisection_cube_root(1000, epsilon2=0.001))
