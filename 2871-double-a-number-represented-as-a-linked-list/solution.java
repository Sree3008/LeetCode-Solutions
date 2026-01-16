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
    public ListNode doubleIt(ListNode head) {
        ListNode temp=head;
        Stack<Integer> list=new Stack<Integer>();
        while(temp!=null){
            list.push(temp.val);
            temp=temp.next;
        }
        ArrayList<Integer> li=new ArrayList<>();
        int c=0;
        while(!list.isEmpty()){
            int x=list.pop(); 
            int y=x*2+c;
            li.add(y%10);
            c=y/10;
        }
        if(c>0){
            li.add(c);
        }
        ListNode newNode=null;
        for(int i=0;i<li.size();i++){
            ListNode node=new ListNode(li.get(i));
            node.next=newNode;
            newNode=node;
        } 
        return newNode;
    }
} 
