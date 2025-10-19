class Solution {
    public int missingMultiple(int[] nums, int k) {
        Set<Integer> set=new HashSet<Integer>();
        for(int i=0;i<nums.length;i++){
            set.add(nums[i]);
        }
        int mul=k;
        while(true){
            if(!set.contains(mul)){
                return mul;
            }
            mul+=k;
        }
    }
}
