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
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode temp = head;
        while(temp.next!=null){
            ListNode ne = new ListNode(gcd(temp.val,temp.next.val));
            ne.next = temp.next;
            temp.next = ne;
            temp = ne.next;
        }
        return head;
    }
    int gcd(int a,int b){
        for(int i=Math.min(a,b);i>0;i--){
            if(a%i==0 && b%i==0)
                return i;
        }
        return 1;
    }
}
