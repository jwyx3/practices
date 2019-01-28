# https://leetcode.com/problems/expressive-words/
# two-pointers
# Time: O(len(S)*len(words) + sum(len(word)))
# Space: O(1)

class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        N = len(S)
        res = 0
        for word in words:
            i = j = 0
            M = len(word)
            while i < N and j < M:
                ic = jc = 1
                while i < N - 1 and S[i] == S[i+1]:
                    ic, i = ic + 1, i + 1
                while j < M - 1 and word[j] == word[j+1]:
                    jc, j = jc + 1, j + 1
                if S[i] != word[j] or (ic >= 3 and jc > ic) or (ic < 3 and jc != ic):
                    break
                i, j = i + 1, j + 1
            if i >= N and j >= M:
                res += 1
        return res

# Run Length Encoding
# https://leetcode.com/problems/expressive-words/solution/
# E.g. S = 'heeellooo', RLE(S) = [('h', 'e', 'l', 'o'), (1, 3, 2, 3)]
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def RLE(num):
            return zip(*[(k, len(list(grp))) for k, grp in itertools.groupby(num)])
        
        l1, count1 = RLE(S)
        res = 0
        for word in words:
            l2, count2 = RLE(word)
            if l1 == l2 and all(c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(count1, count2)):
                res += 1
        return res
