class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        adj = [[]for i in range(n+1)]
        visited = set()
        for a,b,distance in roads:
            adj[a].append((b,distance))
            adj[b].append((a,distance))
        minimum = float('inf')

        def find(place):
            nonlocal minimum
            if not place in visited:
                visited.add(place)
                for neighbor,dis in adj[place]:
                    if dis < minimum:
                        minimum = dis
                    find(neighbor)
        find(1)




        return minimum
    #float('inf')無限大 float('-inf')無限小