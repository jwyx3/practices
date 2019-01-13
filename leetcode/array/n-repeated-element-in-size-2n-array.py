# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/discuss/208563/JavaC%2B%2BPython-O(1)-Solution
# from comment
# For array of length > 4: the only way to not have two neighbouring x is to put a different number in between all x, i.e. x y x z x a x b ... since half the elements are x. This means for i-th element by checking A[i-1] and A[i-2] we can always find x
# For array of length == 4, there is a configuration x y z x which doesn't fit into the first case, we handle this edge case specifically
# Time: O(n)
# Space: O(1)

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # len(A) > 4
        for i in xrange(2, len(A)):
            if A[i] == A[i-1] or A[i] == A[i-2]:
                return A[i]
        # special case: [x,y,z,x], [x,x,y,z]
        return A[0]

# or use probability: avg Time O(1)
