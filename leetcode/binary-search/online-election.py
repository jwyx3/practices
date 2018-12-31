# https://leetcode.com/problems/online-election/
# https://leetcode.com/problems/online-election/solution/
#
# pre-compute + binary search
#
# Time: O(N + qlogN)
# Space: O(N)

class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        counter = collections.Counter()        
        self.leaders = []
        leader, m = None, 0 # m is votes of leader
        
        for p, t in itertools.izip(persons, times):
            counter[p] = c = counter[p] + 1
            if c >= m:  # use = to handle tie case 
                if p != leader:
                    leader = p
                    self.leaders.append((t, leader))
                if c > m:
                    m = c
        
    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        # use library
        # i = bisect.bisect(self.leaders, (t, float('inf')))
        # return None if i == 0 else self.leaders[i - 1][1]
        
        # homemade binary search
        start, end = 0, len(self.leaders) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if self.leaders[mid][0] <= t:
                start = mid
            else:
                end = mid - 1
        i = start
        if self.leaders[end][0] <= t:
            i = end
        return self.leaders[i][1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
