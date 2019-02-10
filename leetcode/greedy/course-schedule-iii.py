# https://leetcode.com/problems/course-schedule-iii/
# https://leetcode.com/problems/course-schedule-iii/solution/
# compare different case for (a, x) and (b, y)
# conclusion: a + b < y, then always use smaller end time
# otherwise, replace the largest duration with current one
# Time: O(nlogn), use max heap
# Space: O(n)

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        if not courses:
            return 0
        courses.sort(key=lambda x: x[1])
        h, time = [], 0
        for d, end in courses:
            if time + d <= end:
                time += d
                heapq.heappush(h, -d)
            elif h and -h[0] > d:
                time += d + h[0]
                heapq.heappushpop(h, -d)
        return len(h)
