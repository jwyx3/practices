# https://leetcode.com/problems/di-string-match/
# https://leetcode.com/problems/di-string-match/solution/
# divide and conquer
# if I, put smallest number, the smaller problem is [1,2,..,N] and S[1:]
# if D, put largest number, the smaller problem is [0,1,..,N-1] and S[1:]

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        N = len(S)
        lo, hi = 0, N
        for c in S:
            if c == 'I':
                res.append(lo)
                lo += 1
            else:
                res.append(hi)
                hi -= 1
        res.append(lo)
        return res
