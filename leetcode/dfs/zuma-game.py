# https://leetcode.com/problems/zuma-game/
# https://leetcode.com/problems/zuma-game/discuss/97027/StraightForward-Recursive-Java-Solution-beat-97
# Time: O(min(N**len(hand), N!))
# Space: O(N)

class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        free = collections.Counter(hand)
        
        # given board s and available balls, return min used balls
        def dfs(s):
            if not s:
                return 0
            ans = len(hand) + 1
            i = j = 0
            while i < len(s):
                j = i
                while i < len(s) and s[i] == s[j]:
                    i += 1
                used = max(0, 3 - (i - j))
                if free[s[j]] < used:
                    continue
                free[s[j]] -= used
                rem = dfs(s[:j] + s[i:])
                if rem >= 0:
                    ans = min(ans, used + rem)
                free[s[j]] += used
            return -1 if ans > len(hand) else ans
        
        return dfs(board)
