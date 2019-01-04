# https://leetcode.com/problems/similar-rgb-color/
# https://leetcode.com/problems/similar-rgb-color/solution/

class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        def f(comp):
            # 17 * q = 16 * q + q
            q, r = divmod(int(comp, 16), 17)
            if r > 8: q += 1  # because it's closer to upper bound
            return '{:02x}'.format(17 * q)
        return '#' + f(color[1:3]) + f(color[3:5]) + f(color[5:7])
