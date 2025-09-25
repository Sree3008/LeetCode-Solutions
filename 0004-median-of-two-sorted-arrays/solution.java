class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        ArrayList<Double> list=new ArrayList<>();
        ArrayList<Double> list1=new ArrayList<>();
        for(double i:nums1){
            list.add(i);
        }
        for(double j:nums2){
            list1.add(j);
        }
        list.addAll(list1);
        Collections.sort(list);
        int st=0;
        int last=list.size()-1;
        int mid=(st+last)/2;
        int n=list.size();
        if(n%2==1){
              return list.get(n/2);
        }
       else{
         return (list.get(n/2-1)+list.get(n/2))/2.0;
       }
        
    }
}
