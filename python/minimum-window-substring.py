class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        if len(source) < len(target) and not target:
            return ""
        S, T = source, target
        d, dt = {}, dict.fromkeys(T, 0)
        for c in T:
            d[c] = d.get(c, 0) + 1
        ans, j, count = "", 0, 0
        for i in xrange(len(S)):
            # If it doesn't contain all characters in target
            while count != len(T) and j < len(S):
                if S[j] in dt:
                    if dt[S[j]] < d[S[j]]:
                        count += 1
                    dt[S[j]] += 1
                j += 1
            # collect ans
            if count == len(T) and S[i] in dt and dt[S[i]] == d[S[i]]:
                if ans == "" or j - i < len(ans):
                    ans = S[i: j]
            # move i
            if S[i] in dt:
                if dt[S[i]] <= d[S[i]]:
                    count -= 1
                dt[S[i]] -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print s.minWindow("abc", "ac"), "#", "abc"
    print s.minWindow("abcde", "db"), "#", "bcd"
    print s.minWindow("absdfaabab", "adb"), "#", "absd"
