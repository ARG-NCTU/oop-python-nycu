from typing import List

class Union:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def lead(self, x) -> int:
        if self.parent[x] == x:
            return x

        self.parent[x] = self.lead(self.parent[x])
        return self.parent[x]

    def connect(self, a, b):
        self.parent[self.lead(a)] = self.lead(b)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        a = Union(n)

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    a.connect(i, j)

        return len(set([a.lead(i) for i in range(n)]))

# Example usage
if __name__ == "__main__":
    isConnected = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    solution = Solution()
    print(solution.findCircleNum(isConnected))