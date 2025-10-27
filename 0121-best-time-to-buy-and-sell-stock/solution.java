class Solution {
    public int maxProfit(int[] nums) {
        int minp=Integer.MAX_VALUE;
        int profit=0;
        int maxp=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]<minp){
                minp=nums[i];
            }
            else{
           profit=nums[i]-minp; 
           if(maxp<profit){
                maxp=profit;
            }
            }
            
        }
        return maxp;
    }
}
