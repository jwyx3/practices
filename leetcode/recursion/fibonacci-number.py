# https://leetcode.com/problems/fibonacci-number/
# Time: O(N)
# Space: O(N)

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        memo = {}
        
        def f(n):
            if n < 2:
                return n
            if n in memo:
                return memo[n]
            memo[n] = f(n-1) + f(n-2)
            return memo[n]
        
        return f(N)
