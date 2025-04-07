####################
## EXAMPLE: for loops over strings
####################
print("=== For loop over string ===")
s = "demo loops"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or u")

for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")


####################
## EXAMPLE: while loops and strings
## CHALLENGE: rewrite while loop with a for loop
####################
print("\n=== Cheer with for loop ===")
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = "hello"  # testing input
times = 3       # testing enthusiasm level

for char in word:
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a  " + char + "! " + char)
print("What does that spell?")
for _ in range(times):
    print(word, "!!!")


####################
## EXAMPLE: perfect cube 
####################
print("\n=== Perfect cube check ===")
cube = 27  # try 8120601 to test large cube
for guess in range(cube + 1):
    if guess ** 3 == cube:
        print("Cube root of", cube, "is", guess)
        break


####################
## EXAMPLE: guess and check cube root 
####################
print("\n=== Guess and check cube root ===")
cube = 27  # or try cube = -27 or 8120601
for guess in range(abs(cube) + 1):
    if guess ** 3 >= abs(cube):
        break

if guess ** 3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))


####################
## EXAMPLE: approximate cube root 
####################
print("\n=== Approximate cube root ===")
cube = 27  # or try cube = 10000
epsilon = 0.1
guess = 0.0
increment = 0.01
num_guesses = 0

while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1

print('num_guesses =', num_guesses)
if abs(guess ** 3 - cube) >= epsilon:
    print('Failed on cube root of', cube, "with these parameters.")
else:
    print(guess, 'is close to the cube root of', cube)


####################
## EXAMPLE: bisection cube root (only positive cubes!)
####################
print("\n=== Bisection cube root ===")
cube = 27  # or 8120601 or 0.25 (must be > 0)
epsilon = 0.01
num_guesses = 0
low = 0
high = max(1.0, cube)  # make it work for 0 < cube < 1 too
guess = (high + low) / 2.0

while abs(guess ** 3 - cube) >= epsilon:
    if guess ** 3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1

print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)

