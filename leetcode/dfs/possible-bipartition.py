# https://leetcode.com/problems/possible-bipartition/
# https://leetcode.com/problems/possible-bipartition/solution/

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        for u, v in dislikes:
            graph[u].add(v)
            graph[v].add(u)
        
        color = {}
        
	# color all node and its neighbors
	# if it's colored, validate it
	# otherwise, color it and its neighbors
        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c^1) for nei in graph[node])
        
        return all(dfs(node) for node in xrange(1, N + 1) if node not in color)
