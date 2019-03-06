# https://leetcode.com/problems/split-array-into-fibonacci-sequence/
# https://leetcode.com/problems/split-array-into-fibonacci-sequence/solution/
# Time: O(N**2) ??, two loops outside is constant, while and string compare are N**2
# Space: O(N) ??, copy string

class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        MAX_INT = (1<<31) - 1
        n = len(S)
        for i in xrange(1, min(10, n) + 1):
            for j in xrange(i + 1, min(i + 10, n) + 1):
                ans = []
                a, b = S[:i], S[i:j]
                ia, ib = int(a), int(b)
                if (a[0] == '0' and len(a) > 1) or (b[0] == '0' and len(b) > 1):
                    continue
                k = len(a) + len(b)
                if k == n:
                    continue
                ans.extend((ia, ib))
                while k < n:
                    c = str(int(a) + int(b))
                    ic = int(c)
                    if c != S[k:k + len(c)] or ic > MAX_INT:
                        break
                    ans.append(ic)
                    k += len(c)
                    a, b = b, c
                if k == n:
                    return ans
        return []
