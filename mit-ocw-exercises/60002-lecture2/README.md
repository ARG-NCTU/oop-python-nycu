# Menu for 0/1 Knapsack Problem

This is a modified version of the lecture code in the 
[OCW Lecture 2](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/resources/lecture2/)

## Run with PyTest

Run all
```
$ cd ~/oop-python-nycu/mit-ocw-exercises/60002-lecture2/
$ pytest
```

Run all and show all print()
```
$ pytest -s
```

Run single test_XXX file
```
$ pytest -s test_food.py
$ pytest -s test_menu.py
```

Run specific function in a file with time clock. (you can see the time from pytest and sys)
```
$ time pytest -s test_max_value.py -k test_max_val_large_menu
$ time pytest -s test_max_value.py -k test_fast_max_val_large_menu
```
