# https://leetcode.com/problems/count-the-repetitions/
# http://www.cnblogs.com/grandyang/p/6149294.html
# find repetition pattern for s2 from S1
# find count of s2 in S1 as count, then answer will count / n2.
# the problem can be two subproblems: count of repeat pattern part and remaining part
# use Pigeonhole Principle
# Time: O(len(s1)*len(s2))
# Space: O(min(n1, len(s2))

class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        n = min(len(s2) + 1, n1)
        repeat_count = [0] * (n + 1)
        next_idx = [0] * (n + 1)
        visited = [-1] * len(s2)
        visited[0] = 0
        j = count = 0
        for k in xrange(1, n + 1):
            for i in xrange(len(s1)):
                if s1[i] == s2[j]:
                    j += 1
                    if j == len(s2):
                        count += 1
                        j = 0
            repeat_count[k] = count
            next_idx[k] = j
            if visited[j] >= 0:
                start = visited[j]
                interval = k - start
                repeat, remain = divmod(n1 - start, interval)
                pattern_count = (repeat_count[k] - repeat_count[start]) * repeat
                remain_count = repeat_count[start + remain]
                return (pattern_count + remain_count) / n2
            visited[j] = k
        return repeat_count[n1] / n2
