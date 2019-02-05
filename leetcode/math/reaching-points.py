# https://leetcode.com/problems/reaching-points/
# https://leetcode.com/problems/reaching-points/solution/
# Time: O(log(max(tx, ty))); the analysis of the Euclidean algorithm?
# Space: O(1)

class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        # sx, sy, tx, ty >= 1
        # (x, y) -> (x, x+y) or (x+y, y)
        # check backward
        # (tx-ty, ty) if tx > ty
        # (tx, ty-tx) if tx < ty
        # use module to reduce calculation
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:  # ty will not change
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:  # tx will not change
                    return (ty - sy) % tx == 0
        return tx == sx and ty == sy
                    
