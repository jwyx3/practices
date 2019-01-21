# https://leetcode.com/problems/custom-sort-string/
# https://leetcode.com/problems/custom-sort-string/solution/
# count and sort
# Time: O(len(S) + len(T))
# Space: O(len(T))

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        count = collections.Counter(T)
        res = []
        for c in S:
            res.extend([c] * count[c])
            count[c] = 0
        for c in count.iterkeys():
            if count[c] > 0:
                res.extend([c] * count[c])
        return ''.join(res)
        
