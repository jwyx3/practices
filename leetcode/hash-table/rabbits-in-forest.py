# https://leetcode.com/problems/rabbits-in-forest/
# https://leetcode.com/problems/rabbits-in-forest/solution/
# https://leetcode.com/problems/rabbits-in-forest/discuss/114721/C%2B%2BJavaPython-Easy-and-Concise-Solution
# assume v rabbits belongs has value k
# if v % (k + 1) == 0, v / (k + 1) groups
# if v % (k + 1) != 0, v / (k + 1) + 1 groups
# combine them into one expression, (v + k) / (k + 1)
# rabbits count in each group is (k + 1)

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        count = collections.Counter(answers)
        return sum((v + k) / (k + 1) * (k + 1) for k, v in count.iteritems())
