# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        c=0
        while temp is not None:
            c+=1
            temp=temp.next
        x=c//2
        temp=head
        for i in range(x):
            temp=temp.next
        return temp
           



