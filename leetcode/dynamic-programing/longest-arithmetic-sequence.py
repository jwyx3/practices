# https://leetcode.com/problems/longest-arithmetic-sequence/
# use array of dict
# Time: O(n*n)
# Space: O(n*abs(max(nums) - min(nums)))

class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # dp[i][d]: length of LIS ending at A[i] with A[i] - A[j] == d
        # dp[i][d] = max(dp[j].get(d, 1) + 1), if A[i] - A[j] == d, 0 <= j < i
        # Answer: max(dp[*][*])
        # Special case:
        # max(x): x can't be empty list
        n = len(A)
        dp = [{} for _ in xrange(n)]
        for i in xrange(n):
            for j in xrange(i):
                d = A[i] - A[j]
                if d not in dp[i]:
                    dp[i][d] = dp[j].get(d, 1) + 1
                else:
                    dp[i][d] = max(dp[i][d], dp[j].get(d, 1) + 1)
        return max(max(dp[i].itervalues() if dp[i] else [1]) for i in xrange(n))
                
# use one dict
# https://leetcode.com/problems/longest-arithmetic-sequence/discuss/274611/JavaC%2B%2BPython-DP
# dp[i, d]: length of LIS ending at A[i] with A[i] - A[j] == d  
