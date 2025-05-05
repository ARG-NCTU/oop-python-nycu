# You are given a positive integer n representing n cities numbered from 1 to n. 
# You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that 
# there is a bidirectional road between cities ai and bi with a distance equal to distancei. 
# The cities graph is not necessarily connected.
# The score of a path between two cities is defined as the minimum distance of a road in this path.
# Return the minimum possible score of a path between cities 1 and n.

class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        