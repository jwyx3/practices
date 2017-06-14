class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        count = 0
        # handle special case
        if k == 0:
            count = 1
        for i in xrange(k, n + 1):
            j = i
            while j > 0:
                if j % 10 == k:
                    count += 1
                j /= 10
        return count
