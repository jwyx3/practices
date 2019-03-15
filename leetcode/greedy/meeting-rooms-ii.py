# https://leetcode.com/problems/meeting-rooms-ii/
# Time: O(NlogN)
# Space: O(N)

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: (x.start, x.end))
        h, ans = [], 0
        for interval in intervals:
            start, end = interval.start, interval.end
            while h and h[0] <= start:
                heapq.heappop(h)
            heapq.heappush(h, end)
            ans = max(ans, len(h))
        return ans


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        events = [(interval.start, 1) for interval in intervals]
        events.extend([(interval.end, -1) for interval in intervals])
        events.sort()
        ans = opened = 0
        for _, d in events:
            opened += d
            ans = max(ans, opened)
        return ans
