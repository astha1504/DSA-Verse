# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        x=dummy
        y=head
        while y!=None and y.next!=None:
            if(y.val==y.next.val):
                while (y!=None and y.val==y.next.val):
                    y=y.next
                x.next=y.next
            else:
                x=x.next
            y=y.next
        return dummy.next