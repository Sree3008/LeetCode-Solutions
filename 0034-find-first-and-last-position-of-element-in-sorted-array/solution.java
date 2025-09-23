class Solution {
    public int[] searchRange(int[] nums, int target) {
        int left=0;
        int right=nums.length-1;
        int m=-1;
        int n=-1;
       for(int i=0;i<nums.length;i++){
        if(nums[i]==target){
            m=i;
            break;
        }
       }
       for(int i=nums.length-1;i>=0;i--){
        if(nums[i]==target){
            n=i;
            break;
        }
       }
        return new int[]{m,n};
        
    }
}
