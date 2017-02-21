import heapq

class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''

    # heap
    # TLE!!
    def topk1(self, nums, k):
        # Write your code here
        if not nums or k <= 0:
            return []
        h = []
        for num in nums:
            if len(h) == k and h[0] >= num:
                continue
            heapq.heappush(h, num)
            if len(h) > k:
                heapq.heappop(h)
        ans = []
        while len(h) > 0:
            ans.insert(0, heapq.heappop(h))
        return ans

    # heap 2
    # O(nlogk)
    def topk2(self, nums, k):
        heapq.heapify(nums)
        ans = heapq.nlargest(k, nums)
        return ans

    # quick select
    # O(n + klogk)
    def topk(self, nums, k):
        if not nums or k <= 0:
            return []
        index = self.quickselect(nums, 0, len(nums) - 1, k)
        return sorted(nums[:index + 1], reverse=True)

    def partition(self, nums, left, right):
        mid = (left + right) / 2
        nums[left], nums[mid] = nums[mid], nums[left]
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] <= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] >= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left

    # k is Kth, don't modify k
    def quickselect(self, nums, left, right, k):
        mid = self.partition(nums, left, right)
        if mid + 1 == k:
            return mid
        elif mid + 1 < k:
            return self.quickselect(nums, mid + 1, right, k)
        else:
            return self.quickselect(nums, left, mid - 1, k)


if __name__ == '__main__':
    s = Solution()
    print s.topk([3,10,1000,-99,4,100], 3)
