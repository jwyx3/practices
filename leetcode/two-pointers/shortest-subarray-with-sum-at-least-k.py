# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# https://www.cnblogs.com/tobeabetterpig/p/9550545.html
# Time: O(N)
# Space: O(N)

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # prefix sum + increasing queue
        # if psums[j] - psums[i] >= K, then we don't need to consider psums[i+1] and psums[j]
        # if psums[j] > psums[i] and i > j, psums[j] will not be candidate for psums[i + 1]
        n = len(A)
        q = collections.deque()
        ans = n + 1
        psums = [0] * (n + 1)
        for i in xrange(n):
            psums[i+1] = psums[i] + A[i]
        for i, x in enumerate(psums):
            while q and x - psums[q[0]] >= K:
                ans = min(ans, i - q.popleft())
            while q and x < psums[q[-1]]:
                q.pop()
            q.append(i)
        return ans if ans <= n else -1
