class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        Arrays.sort(nums);
        // ArrayList<Integer> list=new ArrayList<>();
        // for(int i=nums[0];i<=nums[nums.length-1];i++){
        //     if(Arrays.binarySearch(nums,i)<0){
        //     list.add(i);    
        //     }
        // }
        // return list;
    HashSet<Integer> list=new HashSet<>();
    List<Integer> list1=new ArrayList<>();
    for(int i=0;i<nums.length;i++){
        list.add(nums[i]);
    }
    for(int j=nums[0];j<nums[nums.length-1];j++){
        if(list.add(j)){
            list1.add(j);
        }
    }
    return list1;
        
    }
}
