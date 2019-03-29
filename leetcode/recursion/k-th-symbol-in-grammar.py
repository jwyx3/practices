# https://leetcode.com/problems/k-th-symbol-in-grammar/
# https://leetcode.com/problems/k-th-symbol-in-grammar/solution/
# Time: O(N)
# Space: O(N), call stacks

class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        # similar to heap
        # the value of N,K depends on parent and even/odd
        if n == 1 and k == 1:
            return 0
        # find parent in last line: (k + 1) / 2
        # current one is even, revert the digit
        return (1 - (k & 1)) ^ self.kthGrammar(n-1, (k + 1) / 2)
