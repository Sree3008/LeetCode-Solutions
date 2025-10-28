public class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0; // Pointer for the position of the next element not equal to val
        
        // Iterate through the array
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }
        
        // i is the count of elements not equal to val
        return i;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        
        int[] nums1 = {3, 2, 2, 3};
        int val1 = 3;
        int k1 = sol.removeElement(nums1, val1);
        System.out.println("Output: " + k1); 
        System.out.print("Array: ");
        for (int i = 0; i < k1; i++) {
            System.out.print(nums1[i] + " ");
        }
        System.out.println();
        int[] nums2 = {0, 1, 2, 2, 3, 0, 4, 2};
        int val2 = 2;
        int k2 = sol.removeElement(nums2, val2);
        System.out.println("Output: " + k2); 
        System.out.print("Array: ");
        for (int i = 0; i < k2; i++) {
            System.out.print(nums2[i] + " ");
        }
        System.out.println();
    }
}
