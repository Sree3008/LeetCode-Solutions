class Solution {
    public int[] concatWithReverse(int[] nums) {
        ArrayList<Integer> num1=new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            num1.add(nums[i]);
        }
        for(int i=nums.length-1;i>=0;i--){
            num1.add(nums[i]);
        }
        int[] num2=new int[num1.size()];
        for(int i=0;i<num1.size();i++){
            num2[i]=num1.get(i);
        }
        return num2;
    }
}
