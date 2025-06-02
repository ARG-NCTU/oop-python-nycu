from typing import List
from bisect import bisect_left

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """
        Given a 0-indexed integer array nums and an integer p, finds p pairs of indices of nums
        such that the maximum difference amongst all the pairs is minimized. Also, ensures no index
        appears more than once amongst the p pairs.

        Args:
        nums (List[int]): A 0-indexed integer array.
        p (int): The number of pairs to be formed.

        Returns:
        int: The minimum maximum difference among all p pairs.

        Examples:
        >>> solution = Solution()
        >>> solution.minimizeMax([10, 1, 2, 7, 1, 3], 2)
        1
        >>> solution.minimizeMax([4, 2, 1, 2], 1)
        0
        """
        nums.sort()

        def valid_diff(diff):
            count, index = 0, 0
            while count < p and index < len(nums) - 1:
                if nums[index + 1] - nums[index] <= diff:
                    index += 2
                    count += 1
                else: index += 1

            return count == p

        return bisect_left(range(nums[-1] - nums[0]), True, key=valid_diff)

        # nums.sort()
        # left, right = 0, nums[-1] - nums[0]

        # def valid_diff(diff: int):
        #     i, count = 0, 0

        #     while i < len(nums) - 1 and count < p:
        #         if (nums[i + 1] - nums[i]) <= diff:
        #             count += 1
        #             i += 2
        #         else: 
        #             i += 1
        #     return count == p

        # while left < right:
        #     mid = (left + right) // 2
            
        #     if valid_diff(mid): 
        #         right = mid 
        #     else:
        #         left = mid + 1               

        # return left

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)