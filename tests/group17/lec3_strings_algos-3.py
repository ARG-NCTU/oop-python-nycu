####################
## V3: Enhanced for loop over strings with formatted output
####################
print("=== V3: Looping through string with index and char ===")
text = "demo loops"
for i, ch in enumerate(text):
    if ch in ['i', 'u']:
        print(f"At index {i}: Found vowel '{ch}'")

for ch in text:
    if ch in ['i', 'u']:
        print(f"Found vowel: {ch}")


####################
## V3: Simulated cheer with capital letters and added spacing
####################
print("\n=== V3: Simulated Cheer with capitalization ===")
an_set = "aefhilmnorsxAEFHILMNORSX"
test_word = "hello"
cheer_level = 3

for c in test_word:
    article = "an" if c in an_set else "a"
    print(f"Give me {article} {c.upper()}! {c.upper()}")
print("\nWhat does that spell?\n")
for _ in range(cheer_level):
    print(test_word.upper() + "!!!")


####################
## V3: Perfect cube with else clause
####################
print("\n=== V3: Perfect cube with early exit ===")
cube_num = 27
for g in range(cube_num + 1):
    if g ** 3 == cube_num:
        print(f"Cube root of {cube_num} is {g}")
        break
else:
    print(f"{cube_num} is not a perfect cube.")


####################
## V3: Signed cube root guessing
####################
print("\n=== V3: Signed cube root guessing ===")
cube_check = -27
abs_guess = 0
while abs_guess ** 3 < abs(cube_check):
    abs_guess += 1

if abs_guess ** 3 != abs(cube_check):
    print(f"{cube_check} is not a perfect cube")
else:
    final_guess = -abs_guess if cube_check < 0 else abs_guess
    print(f"Cube root of {cube_check} is {final_guess}")


####################
## V3: Approximate cube root with percent error
####################
print("\n=== V3: Approximate cube root with feedback ===")
target = 27
eps = 0.1
step_size = 0.01
g_val = 0.0
count = 0

while abs(g_val ** 3 - target) >= eps and g_val <= target:
    g_val += step_size
    count += 1

print(f"Steps taken: {count}")
if abs(g_val ** 3 - target) < eps:
    print(f"{g_val} is close enough to the cube root of {target}")
else:
    print(f"Could not find cube root of {target} within given precision.")


####################
## V3: Bisection with midpoint log
####################
print("\n=== V3: Bisection cube root with midpoint tracking ===")
value = 27
eps_bisect = 0.01
guesses = 0
low = 0
high = max(1.0, value)
mid = (low + high) / 2.0

while abs(mid ** 3 - value) >= eps_bisect:
    print(f"Trying: {mid}")
    if mid ** 3 < value:
        low = mid
    else:
        high = mid
    mid = (low + high) / 2.0
    guesses += 1

print(f"Guesses: {guesses}")
print(f"{mid} is approximately the cube root of {value}")

