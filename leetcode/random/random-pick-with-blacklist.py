# https://leetcode.com/problems/random-pick-with-blacklist/
# https://leetcode.com/problems/random-pick-with-blacklist/solution/
# virtual array
# mapping first [:N-len(B)] blacklist element into whitelist element in [N-len(B):]
# Time: O(len(b))
# Space: O(len(b))

class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.m = {}
        b = blacklist
        self.size = N - len(b)
        # find whitelist element within [N-len(B), N)
        w = set(xrange(self.size, N))
        for x in b:
            w.discard(x)
        # find mapping between blacklist element within [0, N-len(B))
        for x in b:
            if x < self.size:
                self.m[x] = w.pop()
        

    def pick(self):
        """
        :rtype: int
        """
        x = random.randint(0, self.size - 1)
        return self.m[x] if x in self.m else x


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
