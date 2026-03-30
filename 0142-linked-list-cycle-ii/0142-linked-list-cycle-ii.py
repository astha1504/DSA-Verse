# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        q=head
        while q and q.next:
            p=p.next
            q=q.next.next
            if p==q:
                break
        else:
            return None
        
        p=head
        while p!=q:
            p=p.next
            q=q.next
        return p