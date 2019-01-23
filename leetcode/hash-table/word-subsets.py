# https://leetcode.com/problems/word-subsets/
# https://leetcode.com/problems/word-subsets/solution/
# combine B as one word

class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        # combine B into one word
        def count(word):
            res = [0] * 26
            for c in word:
                res[ord(c) - ord('a')] += 1
            return res
        
        maxb = [0] * 26
        for b in B:
            for i, x in enumerate(count(b)):
                maxb[i] = max(maxb[i], x)
        
        res = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), maxb)):
                res.append(a)
        return res
