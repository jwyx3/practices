class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    # time O(n)
    def longestConsecutive(self, num):
        if not num:
            return 0
        visited = {}
        for n in num:
            visited[n] = 1
        longest = 0
        for n in num:
            # find to the smaller bound
            down = n - 1
            while visited.get(down, 0) == 1:
                # remove used element
                visited[down] = 0
                down -= 1
            # find the larger bound
            up = n + 1
            while visited.get(up, 0) == 1:
                visited[up] = 0
                up += 1
            # both down and up point to element not in sequence
            longest = max(longest, up - down - 1)
        return longest
