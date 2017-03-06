class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        if not nestedList:
            return []
        if isinstance(nestedList, int):
            nestedList = [nestedList]
        result, stack = [], list(reversed(nestedList))
        while stack:
            top = stack.pop()
            if isinstance(top, list):
                for x in reversed(top):
                    stack.append(x)
            else:
                result.append(top)
        return result
