####################
## V4: Modular for loop example
####################
def find_vowels_in_string(s):
    for idx in range(len(s)):
        if s[idx] in "iu":
            print(f"Index {idx}: found '{s[idx]}'")
    for ch in s:
        if ch in "iu":
            print(f"Found '{ch}' again in second loop")

print("=== V4: Modular string loop ===")
find_vowels_in_string("demo loops")


####################
## V4: Cheer function with dynamic input
####################
def cheer(word, level):
    an_letters = "aefhilmnorsxAEFHILMNORSX"
    for c in word:
        article = "an" if c in an_letters else "a"
        print(f"Give me {article} {c.upper()}! {c.upper()}")
    print("What does that spell?")
    for _ in range(level):
        print(word.upper() + "!!!")

print("\n=== V4: Cheer function ===")
cheer("hello", 3)


####################
## V4: Perfect cube function
####################
def is_perfect_cube(n):
    for g in range(abs(n) + 1):
        if g ** 3 == abs(n):
            return -g if n < 0 else g
    return None

print("\n=== V4: Cube root check function ===")
result = is_perfect_cube(-27)
if result is not None:
    print(f"Cube root is {result}")
else:
    print("Not a perfect cube")


####################
## V4: Approximation with return value
####################
def approx_cube_root(cube, epsilon=0.1, step=0.01):
    guess = 0.0
    tries = 0
    while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
        guess += step
        tries += 1
    if abs(guess ** 3 - cube) >= epsilon:
        return None, tries
    return guess, tries

print("\n=== V4: Cube root approx function ===")
g, t = approx_cube_root(27)
if g is not None:
    print(f"Found approx root: {g} in {t} steps")
else:
    print(f"Failed after {t} tries")


####################
## V4: Bisection root finder function
####################
def bisection_cube_root(val, epsilon=0.01):
    low = 0
    high = max(1.0, val)
    mid = (low + high) / 2.0
    tries = 0
    while abs(mid ** 3 - val) >= epsilon:
        if mid ** 3 < val:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2.0
        tries += 1
    return mid, tries

print("\n=== V4: Bisection function ===")
root, tries = bisection_cube_root(27)
print(f"Root: {root} (in {tries} steps)")

