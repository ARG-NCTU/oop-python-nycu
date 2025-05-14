class Solution:
    def fib(self, n: int) -> int:
        memo = {}  # 局部記憶化字典
        
        def fib_helper(n: int) -> int:
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n in memo:
                return memo[n]
            
            memo[n] = fib_helper(n - 1) + fib_helper(n - 2)
            return memo[n]
        
        return fib_helper(n)