# https://leetcode.com/problems/ipo/
# Time: O(NlogN)
# Space: O(N)

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        # get max profit with enough captival
        n = len(profits)
        
        projects = sorted([(c, p) for c, p in itertools.izip(capital, profits)])
        h, curr = [], 0
        while curr < n and projects[curr][0] <= w:
            heapq.heappush(h, -projects[curr][1])
            curr += 1
        
        while h and k:
            profit = -heapq.heappop(h)
            w += profit
            k -= 1
            while curr < n and projects[curr][0] <= w:
                heapq.heappush(h, -projects[curr][1])
                curr += 1
        
        return w
