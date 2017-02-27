"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    # @param node: the node in the list should be deleted
    # @return: nothing

    # copy value
    def deleteNode(self, node):
        if node is None or node.next is None:
            return
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next

