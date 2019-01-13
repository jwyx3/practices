# https://leetcode.com/contest/weekly-contest-119/problems/subarray-sums-divisible-by-k/
# 1) DP. Time: O(n*K), TLE
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dp, res = {}, 0
        for i in xrange(len(A)):
            dp1 = {}
            for k, v in dp.iteritems():
                nk = (k + A[i]) % K
                dp1[nk] = dp1.get(nk, 0) + v
                if nk == 0:
                    res += v
            nk = A[i] % K
            if nk == 0:
                res += 1
            dp1[nk] = dp1.get(nk, 0) + 1
            dp = dp1
        return res

# 2) O(n), use prefix sums

class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        sums = [0]
        for x in A:
            sums.append(sums[-1] + x)
        d, res = {0: 1}, 0
        for i in xrange(1, len(sums)):
            rem = sums[i] % K
            if rem in d:
                res += d[rem]
            d[rem] = d.get(rem, 0) + 1
        return res
