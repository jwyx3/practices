# https://leetcode.com/problems/pour-water/
# https://zxi.mytechroad.com/blog/simulation/leetcode-755-pour-water/
# simulation
# Time: O(V*N)
# Space: O(1)

class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        N, H = len(heights), heights
        for _ in xrange(V):
            best = K
            for d in (-1, 1):
                i = K
                while 0 <= i + d < N and H[i + d] <= H[i]:
                    if H[i + d] < H[best]:
                        best = i + d
                    i += d
                if best != K:
                    break
            H[best] += 1
        return H
