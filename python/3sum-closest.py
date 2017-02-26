class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    # O(n^2) time, O(1) extra space
    def threeSumClosest(self, numbers, target):
        A = numbers
        if not A or len(A) < 3:
            return None
        A.sort()
        ans, min_diff = None, sys.maxint
        for i in range(len(A) - 2):
            left, right = i + 1, len(A) - 1
            while left < right:
                diff = A[left] + A[right] + A[i] - target
                if diff == 0:
                    return target
                elif diff < 0:
                    left += 1
                else:
                    right -= 1
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    ans = diff + target
        return ans
