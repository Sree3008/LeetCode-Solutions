class Solution {
    public int maxSubArray(int[] nums) {
        int cs=0;
        int ms=Integer.MIN_VALUE;
        
        for(int i=0;i<nums.length;i++){
            int sum=cs+nums[i];
            if(sum<nums[i]){
                cs=nums[i];
            } 
            else{
                cs=sum;
            }
            if(ms<cs){
                ms=cs;
            }
        }
        return ms;
    }
}
