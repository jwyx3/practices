# https://leetcode.com/problems/number-of-recent-calls/
# https://leetcode.com/problems/number-of-recent-calls/solution/

# We only care about the most recent calls in the last 3000 ms, so let's use a data structure that keeps only those.

class RecentCounter(object):

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        self.q.append(t)
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
