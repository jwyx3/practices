# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/solution/
# Time: O(2**N * N)??
# Space: O(2**N * N) 

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        q = collections.deque()
        dist = collections.defaultdict(lambda: N*N)
        for i in xrange(N):
            dist[1 << i, i] = 0
            q.append((1 << i, i))
        target = (1 << N) - 1
        while q:
            state, head = q.popleft()
            d = dist[state, head]
            if state == target:
                return d
            for nei in graph[head]:
                state2 = state | (1 << nei)
                if d + 1 < dist[state2, nei]:
                    dist[state2, nei] = d + 1
                    q.append((state2, nei))
        return -1
        
# normal template with different way to check visited.

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        q = collections.deque([(1 << x, x) for x in xrange(N)])
        visited = collections.defaultdict(int)
        target = (1 << N) - 1
        steps = 0
        while q:
            size = len(q)
            for _ in xrange(size):
                state, head = q.popleft()
                if state == target:
                    return steps
                if visited[state, head]: continue
                visited[state, head] = 1
                for nei in graph[head]:
                    q.append((state | (1 << nei), nei))
            steps += 1
        return -1

# Less memory + less time. -> because less node in queue. 
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        q = collections.deque([(1 << x, x) for x in xrange(N)])
        visited = [[0] * N for _ in xrange(1 << N)]
        for x in xrange(N):
            visited[1 << x][x] = 1
        target = (1 << N) - 1
        steps = 0
        # how to understand the position of visited.
        # it depends on the definition of queue.
        # 1. check and mark visited after pop from queue. so queue can contain visited node.
        # 2. check and mark visited after insert from queue. so queue can't contain visited node.
        while q:
            size = len(q)
            for _ in xrange(size):
                state, head = q.popleft()
                if state == target:
                    return steps
                for nei in graph[head]:
                    state2 = state | (1 << nei)
                    if not visited[state2][nei]:
                        visited[state2][nei] = 1
                        q.append((state2, nei))
            steps += 1
        return -1
