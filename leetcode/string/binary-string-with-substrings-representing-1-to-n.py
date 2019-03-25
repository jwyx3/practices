# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/
# https://www.youtube.com/watch?v=AxVUCzee-XI
# Time: O(len(S)**2)
# Space: O(1)

class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        # if 11, 10 in S, then 1, 0 is in S
        # [1024, 2047] -> last 10 bits are different
        # given len(S) = 1000, then if can represent 1000 - 10 + 1 = 991 numbers
        # So time will be O(len(S)**2)
        for i in xrange(N, N / 2 - 1, -1):
            if S.find(bin(i)[2:]) == -1:
                return False
        return True
