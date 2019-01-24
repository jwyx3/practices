# https://leetcode.com/problems/most-profit-assigning-work/
# https://leetcode.com/problems/most-profit-assigning-work/solution/
# Binary search
# Time: O(NlogN + MlogM), N is len(jobs), M is len(worker)
# Space: O(N) ??

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = zip(difficulty, profit) 
        jobs.sort()
        res = 0
        best = i = 0
        for w in sorted(worker):
            while i < len(jobs) and jobs[i][0] <= w:
                best = max(best, jobs[i][1])
                i += 1
            res += best
        return res
