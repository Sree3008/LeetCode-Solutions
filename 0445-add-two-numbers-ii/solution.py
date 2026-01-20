# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        s1=''
        s2=''
        while l1:
            list1.append(l1.val)
            l1=l1.next
        list2=[]
        while l2:
            list2.append(l2.val)
            l2=l2.next
        for i in list1:
            s1+=str(i)
        for i in list2:
            s2+=str(i)
        k1=str(int(s1)+int(s2))
        list1=[]
        for i in k1:
            list1.append(int(i))
        print(list1)
        d=ListNode(0)
        curr=d
        for i in list1:
            curr.next=ListNode(i)
            curr=curr.next
        return d.next

