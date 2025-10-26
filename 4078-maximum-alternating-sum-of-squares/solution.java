class Solution {
    public long maxAlternatingSum(int[] nums) {
       
        for(int k=0;k<nums.length;k++){
            nums[k]=nums[k]*nums[k];
        }
        int j=nums.length-1;
        int i=0;
        Arrays.sort(nums);
        long sum=0;
        while(i<j){
           sum+=nums[j]-nums[i];
            i++;
            j--;
        }
        if(i==j){
            return sum+nums[j];
        }
        return sum;
    }
}
