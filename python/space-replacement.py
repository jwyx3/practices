class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string

    # start from end
    def replaceBlank(self, string, length):
        count = 0
        for i in range(length):
            if string[i] == ' ':
                count += 1
        result = length + 2 * count
        left, right = length - 1, result - 1
        while left >= 0:
            if string[left] == ' ':
                for c in "02%":
                    string[right] = c
                    right -= 1
            else:
                string[right] = string[left]
                right -= 1
            left -= 1
        return result
