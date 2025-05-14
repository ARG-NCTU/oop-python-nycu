class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums = sorted(nums)
        n = len(nums)
        left = 0
        right = nums[n-1] - nums[0]
        while left < right:
            mid = (left + right)//2
            counts = 0
            i = 0
            while i < n-1:
                if nums[i+1] - nums[i] <= mid:
                    counts += 1
                    i += 2
                else:
                    i += 1

            if counts >= p:
                right = mid
            else:
                left = mid + 1
        return left