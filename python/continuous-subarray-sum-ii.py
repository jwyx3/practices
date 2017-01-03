import sys

class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the
    #                  first number and the index of the last number

    # O(n^2)
    # TLE!
    def continuousSubarraySumII0(self, A):
        ans = [-1, -1]
        if not A:
            return ans
        max_sum, n = -sys.maxint - 1, len(A)
        for x in xrange(n):
            start, end, curr_sum = -1 + x, x, 0
            for i in xrange(n):
                curr_sum += A[(i+x) % n]
                if max_sum < curr_sum:
                    max_sum = curr_sum
                    ans = [(start + 1) % n, end % n]
                if curr_sum < 0:
                    start = end % n
                    curr_sum = 0
                end += 1
        return ans

    # O(n)
    def continuousSubarraySumII(self, A):
        ans = [-1, -1]
        if not A:
            return ans
        total, max_sum, n = 0, -sys.maxint - 1, len(A)
        start, end, curr_sum = -1, 0, 0
        for x in A:
            total += x
            curr_sum += x
            if max_sum < curr_sum:
                max_sum = curr_sum
                ans = [start + 1, end]
            if curr_sum < 0:
                start = end
                curr_sum = 0
            end += 1

        start, end, curr_sum = -1, 0, 0
        for x in A:
            # handle invalid case
            if start == -1 and end == n - 1:
                continue
            curr_sum += x
            if max_sum < total - curr_sum:
                max_sum = total - curr_sum
                ans = [(end + 1) % n, start]
            if curr_sum > 0:
                start = end
                curr_sum = 0
            end += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print s.continuousSubarraySumII([-101,-33,-44,-55,-67,-78,-101,-33,-44,-55,-67,-78,-100,-200,-1000,-22,-100,-200,-1000,-22]), '#', '[15,15]'
