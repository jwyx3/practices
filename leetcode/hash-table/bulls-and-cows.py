# https://leetcode.com/problems/bulls-and-cows/
# https://leetcode.com/problems/bulls-and-cows/discuss/74820/C%2B%2B-one-pass-O(N)-time-O(1)-space
# Time: O(N)
# Space: O(1)

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = b = 0
        cnt_s, cnt_g = [0] * 10, [0] * 10
        for x, y in itertools.izip_longest(secret, guess):
            if x == y:
                a += 1
            else:
                s, g = ord(x) - ord('0'), ord(y) - ord('0')
                if cnt_s[g] > 0:
                    cnt_s[g] -= 1
                    b += 1
                else:
                    cnt_g[g] += 1
                if cnt_g[s] > 0:
                    cnt_g[s] -= 1
                    b += 1
                else:
                    cnt_s[s] += 1
        return '{}A{}B'.format(a, b)
