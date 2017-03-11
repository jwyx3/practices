from collections import defaultdict


class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        d = defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
        result = []
        for words in d.values():
            if len(words) >= 2:
                result.extend(words)
        return result
