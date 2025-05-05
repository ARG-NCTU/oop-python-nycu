from typing import List
from itertools import pairwise

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        """
        Partition nums into two arrays, nums1 and nums2, such that:
        - Each element of the array nums belongs to either the array nums1 or the array nums2.
        - Both arrays are non-empty.
        - The value of the partition is minimized.
        - The value of the partition is |max(nums1) - min(nums2)|.

        Args:
        nums (List[int]): A positive integer array.

        Returns:
        int: The value of the partition.

        Examples:
        >>> solution = Solution()
        >>> solution.findValueOfPartition([1, 3, 2, 4])
        1
        >>> solution.findValueOfPartition([100, 1, 10])
        9
        """
        nums.sort()
        min = nums[1] - nums[0]
        for i in range(2, len(nums)):
            val = nums[i] - nums[i - 1]
            if val < min:
                min = val
        return min
    
# class Solution:
#     def findValueOfPartition(self, nums: List[int]) -> int:
#         return min(x - y for y, x in pairwise(sorted(nums)))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)    