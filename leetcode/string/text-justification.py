# https://leetcode.com/problems/text-justification/

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        i = 0
        res = []
        while i < len(words):
            line = []
            width = 0
            while i < len(words) and width + len(line) + len(words[i]) <= maxWidth:
                width += len(words[i])
                line.append(words[i])
                i += 1
            if line:
                res.append([])
            # not last line and not one word
            if i < len(words) and len(line) > 1:
                quot, rem = divmod(maxWidth - width, len(line) - 1)
                for j, word in enumerate(line):
                    # not last word
                    if j < len(line) - 1:
                        # if rem is not zero, add one more space
                        res[-1].extend([word, ' ' * (quot + min(1, rem))])
                    else:
                        res[-1].append(word)
                    # minus 1 from rem
                    rem = max(0, rem - 1)
                # create spaces
                res[-1] = ''.join(res[-1])
            else:
                res[-1] = ' '.join(line)
                res[-1] += ' ' * (maxWidth - len(res[-1]))
        return res
