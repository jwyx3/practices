# https://leetcode.com/problems/number-of-squareful-arrays/
# Time: O(N*N*2**N)??
# Space: O(N*2**N)

class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # f(visited, prev_idx) -> dp(s, i)
        m, n = 1 << len(A), len(A)
        A.sort()
        
        graph = collections.defaultdict(set)
        for i in xrange(n - 1):
            for j in xrange(i + 1, n):
                t = A[i] + A[j]
                if int(t ** 0.5) ** 2 == t:
                    graph[i].add(j)
                    graph[j].add(i)
        
        dp = [[0] * n for _ in xrange(m)]
        for i in xrange(n):
            if i > 0 and A[i-1] == A[i]:
                continue
            dp[1 << i][i] = 1
        
        for s in xrange(m):
            for i in xrange(n):
                if dp[s][i]:  # valid previous state
                    for j in graph[i]:
                        # remove duplicate. if two elements are same,
                        # only pick the second one if the previous one are used.
                        if j > 0 and A[j-1] == A[j] and s & (1 << (j-1)) == 0:
                            continue
                        if s & (1 << j) == 0:  # not visited
                            dp[s | (1 << j)][j] += dp[s][i]
        return sum(dp[m - 1])


# TODO: check backtracking!!
# https://leetcode.com/problems/number-of-squareful-arrays/solution/
# Hamiltonian paths of this graph: paths that visit all the nodes exactly once
