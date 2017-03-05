from collections import deque
import sys


class Solution(object):
    # @param image {List[List[str]]}  a binary matrix with '0' and '1'
    # @param x, y {int} the location of one of the black pixels
    # @return an integer

    # BFS + connected component + find min and max of x and y
    # LTE!!
    def minArea(self, image, x, y):
        if not image or not image[0]:
            return 0
        n, m = len(image), len(image[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return 0
        min_x = min_y = sys.maxint
        max_x = max_y = -sys.maxint
        q = deque([(x, y)])
        # remember!!
        visited = [[0 for i in range(m)] for j in range(n)]
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and\
                        image[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    min_x, max_x = min(min_x, nx), max(max_x, nx)
                    min_y, max_y = min(min_y, ny), max(max_y, ny)
        return (max_y - min_y + 1) * (max_x - min_x + 1)

    # binary search: search range
    def minArea1(self, image, x, y):
        if not image or not image[0]:
            return 0
        n, m = len(image), len(image[0])

        # decide start and end
        start, end = 0, x
        while start + 1 < end:
            mid = start + (end - start) / 2
            if self.checkRow(image, mid):
                end = mid
            else:
                start = mid + 1
        up = end
        if self.checkRow(image, start):
            up = start

        start, end = x, len(image) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if self.checkRow(image, mid):
                start = mid
            else:
                end = mid - 1
        down = start
        if self.checkRow(image, end):
            down = end

        start, end = 0, y
        while start + 1 < end:
            mid = start + (end - start) / 2
            if self.checkColumn(image, mid):
                end = mid
            else:
                start = mid + 1
        left = end
        if self.checkColumn(image, start):
            left = start

        start, end = y, len(image[0]) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if self.checkColumn(image, mid):
                start = mid
            else:
                end = mid - 1
        right = start
        if self.checkColumn(image, end):
            right = end

        return (right - left + 1) * (down - up + 1)

    def checkRow(self, image, row):
        for i in range(len(image[row])):
            if image[row][i] == '1':
                return True
        return False

    def checkColumn(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    #print s.minArea1(["0010","0110","0100"], 0, 2)
    print s.minArea1(["0000000000000000000000001100111111110000000000000000000000000000000000000000000","0000000000000000000000000111111111110000000000000000000000000000000000000000000","0000000000000000000000000001111110110000000000000000000000000000000000000000000","0000000000000000000000000011111110100000000000000000000000000000000000000000000","0000000000000000000000001111111110000000000000000000000000000000000000000000000"], 3, 34)
