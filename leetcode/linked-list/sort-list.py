# idea: Time: O(nlog), Space: O(1)

# merge sort:
# 1) find_mid, merge
# 2) merge sorted lists

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    # merge sort
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.find_mid(head)
        h1 = self.sortList(mid.next)
        mid.next = None
        h2 = self.sortList(head)
        return self.merge(h1, h2)

    def merge(self, h1, h2):
        dummy = tail = ListNode(0)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2 = h2.next
            tail = tail.next
        if h1:
            tail.next = h1
        else:
            tail.next = h2
        return dummy.next

    # d->1->3->2->null
    def find_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# quick sort:
# 1) find_mid (pivot), partition, sort and concat
# 2) partition into three part: <, ==, >
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    # quick sort
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.find_mid(head)
        hl, hm, hr = self.partition(head, mid)
        hl = self.sortList(hl)
        hr = self.sortList(hr)
        return self.concat(hl, hm, hr)

    # d->1->3->2->end
    def find_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def find_tail(self, head):
        dummy = tail = ListNode(0, head)
        while tail.next:
            tail = tail.next
        return tail

    def partition(self, head, mid):
        dl, dm, dr = ListNode(0), ListNode(0), ListNode(0)
        tl, tm, tr = dl, dm, dr
        while head:
            if head.val < mid.val:
                tl.next = head
                tl = tl.next
            elif head.val > mid.val:
                tr.next = head
                tr = tr.next
            else:
                tm.next = head
                tm = tm.next
            head = head.next
        tl.next = tm.next = tr.next = None
        return dl.next, dm.next, dr.next

    def concat(self, hl, hm, hr):
        dummy = tail = ListNode(0)
        for head in [hl, hm, hr]:
            tail.next = head
            tail = self.find_tail(tail)
        return dummy.next

