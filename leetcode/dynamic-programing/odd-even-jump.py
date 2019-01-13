# https://leetcode.com/contest/weekly-contest-119/problems/odd-even-jump/
# Time: O(n*logn + n * n) == O(n*n)
# Space: O(n)

class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # dp1[i]: can reach end from A[i] as odd jump
        # dp2[i]: can reach end from A[i] as even jump
        # dp1[i] = dp2[j], j from asc nums
        # dp2[i] = dp1[j], j from desc nums
        # initial: dp1[-1] = dp2[-1] = 1
        # answer: sum(dp1)
        N = len(A)
        dp1, dp2 = [0] * len(A), [0] * len(A)
        dp1[N - 1] = dp2[N - 1] = 1
        nums1, nums2 = [(A[-1], N - 1)], [(-A[-1], N - 1)]
        for i in xrange(N - 2, -1, -1):
            j = bisect.bisect_left(nums1, (A[i], -1))
            if j < len(nums1):
                dp1[i] = dp2[nums1[j][1]]
            nums1.insert(j, (A[i], i))
            
            j = bisect.bisect_left(nums2, (-A[i], -1))
            if j < len(nums2):
                dp2[i] = dp1[nums2[j][1]]
            nums2.insert(j, (-A[i], i))
        return sum(dp1)

# TODO: optimization
# can use BST to insert and search nums1 and nums2 in O(logn)
# Time: O(nlogn)
