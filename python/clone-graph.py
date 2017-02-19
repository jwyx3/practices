# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
import Queue


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # steps:
        # 1) BFS all nodes and create one clone for each node
        #    => no duplicate and mapping between old and new nodes
        # 2) go through all nodes (in mapping) to fill in neighbors of new nodes
        # 3) return new node of initial node
        if node is None:
            return None

        q = Queue.Queue()
        mapping = {}  # check duplicate and maintain mapping
        q.put(node)

        # step 1
        while not q.empty():
            curt = q.get()
            if curt not in mapping:
                mapping[curt] = UndirectedGraphNode(curt.label)
            for neighbor in curt.neighbors:
                if neighbor not in mapping:
                    q.put(neighbor)
        # step 2
        for old_node, new_node in mapping.items():
            for neighbor in old_node.neighbors:
                new_node.neighbors.append(mapping[neighbor])

        # step 3
        return mapping[node]

