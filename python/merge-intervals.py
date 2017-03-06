"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        result, last = [], intervals[0]
        for i in range(1, len(intervals)):
            curt = intervals[i]
            if last.end >= curt.start:
                last.end = max(curt.end, last.end)
            else:
                # last is determined when last.end < curt.start
                result.append(last)
                last = curt
        result.append(last)
        return result
