# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s=set(nums)
        c=0
        temp=head
        while temp is not None:
            if temp.val in s and (temp.next is None or temp.next.val not in s):
                c+=1
            temp=temp.next
        return c
