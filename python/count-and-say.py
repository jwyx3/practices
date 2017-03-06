class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        result = '1'
        for i in range(1, n):
            last, count, next_result = result[0], 1, ''
            for j in range(1, len(result)):
                curt = result[j]
                if last != curt:
                    next_result += (str(count) + str(last))
                    count = 0
                count += 1
                last = curt
            next_result += (str(count) + str(last))
            result = next_result
        return result
