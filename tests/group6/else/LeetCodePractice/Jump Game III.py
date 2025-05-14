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
    #注意：不能用 {} 創建空集合（這會創建空字典），必須用 set()。

#from typing import List

#class Solution: def canReach(self, arr: List[int], start: int) -> bool: # 創建集合記錄已訪問的索引 visited = set()