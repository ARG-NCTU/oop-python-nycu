#merge sort python test file

import unittest
from lec12_sortings import merge_sort as g8_merge_sort

class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        arr = [12, 11, 13, 5, 6, 7]
        self.assertEqual(g8_merge_sort(arr), [5, 6, 7, 11, 12, 13])
        arr = [38, 27, 43, 3, 9, 82, 10]
        self.assertEqual(g8_merge_sort(arr), [3, 9, 10, 27, 38, 43, 82])
        arr = [38, 27, 43, 3, 9, 82, 10, 1]
        self.assertEqual(g8_merge_sort(arr), [1, 3, 9, 10, 27, 38, 43, 82])
        arr = [12, 11, 13, 5, 6, 7, 1]
        self.assertEqual(g8_merge_sort(arr), [1, 5, 6, 7, 11, 12, 13])
        arr = [12, 11, 13, 5, 6, 7, 1, 2]
        self.assertEqual(g8_merge_sort(arr), [1, 2, 5, 6, 7, 11, 12, 13])
        arr = [12, 11, 13, 5, 6, 7, 1, 2, 0]
        self.assertEqual(g8_merge_sort(arr), [0, 1, 2, 5, 6, 7, 11, 12, 13])
        arr = [12, 11, 13, 5, 6, 7, 1, 2, 0, 10]
        self.assertEqual(g8_merge_sort(arr), [0, 1, 2, 5, 6, 7, 10, 11, 12, 13])

if __name__ == '__main__':

    unittest.main()