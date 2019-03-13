# https://leetcode.com/problems/groups-of-special-equivalent-strings/
# https://leetcode.com/problems/groups-of-special-equivalent-strings/solution/
# Time: O(sum(len(word)))
# Space: O(N)

class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # key: (odd count, even count)
        # find identity of each word in A
        def count(word):
            ans = [0] * 52
            for i, c in enumerate(word):
                ans[ord(c) - ord('a') + 26 * (i % 2)] += 1
            return tuple(ans)

        return len({count(word) for word in A})
    
