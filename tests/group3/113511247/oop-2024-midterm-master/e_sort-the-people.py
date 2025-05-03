from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """
        Sorts the names of people in descending order by their heights.

        Parameters:
            names (List[str]): An array of strings representing the names of people.
            heights (List[int]): An array of distinct positive integers representing the heights of people.

        Returns:
            List[str]: The names sorted in descending order by heights.

        Examples:
            >>> solution = Solution()
            >>> names1 = ["Mary", "John", "Emma"]
            >>> heights1 = [180, 165, 170]
            >>> solution.sortPeople(names1, heights1)
            ['Mary', 'Emma', 'John']

            >>> names2 = ["Alice", "Bob", "Bob"]
            >>> heights2 = [155, 185, 150]
            >>> solution.sortPeople(names2, heights2)
            ['Bob', 'Alice', 'Bob']
        """
        # zip(heights, names) = a list of tuples where each tuple is (height, name)
        # _, name : heights ignored (_ means dontcare)
        # reverse = True : descending
        return[name for _, name in sorted(zip(heights, names), reverse = True)]
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)