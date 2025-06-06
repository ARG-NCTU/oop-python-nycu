import pytest
import lec3_strings_algos as lec3
import math

def test_cube_root():
    assert lec3.cube_root(27) == 3
    assert lec3.cube_root(1000) == 10
    assert lec3.cube_root(1) == 1
    assert lec3.cube_root(125) == 5
    assert lec3.cube_root(8) == 2

def test_approximate_root():
    assert lec3.approximate_root(125,0.01) == (500, 4.999999999999938)
    assert lec3.approximate_root(125,0.1) == (500, 4.999999999999938)
    assert lec3.approximate_root(27,0.00001) == (300, 2.99999999999998)
    assert lec3.approximate_root(9,0.01) == (208, 2.0799999999999996)

####################
## EXAMPLE: while loops and strings
## CHALLENGE: rewrite while loop with a for loop
####################
def while_to_for():
    an_letters = "aefhilmnorsxAEFHILMNORSX"
    word = input("I will cheer for you! Enter a word: ")
    times = int(input("Enthusiasm level (1-10): "))

    i = 0
    for i in range(len(word)):
        char = word[i]
        if char in an_letters:
            print("Give me an " + char + "! " + char)
        else:
            print("Give me a  " + char + "! " + char)
    print("What does that spell?")
    for i in range(times):
        print(word, "!!!")

