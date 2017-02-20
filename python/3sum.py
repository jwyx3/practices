class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if not numbers or len(numbers) < 3:
            return []
        numbers.sort()
        ans = []
        for i in range(len(numbers) - 2):
            # remove dup
            if i > 0 and numbers[i - 1] == numbers[i]:
                continue
            # two sum
            left, right, target = i + 1, len(numbers) - 1, - numbers[i]
            while left < right:
                nums_sum = numbers[left] + numbers[right]
                if nums_sum == target:
                    ans.append([numbers[i], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    # remove dup
                    while left < right and numbers[left - 1] == numbers[left]:
                        left += 1
                    while left < right and numbers[right + 1] == numbers[right]:
                        right -= 1
                elif nums_sum > target:
                    right -= 1
                else:
                    left += 1
        return ans
