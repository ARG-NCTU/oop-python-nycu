from typing import List

class DisjointSetUnion:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        
    def find(self, x):
        if self.parents[x] == x:
            return x
        
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x_par, y_par = self.find(x), self.find(y)
        self.parents[x_par] = y_par

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Return the total number of provinces in a group of directly or indirectly connected cities.

        Parameters:
            isConnected (List[List[int]]): An n x n matrix where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

        Returns:
            int: The total number of provinces.

        Examples:
            >>> solution = Solution()

            # Example 1:
            >>> isConnected1 = [[1,1,0],[1,1,0],[0,0,1]]
            >>> solution.findCircleNum(isConnected1)
            2

            # Example 2:
            >>> isConnected2 = [[1,0,0],[0,1,0],[0,0,1]]
            >>> solution.findCircleNum(isConnected2)
            3
        """
        m = len(isConnected)
        dsu = DisjointSetUnion(m)

        for i in range(m):
            for j in range(i+1, m):
                if isConnected[i][j]: 
                    dsu.union(i, j)

        return len(set(dsu.find(i) for i in range(m)))
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)    