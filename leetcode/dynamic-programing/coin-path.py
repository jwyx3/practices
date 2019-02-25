# https://leetcode.com/problems/coin-path/
# Time: O(N*B)
# Space: O(N)
# Input: O(n), Subproblems: O(n), Depends on: O(1)
# category: 1.1
# other factors:
# 1. define of subproblem: A[:i+1] or A[i:]
# 2. recurrence formula: pull or push
# 3. prev vs. next array

# http://www.cnblogs.com/grandyang/p/8183477.html
# A[:i+1], pull, prev -> can't handle lexicographically smallest such path elegantly

class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        # dp[i]: min cost to reach A[i].
        # dp[i] = min(dp[k] + A[i]) if A[i] >= 0, i-B<=k<i
        # prev[i]: the index of previous jump
        # initial: dp[0] = 0, others -1
        # answer: [] if dp[N-1] < 0
        #         get answer from prev
        
        if not A or A[-1] == -1 or B <= 0:
            return []
        N = len(A)
        # size: use to get the lexicographically smallest such path.
        # e.g. [0,0,0,0,0,0], 3
        dp, prev, size = [-1] * N, [-1] * N, [1] * N
        dp[0] = 0
        for i in xrange(1, N):
            if A[i] < 0:
                continue
            for k in xrange(max(0, i - B), i):
                if dp[k] < 0 :
                    continue
                cost = dp[k] + A[i]
                if dp[i] < 0 or dp[i] > cost or (dp[i] == cost and size[k] + 1 > size[i]):
                    dp[i] = dp[k] + A[i]
                    size[i] = size[k] + 1
                    prev[i] = k
        if dp[-1] < 0:
            return []
        ans, i = [], N - 1
        while i >= 0:
            ans.append(i+1)
            i = prev[i]
        return ans[::-1]

# better way
# A[i:], pull, next array

class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        # dp[i]: min cost for A[i:]
        # dp[i] = min(dp[k] + A[i]), i+1<=k<=min(N-1, i+B), if dp[k] and A[i] >= 0
        # initial: dp[N-1] = 0
        # answer: [] if dp[0] < 0, construct from next
        if not A or A[-1] < 0 or B <= 0:
            return []
        N = len(A)
        dp, pos = [-1] * N, [-1] * N
        dp[-1] = 0
        for i in xrange(N-2, -1, -1):
            if A[i] < 0:
                continue
            for k in xrange(i+1, min(N-1, i+B) + 1):
                if dp[k] < 0:
                    continue
                if dp[i] < 0 or dp[i] > dp[k] + A[i]:
                    dp[i] = dp[k] + A[i]
                    pos[i] = k
        if dp[0] < 0:
            return []
        ans, i = [], 0
        while i >= 0:
            ans.append(i+1)
            i = pos[i]
        return ans
