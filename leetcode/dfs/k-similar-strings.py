# https://leetcode.com/problems/k-similar-strings/
# TODO: more methods
# Time of DFS??

class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        
        n, A = len(A), list(A)
        memo = {}
        
        def dfs(start):
            if start == n:
                return 0
            key = tuple(A[start:])
            if key in memo:
                return memo[key]
            if A[start] == B[start]:
                k = dfs(start + 1)
            else:
                k = float('inf')
                for i in xrange(start + 1, n):
                    if A[i] == B[start]:
                        A[i], A[start] = A[start], A[i]
                        k = min(k, dfs(start + 1) + 1)
                        A[i], A[start] = A[start], A[i]
            memo[key] = k
            return k
        
        return dfs(0)
