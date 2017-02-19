from collections import deque

class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {int[]} the course order
    def findOrder(self, numCourses, prerequisites):
        ans = []
        if numCourses <= 0:
            return ans
        # dict(course, indegree number)
        # dict(prerequisite, list of courses)
        indegree = [0 for _ in range(numCourses)]
        next_courses = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            indegree[course] += 1
            next_courses[prerequisite].append(course)

        q = deque()
        # collect all courses of which the indegree is 0 =>
        # use dict(course, indegree number)
        for course, num in enumerate(indegree):
            if num == 0:
                q.append(course)
        while len(q) > 0:
            curt = q.popleft()
            ans.append(curt)
            # modify indegree =>
            # use dict(prerequisite, list of courses)
            # modify dict(course, indegree number)
            for course in next_courses[curt]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        if len(ans) == numCourses:
            return ans
        return []

if __name__ == '__main__':
    s = Solution()
    print s.findOrder(2, [[1, 0]])
