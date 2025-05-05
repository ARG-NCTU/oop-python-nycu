import unittest

from typing import Tuple

# 引入要測試的函數（你可以視情況分開放檔案或整理在一起）
def quotient_and_remainder(x, y) -> Tuple[int, int]:
    q = x // y
    r = x % y
    return (q, r)

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

def sum_elem_method1(L):
    total = 0 
    for i in range(len(L)): 
        total += L[i] 
    return total

def sum_elem_method2(L):
    total = 0 
    for i in L: 
        total += i 
    return total

def remove_dups(L1, L2):
    for e in L1[:]:  # 修正：避免修改中疊代
        if e in L2:
            L1.remove(e)

def remove_dups_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

class TestExamples(unittest.TestCase):

    def test_quotient_and_remainder(self):
        self.assertEqual(quotient_and_remainder(5, 3), (1, 2))
        self.assertEqual(quotient_and_remainder(10, 2), (5, 0))
        self.assertEqual(quotient_and_remainder(9, 4), (2, 1))

    def test_get_data(self):
        test_data = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
        self.assertEqual(get_data(test_data), (1, 7, 2))

        tswift_data = ((2014,"Katy"), (2014, "Harry"), (2012,"Jake"), 
                       (2010,"Taylor"), (2008,"Joe"))
        self.assertEqual(get_data(tswift_data), (2008, 2014, 5))

    def test_sum_elem_methods(self):
        L = [1, 2, 3, 4]
        self.assertEqual(sum_elem_method1(L), 10)
        self.assertEqual(sum_elem_method2(L), 10)
        self.assertEqual(sum_elem_method1([]), 0)
        self.assertEqual(sum_elem_method2([]), 0)

    def test_remove_dups(self):
        L1 = [1, 2, 3, 4]
        L2 = [1, 2, 5, 6]
        remove_dups(L1, L2)
        self.assertEqual(L1, [3, 4])
        self.assertEqual(L2, [1, 2, 5, 6])  # 應該沒變

    def test_remove_dups_new(self):
        L1 = [1, 2, 3, 4]
        L2 = [1, 2, 5, 6]
        remove_dups_new(L1, L2)
        self.assertEqual(L1, [3, 4])
        self.assertEqual(L2, [1, 2, 5, 6])  # 應該沒變

if __name__ == '__main__':
    unittest.main()

