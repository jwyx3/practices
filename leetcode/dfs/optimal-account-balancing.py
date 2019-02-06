# https://leetcode.com/problems/optimal-account-balancing/
# https://leetcode.com/problems/optimal-account-balancing/discuss/95355/11-liner-9ms-DFS-solution-(detailed-explanation)
# Time: O(2^n), T(n) = T(n-1) + T(n-2) + ... + T(1) + 1
# Space: O(n)

class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        # debt[i]: i need to get -debt[i] back if debt[i] < 0. otherwise, i need to pay debt[i]
        balances = collections.defaultdict(int)
        for i, j, bal in transactions:
            balances[i] -= bal
            balances[j] += bal
        # not zero
        debt = [bal for bal in balances.itervalues() if bal != 0]
        # sort to make de-dup easier
        debt.sort()
        
        def dfs(start):
            # skip processed debt
            while start < len(debt) and debt[start] == 0:
                start += 1
            res = float('inf')
            for i in xrange(start + 1, len(debt)):
                # de-dup, similar to subset
                if i > start + 1 and debt[i] == debt[i-1]:
                    continue
                # only consider different sign
                if debt[i] * debt[start] < 0:
                    debt[i] += debt[start]
                    res = min(res, 1 + dfs(start + 1))
                    debt[i] -= debt[start]
            # if no debt is needed to process, return 0
            return res if res < float('inf') else 0
        
        return dfs(0)
