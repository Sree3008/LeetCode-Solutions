class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        int n=nums.length;
        int[] ans=new int[n-k+1];
        for(int i=0;i<=n-k;i++){
            Map<Integer,Integer> freq=new HashMap<>();
            for(int j=i;j<i+k;j++){
                freq.put(nums[j],freq.getOrDefault(nums[j],0)+1);
            }
            List<int[]> list=new ArrayList<>();
            for(Map.Entry<Integer,Integer> e: freq.entrySet()){
                list.add(new int[]{e.getKey(),e.getValue()});
            }
               Collections.sort(list, new Comparator<int[]>() {
                @Override
                public int compare(int[] a, int[] b) {
                    if (b[1] == a[1]) return b[0] - a[0];
                    return b[1] - a[1];
                }
            });
            int sum=0;
            int count=0;
            for(int[] pair:list){
                if(count==x) break;
                int num=pair[0];
                int occ=pair[1];
                sum+=num*occ;
                count++;
            }
            ans[i]=sum;
        }
        return ans;
    }
}
