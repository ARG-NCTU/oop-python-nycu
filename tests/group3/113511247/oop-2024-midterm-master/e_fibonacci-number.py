class Solution:
    def fib(self, n: int) -> int:
        """
        Calculates the nth Fibonacci number.

        Parameters:
            n (int): The index of the Fibonacci number to calculate.

        Returns:
            int: The value of the nth Fibonacci number.

        Constraints:
            0 <= n <= 30

        Examples:
            >>> solution = Solution()
            >>> solution.fib(2)
            1
            >>> solution.fib(3)
            2
            >>> solution.fib(4)
            3
            >>> solution.fib(0)
            0
            >>> solution.fib(1)
            1
            >>> solution.fib(30)
            832040
        """
        
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)    