# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        temp=head
        while temp is not None:
            list1.append(temp.val)
            temp=temp.next
        x=Counter(list1)
        list2=[]
        for i,v in x.items():
            if v==1:
                list2.append(i)
        print(list2)
        d=ListNode(0)
        c=d
        for i in list2:
            c.next=ListNode(i)
            c=c.next
        return d.next
