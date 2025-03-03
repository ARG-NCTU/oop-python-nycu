import random

import add_path
from mit_ocw_exercises.lec12_sorting import *

#testList = [1,3,5,7,2,6,25,18,13]

# create a list with 1000 random numbers
testList = [random.randint(0, 1000) for i in range(1000)]

bubble_sort(testList)
print(testList)
