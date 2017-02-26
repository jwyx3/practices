class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        A = numbers
        if not A or len(A) < 3:
            return []
        A.sort()
        result = []
        for i in range(len(A) - 2):
            # remove duplicate
            if i > 0 and A[i - 1] == A[i]:
                continue
            target = -A[i]
            left, right = i + 1, len(A) - 1
            while left < right:
                if A[left] + A[right] == target:
                    result.append((A[i], A[left], A[right]))
                    left += 1
                    right -= 1
                    # remove duplicate
                    while left < right and A[left - 1] == A[left]:
                        left += 1
                    while left < right and A[right + 1] == A[right]:
                        right -= 1
                elif A[left] + A[right] < target:
                    left += 1
                else:
                    right -= 1
        return result
