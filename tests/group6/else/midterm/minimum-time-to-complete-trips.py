from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """
        Returns the minimum time required for all buses to complete at least the given number of totalTrips.

        Parameters:
            time (List[int]): An array of integers representing the time taken by each bus to complete one trip.
            totalTrips (int): An integer representing the number of trips all buses should make in total.

        Returns:
            int: The minimum time required for all buses to complete at least totalTrips trips.

        Examples:
            >>> solution = Solution()
            >>> time1 = [1, 2, 3]
            >>> totalTrips1 = 5
            >>> solution.minimumTime(time1, totalTrips1)
            3

            >>> time2 = [2]
            >>> totalTrips2 = 1
            >>> solution.minimumTime(time2, totalTrips2)
            2
        """
        check = lambda t: sum(t // bus for bus in time) >= totalTrips
        lo, hi = 0, time[0] * totalTrips
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid): 
                hi = mid
            else:          
                lo = mid + 1
        return lo
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)