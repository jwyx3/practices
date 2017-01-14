class Solution:
    #@param A: An list of list integer
    #@return: The index of position is a list of integer, for example [2,2]
    # O(n+m)
    def findPeakII(self, A):
        def find(l1, r1, l2, r2, flag):
            if flag:
                mid = l1 + (r1 - l1) / 2
                max_col, max_v = l2, A[mid][l2]
                for i in xrange(l2, r2+1):
                    if A[mid][i] > max_v:
                        max_v = A[mid][i]
                        max_col = i
                if A[mid][max_col] < A[mid-1][max_col]:
                    return find(l1, mid-1, l2, r2, False)
                elif A[mid][max_col] < A[mid+1][max_col]:
                    return find(mid+1, r1, l2, r2, False)
                return [mid, max_col]
            else:
                mid = l2 + (r2 - l2) / 2
                max_row, max_v = l1, A[l1][mid]
                for i in xrange(l1, r1+1):
                    if A[i][mid] > max_v:
                        max_v = A[i][mid]
                        max_row = i
                if A[max_row][mid] < A[max_row][mid-1]:
                    return find(l1, r2, l2, mid-1, True)
                elif A[max_row][mid] < A[max_row][mid+1]:
                    return find(l1, r1, mid+1, r2, True)
                return [max_row, mid]

        # write your code here
        if not A or not A[0]:
            return [-1, -1]
        l1, r1, l2, r2 = 1, len(A) - 2, 1, len(A[0]) - 2
        return find(l1, r1, l2, r2, True)


if __name__ == '__main__':
    s = Solution()
    print s.findPeakII([[1,3,2],[4,6,5],[7,9,8],[13,15,14],[10,12,11]]), "#", "15"
