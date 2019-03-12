# https://leetcode.com/problems/orderly-queue/
# https://leetcode.com/problems/orderly-queue/solution/
# Time: O(N**2 + NlogN)
# Space: O(N**2)

class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # bubble sort
        # if K > 1, we can always swap two adjacent characters
        # E.g. swap S[i] and S[i+1]
        # 1. rotate the whole string to be starting with S[i]
        # 2. rotate the S[1:] to be ending with S[i+1]
        # 3. rotate the whole string to be ending with S[i+1], S[i]
        # 4. rotate the whole string to be ..., S[i-1], S[i+1], S[i], S[i+2], ...
        if K > 1:
            return ''.join(sorted(S))
        return min(S[i:] + S[:i] for i in xrange(len(S)))
    
