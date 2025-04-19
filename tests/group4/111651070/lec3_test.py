def for_loop_over_string_to_find_e(str):
    for char in str:
        if char == "e":
            print("found e")

def while_loop_and_strings():
    an_letters = "aefhilmnorsxAEFHILMNORSX"
    word = input("I will cheer for you! Enter a word: ")
    times = int(input("Enthusiasm level (1-10): "))
    for i in range(len(word)):
        char = word[i]
        if char in an_letters:
            print("Give me an " + char + "! " + char)
        else:
            print("Give me a  " + char + "! " + char)
    print("What does that spell?")
    for i in range(times):
        print(word, "!!!")

def perfect_cube():
    #cube = int(input("Enter a perfect cube: "))
    cube = 27
    for guess in range(cube+1):
       if guess**3 == cube:
           print("Cube root of", cube, "is", guess)

def guess_and_check_cube_root():
    # cube = int(input("Enter an integer for cube: "))
    cube = 25
    for guess in range(abs(cube)+1):
        if guess**3 >= abs(cube):
           break
    if guess**3 != abs(cube):
        print(cube, 'is not a perfect cube')
    elif cube < 0:
        guess = -guess
    else:
        print('Cube root of ' + str(cube) + ' is ' + str(guess))

def approximate_cube_root():
    # cube = int(input("Enter an integer for cube: "))
    cube = 8
    epsilon = 0.1
    guess = 0.0
    increment = 0.01
    num_guesses = 0
    # look for close enough answer and make sure
    # didn't accidentally skip the close enough bound
    while abs(guess**3 - cube) >= epsilon and guess <= cube:
        guess += increment
        num_guesses += 1
    print('num_guesses =', num_guesses)
    if abs(guess**3 - cube) >= epsilon:
        print('Failed on cube root of', cube, "with these parameters.")
    else:
        print(guess, 'is close to the cube root of', cube)

#################################################
s = 'hello'
for_loop_over_string_to_find_e(s)
while_loop_and_strings()
perfect_cube()
guess_and_check_cube_root()
approximate_cube_root()