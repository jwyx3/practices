# https://leetcode.com/problems/three-equal-parts/
# https://leetcode.com/problems/three-equal-parts/solution/
# Time: O(N)
# Space: O(N)
# find same number of ones in three part

class Solution(object):
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        NA = [-1, -1]
        
        ones = sum(A)
        if ones % 3 != 0:
            return NA
        if ones == 0:
            return [0, len(A) - 1]
        
        m, breaks, k = ones / 3, [], 0
        starts, ends = {1, m + 1, 2 * m + 1}, {m, 2 * m, 3 * m}
        for i, x in enumerate(A):
            if x:
                k += 1
                if k in starts:
                    breaks.append(i)
                # use if instead of elif. e.g. m = 1
                if k in ends:
                    breaks.append(i)
        
        i1, j1, i2, j2, i3, j3 = breaks
        # the part with ones should be same
        if not(A[i1:j1+1] == A[i2:j2+1] == A[i3:j3+1]):
            return NA
        
        # number of zeros after each part
        x = i2 - j1 - 1
        y = i3 - j2 - 1
        z = len(A) - j3 - 1
        
        if x < z or y < z:
            return NA
        
        j1 += z
        j2 += z
        return [j1, j2 + 1]
