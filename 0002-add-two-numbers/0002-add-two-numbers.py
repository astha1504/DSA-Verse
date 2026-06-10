# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        r = dummy
        c = 0
        p = l1
        q = l2

        while p is not None and q is not None:
            s = p.val + q.val + c
            r.next = ListNode(s % 10)
            r = r.next
            c = s // 10
            p = p.next
            q = q.next

        while p is not None:
            s = p.val + c
            r.next = ListNode(s % 10)
            r = r.next
            c = s // 10
            p = p.next

        while q is not None:
            s = q.val + c
            r.next = ListNode(s % 10)
            r = r.next
            c = s // 10
            q = q.next

        if c != 0:
            r.next = ListNode(c)

        return dummy.next