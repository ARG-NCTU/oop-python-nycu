import lec11_complexity_part2 as lec
import pytest


testList = []
for i in range(100):
    testList.append(i)

def test_bisect_search():
    assert lec.bisect_search1(testList, 76) == True
    assert lec.bisect_search2(testList, 76) ==True
    assert lec.bisect_search1(testList, 100) == False
    assert lec.bisect_search2(testList, 100) == False
    print("76 is in the testList")
    print("100 is not in the testList")

def test_gensubset():
    testSet = [1,2,3]
    assert lec.genSubsets(testSet) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print("there are so many subsets!!")

if __name__ == "__main__":
    pytest.main([__file__])
    # Alternatively, you can run pytest from the command line:
    # pytest test_lec11-1.py