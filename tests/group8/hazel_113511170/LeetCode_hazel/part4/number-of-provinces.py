from collections import deque

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        grid=[[] for j in range (n)]

        for city in range(n):
            for i in range(n):
                if isConnected[city][i]==1 and city!=i:
                    grid[city].append(i)

        visited=[0 for k in range(n)]
        
        p=0
        for prov in range(n):
            if visited[prov]:
                continue

            queue=deque(grid[prov])
            
            while queue:
                curr=queue.popleft()
                for neighbor in grid[curr]:
                    if visited[neighbor] == 0:
                        visited[neighbor] = 1
                        queue.append(neighbor) 
            p=p+1

        return p
            
           


isConnected =[[1,1,0],[1,1,0],[0,0,1]]
a=Solution()
print(a.findCircleNum(isConnected))