class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        int c[] = new int[nums.length+1];
        for(int i = 0; i<nums.length; i++)
        {
            c[nums[i]]++;
        }
        for(int i=0;i<c.length;i++){
            if(c[i]==0){
                return i;
            }
        }
        return nums.length+1;
    }
}
