class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    // Deserialize method to create a ListNode from a string representation
    public static ListNode deserialize(String data) {
        // Remove brackets and check if the string is empty
        if (data == null || data.isEmpty() || data.equals("[]")) return null;
        
        // Remove the surrounding brackets
        data = data.substring(1, data.length() - 1).trim();
        
        if (data.isEmpty()) return null; // Handle the case of an empty list
        
        String[] parts = data.split("\\s*,\\s*");
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        
        for (String part : parts) {
            if (!part.isEmpty()) {
                try {
                    int value = Integer.parseInt(part.trim());
                    current.next = new ListNode(value);
                    current = current.next;
                } catch (NumberFormatException e) {
                    throw new IllegalArgumentException("Invalid input string format", e);
                }
            }
        }
        return dummy.next;
    }

    // Serialize method to convert a ListNode to a string representation
    public static String serialize(ListNode head) {
        if (head == null) return "[]";
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        ListNode current = head;
        while (current != null) {
            sb.append(current.val).append(",");
            current = current.next;
        }
        sb.setLength(sb.length() - 1); // Remove trailing comma
        sb.append("]");
        return sb.toString();
    }
}

public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode current = head;
        while (current != null && current.next != null) {
            if (current.val == current.next.val) {
                current.next = current.next.next;
            } else {
                current = current.next;
            }
        }
        return head;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Example 1
        ListNode head1 = ListNode.deserialize("[1,1,2]");
        ListNode result1 = sol.deleteDuplicates(head1);
        System.out.println("Output: " + ListNode.serialize(result1)); // Output: [1,2]
        
        // Example 2
        ListNode head2 = ListNode.deserialize("[1,1,2,3,3]");
        ListNode result2 = sol.deleteDuplicates(head2);
        System.out.println("Output: " + ListNode.serialize(result2)); // Output: [1,2,3]
    }
}

