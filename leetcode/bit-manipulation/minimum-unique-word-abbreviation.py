# https://leetcode.com/problems/minimum-unique-word-abbreviation
# https://leetcode.com/problems/minimum-unique-word-abbreviation/discuss/89884/Python-with-bit-masks
# Time: O(N*2**M)
# Space: O(N)

class Solution(object):
    def minAbbreviation(self, target, words):
        """
        :type target: str
        :type words: List[str]
        :rtype: str
        """
        # try all abbreviation and get min
        def convert(word):
            ans = []
            for i, c in enumerate(word):
                if i > 0 and c.isdigit():
                    ans[-1] += c
                else:
                    ans.append(c)
            return ans
        
        t = convert(target)
        n = len(t)
        words = [convert(word) for word in words]
        diffs = []
        for word in words:
            if len(word) == len(t):
                diffs.append(reduce(
                    operator.add, ((1 << i) for i in xrange(len(t)) if word[i] != t[i])))   
        if not diffs:
            return str(n)
        
        min_bits, min_len = (1 << n) - 1, n
        for x in xrange(2**len(target)):
            if all((x & diff) for diff in diffs):
                # m: number of reduced zero
                m = sum((x >> i) & 3 == 0 for i in xrange(n - 1))
                if n - m < min_len:
                    min_bits, min_len = x, n - m

        ans, num = [], 0
        for i in xrange(n):
            if min_bits & 1:
                if num:
                    ans.append(str(num))
                    num = 0
                ans.append(t[i])
            else:
                num += 1
            min_bits >>= 1
        if num:        
            ans.append(str(num))
        return ''.join(ans)
        
