from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        Check if it's possible to reach any index with value 0 starting from a given start index.

        You are initially positioned at the start index of the array. When you are at index i, 
        you can jump to i + arr[i] or i - arr[i].

        Parameters:
            arr (List[int]): An array of non-negative integers.
            start (int): The start index of the array.

        Returns:
            bool: True if it's possible to reach any index with value 0, False otherwise.

        Examples:
            >>> solution = Solution()

            # Example 1:
            >>> arr1 = [4,2,3,0,3,1,2]
            >>> start1 = 5
            >>> solution.canReach(arr1, start1)
            True

            # Example 2:
            >>> arr2 = [4,2,3,0,3,1,2]
            >>> start2 = 0
            >>> solution.canReach(arr2, start2)
            True

            # Example 3:
            >>> arr3 = [3,0,2,1,2]
            >>> start3 = 2
            >>> solution.canReach(arr3, start3)
            False
        """
        n = len(arr)
        visited = [False] * n

        def dfs(i):
            nonlocal arr, visited, n
            if i < 0 or i >= n or visited[i]:
                return False
            if arr[i] == 0:
                return True
            
            visited[i] = True
    
            return dfs(i + arr[i]) or dfs(i - arr[i])
        
        return dfs(start)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)    