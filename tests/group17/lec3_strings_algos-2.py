####################
## REFACTORED: for loops over strings
####################
print("=== Refactored: For loop over string ===")
string_sample = "demo loops"
for idx in range(len(string_sample)):
    if string_sample[idx] in ('i', 'u'):
        print("Found a vowel: i or u")

for letter in string_sample:
    if letter in ('i', 'u'):
        print("Found a vowel: i or u")


####################
## REFACTORED: while loop rewritten as for loop
####################
print("\n=== Refactored: Cheer with for loop ===")
vowel_like = "aefhilmnorsxAEFHILMNORSX"
cheer_word = "hello"   # test input
enthusiasm = 3         # test enthusiasm level

for ch in cheer_word:
    article = "an" if ch in vowel_like else "a"
    print(f"Give me {article} {ch}! {ch}")
print("What does that spell?")
for _ in range(enthusiasm):
    print(cheer_word.upper(), "!!!")


####################
## REFACTORED: perfect cube 
####################
print("\n=== Refactored: Perfect cube check ===")
test_cube = 27
for attempt in range(test_cube + 1):
    if attempt ** 3 == test_cube:
        print(f"Cube root of {test_cube} is {attempt}")
        break


####################
## REFACTORED: guess and check cube root 
####################
print("\n=== Refactored: Guess and check cube root ===")
cube_number = -27
for trial in range(abs(cube_number) + 1):
    if trial ** 3 >= abs(cube_number):
        break

if trial ** 3 != abs(cube_number):
    print(f"{cube_number} is not a perfect cube.")
else:
    if cube_number < 0:
        trial = -trial
    print(f"Cube root of {cube_number} is {trial}")


####################
## REFACTORED: approximate cube root 
####################
print("\n=== Refactored: Approximate cube root ===")
cube_val = 27
eps = 0.1
g = 0.0
step = 0.01
tries = 0

while abs(g ** 3 - cube_val) >= eps and g <= cube_val:
    g += step
    tries += 1

print('Tries needed =', tries)
if abs(g ** 3 - cube_val) >= eps:
    print('Approximation failed for cube root of', cube_val)
else:
    print(f"{g} is close to the cube root of {cube_val}")


####################
## REFACTORED: bisection cube root (positive cubes only)
####################
print("\n=== Refactored: Bisection cube root ===")
target_cube = 27
precision = 0.01
guess_count = 0
low_bound = 0
high_bound = max(1.0, target_cube)
estimate = (high_bound + low_bound) / 2.0

while abs(estimate ** 3 - target_cube) >= precision:
    if estimate ** 3 < target_cube:
        low_bound = estimate
    else:
        high_bound = estimate
    estimate = (high_bound + low_bound) / 2.0
    guess_count += 1

print("Guesses made =", guess_count)
print(f"{estimate} is close to the cube root of {target_cube}")

