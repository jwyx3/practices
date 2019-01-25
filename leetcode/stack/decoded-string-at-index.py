# https://leetcode.com/problems/decoded-string-at-index/
# https://leetcode.com/problems/decoded-string-at-index/solution/
# We can use this insight by working backwards, keeping track of the size of the decoded string. Whenever the decoded string would equal some word repeated d times, we can reduce K to K % (word.length).
# Time: O(N)
# Space: O(1)

class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        size = 0
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
        
        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c
            
            if c.isdigit():
                size /= int(c)
            else:
                size -= 1
