# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        while temp and temp.next:
            x,y = temp.val,temp.next.val
            new = ListNode(math.gcd(x,y))
            new.next=temp.next
            temp.next=new
            temp=new.next
        return head

        
