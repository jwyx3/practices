# https://leetcode.com/problems/binary-trees-with-factors/
# Time: O(N**2)
# Space: O(N)

class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        if not A:
            return 0
        
        A.sort(reverse=True)
        memo = {}
        def dp(start):
            if start in memo:
                return memo[start]
            l, r = start + 1, len(A) - 1
            res = 1  # without any child
            while l <= r:
                if A[l] * A[r] == A[start]:
                    cnt = dp(l) * dp(r)
                    if l != r:
                        cnt *= 2  # swap left and right subtree
                    res += cnt
                    l += 1
                    r -= 1
                elif A[l] * A[r] < A[start]:
                    r -= 1
                else:
                    l += 1
            memo[start] = res
            return res
        return sum(dp(i) for i in xrange(len(A))) % (10**9 + 7)
