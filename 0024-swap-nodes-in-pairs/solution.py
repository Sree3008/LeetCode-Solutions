# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        temp=head
        while temp is not None:
            list1.append(temp.val)
            temp=temp.next
        for i in range(0,len(list1)-1,2):
            list1[i],list1[i+1]=list1[i+1],list1[i]
        d=ListNode(0)
        c=d
        for i in list1:
            c.next=ListNode(i)
            c=c.next
        return d.next
