# idea: 将ACGT用2bits进行编码
#       10-letter-long sequence可以转化为20bits的hash值
#       使用0xfffff作为mask
#       使用hash来记录相同hash值出现次数
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result, count = [], collections.defaultdict(int)
        mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        code, mask = 0, 0xfffff
        for i, c in enumerate(s):
            code <<= 2
            code |= mapping[c]
            code &= mask
            if i >= 9:
                count[code] += 1
            if i >= 10 and count[code] == 2:
                result.append(s[i - 9:i + 1])
        return result
