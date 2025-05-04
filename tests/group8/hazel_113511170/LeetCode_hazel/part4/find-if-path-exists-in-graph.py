from collections import deque

# Target :use BFS and get better time efficiency

class Solution(object):

    # whether or not the path can go from src to destination
    def validPath(self, n, edges, source, destination):
        grid=[[] for i in range (n)]
        for path in edges:
            grid[path[0]].append(path[1])
            grid[path[1]].append(path[0])


        # Make graph[source] be queue and set all the point unvisited other than source
        visited=[0 for m in range(n)]
        queue=deque(grid[source])
        visited[source]=True

        # Perform BFS 
        # Search for all neighbors of the source
        while queue:
            curr=queue.popleft()
            if curr==destination:
                return True
            
            for neighbor in grid[curr]:
                if visited[neighbor] == 0:
                    visited[neighbor] = 1
                    # the point in queue is all the points the source can reach
                    queue.append(neighbor)         
        # If queue become empty, the destination cannot be reached
        return False
    
n = 10
edges =[[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
source = 7
destination = 5
apple= Solution()
print("Apple Map (From {} to {}): {}".format(source,destination, apple.validPath(n,edges,source,destination)))

n =6
edges =[[0,1],[0,2],[3,5],[5,4],[4,3]]
source =0
destination =5
mango=Solution()
print("Mango Map (From {} to {}): {}".format(source,destination,mango.validPath(n,edges,source,destination)))

