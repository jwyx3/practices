class HashHeap(object):
    def __init__(self, min_heap=True):
        self._h = []
        self._pos = {}
        self._count = {}
        self._size = 0
        self._sign = (1 if min_heap else -1)

    def __len__(self):
        return self._size

    def push(self, v):
        v = self._sign * v
        self._size += 1
        self._count[v] = self._count.get(v, 0) + 1
        # If v is new
        if self._count[v] == 1:
            n = len(self._h)
            self._h.append(v)
            self._pos[v] = n
            self._shiftup(n)

    def pop(self):
        if len(self._h) == 0:
            raise IndexError("Empty")
        top = self._h[0]
        self._size -= 1
        self._count[top] -= 1
        # If all v have been removed
        if self._count[top] == 0:
            n = len(self._h)
            self._swap(0, n - 1)
            self._h.pop() # remove last one
            self._shiftdown(0)
            del self._pos[top]
            del self._count[top]
        return self._sign * top

    def _swap(self, x, y):
        if x != y:
            self._pos[self._h[x]], self._pos[self._h[y]] = y, x
            self._h[x], self._h[y] = self._h[y], self._h[x]

    def _shiftup(self, idx):
        while idx > 0:
            parent = (idx - 1) / 2
            if self._h[parent] <= self._h[idx]:
                break
            self._swap(parent, idx)
            idx = parent

    def _shiftdown(self, idx):
        while idx < len(self._h):
            smallest, left, right = idx, 2 * idx + 1, 2 * idx + 2
            if right < len(self._h) and self._h[smallest] > self._h[right]:
                smallest = right
            if left < len(self._h) and self._h[smallest] > self._h[left]:
                smallest = left
            if smallest == idx:
                break
            self._swap(smallest, idx)
            idx = smallest

    def delete(self, v):
        v = self._sign * v
        elem, pos = self._h[self._pos[v]], self._pos[v]
        self._size -= 1
        self._count[v] -= 1
        if self._count[v] == 0:
            n = len(self._h)
            self._swap(pos, n - 1)
            self._h.pop()
            del self._pos[v]
            del self._count[v]
            if pos != n - 1:
                self._shiftup(pos)
                self._shiftdown(pos)
        return self._sign * elem

    def peek(self):
        return self._sign * self._h[0]


class Solution:
    """
    @param nums: A list of integers.
    @return: The median of element inside the window at each moving.
    """
    def medianSlidingWindow(self, nums, k):
        if k == 0:
            return []

        # min_heap: >= median, max_heap: <= median
        min_heap, max_heap = HashHeap(), HashHeap(min_heap=False)
        ans, median = [], nums[0]
        for i in xrange(len(nums)):
            # push new num
            if nums[i] >= median:
                min_heap.push(nums[i])
            else:
                max_heap.push(nums[i])

            if i >= k:
                # move windows
                if nums[i - k] > median:
                    min_heap.delete(nums[i - k])
                else:
                    max_heap.delete(nums[i - k])

            while len(min_heap) > len(max_heap):
                max_heap.push(min_heap.pop())
            while len(max_heap) > len(min_heap) + 1:
                min_heap.push(max_heap.pop())
            median = max_heap.peek()

            # start to move window
            if i >= k - 1:
                ans.append(median)
        return ans

if __name__ == '__main__':
    #test_hashheap()
    s = Solution()
    print s.medianSlidingWindow([1,2,7,8,5], 3), "#", "[2,7,7]"
    print s.medianSlidingWindow([1,2,7,7,2,10,3,4,5], 2), "#", "[1,2,7,2,2,3,3,4]"
    print s.medianSlidingWindow([142,38,100,53,22,84,168,50,194,136,111,13,47,45,151,164,126,47,106,124,183,8,87,38,91,121,102,46,82,195,53,18,11,165,61], 35), '#', "[87]"
    print s.medianSlidingWindow([76,132,106,88,187,22,76,121,187,84,53,176,9,192,22,126,127,178,26,195,142,141,4,33,112,154,127,58,90,194,80,152,178,144,110,166,169,104,120,187,89,134,118,69,5], 36), '#', "[121,126,121,121,126,121,126,126,126,120]"
    print s.medianSlidingWindow([1,2,7,7,2], 1), "#", "[1,2,7,7,2]"
    print s.medianSlidingWindow([1, 1, 1, 1, 1], 3), "#", "[1, 1, 1]"
