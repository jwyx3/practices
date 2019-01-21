# https://leetcode.com/problems/water-and-jug-problem
# https://leetcode.com/problems/water-and-jug-problem/discuss/159226/python-O(n)-time-O(1)-space...gcd-based-solution-with-explanation
# https://leetcode.com/problems/water-and-jug-problem/discuss/83715/Math-solution-Java-solution
# from the post
# Key idea is that z litres is measurable using jugs of size x and y only if , z is a linear combination of x and y.

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """    
        def gcd(x, y):
            if x < y:
                x, y = y, x
            while x != y and y != 0:
                rem = x % y
                x, y = y, rem
            return x
        
        d = gcd(x, y)
        if d == 0:
            return z == 0
        return x + y >= z and z % d == 0
