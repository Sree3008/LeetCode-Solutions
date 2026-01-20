# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        temp=head
        while temp is not None:
            list1.append(temp.val)
            temp=temp.next
        o=[]
        e=[]
        for idx,i in enumerate(list1):
            if (idx+1)%2==0:
                e.append(i)
            else:
                o.append(i)
        o.extend(e)
        d=ListNode(0)
        c=d
        for i in o:
            c.next=ListNode(i)
            c=c.next
        return d.next

