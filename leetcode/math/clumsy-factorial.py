# https://leetcode.com/problems/clumsy-factorial/
# Time: O(N)
# Space: O(1)

class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        def get_part(i):
            ans = i
            if i > 1:
                ans *= i - 1
            if i > 2:
                ans /= i - 2
            if i < N:
                ans = -ans
            if i > 3:
                ans += i - 3
            return ans
        
        return sum(get_part(i) for i in xrange(N, 0, -4))

# TODO: try Time O(1)
# https://leetcode.com/problems/clumsy-factorial/discuss/252279/You-never-think-of-this-amazing-O(1)-solution!!!
# i * (i-1) / (i-2) = i+1 when i >= 5
# corner cases: N <= 2, N <= 4
# (i - 4) % 4 == 0: e.g. N = 8, 8*7/6 + 5 - 4*3/2 + 1 = i + 1
# (i - 4) % 4 == 1: e.g. N = 5, 5*4/3 + 2 - 1 = i + 1 + 2 - 1 = i + 2
# (i - 4) % 4 == 2: e.g. N = 6, 6*5/4 + 3 - 2*1 = i + 1 + 3 - 2 = i + 2
# (i - 4) % 4 == 3: e.g. N = 7, 7*6/5 + 4 - 3*2/1 = i + 1 + 4 - 6 = i - 1

class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 2:
            return N
        if N <= 4:
            return N + 3
        
        rem = (N - 4) % 4
        if rem == 0:
            return N + 1
        elif rem <= 2:
            return N + 2
        else:
            return N - 1
