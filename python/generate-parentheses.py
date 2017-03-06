class Solution:
    # @param {int} n n pairs
    # @return {string[]} All combinations of well-formed parentheses
    def generateParenthesis(self, n):
        if n <= 0:
            return []
        result = []
        self.dfs(n, 0, [], result)
        return result

    # n: number of open parentheses we can use
    # m: number of close parentheses we can use
    # put all possible parenthesis prefixing with parenthesis in result
    def dfs(self, n, m, parenthesis, result):
        if n == 0 and m == 0:
            result.append(''.join(parenthesis))
            return
        # NOT use loop
        if n > 0:
            parenthesis.append('(')
            self.dfs(n - 1, m + 1, parenthesis, result)
            parenthesis.pop()
        if m > 0:
            parenthesis.append(')')
            self.dfs(n, m - 1, parenthesis, result)
            parenthesis.pop()

