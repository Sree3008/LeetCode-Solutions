class Solution {
    public int[] twoSum(int[] nums, int target) {
        int left=0;
        int right=nums.length-1;
        Arrays.sort(nums);
        int[] num=new int[2];
        while(left<right){
            int k=nums[left]+nums[right];
            if(k==target){
                num[0]=left+1;
                num[1]=right+1;
                return num;
            }
            else if(k<target){
                left++;
            }
            else{
                right--;
            }
        }
        return new int[]{};
    }
}
