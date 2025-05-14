from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = min(time) * totalTrips
        
        while left < right:
            mid = (left + right) // 2
            trips = sum(mid // t for t in time)
            
            if trips >= totalTrips:
                right = mid  # 時間可能過大，試更小的時間
            else:
                left = mid + 1  # 時間太小，試更大的時間
                
        return left
    # mid = (left + right) // 2 搭配 return left if trips >= totalTrips: right = mid # 時間可能過大，試更小的時間 else: left = mid + 1