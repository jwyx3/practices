class Solution:
    # @param {int} n a positive integer
    # @return {int[][]} n x 3 matrix
    def consistentHashing(self, n):
        # Write your code here
        result = [[0, 359, 1]]
        for i in xrange(1, n):
            index = 0
            for j in xrange(0, i):
                curr_len = result[j][1] - result[j][0] + 1
                max_len = result[index][1] - result[index][0] + 1
                if curr_len == max_len and result[j][2] < result[index][2] or\
                        curr_len > max_len:
                    index = j
            y, result[index][1] = result[index][1], sum(result[index][:2]) / 2
            result.insert(index + 1, [result[index][1] + 1, y, i + 1])
        return result
