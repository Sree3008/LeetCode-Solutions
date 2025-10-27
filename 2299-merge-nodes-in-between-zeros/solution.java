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
    public ListNode mergeNodes(ListNode head) {
        ListNode temp=head.next;
        ListNode head1 = null,temp1 = head1;
        while(temp!=null){
            int sum=0;
            while(temp.val!=0){
                sum+=temp.val;
                temp = temp.next;
            }
            ListNode ne = new ListNode(sum);
            if(head1==null){
                head1 = ne;
            }else{
                temp1.next = ne;
            }
            temp1 = ne;
            temp = temp.next;
        }
        return head1;
    }
}
