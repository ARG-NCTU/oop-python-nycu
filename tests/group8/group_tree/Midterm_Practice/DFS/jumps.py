from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False]*n
        def dfs(pos) -> bool:
            nonlocal n, visited, arr
            if pos < 0 or pos >= n or visited[pos]:
                return False
            if arr[pos] == 0:
                return True
            visited[pos] = True
            return dfs(pos - arr[pos]) or dfs(pos + arr[pos])
        return dfs(start)