# https://leetcode.com/problems/3sum-with-multiplicity/
# https://leetcode.com/problems/3sum-with-multiplicity/solution/
# Time: O(N + W**2), W is length of keys
# Space: O(W)

class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        counter = collections.Counter(A)
        ans, n = 0, len(counter)
        B = sorted(counter)
        
        def count(i, j, k):
            ans = 0
            if i < j < k:
                ans = counter[B[i]] * counter[B[j]] * counter[B[k]]
            elif i == j == k:
                x = counter[B[i]]
                ans = x * (x - 1) * (x - 2) / 6
            elif i == j < k:
                x = counter[B[i]]
                ans = x * (x - 1) / 2 * counter[B[k]]
            elif i < j == k:
                x = counter[B[k]]
                ans = x * (x - 1) / 2 * counter[B[i]]
            ans %= MOD
            return ans
        
        for i in xrange(n):
            t = target - B[i]
            j, k = i, n - 1
            while j <= k:
                s = B[j] + B[k]
                if s == t:
                    ans += count(i, j, k)
                    j += 1
                    k -= 1
                elif s < t:
                    j += 1
                else:
                    k -= 1
        return ans % MOD
