# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return {boolean} True if this NestedInteger holds a single integer,
#        rather than a nested list.
#        """
#
#    def getInteger(self):
#        """
#        @return {int} the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return {NestedInteger[]} the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from collections import deque


class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    # BFS
    def depthSum(self, nestedList):
        if not nestedList:
            return 0
        ans = 0
        q = deque([(nestedList, 1)])
        while len(q) > 0:
            curt, level = q.popleft()
            for elem in curt:
                if elem.isInteger():
                    ans += elem.getInteger() * level
                else:
                    q.append((elem.getList(), level + 1))
        return ans

