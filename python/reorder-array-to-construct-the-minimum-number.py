class Solution:
    # @param {int[]} nums n non-negative integer array
    # @return {str} a string
    def minNumber(self, nums):
        def compare(a, b):
            if str(a) + str(b) < str(b) + str(a):
                return -1
            elif str(a) + str(b) == str(b) + str(a):
                return 0
            else:
                return 1

        nums.sort(cmp=compare)
        result = ''.join([str(n) for n in nums])
        start = 0
        # if it's 0, keep it
        while start < len(result) - 1:
            if result[start] != '0':
                break
            start += 1
        return result[start:]


