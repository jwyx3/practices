class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    result, mask = 0, 0
    for i in xrange(32, -1, -1):
        mask |= 1 << i
        # construct all a and b
        prefixes = {num & mask for num in nums}
        # assume a ^ b will be result | (1 << i)
        next_result = result | (1 << i)
        # check for all a whether there is b is in prefixes with (a ^ b)
        for prefix in prefixes:
            # if (a ^ b) ^ a == b
            if next_result ^ prefix in prefixes:
                result = next_result
                break
        #otherwise ith bit will be 0
    return result
