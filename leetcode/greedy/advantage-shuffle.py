# https://leetcode.com/problems/advantage-shuffle/
# https://leetcode.com/problems/advantage-shuffle/solution/
# Time: O(N)
# Space: O(N)
# greedy: if smallest in A is less than current smallest in B, then this can't beat any letter

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sortedA = sorted(A)
        sortedB = sorted(B)
        
        assigned = {b: [] for b in B}
        remaining = []
        
        i = 0
        for a in sortedA:
            if a > sortedB[i]:
                assigned[sortedB[i]].append(a)
                i += 1
            else:
                remaining.append(a)
        
        return [assigned[b].pop() if assigned[b] else remaining.pop() for b in B]
