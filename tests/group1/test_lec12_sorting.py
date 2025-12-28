# Minor comment change for version control
import unittest
from add_path import add_path
add_path()
from lec12_sorting import bubble_sort_np, selection_sort_np, merge_sort_np

class TestSortingAlgorithms(unittest.TestCase):
    """
    測試 lec12_sorting.py 中所有 'np' 版本的排序演算法。
    """
    
    def setUp(self):
        self.flag = True 
        """
        設定測試用的列表數據
        """
        # 亂序列表
        self.unsorted_list = [6, 2, 7, 3, 5, 9, 1, 4, 8, 0]
        # 已排序的標準答案
        self.sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 含有重複元素的列表
        self.duplicate_list = [5, 2, 8, 2, 5, 1, 8]
        self.duplicate_sorted = [1, 2, 2, 5, 5, 8, 8]
        # 空列表
        self.empty_list = []
        # 單一元素列表
        self.single_element_list = [42]
        
    def test_bubble_sort_np(self):
        """測試氣泡排序"""
        # 測試亂序列表
        list_to_test = list(self.unsorted_list) # 使用 list() 避免修改原始 unsorted_list
        self.assertEqual(bubble_sort_np(list_to_test), self.sorted_list, "氣泡排序測試失敗 (亂序)")
        
        # 測試重複元素
        list_to_test = list(self.duplicate_list)
        self.assertEqual(bubble_sort_np(list_to_test), self.duplicate_sorted, "氣泡排序測試失敗 (重複元素)")
        
        # 測試空列表
        list_to_test = list(self.empty_list)
        self.assertEqual(bubble_sort_np(list_to_test), self.empty_list, "氣泡排序測試失敗 (空列表)")
        
        # 測試單一元素
        list_to_test = list(self.single_element_list)
        self.assertEqual(bubble_sort_np(list_to_test), self.single_element_list, "氣泡排序測試失敗 (單一元素)")
        
    def test_selection_sort_np(self):
        """測試選擇排序"""
        # 測試亂序列表
        list_to_test = list(self.unsorted_list)
        self.assertEqual(selection_sort_np(list_to_test), self.sorted_list, "選擇排序測試失敗 (亂序)")
        
        # 測試重複元素
        list_to_test = list(self.duplicate_list)
        self.assertEqual(selection_sort_np(list_to_test), self.duplicate_sorted, "選擇排序測試失敗 (重複元素)")
        
    def test_merge_sort_np(self):
        """測試合併排序"""
        # 測試亂序列表
        list_to_test = list(self.unsorted_list)
        self.assertEqual(merge_sort_np(list_to_test), self.sorted_list, "合併排序測試失敗 (亂序)")
        
        # 測試重複元素
        list_to_test = list(self.duplicate_list)
        self.assertEqual(merge_sort_np(list_to_test), self.duplicate_sorted, "合併排序測試失敗 (重複元素)")
        
        # 測試空列表
        list_to_test = list(self.empty_list)
        self.assertEqual(merge_sort_np(list_to_test), self.empty_list, "合併排序測試失敗 (空列表)")
        
        # 測試單一元素
        list_to_test = list(self.single_element_list)
        self.assertEqual(merge_sort_np(list_to_test), self.single_element_list, "合併排序測試失敗 (單一元素)")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)