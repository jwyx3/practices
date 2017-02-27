import sys

class Solution:
     # @param nums: a list of integers
     # @param s: an integer
     # @return: an integer representing the minimum size of subarray

    # time O(n), space O(n)
    def minimumSize1(self, nums, s):
        if not nums:
            return -1
        # prefix sum
        sums = [0]
        for i in range(len(nums)):
            sums.append(sums[i] + nums[i])
        ans, j = sys.maxint, 0
        for i in range(len(sums)):
            # first pointer keeps moving until it find subarray >= s
            while j < len(sums) and sums[j] - sums[i] < s:
                j += 1
            # if it's valid subarray and shorter length
            if j < len(sums) and j - i < ans:
                ans = j - i
        # not found
        if ans == sys.maxint:
            ans = -1
        return ans

    # time O(n), space O(1)
    def minimumSize(self, nums, s):
        if not nums:
            return -1
        ans, left, right, total = sys.maxint, 0, 0, 0
        while right < len(nums):
            while right < len(nums) and total < s:
                #print "+ %d" % nums[right]
                total += nums[right]
                right += 1
            if total < s:
                break
            while left < right and total >= s:
                #print "- %d" % nums[left]
                total -= nums[left]
                left += 1
            # both right and left point to next element
            # so it's right - left + 1
            ans = min(ans, right - left + 1)
            #print ans
        if ans == sys.maxint:
            ans = -1
        return ans


if __name__ == '__main__':
    s = Solution()
    print s.minimumSize([2,3,1,2,4,3], 7)
