"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# NOTE: use class instead of namedtuple

class Event(object):
    def __init__(self, time, change):
        self.time = time
        self.change = change

class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        time_dict = dict()
        for airplane in airplanes:
            start, end = airplane.start, airplane.end
            if start not in time_dict:
                time_dict[start] = Event(start, 1)
            else:
                time_dict[start].change += 1
            if end not in time_dict:
                time_dict[end] = Event(end, -1)
            else:
                time_dict[end].change -= 1
        events = sorted(time_dict.values(), key=lambda x: x.time)
        max_count, count = 0, 0
        for e in events:
            count += e.change
            max_count = max(count, max_count)
        return max_count

