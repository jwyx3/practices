# https://leetcode.com/problems/stickers-to-spell-word/
# https://leetcode.com/problems/stickers-to-spell-word/solution/
# Time: O(2**N * S * W), S is letter numbers of stickers, W is letter number of target.
# Space: O(2**N)

class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        # dp(state): one bit for each letter in target
        # dp(state | bit) = dp(start) + 1. remove if same letter found from sticker
        # initial: dp(0) = 0, others -1
        # answer: dp((1<<len(target))-1)
        N = len(target)
        def count(word):
            res = [0] * 26
            for c in word:
                res[ord(c) - ord('a')] += 1
            return res
        
        t_count = count(target)
        # remove some unuseful words
        words = []
        for sticker in stickers:
            s_count = count(sticker)
            for i in xrange(26):
                if t_count[i] and s_count[i]:
                    words.append(sticker)
                    break
    
        dp = [-1] * (1 << N)
        dp[0] = 0
        for state in xrange(1 << N):
            if dp[state] == -1:
                continue
            for word in words:
                nstate = state
                for letter in word:
                    for i, c in enumerate(target):
                        # If the character is not used
                        if c == letter and ((nstate >> i) & 1) == 0:
                            nstate |= 1 << i
                            break
                if dp[nstate] < 0 or dp[nstate] > dp[state] + 1:
                    dp[nstate] = dp[state] + 1
        return dp[-1]

# Runtime: 6260 ms
# Too slow. Use array as state + memoization

