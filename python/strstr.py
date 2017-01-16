class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        ns, nt = len(source), len(target)
        for i in xrange(ns - nt + 1):
            found = True
            for j in xrange(nt):
                if source[i + j] != target[j]:
                    found = False
                    break
            if found:
                return i
        return -1
