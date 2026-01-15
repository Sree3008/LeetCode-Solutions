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
    public ListNode removeNodes(ListNode head) {
        Stack<ListNode> list=new Stack<ListNode>();
        ListNode temp=head;
        while(temp!=null){
            while(!list.isEmpty()&&list.peek().val<temp.val){
                list.pop();
            } 
            list.push(temp);
            temp=temp.next;
        }
        head=null;
        while(!list.isEmpty()){
            temp=list.pop();
            temp.next=head;
            head=temp;
        }
        return head;
    }
} 
