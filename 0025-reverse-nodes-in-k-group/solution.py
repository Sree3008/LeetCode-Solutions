# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c = 0
        st = []
        temp = head
        prev = None
        while temp:
            x = temp
            temp = temp.next
            x.next = prev
            prev = x
            c+=1
            if c==k:
                c = 0
                st.append(prev)
                prev = None
        temp = prev
        prev = None
        if c!=0:
            while temp:
                x = temp
                temp = temp.next
                x.next = prev
                prev = x
            st.append(prev)
        for i in range(len(st)-1):
            x = st[i]
            while x.next:
                x = x.next
            x.next = st[i+1]
        return st[0]

