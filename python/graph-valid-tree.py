class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        father = [0 for i in xrange(n)]
        count = n

        def find(a):
            if father[a] == 0:
                return a
            father[a] = find(father[a])
            return father[a]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return (False, count)
            father[ra] = rb
            return (True, count - 1)

        for edge in edges:
            ok, count = union(edge[0], edge[1])
            if not ok:
                return False
        return True if count == 1 else False
