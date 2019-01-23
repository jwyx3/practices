# https://leetcode.com/problems/boats-to-save-people/
# https://leetcode.com/problems/boats-to-save-people/solution/
# Time: O(NlogN)
# Space: O(N), python sort is variant of merge sort.

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i, j = 0, len(people) - 1
        res = 0
        while i <= j:
            res += 1
            # if the heaviest person can share with the lightest person
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return res
