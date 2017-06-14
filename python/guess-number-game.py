# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# you can call Guess.guess(num)

class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        if n < 1:
            return -1
        start, end = 1, n
        while start + 1 < end:
            mid = start + (end - start) / 2
            ans = Guess.guess(mid)
            if ans == 0:
                return mid
            elif ans == 1:
                start = mid
            else:
                end = mid
        if Guess.guess(end) == 0:
            return end
        return start
