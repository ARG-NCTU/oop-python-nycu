import pytest
import add_path
import random
import mit_ocw_exercises.lec12_sorting as lec12
def genList(n):
	re=[]
	for i in range(n):
		re.append(random.randint(1,100))
	return re
def test_sort():
	n=random.randint(1,30)
	l=genList(n)
	assert lec12.bubble_sort(l) == sorted(l)
	lec12.selection_sort_np(l) 
	assert l == sorted(l)
