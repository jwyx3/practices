from collections import deque


class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {boolean} true if can finish all courses or false
    def canFinish(self, numCourses, prerequisites):
        if numCourses < 0 or prerequisites is None:
            return False
        courses, q = [], deque()
        indegree = dict.fromkeys(range(numCourses), 0)
        dependencies = {}
        for course, prerequisite in prerequisites:
            if prerequisite not in dependencies:
                dependencies[prerequisite] = set()
            # avoid duplicate
            if course not in dependencies[prerequisite]:
                dependencies[prerequisite].add(course)
                indegree[course] += 1
        for course in indegree.keys():
            if indegree[course] == 0:
                q.append(course)
                courses.append(course)
        while q:
            curt = q.popleft()
            if curt in dependencies:
                for course in dependencies[curt]:
                    indegree[course] -= 1
                    if indegree[course] == 0:
                        q.append(course)
                        courses.append(course)
        return len(courses) == numCourses


if __name__ == '__main__':
    s = Solution()
    print s.canFinish(10, [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]])
