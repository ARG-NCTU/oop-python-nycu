import unittest
from add_path import add_path
add_path()
from lec12_sorting import bubble_sort_np, selection_sort_np, merge_sort_np

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.unsorted_list = [6, 2, 7, 3, 5, 9, 1, 4, 8, 0]
        self.sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.duplicate_list = [5, 2, 8, 2, 5, 1, 8]
        self.duplicate_sorted = [1, 2, 2, 5, 5, 8, 8]
        self.empty_list = []
        self.single_element_list = [42]
        
    def test_bubble_sort_np(self):
        self.assertEqual(bubble_sort_np(list(self.unsorted_list)), self.sorted_list)
        self.assertEqual(bubble_sort_np(list(self.duplicate_list)), self.duplicate_sorted)
        self.assertEqual(bubble_sort_np(list(self.empty_list)), self.empty_list)
        self.assertEqual(bubble_sort_np(list(self.single_element_list)), self.single_element_list)
        
    def test_selection_sort_np(self):
        self.assertEqual(selection_sort_np(list(self.unsorted_list)), self.sorted_list)
        self.assertEqual(selection_sort_np(list(self.duplicate_list)), self.duplicate_sorted)
        
    def test_merge_sort_np(self):
        self.assertEqual(merge_sort_np(list(self.unsorted_list)), self.sorted_list)
        self.assertEqual(merge_sort_np(list(self.duplicate_list)), self.duplicate_sorted)
        self.assertEqual(merge_sort_np(list(self.empty_list)), self.empty_list)
        self.assertEqual(merge_sort_np(list(self.single_element_list)), self.single_element_list)

if __name__ == '__main__':
    unittest.main()
# Added comprehensive test cases

# TODO: Optimize large list sorting
