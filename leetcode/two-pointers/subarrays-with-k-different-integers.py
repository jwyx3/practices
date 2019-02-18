# https://leetcode.com/problems/subarrays-with-k-different-integers/
# https://leetcode.com/problems/subarrays-with-k-different-integers/solution/
# other idea: convert K to at most K - at most (K-1)
# Time: O(N)
# Space: O(1)
#
# for each r, [l1,l2] are be a contiguous interval.
# Thr r, l1 and l2 must be monotone increeasing. 
# -> use sliding window

class Window(object):
    def __init__(self):
        self.count = collections.Counter()
        self.unique = 0
    def add(self, x):
        if self.count[x] == 0:
            self.unique += 1
        self.count[x] += 1
    def remove(self, x):
        self.count[x] -= 1
        if self.count[x] == 0:
            self.unique -= 1

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        w1 = Window()
        w2 = Window()
        res = l1 = l2 = 0
        for x in A:
            w1.add(x)
            w2.add(x)
            while w1.unique > K:
                w1.remove(A[l1])
                l1 += 1
            while w2.unique >= K:
                w2.remove(A[l2])
                l2 += 1
            res += l2 - l1
        return res
