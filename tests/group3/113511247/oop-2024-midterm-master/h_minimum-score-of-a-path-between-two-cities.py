from typing import List
import math

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
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """
        Return the minimum possible score of a path between cities 1 and n.

        Parameters:
            n (int): The number of cities.
            roads (List[List[int]]): A list of roads represented as triples of cities and distances.

        Returns:
            int: The minimum possible score of a path between cities 1 and n.

        Examples:
            >>> solution = Solution()

            # Example 1:
            >>> n1 = 4
            >>> roads1 = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
            >>> solution.minScore(n1, roads1)
            5

            # Example 2:
            >>> n2 = 4
            >>> roads2 = [[1,2,2],[1,3,4],[3,4,7]]
            >>> solution.minScore(n2, roads2)
            2
        """
        dsu = DisjointSetUnion(n)

        for v1, v2, c in roads:
            dsu.union(v1-1, v2-1)

        min_score = math.inf
        s_par = dsu.find(0)
        
        for v1, v2, c in roads:
            if dsu.find(v1-1) == s_par:
                min_score = min(min_score, c)

        return min_score
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)    