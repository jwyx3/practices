# idea: 将word转化为单词的bitset，因为我们只需要知道单词是否有重叠
#       记录相同bitset的最长单词长度
#       历遍所有bitset找到最大不重叠单词的长度之积
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        h = collections.defaultdict(int)
        for word in words:
            code = 0
            for c in word:
                code |= 1 << (ord(c) - ord('a'))
            h[code] = max(h[code], len(word))
        return max([h[c1] * h[c2] for c1 in h for c2 in h if not c1 & c2] or [0])
