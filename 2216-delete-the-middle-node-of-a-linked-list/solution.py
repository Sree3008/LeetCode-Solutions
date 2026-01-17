# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        temp=head
        c=0
        while temp is not None :
            c+=1
            temp=temp.next
        x=c//2
        temp=head
        for i in range(x-1):
            temp=temp.next
        temp.next=temp.next.next
        return head
        
         
