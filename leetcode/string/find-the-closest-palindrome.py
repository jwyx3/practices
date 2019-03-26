# https://leetcode.com/problems/find-the-closest-palindrome/
# https://www.cnblogs.com/grandyang/p/6915355.html
# Time: O(logN)
# Space: O(1)

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type N: str
        :rtype: str
        """
        # generate candidates palindrome
        num = int(n)
        k, m = (len(n) + 1) / 2, len(n)  # 123 -> 12, 1234 -> 12
        # for m digits, the closest one is between [10**(m - 1) - 1, 10**m + 1]
        cands = set([str(10**m + 1), str(10**(m - 1) - 1)])
        for d in (-1, 0, 1):  # candidates: +1, 0, -1 for middle digits
            prefix = str(int(n[:k]) + d)
            l = len(prefix)
            cands.add(prefix + prefix[:l - (m % 2)][::-1])
        cands.discard(n)
        return min(cands, key=lambda x: (abs(int(x) - num), int(x)))
        
