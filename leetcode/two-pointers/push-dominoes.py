# https://leetcode.com/problems/push-dominoes/
# https://leetcode.com/problems/push-dominoes/solution/
# shortest distance to L and R and direction
# Time: O(N)
# Space: O(N)

class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        N = len(dominoes)
        force = [0] * N
        # R: positive
        f = 0
        for i in xrange(N):
            if dominoes[i] == 'R':
                f = N
            elif dominoes[i] == 'L':
                f = 0
            force[i] += f
            f = max(0, f - 1)
        # L: negative
        f = 0
        for i in xrange(N-1, -1, -1):
            if dominoes[i] == 'L':
                f = -N
            elif dominoes[i] == 'R':
                f = 0
            force[i] += f
            f = min(0, f + 1)
        
        return ''.join(['.RL'[cmp(f, 0)] for f in force])
            
