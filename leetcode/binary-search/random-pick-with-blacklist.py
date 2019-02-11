# https://leetcode.com/problems/random-pick-with-blacklist/
# https://leetcode.com/problems/random-pick-with-blacklist/solution/
# https://zhanghuimeng.github.io/post/leetcode-710-random-pick-with-blacklist/
# Time: O(MlogM), M = len(blacklist)
# Space: O(M)
# from post:
# 在讨论区里我看到了类似的做法，但是思考的角度不太一样。我们可以把从区间[0, N - M)中生成随机数r的情形这样分类：[1]
# r在[0, B[0])区间内，可以直接返回r
# r在[B[0], B[1] - 1)区间内，应返回r + 1
# ...
# r在[B[i]-i, B[i+1]-(i+1))区间内，应返回r + i + 1。注意到r + i + 1位于[B[i] + 1, B[i+1])区间内，因此这样做是安全的。
# 因此可以在B[i] - (i+1)数组中进行二分查找。

class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.b = sorted(blacklist)
        self.size = N - len(self.b)
        

    def pick(self):
        """
        :rtype: int
        """
        x = random.randint(0, self.size - 1)
        lo, hi = 0, len(self.b) - 1
        while lo + 1 < hi:
            mid = (lo + hi) / 2
            # self.b[mid] - mid: the position in [0, N-len(B)) for this blacklist element
            if self.b[mid] - mid > x:
                hi = mid - 1
            else:
                lo = mid
        if lo <= hi:
            if self.b[hi] - hi <= x:
                return x + hi + 1  # hi + 1 is number of element in blacklist
            if self.b[lo] - lo <= x:
                return x + lo + 1
        # no blacklist
        return x
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
