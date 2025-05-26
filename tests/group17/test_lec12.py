import unittest

from copy import deepcopy

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        # 多種測資：空、單一元素、重複元素、已排序、反向排序、隨機順序
        self.test_cases = [
            [],
            [1],
            [2, 2, 1, 1],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [3, 1, 4, 5, 2]
        ]
        self.sorted_cases = [sorted(case) for case in self.test_cases]

if __name__ == "__main__":
    unittest.main()
