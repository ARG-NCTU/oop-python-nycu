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
        self.parents[self.find(x)] = self.find(y)

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dsu = DisjointSetUnion(n)

        for v1, v2, c in roads:
            dsu.union(v1-1, v2-1)

        min_score = 10000
        s_par = dsu.find(0)
        
        for v1, v2, c in roads:
            if dsu.find(v2-1) == s_par:
                min_score = min(min_score, c)

        return min_score