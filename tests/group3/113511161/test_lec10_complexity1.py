import add_path
import mit_ocw_exercises.lec10_complexity_part1 as lec10
import pytest
import time
import random
def generateTestList(n:int) ->list[int]:
	tl=[]
	for i in range(n):
		tl.append(random.randint(0,100))
	return tl

def test_linear_search():
	n=random.randint(1,20)
	testlist=generateTestList(n)
	assert lec10.linear_search(testlist,testlist[0])==True
	assert lec10.linear_search([],5) ==False
def test_search():
	assert 1==1
