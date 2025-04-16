#####################
## EXAMPLE: for loops over strings
test = False                                        ##bool value of True and False need to be capital letter in first letter 
s = input("Enter a name : ")
for char in s:
    if char == 'i' or char == 'u':
        test = True
if test:
    print("There is an i or u")

for index in range(len(s)):
    if s[index] == 'i':
        print("There is an i at ", index)
    if s[index] == 'u':
        print("There is an u at ", index)


#####################
## EXAMPLE: while loops and strings
## CHALLENGE: rewrite while loop with a for loop
an_letters = "aeiouAEIOU"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))      ##variable = type(input("say something : ")

i = 0
while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a  " + char + "! " + char)
    i += 1
print("What does that spell?")
for i in range(times):
    print(word, "!!!")

## CHALLENGE
an_letters = "aeiouAEIOU"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

for i in range(len(word)):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a  " + char + "! " + char)

print("What does that spell?")

i = 0
while i < times:
    print(word, "!!!")
    i += 1


####################
## EXAMPLE: perfect cube 
####################
#cube = 27
cube = int(input("enter an positive integer : "))
for guess in range(cube+1):
    if guess**3 == cube:                                ##in python a^3 = a**3
        print("Cube root of", cube, "is", guess)
        break
#loops end after found the root of cube

    

####################
## EXAMPLE: guess and check cube root 
####################
#cube = 27
cube = int(input("Enter an integer : "))
for guess in range(abs(cube)+1):
# passed all potential cube roots
    if guess**3 >= abs(cube):
# no need to keep searching
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))##this line is equal to print("Cube root of ", cube, " is ", guess) 


####################
## EXAMPLE: approximate cube root 
####################
cube = float(input("Enter a real number : "))
epsilon = 0.1
guess = 0.0
increment = 0.01
num_guesses = 0
## look for close enough answer and make sure
## didn't accidentally skip the close enough bound
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube, "with these parameters.")
else:
    print(guess, 'is close to the cube root of', cube)


####################
## EXAMPLE: bisection cube root (only positive cubes!)
####################
#cube = 27
##cube = 8120601
## won't work with x < 1 because initial upper bound is less than ans
cube = float(input("Enter a real number : "))
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
# look only in upper half search space
        low = guess
    else:
# look only in lower half search space
        high = guess
# next guess is halfway in search space
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
   
