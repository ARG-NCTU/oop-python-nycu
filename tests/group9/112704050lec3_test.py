#lecture 3 test
## EXAMPLE: for loops over strings
# for語法
# for 變數 in 可迭代物件-->range,list,str:
#       執行區塊
s = "demo loops"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("time", index ,": There is i or u")
    else:
        print("time", index ,": There is no i or u")

print("\n")
demo = "testing words"
demolen = len(demo)
for char in range(demolen):
    if demo[char] == 'i' or char == 'o':
        print("time", char ,": There is i or o")
    else:
        print("time", char ,": There is no i or o")

####################
## EXAMPLE: while loops and strings
## CHALLENGE: rewrite while loop with a for loop
####################
password = "hahaisme"
pw = input("I will cheer for you! Enter your password: ")
times = int(input("Enthusiasm level (1-10): "))
#   
i = 0
if pw == password:
    n=0
    while i < len(pw):        
        print("Password correct!!!")
        i += 1
elif pw in password:  
    n=1
    while i < len(pw):        
        print("Password almost correct")
        i += 1
else:
    n=2
    while i < len(pw):        
        print("Come on, try again")
        i += 1
print("What does that call?")
for i in range(times):
    if n == 0:
        print("You got it !!!")
    elif n == 1:
        print("I don't know??")
    else:
        print("BYe!!!")

####################
## EXAMPLE: perfect cube 
####################
import random
i = 0 
count = 1
while i == 0:
    cube = random.randint(1, 1000)
    for guess in range(cube+1):
        if guess**3 == cube:
            print("Cube root of", cube, "is", guess)
            i=1
            # loops keeps going even after found the cube root
            
    if i == 0:
        print("#",count," I can't find the cube root this time, try again")
        count += 1  

####################
## EXAMPLE: guess and check cube root 
####################
import random
i = 0
count = 1
while i == 0:
    cube = random.randint(1, 1000)
    for guess in range(abs(cube)+1):
        # passed all potential cube roots
        if guess**3 >= abs(cube):
            # no need to keep searching
            break
    if guess**3 != abs(cube):
        print("#",count," ",cube, 'is not a perfect cube')
    else:
        i = 1
        print("#",count," ",cube, 'is  a perfect cube')
        if cube < 0:
            guess = -guess
        print('Cube root of ' + str(cube) + ' is ' + str(guess))
    count += 1

####################
## EXAMPLE: approximate cube root 
####################
import random
cube = 27
cube = 8120601
cube = 1000
cube = random.randint(1, 1000)
epsilon = 0.1
guess = 0.0
increment = 0.01
num_guesses = 1
# look for close enough answer and make sure
# didn't accidentally skip the close enough bound
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    print("#",num_guesses," guess=", guess)
    guess += increment
    num_guesses += 1
#print("\n")
print('total guesses =', num_guesses-1)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube, "with these parameters.")
else:  
    print(guess, 'is close to the cube root of', cube)
