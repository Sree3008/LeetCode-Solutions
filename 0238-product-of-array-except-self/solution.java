class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] l = new int[n];
        int[] r = new int[n];
        l[0] = nums[0];
        r[n-1] = nums[n-1];
        for(int i=1;i<n;i++){
            l[i] = l[i-1]*nums[i];
            r[n-i-1] = r[n-i]*nums[n-i-1];
        }
        for(int i=0;i<n;i++){
            int x=1,y=1;
            if(i!=0)
            x = l[i-1];
            if(i!=n-1)
            y = r[i+1];
            nums[i] = x*y;
        }
        return nums;
    }
}
