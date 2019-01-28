# https://leetcode.com/problems/employee-free-time/

# use start and stop
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        # use heap, (time, 0|1), open 0, close 1
        # state: active interval
        N = len(schedule)
        h = []
        for i, ts in enumerate(schedule):
            if ts:
                h.append((ts[0].start, 0, i, 0))
                h.append((ts[0].end, 1, i, 0))
        heapq.heapify(h)
        res, active = [], 0
        while h:
            t, state, i, j = heapq.heappop(h)
            if state == 0:
                active += 1
                if active == 1 and res:
                    res[-1][1] = t
            else:
                active -= 1
                if active == 0:
                    res.append([t, -1])
                ts = schedule[i]
                if j < len(ts) - 1:
                    heapq.heappush(h, (ts[j+1].start, 0, i, j + 1))
                    heapq.heappush(h, (ts[j+1].end, 1, i, j + 1))
        return res[:-1]
                
# https://leetcode.com/problems/employee-free-time/solution/
# heap + greedy
# Time: O(ElogN), E is number of events, N is number of employee
# Space: O(N)
# intuition: Say we are at some time where no employee is working. That work-free period will last until the next time some employee has to work.

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        h = [(emp[0].start, i, 0) for i, emp in enumerate(schedule) if emp]
        heapq.heapify(h)
        end = h[0][0]
        res = []
        while h:
            t, i, j = heapq.heappop(h)
            if end < t:
                res.append((end, t))
            end = max(end, schedule[i][j].end)
            emp = schedule[i]
            if j + 1 < len(emp):
                heapq.heappush(h, (emp[j + 1].start, i, j + 1))
        return res
