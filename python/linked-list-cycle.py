"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    # space: O(n)
    def hasCycle(self, head):
        visited = {}
        curt = head
        while curt:
            if curt in visited:
                return True
            visited[curt] = 1
            curt = curt.next
        return False

    # space: O(1)
    def hasCycle(self, head):
        p1 = p2 = head

        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            if p2:
                p2 = p2.next
            if p1 == p2 and p1:
                return True
        return False

