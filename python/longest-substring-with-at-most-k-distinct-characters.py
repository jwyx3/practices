class Solution:
    # @param s : A string
    # @return : An integer
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s:
            return 0
        dt = dict.fromkeys(s, 0)
        # count: number of distinct characters
        ans, j, count = 0, 0, 0
        for i in xrange(len(s)):
            # meet requirement: at most k
            while j < len(s) and count <= k:
                if dt[s[j]] == 0:
                    count += 1
                dt[s[j]] += 1
                j += 1
            # s[j - 1] make count == k + 1
            if count == k + 1:
                ans = max(j - i - 1, ans)
            else:
                ans = max(j - i, ans)
            # move i
            dt[s[i]] -= 1
            if dt[s[i]] == 0:
                count -= 1
            i += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLongestSubstringKDistinct('eceba', 3), '#', '4'
    print s.lengthOfLongestSubstringKDistinct('eqgkcwGFvjjmxutystqdfhuMblWbylgjxsxgnoh', 16), "#", "27"
