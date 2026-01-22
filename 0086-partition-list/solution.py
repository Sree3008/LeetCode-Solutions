# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list1=[]
        list2=[]
        list3=[]
        temp=head
        while temp is not None:
            list1.append(temp.val)
            temp=temp.next
        for i in list1:
            if i<x:
                list2.append(i)
            else:
                list3.append(i)
        list2.extend(list3)
        d=ListNode(0)
        c=d
        for i in list2:
            c.next=ListNode(i)
            c=c.next
        return d.next

        
