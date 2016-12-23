import heapq

class Solution:
    # @param {int[][]} arrays a list of array
    # @param {int} k an integer
    # @return {int} an integer, K-th largest element in N arrays
    def KthInArrays(self, arrays, k):
        # corner case:
        # 1. empty array in arrays
        # 2. k > number of elements
        # 3. k == 0
        n = reduce(lambda n, arr: n + len(arr), arrays, 0)
        if k > n:
            return None
        # reverse and sort
        arrays = [sorted([-1*x for x in arr]) for arr in arrays]
        # initialize heap
        x, h = None, []
        for i in range(len(arrays)):
            # handle empty array case
            if len(arrays[i]) > 0:
                heapq.heappush(h, (arrays[i][0], i, 0))
        # pop k times
        for i in range(k):
            x = heapq.heappop(h)
            next_arr, next_idx = x[1], x[2] + 1
            if next_idx < len(arrays[next_arr]):
                heapq.heappush(
                    h, (arrays[next_arr][next_idx], next_arr, next_idx))
        # reverse result
        return x and -1 * x[0]
