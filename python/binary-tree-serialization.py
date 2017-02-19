"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import Queue


class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        if root is None:
            return ''

        ans, q = [], Queue.Queue()
        q.put(root)
        while not q.empty():
            curt = q.get()
            if curt is None:
                ans.append("#")
            else:
                ans.append(str(curt.val))
                q.put(curt.left)
                q.put(curt.right)
        while ans[-1] == '#':
            ans.pop()
        return ','.join(ans)

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    '''
    def deserialize(self, data):
        nodes = data.split(',')
        if len(nodes) == 0:
            return None
        root, idx = TreeNode(nodes[0]), 0
        q = Queue.Queue()
        q.put(root)
        while not q.empty():
            curt = q.get()
            idx += 1
            if idx < len(nodes) and nodes[idx] != '#':
                curt.left = TreeNode(int(nodes[idx]))
                q.put(curt.left)
            idx += 1
            if idx < len(nodes) and nodes[idx] != '#':
                curt.right = TreeNode(int(nodes[idx]))
                q.put(curt.right)
        return root

