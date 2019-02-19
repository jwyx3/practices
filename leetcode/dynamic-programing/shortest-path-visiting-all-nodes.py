# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/solution/
# A path 'state' can be represented as the subset of nodes visited, plus the current 'head' node.
# dp[state][head]: shortest distance for current state
# dp[state][head] = min(1 + dp[state|(1 << nei)][nei] for nei in graph[head])
# initial: dp[1<<head][head] = 0, one node
# answer: min(dp[2**N-1])
# notice:
# 1. state|(1<<nei) >= state, so the recurrence on states form a DAG. so we can use dynamic programming.
# 2. because state|(1<<nei) == state, so we need to recalculate this state to get potential new min.
# Time: O(2**N * N)
# Space: O(2**N * N)
#
# also refer to bfs/shortest-path-visiting-all-nodes.py

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        dp = [[N * N] * N for _ in xrange(1 << N)]
        for x in xrange(N):
            dp[1 << x][x] = 0
        
        for state in xrange(1 << N):
            repeat = True
            while repeat:
                repeat = False
                for head in xrange(N):
                    d = dp[state][head]
                    for nei in graph[head]:
                        state2 = state | (1 << nei)
                        if d + 1 < dp[state2][nei]:
                            dp[state2][nei] = d + 1
                            if state == state2:
                                repeat = True
        return min(dp[(1 << N) - 1])
