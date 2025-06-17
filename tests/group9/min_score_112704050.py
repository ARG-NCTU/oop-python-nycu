"""
Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.
Example 2:


Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.
"""

def path(roads,node,n):
    visited = set()
    score = []
    queue = [node]
    min_score = 10**10
    while queue:
        node = queue.pop(0)
        print(f"node:{node}")

        if node == n:
            return min_score
        
        visited.add(node)
        for u,v,d in roads:
            if u == node or v == node:
                min_score = min(min_score,d)
                if u == node:
                    neighbor = v
                else:
                    neighbor = u
                if neighbor not in visited:
                    queue.append(neighbor)
     
        print(min_score)
        
n = 4
roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
n = 4
roads = [[1,2,2],[1,3,4],[3,4,7]]
print(path(roads,1,n))