# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/210994/easy-to-understand-java-iterative-solution-with-Stack
# more practice!

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    # format: 1[3[5 6] 2 4]
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root: return ''
        res = [str(root.val)]
        if root.children:
            res.append('[')
        for child in root.children:
            res.append(self.serialize(child))
            res.append(' ')
        if res[-1] == ' ':
            res.pop()
        if root.children:
            res.append(']')
        return ''.join(res)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        stack, i = [], 0
        while i < len(data):
            if data[i].isdigit():
                # create node here
                num = 0
                while i < len(data) and data[i].isdigit():
                    num = 10 * num + int(data[i])
                    i += 1
                node = Node(num, [])
                # add into parent
                if stack:
                    stack[-1].children.append(node)
                stack.append(node)
            elif data[i] == '[':
                i += 1
            else:  # space can be replaced with another charactor except digit and '[]'
                stack.pop()
                i += 1
        # if data is not empty, stack will not be empty!
        return stack[0] if stack else None
            
                
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
