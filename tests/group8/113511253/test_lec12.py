import sys, os
import unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lec12_sorting import bubble_sort_np, selection_sort_np, merge_sort_np

class TestSorting(unittest.TestCase):
    def setUp(self):
        self.raw = [5, 2, 9, 1, 5, 6]
        self.sorted = [1, 2, 5, 5, 6, 9]

    def test_bubble(self):
        L = self.raw[:]
        self.assertEqual(bubble_sort_np(L), self.sorted)

    def test_selection(self):
        L = self.raw[:]
        self.assertEqual(selection_sort_np(L), self.sorted)

    def test_merge(self):
        L = self.raw[:]
        self.assertEqual(merge_sort_np(L), self.sorted)

if __name__ == '__main__':
    unittest.main()
