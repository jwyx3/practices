# https://leetcode.com/problems/delete-and-earn/
# https://leetcode.com/problems/delete-and-earn/solution/

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TLE!
        # F[nums]: max number of points if we delete any i from nums
        # F[nums] = max{F[nums - set(nums[i]-1, nums[i]+1)]}, 0<=i<len(nums)
        # initial: F[nums with one element] = nums[0]
        # answer: F[nums]
        # if we take one num, we will take all of them because we have removed all its neighbors
        memo = {}
        
        def count_key(count):
            return tuple(sorted(count.items()))
    
        def get_diff(cand, count):
            diff = collections.Counter()
            diff[cand] = count.get(cand, 0)
            diff[cand-1] = count.get(cand-1, 0)
            diff[cand+1] = count.get(cand+1, 0)
            return diff
        
        def dp(count):
            key = count_key(count)
            if key in memo:
                return memo[key]
            score = 0
            for cand in count:
                diff = get_diff(cand, count)
                rest = count - diff
                score = max(score, diff[cand] * cand + dp(rest))
            memo[key] = score
            return score
        
        return dp(collections.Counter(nums))

# use different way to process; based on solution
# Time: O(NlogN)
# Space: O(N)
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If we add larger number, we can get answer from all previous number
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0
        for num in sorted(count):
            if num - 1 != prev:
                avoid, using = max(avoid, using), num * count[num] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), num * count[num] + avoid
            prev = num
        return max(avoid, using)

# use radix sort; based on solution
# Time: O(N + W), W is the range of the value
# Space: O(W)

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If we add larger number, we can get answer from all previous number
        count = [0] * 10001
        for num in nums:
            count[num] += 1
        prev = None
        avoid = using = 0
        for num in xrange(1, 10001):
            if count[num] == 0:
                continue
            m = max(avoid, using)
            if num - 1 != prev:
                avoid, using = m, num * count[num] + m
            else:
                avoid, using = m, num * count[num] + avoid
            prev = num
        return max(avoid, using)
