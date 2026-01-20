# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list1=[]
        temp=head
        while temp is not None:
            list1.append(temp.val)
            temp=temp.next
        s=''
        for i in list1:
            s+=str(i)
        return s==s[::-1]
