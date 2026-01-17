# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        list1=[]
        temp=head
        while temp:
            list1.append(temp.val)
            temp=temp.next
        list1.sort()
        head=None
        temp=None
        for i in list1:
            newNode=ListNode(i)
            if head is None:
                head=newNode
                temp=newNode
            else:
                temp.next=newNode 
                temp=newNode
        return head
        
