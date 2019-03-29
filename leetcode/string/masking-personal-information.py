# https://leetcode.com/problems/masking-personal-information/
# https://leetcode.com/problems/masking-personal-information/discuss/128955/C%2B%2BJavaPython-Easy-and-Concise
# Time: O(N)
class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if '@' in S:
            name, domain = S.lower().split('@')
            return '{}*****{}@{}'.format(name[0], name[-1], domain)
        else:
            phone = re.sub(r'[\(\)\- \+]', '', S)
            intervals = [(-10, -7), (-7, -4), (-4, -1)]
            parts = []
            for i, (start, end) in enumerate(intervals):
                if i == len(intervals) - 1:
                    parts.append(phone[start:])
                else:
                    parts.append('*' * (end - start))
            ans = '-'.join(parts)    
            if len(phone) > 10:
                ans = '+{}-{}'.format('*' * (len(phone) - 10), ans)
            return ans
