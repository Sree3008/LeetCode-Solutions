# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_set = set(nums)  
        list1=[]
        list2=[]
        temp=head
        while temp is not None:
            list1.append(temp.val)
            temp=temp.next
        for i in list1:
            if i not in num_set:
                list2.append(i)
        d=ListNode(0)
        c=d
        for i in list2:
            c.next=ListNode(i)
            c=c.next
        return d.next
