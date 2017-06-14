class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if not num:
            return None
        return min(num)

# duplicate:
# e.g. 2 2 2 2 2 1 2 -> 2 2 2 2 1 2 2
# when you get num[mid] you don't know which direction you should go
# so you use O(n)
