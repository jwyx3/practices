# https://leetcode.com/problems/basic-calculator-iv/
# https://leetcode.com/problems/basic-calculator-iv/solution/
# https://leetcode.com/problems/basic-calculator-iv/discuss/113549/Easy-%3A-P
# Time: O(2**N + M), N is len of expression, M is len of evalvars; e.g. (a + b) * (c + d) * (e + f) * ...
# Space: O(N + M), N is call stack, M is evalmap


class Poly(collections.Counter):
    def __init__(self, item=None, evalmap=None):
        super(Poly, self).__init__()
        if item:
            x = str(evalmap.get(item, item)) if evalmap else item
            if x[0].isalpha():
                self[(x,)] += 1
            else:
                self[()] += int(x)            

    def __add__(self, other):
        self.update(other)
        return self

    def __sub__(self, other):
        self.subtract(other)
        return self

    def __mul__(self, other):
        ans = Poly()
        for x in self:
            for y in other:
                xy = tuple(sorted(x + y))
                ans[xy] += self[x] * other[y]
        return ans
    
    def __neg__(self):
        return Poly() - self


class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        evalmap = dict(zip(evalvars, evalints))
        
        def calc(expr, start, end):
            if start > end:
                return Poly()
            ans, prev, op = Poly(), Poly(), '+'
            i = start
            while i <= end:
                var = None
                if expr[i] in ('+', '-', '*'):
                    op = expr[i]
                elif expr[i] == '(':
                    j, bal = i + 1, 1
                    while j <= end and bal > 0:
                        if expr[j] == '(':
                            bal += 1
                        elif expr[j] == ')':
                            bal -= 1
                        j += 1
                    var = calc(expr, i + 1, j - 2)
                    i = j - 1
                elif expr[i].isalnum():
                    # variable name can have multiple characters
                    j = i + 1
                    while j <= end and expr[j].isalnum():
                        j += 1
                    var = Poly(expr[i:j], evalmap)
                    i = j - 1
                i += 1
                
                if var is not None:
                    if op == '+':
                        ans += var
                        prev = var
                    elif op == '-':
                        ans -= var
                        prev = -var
                    else:
                        ans -= prev
                        prev *= var
                        ans += prev
            return ans
        
        ans = calc(expression, 0, len(expression) - 1)
        return ['*'.join((str(ans[k]),) + k)
                for k in sorted(ans.iterkeys(), key=lambda x: (-len(x), x)) if ans[k]]

