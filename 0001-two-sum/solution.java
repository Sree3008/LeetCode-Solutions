import java.util.*;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
          
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
    
    public static void main(String[] args) {
        Scanner ob = new Scanner(System.in);
        
        int n = ob.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = ob.nextInt();
        }
        int target = ob.nextInt();
        Solution solution = new Solution();
        int[] result = solution.twoSum(nums, target);
        
        System.out.println(Arrays.toString(result));
        
        ob.close();
    }
}

