# https://leetcode.com/problems/stamping-the-sequence/
# https://www.youtube.com/watch?v=qTDYfhuqCVg
# Time: O(N*(N-M)*M)
# Space: O(N+M)

class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        t, s = list(target), stamp
        if t[0] != s[0] or t[-1] != s[-1]:
            return []
        N, M = len(target), len(stamp)
        
        # t='ababc', s='abc' => t='ab***', ret=3
        # unstamp t[i:i+M] if it's possible and then return newly added *
        def unstamp(i):
            res = M
            for j in xrange(M):
                if t[i+j] == '*':
                    res -= 1
                    continue
                if t[i+j] != s[j]:
                    return 0
            t[i:i+M] = '*' * M
            return res
        
        prev, curr = -1, N
        res = []
        seen = [0] * N
        while curr and prev != curr:
            prev = curr
            for i in xrange(N - M + 1):
                if seen[i]:
                    continue
                changed = unstamp(i)
                if changed:
                    curr -= changed
                    seen[i] = 1
                    res.append(i)
        return res[::-1] if not curr else []
