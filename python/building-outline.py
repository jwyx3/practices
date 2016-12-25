class HashHeap(object):
    def __init__(self):
        self._h = []
        self._pos = {}
        self._count = {}
        self._size = 0

    def __len__(self):
        return self._size

    def push(self, v):
        self._size += 1
        self._count[v] = self._count.get(v, 0) + 1
        if self._count[v] == 1:
            n = len(self._h)
            self._h.append(v)
            self._pos[v] = n
            self._shiftup(n)

    def pop(self):
        if len(self._h) == 0:
            raise IndexError("Empty")
        top = self._h[0]
        self._size -= 1
        self._count[top] -= 1
        if self._count[top] == 0:
            n = len(self._h)
            self._swap(0, n - 1)
            self._h.pop()
            self._shiftdown(0)
            del self._pos[top]
            del self._count[top]
        return top

    def _swap(self, x, y):
        if x != y:
            self._pos[self._h[x]], self._pos[self._h[y]] = y, x
            self._h[x], self._h[y] = self._h[y], self._h[x]

    def _shiftup(self, idx):
        while idx > 0:
            parent = (idx - 1) / 2
            if self._h[parent] <= self._h[idx]:
                break
            self._swap(parent, idx)
            idx = parent

    def _shiftdown(self, idx):
        while idx < len(self._h):
            smallest, left, right = idx, 2 * idx + 1, 2 * idx + 2
            if right < len(self._h) and self._h[smallest] > self._h[right]:
                smallest = right
            if left < len(self._h) and self._h[smallest] > self._h[left]:
                smallest = left
            if smallest == idx:
                break
            self._swap(smallest, idx)
            idx = smallest

    def delete(self, v):
        elem, pos = self._h[self._pos[v]], self._pos[v]
        self._size -= 1
        self._count[v] -= 1
        if self._count[v] == 0:
            n = len(self._h)
            self._swap(pos, n - 1)
            self._h.pop()
            del self._pos[v]
            del self._count[v]
            if pos != n - 1:
                self._shiftup(pos)
                self._shiftdown(pos)
        return elem

    def peek(self):
        return self._h[0]


class Wall(object):
    def __init__(self, x, h, start):
        self.x = x
        self.height = h
        # boolen
        self.start = start

    def __str__(self):
        return "x: %s, height: %s, start: %s" % (self.x, self.height, self.start)


class Solution:
    # @param buildings: A list of lists of integers
    # @return: A list of lists of integers
    def buildingOutline(self, buildings):
        if not buildings:
            return []

        walls = []
        for b in buildings:
            walls.append(Wall(b[0], b[2], True))
            walls.append(Wall(b[1], b[2], False))
        walls = sorted(walls, key=lambda w: w.x)

        ans, outline = [], []
        height, heap = 0, HashHeap()
        for i in xrange(len(walls)):
            # update max heap
            if walls[i].start:
                heap.push(- walls[i].height)
            else:
                heap.delete(- walls[i].height)
            # find the max height of same x
            if i + 1 < len(walls) and walls[i].x == walls[i + 1].x:
                continue
            # get current max height
            new_height = 0
            if len(heap):
                new_height = - heap.peek()
            # if max height is changed
            if height != new_height:
                outline.append(walls[i].x)
            # if outline is closed
            if len(outline) == 2:
                outline.append(height)
                ans.append(outline)
                outline = []
                if new_height != 0:
                    outline = [walls[i].x]
            height = new_height
        return ans

if __name__ == '__main__':
    s = Solution()
    print s.buildingOutline([[1, 3, 3],[2, 4, 4],[5, 6, 1]]), "#", "[[1, 2, 3], [2, 4, 4], [5, 6, 1]]"
    print s.buildingOutline([[1,10,3],[2,5,8],[7,9,8]]), "#", "[[1,2,3],[2,5,8],[5,7,3],[7,9,8],[9,10,3]]"
    print s.buildingOutline([[4,67,187],[3,80,65],[49,77,117],[67,74,9],[6,42,92],[48,67,69],[10,13,58],[47,99,152],[66,99,53],[66,71,34],[27,63,2],[35,81,116],[47,49,10],[68,97,175],[20,33,53],[24,94,20],[74,77,155],[39,98,144],[52,89,84],[13,65,222],[24,41,75],[16,24,142],[40,95,4],[6,56,188],[1,38,219],[19,79,149],[50,61,174],[4,25,14],[4,46,225],[12,32,215],[57,76,47],[11,30,179],[88,99,99],[2,19,228],[16,57,114],[31,69,58],[12,61,198],[70,88,131],[7,37,42],[5,48,211],[2,64,106],[49,73,204],[76,88,26],[58,61,215],[39,51,125],[13,38,48],[74,99,145],[4,12,8],[12,33,161],[61,95,190],[16,19,196],[3,84,8],[5,36,118],[82,87,40],[8,44,212],[15,70,222],[16,25,176],[9,100,74],[38,78,99],[23,77,43],[45,89,229],[7,84,163],[48,72,1],[31,88,123],[35,62,190],[21,29,41],[37,97,81],[7,49,78],[83,84,132],[33,61,27],[18,45,1],[52,64,4],[58,98,57],[14,22,1],[9,85,200],[50,76,147],[54,70,201],[5,55,97],[9,42,125],[31,88,146]]), "#", "[[1,2,219],[2,19,228],[19,45,225],[45,89,229],[89,95,190],[95,97,175],[97,99,152],[99,100,74]]"
