class Solution:
    HASH_BASE = 1000000

    # @param {string} source a source string
    # @param {string} target a target string
    # @return {int} an integer as index
    def strStr2(self, source, target):
        if source is None or target is None:
            return -1
        m, n = len(target), len(source)
        if m == 0:
            return 0

        targetCode = 0
        for c in target:
            targetCode = (targetCode * 31 + ord(c) - ord('a')) % self.HASH_BASE

        power, code = 31 ** (m - 1), 0
        for i in range(n):
            # abcd, bcd; remove first, then add new char
            if i >= m:
                code = (code - (ord(source[i - m]) - ord('a')) * power) % self.HASH_BASE
            code = (code * 31 + ord(source[i]) - ord('a')) % self.HASH_BASE
            if i >= m - 1:
                if targetCode == code and source[i - m + 1:i + 1] == target:
                    # return the start index of matched string
                    return i - m + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    #print s.strStr2("abcdef", "bcd")
    #print s.strStr2("", "")
    #print s.strStr2("tartarget", "target")
    print s.strStr2("tartargetlintcodelintcdejsahriuiwuiurasflhsajfhwahreuwreuwllhfasjflhajshriuwheujwlhadfhsaljfhjahwjehjwhiuehyuwiehyiuwahdjsahjfhajshfjwhuhejwhjehwjehjwhejwhejwhejwhejwhejhwjeh", "riuwheujwlhadfhsaljfhjahwjehjwhiuehyuwiehyiuwahdjsahjfhajshfjwhuhejwhjehwjehjwhejwhej")
