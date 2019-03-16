# https://leetcode.com/problems/reorganize-string/
# Time: O(N)
# Space: O(N)

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ''
        ans, h = [], []
        count = collections.Counter(S)
        for k, v in count.iteritems():
            heapq.heappush(h, (-v, k))
        while len(h) > 1:
            used = []
            for _ in xrange(2):  # only care about adjacent elements
                cnt, c = heapq.heappop(h)
                ans.append(c)
                if -cnt > 1:
                    heapq.heappush(used, (-(-cnt - 1), c))
            for x in used:
                heapq.heappush(h, x)
        if h:
            if -h[0][0] > 1:
                return ''
            ans.append(h[0][1])
        return ''.join(ans)
