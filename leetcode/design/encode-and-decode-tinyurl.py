# https://leetcode.com/problems/encode-and-decode-tinyurl/
# Time: encode O(expectation), decode O(1)
# Space: O(N)

class Codec:
    CHARS = string.ascii_letters + string.digits
    
    def __init__(self):
        self.long2short = {}
        self.short2long = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.long2short:
            code = ''.join(random.choice(self.CHARS) for _ in xrange(6))
            if code not in self.short2long:
                self.long2short[longUrl] = code
                self.short2long[code] = longUrl
        return 'http://tinyurl.com/' + self.long2short[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.short2long[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
