from collections import defaultdict, deque

class Solution(object):
    def minScore(self, n, roads):
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        visited = [False] * (n + 1)
        queue = deque([1])
        min_score = float('inf')
        
        while queue:
            node = queue.popleft()
            visited[node] = True
            for neighbor, weight in graph[node]:
                min_score = min(min_score, weight)
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    
        return min_score
   
    
n = 7
roads = [[1,3,1484],[3,2,3876],[2,4,6823],[6,7,579],[5,6,4436],[4,5,8830]]
a=Solution()
print(a.minScore(n,roads))