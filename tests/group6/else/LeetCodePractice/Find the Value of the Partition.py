
from typing import List

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        minimum = nums_sorted[1] - nums_sorted[0]  # 初始差值
        for i in range(1, len(nums) - 1):  # 從 i=1 到 n-2
            diff = nums_sorted[i + 1] - nums_sorted[i]
            minimum = min(minimum, diff)
        return minimum