# https://leetcode.com/problems/find-and-replace-in-string/
# https://leetcode.com/problems/find-and-replace-in-string/solution/
# Time: O(len(S) * len(targets))
# Space: O(len(S))

class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        res = list(S)
        # in reversed order
        for i, x, y in sorted(zip(indexes, sources, targets), reverse=True):
            if all(i + k < len(S) and S[i+k] == x[k] for k in xrange(len(x))):
                res[i:i+len(x)] = y
        return ''.join(res)
