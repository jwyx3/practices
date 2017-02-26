class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} an integer
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        if not nums or len(nums) < 2:
            return [-1, -1]
        A = [(num, i) for i, num in enumerate(nums)]
        A.sort(key=lambda x: x[0])
        target = abs(target)
        right, ans = 0, [-1, -1]
        for left in range(len(A)):
            if left == right:
                right += 1
            while right < len(A) and A[right][0] - A[left][0] < target:
                right += 1
            if right < len(A) and A[right][0] - A[left][0] == target:
                ans = [A[left][1] + 1, A[right][1] + 1]
                break
        return sorted(ans)
