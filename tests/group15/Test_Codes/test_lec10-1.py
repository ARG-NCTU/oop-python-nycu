import lec10_complexity_part1 as lec

testlist = [1, 3, 4, 5, 9, 10, 18, 27]
t2 = [1, 2, 5, 8]
t3 = [3, 4, 5, 9]
def linear_search_test():
    assert lec.linear_search(testlist, 10) == True
    assert lec.linear_search(testlist, 12) == False
    print("Test complete")

linear_search_test()

def isSubset_test():
    assert lec.isSubset(testlist, t2) == False
    assert lec.isSubset(t3, testlist) == True
    print ("t3 is testlist's sublist")

isSubset_test()

def intersect_test():
    print(lec.intersect(t2, t3))
    assert lec.intersect(t2, t3) == [5]
    print(lec.intersect(testlist, t3))
    assert lec.intersect(testlist, t3) == [3, 4, 5, 9]

intersect_test()