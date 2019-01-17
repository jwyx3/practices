# https://leetcode.com/problems/prime-palindrome/
# https://leetcode.com/problems/prime-palindrome/solution/
# https://leetcode.com/problems/prime-palindrome/discuss/146798/Search-Palindrome-with-Even-Digits
# Time: O(sqrt(N) * 1e(log(N)/log10/2))
# with N <= 2 * 1e8 and we don't check even digits number
# Time: O(sqrt(N) * 1e(log(1e8)/log10/2)) = O(sqrt(N) * 1e4) <= O(sqrt(N) * sqrt(N)) = O(N)
# Space: O(logN): create palindrome

class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        def isPrime(x):
            if x < 2 or x & 1 == 0:
                return x == 2
            for k in xrange(3, int(x ** 0.5) + 1, 2):
                if x % k == 0:
                    return False
            return True
        
        if 8 <= N <= 11:
            return 11
        # because p <= 2 * 10**8
        for p_root in xrange(10 ** (len(str(N)) / 2), 10 ** 5):
            s = str(p_root)
            # only check odd digits palindrome, 
            # because even digits palindrome is not prime. (x % 11 == 0)
            # except for 11
            # Prove. 11 % 11 = 0, 1111 % 11 = 0, ...
            # 1001 = 1111 - 11*10, 100001 = 111111 - 1111*10, ...
            # abcddcba = a * 10000001 + b * 100001 + ...
            p = int(s + s[-2::-1])
            if p >= N and isPrime(p):
                return p
            
