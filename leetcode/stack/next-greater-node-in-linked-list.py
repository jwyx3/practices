# https://leetcode.com/problems/next-greater-node-in-linked-list/
# https://leetcode.com/problems/next-greater-node-in-linked-list/discuss/265508/JavaC%2B%2BPython-Next-Greater-Element
# Time: O(N)
# Space: O(N)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        n = i = 0
        stack, larger = [], collections.defaultdict(int)
        curr = head
        while curr:
            while stack and stack[-1][1] < curr.val:
                j, _ = stack.pop()
                larger[j] = curr.val
            stack.append((i, curr.val))
            i += 1
            n += 1
            curr = curr.next
        return [larger[i] for i in xrange(n)]
            
# better version without map
# https://leetcode.com/problems/next-greater-node-in-linked-list/discuss/265508/JavaC%2B%2BPython-Next-Greater-Element

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        # stack: <index, value>
        stack, ans = [], []
        while head:
            while stack and stack[-1][1] < head.val:
                ans[stack.pop()[0]] = head.val
            stack.append((len(ans), head.val))
            ans.append(0)
            head = head.next
        return ans
