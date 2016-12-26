class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    # Space: O(n), Time: O(nlogn)
    def twoSum(self, numbers, target):
        nums = sorted([(numbers[i], i) for i in xrange(len(numbers))], key=lambda x: x[0])
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i][0] + nums[j][0]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                break
        ans = [nums[i][1] + 1, nums[j][1] + 1]
        if ans[0] > ans[1]:
            ans[0], ans[1] = ans[1], ans[0]
        return ans

    # Space: O(n), Time: O(n)
    def twoSum0(self, numbers, target):
        nums_map = {}
        for i in xrange(len(numbers)):
            # handle duplicate
            if numbers[i] in nums_map:
                nums_map[numbers[i]].append(i)
            else:
                nums_map[numbers[i]] = [i]
        ans = None
        for k in nums_map.keys():
            if target - k in nums_map:
                if target - k == k and len(nums_map[k]) >= 2:
                    ans = [x + 1 for x in nums_map[k][:2]]
                else:
                    ans = [nums_map[k][0] + 1, nums_map[target - k][0] + 1]
        if ans[0] > ans[1]:
            ans[0], ans[1] = ans[1], ans[0]
        return ans
