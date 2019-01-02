# https://leetcode.com/problems/snakes-and-ladders/
# https://leetcode.com/problems/snakes-and-ladders/solution/
#
# TODO: generate graph during computing
# the way to generate r, c
# Time: O(N*N)
# Space: O(N*N)

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        N = len(board)
        dst = N * N
        for x in xrange(1, dst + 1):
            for k in xrange(1, 7):
                if x + k <= dst:
                    quot, rem = divmod(x + k - 1, N)
                    r = N - 1 - quot
                    c = rem if quot % 2 == 0 else N - 1 - rem
                    graph[x].append((x + k) if board[r][c] < 0 else board[r][c])

        visited = [False] * (dst + 1)
        q = collections.deque([1])
        moves = 0
        while q:
            size = len(q)
            for _ in xrange(size):
                node = q.popleft()
                if node == dst:
                    return moves
                for nei in graph[node]:
                    if not visited[nei]:
                        q.append(nei)
                        visited[nei] = True
            moves += 1
        return -1
