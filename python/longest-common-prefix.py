class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        start, stop = 0, False
        while start < len(strs[0]):
            c = strs[0][start]
            for s in strs[1:]:
                if start >= len(s) or s[start] != c:
                    stop = True
                    break
            if stop:
                break
            start += 1
        return strs[0][:start]

