class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        if not S or len(S) < 3:
            return 0
        S.sort(reverse=True)
        count = 0
        for i in range(len(S) - 2):
            left, right = i + 1, len(S) - 1
            while left < right:
                if S[left] + S[right] > S[i]:
                    count += (right - left)
                    # reverse order!!
                    left += 1
                else:
                    right -= 1
        return count
