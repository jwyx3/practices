class Solution:
    # @param {string} digits A digital string
    # @return {string[]} all posible letter combinations
    def letterCombinations(self, digits):
        if not digits:
            return []
        mapping = [
            '', '', 'abc', 'def', 'ghi', 'jkl',
            'mno', 'pqrs', 'tuv', 'wxyz'
        ]
        result = []
        self.dfs(digits, mapping, 0, [], result)
        return result

    def dfs(self, digits, mapping, index, combination, result):
        if index == len(digits):
            result.append(''.join(combination))
            return
        for c in mapping[int(digits[index])]:
            combination.append(c)
            self.dfs(digits, mapping, index + 1, combination, result)
            combination.pop()

