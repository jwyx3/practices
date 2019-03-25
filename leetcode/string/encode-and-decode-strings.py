# https://leetcode.com/problems/encode-and-decode-strings/
# https://leetcode.com/problems/encode-and-decode-strings/discuss/70448/1%2B7-lines-Python-(length-prefixes)
# Time: encode O(N), decode: O(N)
# Space: O(1), exclude answer??
# use prefix sum

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join('{}:{}'.format(len(s), s) for s in strs)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        ans, i = [], 0
        while i < len(s):
            j = i
            while s[j] != ':':
                j += 1
            start, k = j + 1, int(s[i:j])
            ans.append(s[start:start + k])
            i = start + k
        return ans
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
