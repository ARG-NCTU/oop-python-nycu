# -*- coding: utf-8 -*-
an_letters = "aefhilmnorsxAEFHILMNORSX"

word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

for char in word:
    if char in an_letters:
        print(f"Give me an {char}! {char}")
    else:
        print(f"Give me a {char}! {char}")

print("What does that spell?")

for _ in range(times):
    print(f"{word} !!!")

