class Solution {
    public int longestBalanced(int[] nums) {
        int maxLen=0;
        for(int i=0;i<nums.length;i++){
            HashSet<Integer> es=new HashSet<Integer>();
            HashSet<Integer> os=new HashSet<Integer>();
            for(int j=i;j<nums.length;j++){
                if(nums[j]%2==0) es.add(nums[j]);
                else os.add(nums[j]);
                if(es.size()==os.size()){
                    maxLen=Math.max(maxLen,j-i+1);
                }
            }
        }
        return maxLen;
    }
}
