class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        ArrayList<Integer> list1=new ArrayList<>();
        ArrayList<Integer> list2=new ArrayList<>();
        ArrayList<Integer> list3=new ArrayList<>();
        for(int i:nums){
            if(i>pivot){
                list1.add(i);
            }
            else if(i<pivot){
                list2.add(i);
            }
            else{
                list3.add(i);
            }
        }
        list2.addAll(list3);
        list2.addAll(list1);
        int[] num=new int[list2.size()];
        for(int i=0;i<list2.size();i++){
            num[i]=list2.get(i);
        }
        return num;
    }
}
