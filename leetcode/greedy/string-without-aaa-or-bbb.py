# https://leetcode.com/problems/string-without-aaa-or-bbb/
# https://leetcode.com/problems/string-without-aaa-or-bbb/solution/
# should write the most common letter first.
# greedy
# Time: O(A + B)
# Space: O(A + B)

class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        def generate(m, n, mc, nc):
            res = []
            while m > 0 or n > 0:
                if m > 0:
                    res.append(mc)
                    m -= 1
                if m > n:
                    res.append(mc)
                    m -= 1
                if n > 0:
                    res.append(nc)
                    n -= 1
            return ''.join(res)

        if B > A:
            return generate(B, A, 'b', 'a')
        return generate(A, B, 'a', 'b')
 
