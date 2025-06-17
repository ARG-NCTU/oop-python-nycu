import lec_11.py as lec11
import pytest
import pytest

def test_bisect_search2():
    testList = [10, 20, 30, 40, 50, 60]
    assert lec11.bisect_search2(testList, 30) == True     
    assert lec11.bisect_search2(testList, 10) == True     
    assert lec11.bisect_search2(testList, 60) == True     
    assert lec11.bisect_search2(testList, 25) == False    
    assert lec11.bisect_search2(testList, 100) == False   
    assert lec11.bisect_search2([], 30) == False          
