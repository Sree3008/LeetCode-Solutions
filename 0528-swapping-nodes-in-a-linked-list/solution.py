# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list1=[]
        temp=head
        while temp is not None:
            list1.append(temp.val)
            temp=temp.next
        n=len(list1)
        list1[k-1], list1[n-k] = list1[n-k], list1[k-1]
        d=ListNode(0)
        c=d
        for i in list1:
            c.next=ListNode(i)
            c=c.next
        return d.next

