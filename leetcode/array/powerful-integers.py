# https://leetcode.com/contest/weekly-contest-118/problems/powerful-integers/

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        # x or y = 1
        # duplicate
        nxs, nx = [], 1
        while nx < bound:
            nxs.append(nx)
            if x == 1:
                break
            nx *= x
        res, ny = set(), 1
        while ny < bound:
            for nx in nxs:
                if nx + ny > bound:
                    break
                res.add(nx + ny)
            if y == 1:
                break
            ny *= y
        return list(res)
        
