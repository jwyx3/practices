import sys

class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    # O(n)
    def nthUglyNumber(self, n):
        nums = [1]
        bases = [[2, 0], [3, 0], [5, 0]]
        for i in xrange(n - 1):
            for base in bases:
                # get the number larger than nums[-1] after multiply 2, 3 or 5
                while base[0] * nums[base[1]] <= nums[-1]:
                    base[1] += 1
            # get min of potential new nums
            nums.append(min([base[0] * nums[base[1]] for base in bases]))
        return nums[-1]

    # TODO: O(nlogn)


if __name__ == '__main__':
    s = Solution()
    print s.nthUglyNumber(81)
    print s.nthUglyNumber(9)
