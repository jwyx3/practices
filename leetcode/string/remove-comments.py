# https://leetcode.com/problems/remove-comments/
# https://leetcode.com/problems/remove-comments/solution/

class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res = []
        in_block = False
        new_line = []
        for line in source:
            i = 0
            if not in_block:
                new_line = []
            while i < len(line):
                if line[i:i+2] == '/*' and not in_block:
                    in_block = True
                    i += 1
                elif line[i:i+2] == '*/' and in_block:
                    in_block = False
                    i += 1
                elif line[i:i+2] == '//' and not in_block:
                    break
                elif not in_block:
                    new_line.append(line[i])
                i += 1
            # block comment across multiple lines
            if new_line and not in_block:
                res.append(''.join(new_line))
        return res
