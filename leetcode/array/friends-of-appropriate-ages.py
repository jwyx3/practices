# https://leetcode.com/problems/friends-of-appropriate-ages/
# https://leetcode.com/problems/friends-of-appropriate-ages/solution/
# Time: O(N), because 1 <= ages[i] <= 120 
# Space: O(1)

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        # NOT friend
        # aA >= (aB - 7) * 2
        # aA < aB
        # aB > 100 and aA < 100
        if not ages or len(ages) < 2:
            return 0
        counter = collections.Counter(ages)
        ans = 0
        for a, count1 in counter.iteritems():
            for b, count2 in counter.iteritems():
                if a >= (b - 7) * 2 or a < b or a < 100 < b:
                    continue
                ans += count1 * count2
                if a == b:
                    ans -= count1
        return ans
