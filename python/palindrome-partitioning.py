class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        result = []
        if s is None:
            return result
        self.dfs(s, [], result)
        return result

    # definition:
    # s: string to be processed
    # partition: partial partition so far
    # result: valid partitions until now
    def dfs(self, s, partition, result):
        if not s:
            # copy partition
            result.append(partition[:])
        for i in xrange(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                partition.append(s[:i])
                self.dfs(s[i:], partition, result)
                partition.pop()

    def isPalindrome(self, s):
        k = len(s) / 2
        for i in xrange(k):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True
