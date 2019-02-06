# https://leetcode.com/problems/sum-of-distances-in-tree/
# https://leetcode.com/problems/sum-of-distances-in-tree/solution/
# Time: O(N)
# Space: O(N)

class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        tree = collections.defaultdict(set)
        for u, v in edges:
            tree[u].add(v)
            tree[v].add(u)

        count = [0] * N
        def dfs(node, parent):
            if not tree[node]:
                return 0, 0
            # num is the amount of nodes within this tree (including root)
            # dist is the sum of dist from root to all its desendents
            dist = num = 0
            for child in tree[node]:
                if child == parent:
                    continue
                cdist, cnum = dfs(child, node)
                dist += cdist + cnum
                num += cnum
            count[node] = num + 1
            return dist, count[node]
        
        rdist, _ = dfs(0, None)
        
        res = [0] * N
        res[0] = rdist
        def calc_dist(node, parent):
            if not tree[node]:
                return
            for child in tree[node]:
                if child == parent:
                    continue
                # how to calculate sum from parent node!
                res[child] = res[node] + N - 2 * count[child]
                calc_dist(child, node)
        
        calc_dist(0, None)
        return res
