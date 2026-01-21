# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list1=[]
        temp=head
        while temp is not None:
            list1.append(temp.val)
            temp=temp.next
        list1.pop(-n)
        d=ListNode(0)
        c=d
        for i in list1:
            c.next=ListNode(i)
            c=c.next
        return d.next
        
        

