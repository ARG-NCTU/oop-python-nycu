def for_loop_over_string_to_find_e(str):
    flag = 0
    for char in str:
        if char == "e":
            print("Found e")
            flag = 1
    if flag == 0:
        print("Not found e")

def while_loop_and_strings(word, times):
    an_letters = "aefhilmnorsxAEFHILMNORSX"
    for i in range(len(word)):
        char = word[i]
        if char in an_letters:
            print("Give me an " + char + "! " + char)
        else:
            print("Give me a  " + char + "! " + char)
    print("What does that spell?")
    for i in range(times):
        print(word, "!!!")

def perfect_cube(cube):
    for guess in range(cube+1):
       if guess**3 == cube:
           print("Cube root of", cube, "is", guess)

def guess_and_check_cube_root(cube):
    for guess in range(abs(cube)+1):
        if guess**3 >= abs(cube):
           break
    if guess**3 != abs(cube):
        print(cube, 'is not a perfect cube')
    elif cube < 0:
        guess = -guess
    else:
        print('Cube root of ' + str(cube) + ' is ' + str(guess))

def approximate_cube_root(cube):
    epsilon = 0.1
    guess = 0.0
    increment = 0.01
    num_guesses = 0
    while abs(guess**3 - cube) >= epsilon and guess <= cube:
        guess += increment
        num_guesses += 1
    print('num_guesses =', num_guesses)
    if abs(guess**3 - cube) >= epsilon:
        print('Failed on cube root of', cube, "with these parameters.")
    else:
        print(guess, 'is close to the cube root of', cube)

def bisection_cube_root(cube):
    epsilon = 0.01
    num_guesses = 0
    low = 0
    high = cube
    guess = (high + low)/2.0
    while abs(guess**3 - cube) >= epsilon:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
        num_guesses += 1
    print('num_guesses =', num_guesses)
    print(guess, 'is close to the cube root of', cube)

#################################################
print("=====================================")
print("**              Test1              **")
print("=====================================")
for_loop_over_string_to_find_e('hello')
print("-------------------------------------")
for_loop_over_string_to_find_e('ball')
print("=====================================")
print("**              Test2              **")
print("=====================================")
while_loop_and_strings('hello', 3)
print("-------------------------------------")
while_loop_and_strings('hello world!', 2)
print("=====================================")
print("**              Test3              **")
print("=====================================")
perfect_cube(64)
print("-------------------------------------")
perfect_cube(27)
print("-------------------------------------")
perfect_cube(8)
print("=====================================")
print("**              Test4              **")
print("=====================================")
guess_and_check_cube_root(64)
print("-------------------------------------")
guess_and_check_cube_root(60)
print("=====================================")
print("**              Test5              **")
print("=====================================")
approximate_cube_root(60)
print("-------------------------------------")
approximate_cube_root(27)
print("=====================================")
print("**              Test6              **")
print("=====================================")
bisection_cube_root(60)
print("-------------------------------------")
bisection_cube_root(27)
print("-------------------------------------")