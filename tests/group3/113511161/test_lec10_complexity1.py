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
	l1=generateTestList(4)
	assert lec10.search(l1,101) == False
	assert lec10.search(l1,0) == False
def test_isSubset():
	l1=generateTestList(20)
	l2=[]
	for i in range(16):
		l2.append(l1[i])
		i+=2
	assert lec10.isSubset(l2,l1) ==True
def test_intersect():
	l1=generateTestList(20)
	l2=generateTestList(20)
	l3=[]
	for k in l1:
		for m in l2:
			if k==m:
				l3.append(k)
	re=[]
	for e in l3:
		if not(e in re):
			re.append(e)
	assert lec10.intersect(l1,l2)==re
	assert lec10.intersect(l1,l2)!=[]
