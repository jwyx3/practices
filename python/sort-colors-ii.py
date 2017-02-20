class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        self.rainbowSort(colors, 0, len(colors) - 1, 1, k)

    def rainbowSort(self, colors, left, right, colorFrom, colorTo):
        if colorFrom == colorTo:
            return
        if left >= right:
            return
        colorMid = (colorFrom + colorTo) / 2
        start, end = left, right
        while left <= right:
            # let left point to first color which > colorMid
            while left <= right and colors[left] <= colorMid:
                left += 1
            # left right point to first color which <= colorMid
            while left <= right and colors[right] > colorMid:
                right -= 1
            # If it's still valid
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.rainbowSort(colors, start, left, colorFrom, colorMid)
        self.rainbowSort(colors, right, end, colorMid + 1, colorTo)
