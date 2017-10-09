# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start + 1 < end:
            mid = start + (end - start) / 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result < 0:
                end = mid - 1 # mid is not answer
            else:
                start = mid + 1
        if guess(end) == 0:
            return end
        return start
