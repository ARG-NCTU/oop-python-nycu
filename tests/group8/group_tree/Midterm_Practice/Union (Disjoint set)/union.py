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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        dsu = DisjointSetUnion(n)

        for a, b in edges:
            dsu.union(a, b)

        return dsu.find(source) == dsu.find(destination)