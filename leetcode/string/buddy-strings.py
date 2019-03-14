# https://leetcode.com/problems/buddy-strings/
# https://leetcode.com/problems/buddy-strings/solution/
# Time: O(N)
# Space: O(1)

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            visited = set()
            for x in A:
                if x in visited:
                    return True
                visited.add(x)
            return False 
        else:
            pairs = []
            for x, y in itertools.izip(A, B):
                if x != y:
                    pairs.append((x, y))
                    if len(pairs) > 2:
                        return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
