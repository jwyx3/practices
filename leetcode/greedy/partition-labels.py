# https://leetcode.com/problems/partition-labels/
# https://leetcode.com/problems/partition-labels/solution/
# hint: Try to greedily choose the smallest partition that includes the first letter. If you have something like "abaccbdeffed", then you might need to add b. You can use an map like "last['b'] = 5" to help you expand the width of your partition.
# similar to merge intervals
# Time: O(N)
# Space: O(N)

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {}
        for i in xrange(len(S) - 1, -1, -1):
            if S[i] not in last:
                last[S[i]] = i
        res = []
        start = end = 0
        for i, c in enumerate(S):
            end = max(end, last[c])
            if end == i:
                res.append(end - start + 1)
                end += 1
                start = end
        return res
