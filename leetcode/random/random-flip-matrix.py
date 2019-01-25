# https://leetcode.com/problems/random-flip-matrix/
# https://leetcode.com/problems/random-flip-matrix/discuss/154053/Java-AC-Solution-call-Least-times-of-Random.nextInt()-function
# learn how to use dict to represent virtual array
# dict<pos, number>

class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.R = n_rows
        self.C = n_cols
        self.n = n_rows * n_cols
        self.d = {}
        

    def flip(self):
        """
        :rtype: List[int]
        """
        self.n -= 1
        pos = random.randint(0, self.n)
        x = self.d.get(pos, pos)
        # move last element into this pos
        self.d[pos] = self.d.get(self.n, self.n)
        return [x / self.C, x % self.C]

    def reset(self):
        """
        :rtype: void
        """
        self.d.clear()
        self.n = self.R * self.C


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
