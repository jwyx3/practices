class Solution:
    """
    @param chars: The letters array you should sort.
    """

    # O(n): one-pass and in-place
    def sortLetters(self, chars):
        if not chars or len(chars) <= 1:
            return
        left, right = 0, len(chars) - 1
        while left <= right:
            # find first upper char
            while left <= right and chars[left].islower():
                left += 1
            # find last lower char
            while left <= right and chars[right].isupper():
                right -= 1
            if left <= right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

