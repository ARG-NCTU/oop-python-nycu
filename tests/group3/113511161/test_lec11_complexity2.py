import pytest
import add_path
import mit_ocw_exercises.lec11_complexity_part2 as lec11
import add_path
import random
def generateList(n):
	li=[1]
	for i in range(n):
		li.append(li[i]+random.randint(1,4))	
	return li

def test_bisect_search():
	k=random.randint(1,30)
	l1=generateList(k)
	te=random.randint(1,4*k+10)
	assert lec11.bisect_search1(l1,te) == lec11.bisect_search2(l1,te)

	te=random.randint(1,4*k+10)
	assert lec11.bisect_search1(l1,te) == lec11.bisect_search2(l1,te)

	te=random.randint(1,4*k+10)
	assert lec11.bisect_search1(l1,te) == lec11.bisect_search2(l1,te)
