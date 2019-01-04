# https://leetcode.com/problems/reverse-only-letters/
# https://leetcode.com/problems/reverse-only-letters/solution/
# When we encounter a letter, we want to write the next letter that occurs if we iterated through the string backwards.
# can use stack or backward pointer

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        j = len(S) - 1
        for i in xrange(len(S)):
            if S[i].isalpha():
                while not S[j].isalpha():
                    j -= 1
                res.append(S[j])
                j -= 1
            else:
                res.append(S[i])
        return ''.join(res)
