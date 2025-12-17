class Solution {
    public int[] rearrangeArray(int[] nums) {
        ArrayList<Integer> list1=new ArrayList<>();
        ArrayList<Integer> list2=new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            if(nums[i]>0){
                list1.add(nums[i]);
            }
            else{
                list2.add(nums[i]);
            }
        }
        int[] arr=new int[nums.length];
        for(int i=0;i<list1.size();i++){
            arr[i*2]=list1.get(i);
            arr[2*i+1]=list2.get(i);
        }
        return arr;
    }
}
