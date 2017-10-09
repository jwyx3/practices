# Time: O(nlogn), worse than two pointers
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(numbers)):
            start, end = i + 1, len(numbers) - 1
            num = target - numbers[i]
            while start <= end: # standard binary search
                mid = start + (end - start) / 2
                if num == numbers[mid]:
                    return [i + 1, mid + 1]
                elif num < numbers[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return [-1, -1]
