class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        total = 0
        def find(place):
            visited.add(place)
            for j in range(len(isConnected[0])) :
                if not j in visited :
                   if isConnected[place][j] ==1:
                     find(j)
            

        for i in range(len(isConnected)):
            if not i in visited:
                find(i)
                total += 1




        return total