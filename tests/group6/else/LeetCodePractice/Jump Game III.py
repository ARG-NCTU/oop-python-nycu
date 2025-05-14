class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        def find(index):
            if index < 0 or index >= len(arr):
                return False
            if arr[index] == 0:
                return True
            if index in visited:
                return False
            
            else:
                visited.add(index)
                return find(index + arr[index]) or find(index - arr[index])
        
        return find(start)