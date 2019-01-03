# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
# https://buptwc.com/2018/06/26/Leetcode-857-Minimum-Cost-to-Hire-K-Workers/
#
# Time: O(N*logN)
# Space: O(N)

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        # convert into float
        workers = sorted([
            (float(w)/q, q) for q, w in itertools.izip(quality, wage)])
        h, qsum = [], 0
        res = float('inf')
        for r, q in workers:
            # use r as worker with min wage
            heapq.heappush(h, -q)
            qsum += q
            # get smallest sum of K quality
            if len(h) > K:
                qsum += heapq.heappop(h)
            if len(h) == K:
                res = min(res, qsum * r)
        return res
