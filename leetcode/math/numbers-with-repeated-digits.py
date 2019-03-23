# https://leetcode.com/problems/numbers-with-repeated-digits/
# https://leetcode.com/problems/numbers-with-repeated-digits/discuss/256725/JavaPython-Count-the-Number-Without-Repeated-Digit
# Time: O(logN)
# Space: O(1)

class Solution(object):
    def numDupDigitsAtMostN(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 8754
        #   0000 - 0009
        #   0010 - 0099
        #   0100 - 0999
        #   1000 - 7999
        #   8000 - 8699
        #   8700 - 8749
        #   8750 - 8754

        def perm(n, m):  # permutation, pick m from n, order matter
            return 1 if m == 0 else (n - m + 1) * perm(n, m - 1)
        
        num = map(int, str(N + 1))  # handle last digit
        ans, k = 0, len(num)
        # < k 
        for i in xrange(1, k):
            ans += 9 * perm(9, i - 1)
        # == k
        visited = set()
        for i, x in enumerate(num):
            for y in xrange(0 if i else 1, x):
                if y not in visited:
                    ans += perm(9 - i, k - i - 1)
            if x in visited:  # any duplicate found
                break
            visited.add(x)
        return N - ans

