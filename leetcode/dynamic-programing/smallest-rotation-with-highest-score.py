# https://leetcode.com/problems/smallest-rotation-with-highest-score/
# https://leetcode.com/problems/smallest-rotation-with-highest-score/discuss/118725/C%2B%2BJavaPython-Solution-with-Explanation
# https://leetcode.com/problems/smallest-rotation-with-highest-score/discuss/118725/C++JavaPython-Solution-with-Explanation/118234
# Time: O(N)
# Space: O(N)
# A[i] = [0..N]
# A[0] -> A[N-1] is the only way to +1
# rotate (i-A[i]+N)%N, A[i] == i
# so rotate (i-A[i]+N+1)%N will -1
# special case of A[i]=0,N which will never lose score
# if A[i]=0, (i-A[i]+N+1)%N = i+1, always get 1, rotate i+1, from A[0] -> A[N-1], both +1 and -1
# if A[i]=N, (i-A[i]+N+1)%N = i+1, always get 0, rotate i+1, from A[0] -> A[N-1], both +1 and -1

class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        # change of score
        change = [0] * N
        for i, x in enumerate(A):
            change[(i-A[i]+N+1)%N] -= 1
        for i in xrange(1, N):
            # A[0] to A[N-1] always score 1
            change[i] += change[i-1] + 1
        return change.index(max(change))
