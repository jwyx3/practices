from functools import wraps

def memoize(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring

    # search(s, i, j): boolean
    #   => True # if i >= j
    #   => True # if s[i] == s[j] and search(s, i+1, j-1)
    #   => False # otherwise
    def longestPalindrome0(self, s):
        self.ans = ""
        if self.search(s, 0, len(s) - 1):
            self.ans = s
        return self.ans

    # Time Limit Exceeded, RuntimeError: maximum recursion depth exceeded
    @memoize
    def search(self, s, i, j):
        if i > j:
            return True
        ans, is_palindrome = "", False
        if s[i] == s[j] and self.search(s, i+1, j-1):
            ans = s[i:j+1]
            is_palindrome = True
        else:
            if self.search(s, i+1, j):
                ans = s[i+1:j+1]
            elif self.search(s, i, j-1):
                ans = s[i:j]
        if len(self.ans) < len(ans):
            self.ans = ans
        return is_palindrome

    # dp[i][k]: whether s[i:i+k] is palindrome
    # dp[i][k] = True  # if dp[i+1][k-2] and s[i] == s[i+k-1]
    #            False # otherwise
    # initial: dp[i][1] = True, dp[i][0] = True
    # ans: max(dp[i][k])
    # TODO: improve space
    def longestPalindrome(self, s):
        if not s:
            return ""
        n = len(s)
        if n == 1:
            return s
        ans = ""
        dp = [[k <= 1 for k in xrange(n + 1)] for i in xrange(n)]
        for k in xrange(2, n + 1):
            for i in xrange(n - k + 1):
                dp[i][k] = dp[i + 1][k - 2] and s[i] == s[i + k - 1]
                if dp[i][k] and len(ans) < k:
                    ans = s[i:i + k]
        return ans

if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome("abb"), "#", "bb"
    print s.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"), "#", "ranynar"
