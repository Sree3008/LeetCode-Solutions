import java.util.*;
class Solution {
    public void rotate(int[] nums, int k) {
         ArrayList<Integer> list=new ArrayList<Integer>();
          int n = nums.length;
        k = k % n;
        for(int i:nums){
            list.add(i);
        }
        
        ArrayList<Integer> list1=new ArrayList<Integer>();
        
        ArrayList<Integer> list2=new ArrayList<Integer>();

        for(int i=n-k;i<n;i++){
            list1.add(list.get(i));
        }
        for(int i=0;i<n-k;i++){
            list2.add(list.get(i));
        }
        ArrayList<Integer> list3=new ArrayList<Integer>();
        list3.addAll(list1);
        list3.addAll(list2);
        for(int i=0;i<n;i++){
            nums[i]=list3.get(i);
        }
            System.out.print(Arrays.toString(nums));
        
    }
}
