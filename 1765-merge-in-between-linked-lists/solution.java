/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode n1=null;
        ListNode n2=null;
        ListNode temp=list1;
        for(int i=0;i<a-1;i++){
            temp = temp.next;
        }
        n1 = temp;
        for(int i=0;i<b-a+1;i++){
            temp = temp.next;
        }
        n2 = temp.next;
        n1.next = list2;
        temp = list2;
        while(temp.next!=null)
        temp = temp.next;
        temp.next=n2;
        return list1;
    }
}
