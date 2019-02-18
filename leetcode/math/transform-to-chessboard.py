# https://leetcode.com/problems/transform-to-chessboard/
# https://leetcode.com/problems/transform-to-chessboard/solution/
# https://leetcode.com/problems/transform-to-chessboard/discuss/114847/Easy-and-Concise-Solution-with-Explanation-C%2B%2BJavaPython
# key idea: a board where no 0s and no 1s are 4-directionally adjacent
# 1. if swap rows, two same/different columns will still be same/different
# because chessboard will only have two unique rows or columns.
# so current board should be the same.
# 2. these two unique rows or columns should have different bit for each corresponding bit.
# 3. the order of swapping row and column doesn't have side effect. so we can calculate rows and then columns.
# 
# the final rows or columns will only be in the format of 101, 010. or 1010, 0101.
# given N, compare with final rows or columns to get number of swaps. 

class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # make sure only two rows or columns
        # count of two rows or columns in N/2 and (N+1)/2
        # each bit of two rows or columns should be different
        # we can process rows and then columns
        N = len(board)
        res = 0
        # check lines and then columns
        for count in (collections.Counter(map(tuple, board)), collections.Counter(zip(*board))):
            if len(count) != 2 or sorted(count.itervalues()) != [N/2, (N+1)/2]:
                return -1
            line1, line2 = count
            if not all(x ^ y for x, y in zip(line1, line2)):
                return -1
            if N % 2:  # odd
                if line1.count(1) * 2 > N:  # compare with 101
                    # (x & 1) ^ ((i+1) & 1) -> (x - (i+1)) % 2; XOR is same as odd/even property
                    res += sum((x - (i+1)) % 2 for i, x in enumerate(line1)) / 2
                else:  # compare with 010
                    res += sum((x - i) % 2 for i, x in enumerate(line1)) / 2
            else:  # compare with 1010 and 0101
                res += min(sum((x - (i + k)) % 2 for i, x in enumerate(line1)) / 2 for k in xrange(2))
        return res
