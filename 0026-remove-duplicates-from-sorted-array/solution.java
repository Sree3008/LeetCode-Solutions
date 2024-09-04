public class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        
        // Initialize the first pointer
        int i = 0;
        
        // Iterate through the array with the second pointer
        for (int j = 1; j < nums.length; j++) {
            // Check if the current element is different from the last unique element
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        
        // The number of unique elements is i + 1
        return i + 1;
    }

    public static void main(String[] args) {
        // Example usage
        Solution sol = new Solution();

        int[] nums1 = {1, 1, 2};
        int k1 = sol.removeDuplicates(nums1);
        System.out.println("Output: " + k1); // Output: 2
        System.out.print("Array: ");
        for (int i = 0; i < k1; i++) {
            System.out.print(nums1[i] + " ");
        }
        System.out.println();

        int[] nums2 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        int k2 = sol.removeDuplicates(nums2);
        System.out.println("Output: " + k2); // Output: 5
        System.out.print("Array: ");
        for (int i = 0; i < k2; i++) {
            System.out.print(nums2[i] + " ");
        }
        System.out.println();
    }
}

