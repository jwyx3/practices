"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        dummy = ListNode(0)
        # 这个dummy的作用是，把head开头的链表一个个的插入到dummy开头的链表里
        # 所以这里不需要dummy.next = head;
        while head:
            node = dummy
            while node.next and node.next.val < head.val:
                node = node.next
            temp = head.next
            head.next = node.next
            node.next = head
            head = temp
        return dummy.next
