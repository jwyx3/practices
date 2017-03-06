class Solution:
    # @param {string} s the IP string
    # @return {string[]} All possible valid IP addresses
    def restoreIpAddresses(self, s):
        if not s or len(s) < 4:
            return []
        result = []
        self.dfs(s, [], result)
        return result

    # find all valid addresses prefixing with address into result
    def dfs(self, s, address, result):
        if len(address) == 4:
            if s == '':
                result.append('.'.join(address))
            return
        # remember the length of part
        for i in range(1, min(len(s), 3) + 1):
            if self.validPart(s[:i]):
                address.append(s[:i])
                self.dfs(s[i:], address, result)
                address.pop()

    # avoid 00, 010 !!
    def validPart(self, part):
        num = int(part)
        if num >= 0 and num < 10:
            return len(part) == 1
        elif num >= 10 and num < 100:
            return len(part) == 2
        elif num >= 100 and num <= 255:
            return len(part) == 3
        return False

