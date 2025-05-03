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
        """
        Determine if there is a valid path from vertex source to vertex destination in a bi-directional graph.

        Parameters:
            n (int): The number of vertices in the graph.
            edges (List[List[int]]): A list of edges represented as pairs of vertices.
            source (int): The source vertex.
            destination (int): The destination vertex.

        Returns:
            bool: True if there is a valid path from source to destination, False otherwise.

        Examples:
            >>> solution = Solution()

            # Example 1:
            >>> n1 = 3
            >>> edges1 = [[0,1],[1,2],[2,0]]
            >>> source1 = 0
            >>> destination1 = 2
            >>> solution.validPath(n1, edges1, source1, destination1)
            True

            # Example 2:
            >>> n2 = 6
            >>> edges2 = [[0,1],[0,2],[3,5],[5,4],[4,3]]
            >>> source2 = 0
            >>> destination2 = 5
            >>> solution.validPath(n2, edges2, source2, destination2)
            False
        """
        
        # parents = [i for i in range(n)]
        # def find(x):
        #     nonlocal parents
        #     if parents[x] == x:
        #         return x
            
        #     parents[x] = find(parents[x])
        #     return parents[x]
            
        # def union(x, y):
        #     nonlocal parents
        #     x_par, y_par = find(x), find(y)

        #     parents[x_par] = y_par

        # for e in edges:
        #     union(*e)

        # return find(source) == find(destination)
        
        dsu = DisjointSetUnion(n)

        for e in edges:
            dsu.union(*e)

        return dsu.find(source) == dsu.find(destination)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)    
