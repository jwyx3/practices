# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode

    # space: O(n)
    def copyRandomList(self, head):
        mapping = {}

        curt = head
        while curt:
            mapping[curt] = RandomListNode(curt.label)
            curt = curt.next

        for old_node, new_node in mapping.items():
            new_node.next = mapping.get(old_node.next)
            new_node.random = mapping.get(old_node.random)

        return mapping[head]

    # space: O(1)
    def copyRandomList(self, head):
        curt = head
        while curt:
            new_node = RandomListNode(curt.label)
            new_node.next = curt.next
            curt.next = new_node
            curt = new_node.next

        curt = head
        while curt:
            if curt.random:
                curt.next.random = curt.random.next
            next_old_node = curt.next.next
            if next_old_node:
                curt.next.next = next_old_node.next
            curt = next_old_node
        return head.next
