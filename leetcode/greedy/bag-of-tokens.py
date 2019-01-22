# https://leetcode.com/problems/bag-of-tokens/
# https://leetcode.com/problems/bag-of-tokens/solution/
# Time: O(NlogN)
# Space: O(1)
# greedy + two pointers

class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        # greedy
        # if P >= min(tokens), play smalleset token face up
        # else if score > 0, play largest token face down
        score = 0
        tokens.sort()
        res = 0
        i, j = 0, len(tokens) - 1
        while i <= j:
            if P >= tokens[i]:
                score += 1
                P -= tokens[i]
                i += 1
                # each token can be used at most once
                # so we can stop playing any token later
                res = max(res, score)
            elif score > 0:
                score -= 1
                P += tokens[j]
                j -= 1
            else:
                break
        return res
