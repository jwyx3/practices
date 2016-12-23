# Definition for a directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class ConnectedComponent(object):
    def __init__(self, x):
        self.label = x
        self.members = [x]


class Solution:
    # @param {DirectedGraphNode[]} nodes a array of directed graph node
    # @return {int[][]} a connected set of a directed graph
    def connectedSet2(self, nodes):
        # DIFF from normal union-find question:
        # 1. add the element in father[] on fly
        # 2. remember all root nodes
        father = {}
        root_nodes = set()

        def add_node(a):
            if a not in father:
                father[a] = ConnectedComponent(a)
                root_nodes.add(a)

        def find(a):
            if father[a].label == a:
                return father[a]
            father[a] = find(father[a].label)
            return father[a]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra.label != rb.label:
                root_nodes.remove(ra.label)
                rb.members.extend(ra.members)
                father[ra.label] = rb

        for node in nodes:
            add_node(node.label)
            for neighbor in node.neighbors:
                add_node(neighbor.label)
                union(node.label, neighbor.label)

        ans = []
        for x in root_nodes:
            ans.append(sorted(father[x].members))
        return ans

if __name__ == '__main__':
    s = Solution()
    # generate graph
    a = DirectedGraphNode('A')
    b = DirectedGraphNode('B')
    c = DirectedGraphNode('C')
    d = DirectedGraphNode('D')
    e = DirectedGraphNode('E')
    f = DirectedGraphNode('F')
    a.neighbors.extend([b, d])
    b.neighbors.extend([d])
    c.neighbors.extend([e])
    f.neighbors.extend([e])
    print s.connectedSet2([a, b, c, f])
