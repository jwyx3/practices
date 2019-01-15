# https://leetcode.com/problems/array-of-doubled-pairs/
# https://leetcode.com/problems/array-of-doubled-pairs/solution/
# Time: O(nlogn)
# Space: O(n)

class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # If x is currently the array element with the least absolute value,
        # it must pair with 2*x, as there does not exist any other x/2 to pair with it.
        count = collections.Counter(A)
        for x in sorted(A, key=abs):
            if count[x] == 0:  # it's used
                continue
            if count[2*x] == 0:  # not pair
                return False
            count[x] -= 1
            count[2*x] -= 1
        return True
