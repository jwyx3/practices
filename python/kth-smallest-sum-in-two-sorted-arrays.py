import heapq

class Solution:
    # @param {int[]} A an integer arrays sorted in ascending order
    # @param {int[]} B an integer arrays sorted in ascending order
    # @param {int} k an integer
    # @return {int} an integer
    def kthSmallestSum(self, A, B, k):
        # corner case:
        # 1. k > len(A) * len(B)
        # 2. k == 0
        x = None
        if k > len(A) * len(B):
            return x
        h = []
        # NOTE: use matrix will cause memory limit issue
        visited = [set() for i in A]
        # initialize
        heapq.heappush(h, (A[0] + B[0], 0, 0))
        visited[0].add(0)
        # get k elements
        while k > 0:
            x = heapq.heappop(h)
            na, nb, a, b = x[1] + 1, x[2] + 1, x[1], x[2]
            if na < len(A) and b not in visited[na]:
                heapq.heappush(h, (A[na] + B[b], na, b))
                visited[na].add(b)
            if nb < len(B) and nb not in visited[a]:
                heapq.heappush(h, (A[a] + B[nb], a, nb))
                visited[a].add(nb)
            k -= 1
        return x and x[0]

if __name__ == "__main__":
    s = Solution()
    print s.kthSmallestSum([1,7,11], [2,4,6], 8), 15
