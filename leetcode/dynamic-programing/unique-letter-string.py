# https://leetcode.com/problems/unique-letter-string/
# Time: O(N)
# Space: O(N)

class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        # CABADA ->
        # C: 1
        # CA, A: 3
        # CAB, AB, B: 6
        # CABA, ABA, BA, A: 2+1+2+1=6
        # CABAD, ABAD, BAD, AD, D: 3+2+3+2+1=11
        # CABADA, ABADA, BADA, ADA, DA, A: 3+2+2+1+2+1=11
        
        # dp(i): unique characters for s[:i+1]
        # dp(i) = dp(i-1) + (i - last[s[i]]) - gap[s[i]]
        # gap[s[i]] = i - last[s[i]], last[s[i]] = i
        # initial: dp(-1) = 0, last[*] = -1, gap[*] = 0
        # answer: sum(dp)
        if not S:
            return 0
        dp = res = 0
        last = [-1] * 26
        gap = [0] * 26
        for i in xrange(len(S)):
            ci = ord(S[i]) - ord('A')
            # need to consider last three S[i]
            # S[i2]...S[i1]...S[i0]
            # all subsets between (S[i1]...S[i0]] include S[i]
            # all subsets between (S[i2]...S[i1]] exclude S[i]
            # gap is length of (S[i2]...S[i1]]; last is i1
            dp += (i - last[ci]) - gap[ci]
            gap[ci] = i - last[ci]
            last[ci] = i
            res += dp
        return res
