class Solution:
    # @param {int} n an integer
    # @param {string} str a string with number from 1-n
    #                     in random order and miss one number
    # @return {int} an integer
    def findMissing2(self, n, s):
        # Write your code here
        if n <= 0 and not str:
            return -1
        used = [False for _ in range(n + 1)]
        return self.find(n, s, 0, used)

    # return missing number from index and existing used
    def find(self, n, s, index, used):
        if index == len(s):
            result = [i for i in range(1, n + 1) if not used[i]]
            return result[0] if len(result) == 1 else -1

        # it's invalid if first element is 0
        if s[index] == '0':
            return -1

        result = -1
        for l in range(1, 3):
            num = int(s[index: index + l])
            if num >= 1 and num <= n and not used[num]:
                used[num] = True
                result = self.find(n, s, index + l, used)
                # If it's -1, keep searching
                if result != -1:
                    break
                used[num] = False
        return result

