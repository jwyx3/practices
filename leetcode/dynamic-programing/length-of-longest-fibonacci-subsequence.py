# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/solution/
# Time: O(N**2)
# Space: O(N*logM), M = max(A)

class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # strictly increasing, positive -> unique
        # dp(i,j): the longest sequence ending with A[i] and A[j]
        # dp(j,k) = dp(i,j) + 1 if A[k] = A[i] + A[j], i<j<k
        # i = pos.get(A[k]-A[j])
        # fibonacci space O(log(max(A)))
        N = len(A)
        pos = {x: i for i, x in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)
        res = 0
        for k in xrange(2, N):
            for j in xrange(k):
                i = pos.get(A[k] - A[j])
                if i is not None and j > i:
                    longest[j, k] = longest[i, j] + 1
                    res = max(res, longest[j, k])
        return res
