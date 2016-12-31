class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """

    # sums[s]: the sum of first s numbers
    # find sums[i] and sums[j] where sums[i] == sums[j]
    # ans: [i, j-1]
    def subarraySum(self, nums):
        if not nums:
            return None
        n = len(nums)
        # 生成前缀和
        sums = [0]
        for s in xrange(1, n+1):
            sums.append(sums[s-1] + nums[s-1])
        h = {}
        for i in xrange(n+2):
            if sums[i] in h:
                return [h[sums[i]], i-1]
            h[sums[i]] = i
        return None


if __name__ == '__main__':
    s = Solution()
    print s.subarraySum([-3,1,2,-3,4]), '#', '[0, 2]'
