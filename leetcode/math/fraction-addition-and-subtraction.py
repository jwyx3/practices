# https://leetcode.com/problems/fraction-addition-and-subtraction/
# https://leetcode.com/problems/fraction-addition-and-subtraction/solution/
# Time: O(Nlogx). Euclidean GCD algorithm takes O(log(a.b)) time for finding gcd of two numbers a and b. Here N refers to the number of fractions in the input string and x is the maximum possible value of denominator.
# Space: O(len(expression)), 

from fractions import gcd

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        sign, num0, den0 = 1, 0, 1
        for frac in expression.replace('+', ' +').replace('-', ' -').split():
            if frac[0] == '-':
                sign = -1
                frac = frac[1:]
            elif frac[0] == '+':
                sign = 1
                frac = frac[1:]
            num1, den1 = map(int, frac.split('/'))
            num = num0 * den1 + sign * num1 * den0
            den = den0 * den1
            d = gcd(num, den)
            num0, den0 = num / d, den / d
        return str(num0) + '/' + str(den0)
