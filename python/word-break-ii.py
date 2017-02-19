
# divide and conquer + memorize search
class Solution1:
    # @param {string} s a string
    # @param {set[str]} wordDict a set of words
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return []
        self._cache = {}
        return self.dfs(s, wordDict)

    def dfs(self, s, wordDict):
        if s in self._cache:
            return self._cache[s]
        if not s:
            return ['']
        ans = []
        for i in xrange(1, len(s) + 1):
            if s[:i] in wordDict:
                ans.extend([
                    "{} {}".format(s[:i], sentence).rstrip()
                    for sentence in self.dfs(s[i:], wordDict)
                ])
        self._cache[s] = ans
        return ans

# TLE!
class Solution:
    # @param {string} s a string
    # @param {set[str]} wordDict a set of words
    def wordBreak(self, s, wordDict):
        ans = []
        if not s or not wordDict:
            return ans
        self.dfs(s, wordDict, [], ans)
        return ans

    def dfs(self, s, wordDict, words, ans):
        if not s:
            ans.append(' '.join(words))
            return

        for i in xrange(1, len(s) + 1):
            if s[:i] in wordDict:
                words.append(s[:i])
                self.dfs(s[i:], wordDict, words, ans)
                words.pop()


if __name__ == '__main__':
    s = Solution1()
    print s.wordBreak("lintcode", ["de","ding","co","code","lint"])
