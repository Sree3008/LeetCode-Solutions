# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        temp=head
        while temp is not None:
            list1.append(temp.val)
            temp=temp.next
        list2=[]
        list3=[]
        k=1
        i=0
        while i<len(list1):
            list2.clear()
            for j in range(i,min(i+k,len(list1))): 
                list2.append(list1[j])
            if len(list2)%2==0:
                list2.reverse()
            list3.extend(list2)
            i+=k
            k+=1
        
        d=ListNode(0)
        c=d
        for i in list3:
            c.next=ListNode(i)
            c=c.next
        return d.next

        
