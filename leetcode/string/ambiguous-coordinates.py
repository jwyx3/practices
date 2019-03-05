# https://leetcode.com/problems/ambiguous-coordinates/
# Time: O(N**3)
# Space: O(N**3), include result

class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S[1:-1]
        def f(s):
            n = len(s)
            for i in xrange(1, n + 1):
                left, right = s[:i], s[i:]
                if (not left.startswith('0') or left == '0') and not right.endswith('0'):
                    if i == n:
                        yield left
                    else:
                        yield left + '.' + right
        
        return ['(%s, %s)' % x for i in xrange(1, len(S))
                for x in itertools.product(f(S[:i]), f(S[i:]))]

