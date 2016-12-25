# class Comparator:
#     def cmp(self, a, b)
# You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
# if "a" is bigger than "b", it will return 1, else if they are equal,
# it will return 0, else if "a" is smaller than "b", it will return -1.
# When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        if len(nuts) == len(bolts) and (len(nuts) == 1 or len(nuts) == 0):
            return
        self.sort(nuts, bolts, 0, len(nuts) - 1, compare)

    def sort(self, nuts, bolts, left, right, compare):
        if right - left <= 0:
            return

        for i in xrange(left, right + 1):
            if compare.cmp(nuts[i], bolts[left]) == 0:
                nuts[left], nuts[i] = nuts[i], nuts[left]

        idx = self.partition(nuts, left, right, bolts[left], compare)
        self.partition(bolts, left, right, nuts[idx], compare)
        self.sort(nuts, bolts, left, idx - 1, compare)
        self.sort(nuts, bolts, idx + 1, right, compare)

    def partition(self, nums, left, right, pivot, compare):
        def a_ge_b(a, b):
            return (compare.cmp(a, b) >= 0 and compare.cmp(b, a) == 2) or\
                (compare.cmp(b, a) <= 0 and compare.cmp(a, b) ==2)

        def a_le_b(a, b):
            return (compare.cmp(a, b) <= 0 and compare.cmp(b, a) == 2) or\
                (compare.cmp(b, a) >= 0 and compare.cmp(a, b) == 2)

        # pivot must be matching with nums[left]
        first = nums[left]
        while left < right:
            while left < right and a_ge_b(nums[right], pivot):
                right -= 1
            nums[left] = nums[right]
            while left < right and a_le_b(nums[left], pivot):
                left += 1
            nums[right] = nums[left]
        nums[left] = first
        return left

class Comparator():
    def cmp(self, a, b):
        if a.isupper() or b.islower():
            return 2
        if a.lower() == b.lower():
            return 0
        return (1 if a.lower() > b.lower() else -1)

if __name__ == '__main__':
    s = Solution()
    c = Comparator()
    nuts = ["ab","bc","dd","gg"]
    bolts = ["AB","GG","DD","BC"]
    s.sortNutsAndBolts(nuts, bolts, c)
    print nuts, bolts
