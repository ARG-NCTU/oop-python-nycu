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
    cube = int(input("Enter a perfect cube: "))
    for guess in range(cube+1):
       if guess**3 == cube:
           print("Cube root of", cube, "is", guess)

def guess_and_check_cube_root():
    cube = int(input("Enter an integer for cube: "))
    for guess in range(abs(cube)+1):
        if guess**3 >= abs(cube):
           break
    if guess**3 != abs(cube):
        print(cube, 'is not a perfect cube')
    elif cube < 0:
        guess = -guess
    else:
        print('Cube root of ' + str(cube) + ' is ' + str(guess))

#################################################
s = 'hello'
for_loop_over_string_to_find_e(s)
while_loop_and_strings()
perfect_cube()
guess_and_check_cube_root()