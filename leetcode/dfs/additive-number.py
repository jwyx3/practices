# https://leetcode.com/problems/additive-number/
# Time: O(N**3) ??
# Space: O(N) ??

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in xrange(1, n + 1):
            for j in xrange(i + 1, n + 1):
                a, b = num[:i], num[i:j]
                if (a[0] == '0' and len(a) > 1) or (b[0] == '0' and len(b) > 1):
                    continue
                k = len(a) + len(b)
                if k == n:  # length of array >= 3
                    continue
                # k is the start of next number
                while k < n:
                    c = str(int(a) + int(b))
                    if (c[0] == '0' and len(c) > 1) or c != num[k:k + len(c)]:
                        break
                    k += len(c)
                    a, b = b, c
                if k == n:
                    return True
        return False
