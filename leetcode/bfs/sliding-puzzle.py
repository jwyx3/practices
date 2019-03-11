# https://leetcode.com/problems/sliding-puzzle/
# https://leetcode.com/problems/sliding-puzzle/solution/
# TODO: learn A* search!!
# Time: O(6!)
# Space: O(6!)

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        def neighbors(state, i):
            state = list(state)  # tuple -> list
            for j in (i - 3, i + 3, i - 1, i + 1):
                # 2 and 3 are not adjacent!
                if 0 <= j < 6 and (i + j != 5 or abs(i - j) != 1):
                    state[i], state[j] = state[j], state[i]
                    yield tuple(state), j
                    state[i], state[j] = state[j], state[i]
        
        target = (1, 2, 3, 4, 5, 0)
        start = tuple(board[0] + board[1])
        visited = {start}
        q = collections.deque([(start, start.index(0))])
        steps = 0
        while q:
            size = len(q)
            for _ in xrange(size):
                state, pos = q.popleft()
                if state == target:
                    return steps
                for nei, npos in neighbors(state, pos):
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, npos))
            steps += 1
        return -1
