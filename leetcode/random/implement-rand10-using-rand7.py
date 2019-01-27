# https://leetcode.com/problems/implement-rand10-using-rand7/
# https://leetcode.com/problems/implement-rand10-using-rand7/solution/
# reject sampling
# Time: avg: O(1), worst: O(inf)
# Space: O(1)

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

# average: 2 * 49 / 40 = 2.45 times.
class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            a = rand7()
            b = rand7()
            idx = (a - 1) * 7 + b
            if idx <= 40:
                return 1 + (idx - 1) % 10

# https://leetcode.com/problems/implement-rand10-using-rand7/discuss/151567/C%2B%2BJavaPython-Average-1.199-Call-rand7-Per-rand10
# best limit: log10 / log7 = 1.183

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    cache = []
    
    def rand10(self):
        """
        :rtype: int
        """
        if not self.cache:
            self.generate()
        return self.cache.pop()
        
    def generate(self):
        N = 19
        base, num = 1, 0
        for _ in xrange(N):
            num += base * (rand7() - 1)
            base *= 7
        # use rand7 to uniformly generate number within [0, base-1]
        # e.g. 123, same probability for num < 120. 0...9 repeat 11 times.
        while num < base / 10 * 10:
            self.cache.append(num % 10 + 1)
            base /= 10
            num /= 10

# how to calculate average times??
