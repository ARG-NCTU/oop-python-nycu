import pytest
from math_utlis import add, multiply, subtract,devide

def test_add():
	assert add(2,3) ==5
	assert add(-1,1)==0
def test_multiply():
	assert multiply(2,3)==6
	assert multiply(0,10)==0
	assert multiply(23233,1212)==28158396
def test_subtract():
	assert subtract(1,3)==-2
	assert subtract (-2,-4)==2
	assert subtract (100,2)==98
def test_devide():
	assert devide(4,2)==2
