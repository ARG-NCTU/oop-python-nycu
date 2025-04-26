####################
## EXAMPLE: for loops over strings
####################
print("\n---- for loop over string test ----")
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
print("\n---- while loop with string test ----")
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = "hello"
times = 3

# 原版 while 版本
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

# 挑戰：改成 for loop
print("\n---- for loop version ----")
for char in word:
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a  " + char + "! " + char)
print("What does that spell?")
for i in range(times):
    print(word, "!!!")


####################
## EXAMPLE: perfect cube 
####################
print("\n---- perfect cube test ----")
cube = 27
found = False
for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess)
        found = True
if not found:
    print(cube, "is not a perfect cube")


####################
## EXAMPLE: guess and check cube root 
####################
print("\n---- guess and check cube root test ----")
cube = 27
# cube = 8120601
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))


####################
## EXAMPLE: approximate cube root 
####################
print("\n---- approximate cube root test ----")
cube = 27
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


####################
## EXAMPLE: bisection cube root (only positive cubes!)
####################
print("\n---- bisection cube root test ----")
cube = 27
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
   
