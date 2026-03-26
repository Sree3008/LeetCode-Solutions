class Solution {
    public int trap(int[] height) {
        int leftmax=0;
        int rightmax=0;
        int l=0;
        int res=0;
        int r=height.length-1;
        while(l<r){
            if(height[l]<height[r]){
                if(height[l]>=leftmax){
                    leftmax=height[l];
                }
                else{
                    int res1=leftmax-height[l];
                    res+=res1;
                }
                l++;
            }
            else{
                if(height[r]>=rightmax){
                    rightmax=height[r];
                }
                else{
                    int res2=rightmax-height[r];
                    res+=res2;
                }
                r--;
            }
            
        }
        return res;
    }
}
