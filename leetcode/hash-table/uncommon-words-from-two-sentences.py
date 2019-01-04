# https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        counter = collections.Counter()
        for c in A.split(' '):
            counter[c] += 1
        for c in B.split(' '):
            counter[c] += 1
        return [w for w in counter if counter[w] == 1]
