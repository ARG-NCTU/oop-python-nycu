import lec11_complexity_part2 as lec


testList = []
for i in range(100):
    testList.append(i)

def bisect_search_test():
    assert lec.bisect_search1(testList, 76) == True
    assert lec.bisect_search2(testList, 76) ==True
    assert lec.bisect_search1(testList, 100) == False
    assert lec.bisect_search2(testList, 100) == False
    print("76 is in the testList")
    print("100 is not in the testList")

bisect_search_test()

def gensubset_test():
    testSet = [1,2,3]
    assert lec.genSubsets(testSet) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print("there are so many subsets!!")
gensubset_test()