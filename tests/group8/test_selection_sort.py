#selction sort python test file
import unittest
from lec12_sortings import selection_sort

class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(selection_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(selection_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        self.assertEqual(selection_sort([1]), [1])  # Single element
        self.assertEqual(selection_sort([]), [])  # Empty list
        self.assertEqual(selection_sort([1, 2, 3]), [1, 2, 3])  # Already sorted
        self.assertEqual(selection_sort([2, 3, 1]), [1, 2, 3])  # Unsorted
        self.assertEqual(selection_sort([1, 0, -1]), [-1, 0, 1])  # Negative numbers

if __name__ == "__main__":
    unittest.main()   # Run the tests. 
