import sys

class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the
    #                  first number and the index of the last number

    # 最小前缀和
    def continuousSubarraySum(self, A):
        ans = [-1, -1]
        if not A:
            return ans
        n = len(A)
        sums = [0]
        for s in xrange(1, n+1):
            sums.append(sums[s-1] + A[s-1])
        max_sum, min_sum, min_sum_idx = -sys.maxint - 1, 0, 0
        for i in xrange(1, n+1):
            if max_sum < sums[i] - min_sum:
                max_sum = sums[i] - min_sum
                ans = [min_sum_idx, i-1]
            if sums[i] < min_sum:
                min_sum = sums[i]
                min_sum_idx = i
        return ans

    # 两个指针
    def continuousSubarraySum(self, A):
        ans = [-1, -1]
        if not A:
            return ans
        start, end, max_sum, curr_sum = -1, 0, -sys.maxint - 1, 0
        for x in A:
            curr_sum += x
            if curr_sum > max_sum:
                ans = [start + 1, end]
                max_sum = curr_sum
            if curr_sum < 0:
                start = end
                curr_sum = 0
            end += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print s.continuousSubarraySum([-3,1,3,-3,4]), '#', [1,4]
