# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.d[key].append((timestamp, 0, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.d:
            return ''
        i = bisect.bisect_right(self.d[key], (timestamp, 1))
        return self.d[key][i-1][2] if i else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
