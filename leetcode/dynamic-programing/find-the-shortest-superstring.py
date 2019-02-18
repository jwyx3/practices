# https://leetcode.com/problems/find-the-shortest-superstring/
# https://zxi.mytechroad.com/blog/searching/leetcode-943-find-the-shortest-superstring/
# => memoization of the combination and last node instead of permutation.
# dp(state, i): min cost to visit nodes of state and ends with i. each bit in state means whether the node is used or not.
# cost[i][j]: cost of word[j] after word[i]. e.g. word[i] = 'gcta', word[j] = 'ctaagt', cost[i][j] = 3
# parent[state][i]: prev word of i
# dp(state, j) = min{dp(state - (1<<j), i) + cost[i][j]}
# initial: dp((1<<i), i) = len(word[i])
# answer: min(dp((2 << n) - 1, *)) 
#
# O(n!) can only handle n <= 10
# O(2**n) can only handle n <= 20

class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        N = len(A)
        # cost[i][j]: the extra length if we put word[j] after word[i]
        def dist(i, j):
            n, m = len(A[i]), len(A[j])
            res = m
            for k in xrange(1, min(n, m)):
                if A[i][n - k:] == A[j][:k]:
                    res = min(res, m - k)
            return res
        
        cost = [[0] * N for _ in xrange(N)]
        for i in xrange(N):
            for j in xrange(N):
                if i != j:
                    cost[i][j] = dist(i, j)
        
        MAX_LEN = sum(len(x) for x in A) + 1
        dp = [[MAX_LEN] * N for _ in xrange(1 << N)]
        parent = [[-1] * N for _ in xrange(1 << N)]
        # for one word
        for i in xrange(N):
            dp[1 << i][i] = len(A[i])
        # start from small state
        for s in xrange(1 << N):
            for j in xrange(N):
                # if s is invalid. because s must include 1 << j
                if s & (1 << j) == 0:
                    continue
                prev_s = s - (1 << j)
                for i in xrange(N):
                    # if prev_s is valid.
                    if prev_s & (1 << i):
                        nlen = dp[prev_s][i] + cost[i][j]
                        if dp[s][j] > nlen:
                            dp[s][j] = nlen
                            parent[s][j] = i
        # find path
        min_i, min_len = -1, MAX_LEN
        for i, l in enumerate(dp[-1]):
            if l < min_len:
                min_i, min_len = i, l
        res = []
        s, curr = (1 << N) - 1, min_i
        while s:
            n = len(A[curr])
            prev = parent[s][curr]
            if prev == -1:
                res.append(A[curr])
            else:
                res.append(A[curr][n - cost[prev][curr]:])
            s &= ~(1 << curr)
            curr = prev
        return ''.join(res[::-1])

