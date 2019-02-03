# https://leetcode.com/problems/rearrange-string-k-distance-apart/
# Time: O(NlogN)
# Space: O(N)
# greedy + heap + corner case

class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # corner case
        if k <= 1:
            return s
        counter = collections.Counter(s)
        h = [(-cnt, c) for c, cnt in counter.iteritems()]
        # heapify
        heapq.heapify(h)
        res = []
        while h:
            visited = []
            for _ in xrange(k):
                if not h:
                    if visited:
                        return ''
                    break
                cnt, c = heapq.heappop(h)
                cnt = -cnt
                res.append(c)
                if cnt > 1:
                    visited.append((cnt - 1, c))
            for cnt, c in visited:
                heapq.heappush(h, (-cnt, c))
        return ''.join(res)
