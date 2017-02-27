class Solution:
    # @param s : A string
    # @return : An integer

    # O(n)
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s or k <= 0:
            return 0
        dt = dict.fromkeys(s, 0)
        # count: number of distinct characters
        ans, i, j, count = 0, 0, 0, 0
        for i in range(len(s)):
            # meet requirement: at most k
            while j < len(s) and count <= k:
                if dt[s[j]] == 0:
                    count += 1
                dt[s[j]] += 1
                j += 1
            # NOTE: s[j - 1] make count > k
            if count == k + 1:
                # s[i .. j - 2]
                ans = max(ans, j - i - 1)
            else:
                # s[i .. j - 1]
                ans = max(ans, j - i)
            if dt[s[i]] == 1:
                count -= 1
            dt[s[i]] -= 1
        return ans

