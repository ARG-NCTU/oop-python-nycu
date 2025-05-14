class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        def find(place):
            if place == destination:
                return True
            visited.add(place)
            for neighbor in adj[place]:
                if not neighbor in visited:
                    if find(neighbor):
                        return True
            return False
        return find(source)